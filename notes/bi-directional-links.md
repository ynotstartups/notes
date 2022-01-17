# Bi-Directional Links

## What is it?
Basically if one note A contains a hyperlink to another note B, then create also create a link from note B to note A.

## What is it useful?

I think it is powerful because it gives me the ability to link notes together like a graph.

This avoids the need for a navigation system, because navigation system is tree like with no links between the leafs, but knowledge doesn't work this way.

My example would be my investment strategy, my household cleaning philosophy all follows the underlying idea of minimalism, but it would be weird if I put those two notes under minimalism section.

So bi-directional links are simpler.

## Technical Requirements

Following Andy's example below, adding a new section called Links to this note is nice.

Try to contains a snippet of the link too, this will makes me write more [atomic notes](https://notes.andymatuschak.org/Evergreen_notes_should_be_atomic).

No need to implement linking to sections, writing atomic notes basically means no more sections in any notes.

Able to follow the links in Vim.

Make the system works in Vim and basic README first, because it will be my user interface.

Blog framework independent, meaning not depends on mkdocs framework.

## Investigation on finding existing links using terminal programs

Figure out the grep pattern for finding links `[]()`, note I need to ignore images `![]()` and links to other websites.

Finding links - `grep '\[.*\]\(.*\)' *.md`

Ignoring images - `grep '[^!]\[.*\]\(.*\)' *.md`

Needed to use `--perl-regex` for non-greedy match - `grep --perl-regex --recursive --only-match '[^!]\[.*?\]\(.*?\)' *.md`

Ignoring `http` and `#` - `grep --perl-regex --recursive --only-match '[^!]\[.*?\]\(.*?\)' *.md | grep -v 'http' | grep -v '#'`

Ignore special case back quote

```
[^!`]
```

```
grep --perl-regex --recursive --only-match '[^!`]\[.*?\]\(.*?\)' *.md | grep -v 'http' | grep -v '#' | grep --perl-regex '[\w-]+.md'
```

Result

```
index.md: [coffee](coffee.md)
```

Finally using `sed` to format the above into csv format

```
grep --perl-regex --recursive --only-match '[^!`]\[.*?\]\(.*?\)' *.md | grep -v 'http' | grep -v '#' | sed 's/: \[.*\](/,/' | sed 's/)//'
```

```
index.md,coffee.md
```

So here I find all the links, the reverse will become data of the bidirectional links.

I have also just ignores links in this file.

```
grep --perl-regex --recursive --only-match '[^!`]\[.*?\]\(.*?\)' *.md | grep -v 'http' | grep -v '#' | sed 's/: \[.*\](/,/' | sed 's/)//' | grep -v 'bi-directional-links.md'
```

But this will fail once we have added the bi directional links! Because this grep will find those links too...

## Python implementation

At the end, I used python to [implement the finding links](https://github.com/ynotstartups/notes/blob/1c0230e6049fc28738806e9384a1bfbebb416121/bin/generate-bi-directional-links.py#L69) above because I used python to remove existing bi-directional links section so it is simpler to also do finding all links in python.

## Andy Matuschak's Digital Garden Implementation

[Notes by Andy Matuschak](https://notes.andymatuschak.org/About_these_notes)

In this website, it contains a section *Links to this note* at the end of the page to contains all the bi-directional links with a less intrusive color.

## Links to this note

[Andy Matuschak's Digital Garden](andy-matuschak-digital-garden.md)

## Links to this note

[Andy Matuschak's Digital Garden](andy-matuschak-digital-garden.md)
