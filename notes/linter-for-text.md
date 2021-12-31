# linter for text

There are three, proselint, textlint and vale.

Vale has [several writing style guides](https://github.com/errata-ai/styles#available-styles). I didn't even realise there are style guide for documentations, for example, [Microsoft writing guide](https://docs.microsoft.com/en-us/style-guide/welcome/), [google style guide](https://developers.google.com/style) and [apple style guide](https://help.apple.com/applestyleguide/#/apsg1eef9171).

I choose to try Vale first because of it supports markup and can use different style guides.

## Not easy to install Vale in ubuntu

I cannot find a release for ubuntu for vale https://repology.org/project/vale/versions ...

## Trying proselint instead

Because proselint uses python too, so it is simple to add to my current workflow.

Output of proselint:

```
bi-directional-links.md:76:63: leonard.exclamation.30ppm More than 30 ppm of exclamations. Keep them under control.
bi-directional-links.md:76:109: typography.symbols.ellipsis '...' is an approximation, use the ellipsis symbol '…'.
bi-directional-links.md:80:318: typography.symbols.sentence_spacing More than two spaces after the period; use 1 or 2.
boardgame.md:10:11: leonard.exclamation.30ppm More than 30 ppm of exclamations. Keep them under control.
boardgame.md:27:183: misc.but No paragraph should start with a 'But'.
business-idea.md:18:23: annotations.misc Annotation left in text.
cafe-reviews.md:18:13: weasel_words.very Substitute 'damn' every time you're inclined to write 'very'; your editor will delete it and the writing will be just as it should be.
cafe-reviews.md:42:53: leonard.exclamation.30ppm More than 30 ppm of exclamations. Keep them under control.
cleaning.md:12:5: leonard.exclamation.30ppm More than 30 ppm of exclamations. Keep them under control.
...

```

It has less output then I imagine, I am hoping it will point out more problems.

Let me try Vale to compare the output.


## installing vale

I am totally wrong! Downloading the zip in [release](https://github.com/errata-ai/vale/releases) gives me the vale executable.

I moved the executable to `./bin/` in my notes folder.

## using vale

```
~/Documents/notes$ ./bin/vale ./notes/index.md
E100 [.vale.ini] Runtime error

open : no such file or directory

Execution stopped with code 1.
```

Needs to add `.vale.ini`

This file looks something like the following, based on [vale-boilerplate](https://github.com/errata-ai/vale-boilerplate/blob/master/.vale.ini).

```
StylesPath = styles

Vocab = Blog

[*.md]
BasedOnStyles = Vale, write-good
```

So I need to download a styles first...

Trying the Google style first with no specific reason, I have not read [google style guide](https://developers.google.com/style/highlights) in details..

Now, it needs [Vocab](https://docs.errata.ai/vale/cli#vocab), I will just add empty `accept.txt` and `reject.txt`, same with vale-boilerplate..


Okay, I got this ini at the end.

```
StylesPath = styles

Vocab = Note

[*.md]
BasedOnStyles = Google
```

## linting output from google style

I can use only some of them, see examples below.


```
 9:23    warning  Avoid first-person pronouns     Google.FirstPerson 
                  such as ' I '.  
 31:24   warning  Try to avoid using              Google.We          
                  first-person plural like 'we'. 
```

Bad, this is a blog so I am allow use `I` and `We`.

```
 82:65   warning  Use 'command-line tool'         Google.WordList
                  instead of 'CLI'.
```

Good, I like this one.

```
 1:3    warning  'Welcome To Strategy'           Google.Headings 
                 should use sentence-style                       
                 capitalization.       
```

Good, I don't care about which style the headings should be, but I do like it enforces a specific style, maybe I can implement this myself.

```
 23:97  warning  In general, use American        Google.Spelling 
                 spelling instead of                             
                 'organise'.   
```

Good, it ensures consistent spelling.

```
 175:33   error    Don't use exclamation points    Google.Exclamation 
                   in text.     
```

No, I can use exclamation for my notes.

Conclusion, the google style guide is for documentation I should look for others.

## Other style guides

Below are the list of [styles available](https://github.com/errata-ai/styles).


| Style | Description |
| ------------- | ------------- |
| Microsoft| Welcome to the Microsoft Writing Style Guide, your guide to writing style and terminology for all communication—whether an app, a website, or a white paper. If you write about computer technology, this guide is for you. |
| Google | This style guide provides editorial guidelines for writing clear and consistent Google-related developer documentation. |
| write-good |  Naive linter for English prose for developers who can't write good and wanna learn to do other stuff good too.|
| proselint | proselint places the world’s greatest writers and editors by your side, where they whisper suggestions on how to improve your prose. |
| Joblint |  Test tech job posts for issues with sexism, culture, expectations, and recruiter fails.|
| Alex | Catch insensitive, inconsiderate writing. |
| Readability |This repository contains a Vale-compatible implementation of many popular "readability" metrics. |

## Output from write-good

I like the output!

For example

```
 ./notes/index.md
 11:55  warning  'currently' is a weasel word!  write-good.Weasel
```

> A weasel word, or anonymous authority, is an informal term for words and phrases aimed at creating an impression that something specific and meaningful has been said, when in fact only a vague or ambiguous claim has been communicated.

Wikipedia definition of weasel words.

```
31:359  warning  'been presented' may be         write-good.Passive  
                  passive voice. Use active                           
                  voice if you can.  
```

It warns you to avoid passive voice.

```
 40:1     error    Don't start a sentence with     write-good.So
                   'So '.
```

Okay, I didn't know that.

I have a 11 errors and 121 warnings already, I am happy to start with this for now.

I can go and do

1. read and understand how [write-good](https://github.com/btford/write-good) works
1. fix the warning
1. add lint to `pre-push` hook to fail the push 
