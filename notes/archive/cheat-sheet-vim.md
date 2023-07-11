# Cheat Sheet Vim

## Inserting Symbols e.g. £

| keys         | output |
| ------------ | ------ |
| `<ctrl-k>Pd` | £      |

see more in `:diagraph`

## Getting back to file before vim exited

`'0` - go to file where vim exited

`:browse oldfiles` - see last edited files, press `q` and enter a number to edit
numbered file

`:mksession foo.vim` - save session, session stores the looks of the whole of
vim
`:source foo.vim` - use session
`vim -S session-file.vim` - start vim and source session

`:mkview` - save view, view stores properties for one window one file
`:loadview ` - use view

## Editing in command line mode

| keys           | function                     |
| -------------- | ---------------------------- |
| `<ctrl-left>`  | one word left                |
| `<ctrl-right>` | one word right               |
| `<ctrl-b>`     | begin of command line        |
| `<ctrl-e>`     | end of command line          |
| `<ctrl-w>`     | remove one word              |
| `<ctrl-u>`     | removes all text             |
| `<insert>`     | replace mode, `Fn+\` in HHKB |

## Grep

- `:G foo src` - grep in a directory e.g. `src`
- `:G foo -- *.md` - grep for specific file types e.g. `*.md`

## Range

- `{number}, {number}` - from line number to change

- `{number}` - one specific line

- `.` - current line

- `%` - short way of `1,$`

- `{pattern},{pattern}` - e.g. `:?^Chapter?,/^Chapter/s=grey=gray=g`

- `-number, +number` use at the end of number or pattern to specify offset

  - e.g. `/foo/-2` - 2 lines before next foo
  - e.g. `/foo/+2` - 2 lines after next foo

## Using external program

- `[range]!{motion}{program}` - replace text by motion by output of external program
  - `!$date` - replace until end of line by date, e.g. `Mon 31 Jan 11:42:41 GMT 2022`
- `:read !{program}` - append output from extra program

## Argument lists

- Use vim arguments list to manage the list of files
  - use `:argadd`, `:argdelete` to add and remove opened file
  - `[a`, `]a` to go to previous and next argument files
  - `argdo {cmd}` to do operation
    - `:argdo %s/foo/bar/g | update` to run search-replace-save argument files

## Registers

Registers used for recording `qq` is the same one used for yank `"qy`, so we can see the recorded command by `"qp` and edit the recording (see `:help usr_10.txt` Record and playback commands)!

Use uppercase letter to add to registers, e.g. `"ay` and then `"Ay` to append yanked text to register a

## Ask for confirm in substitution

- `[range]:s/foo/bar/gc` - use flag c

## The global command

- `[range]:g/{pattern}/{command}` - execute command on matched pattern

e.g. `g/breakpoint/:normal dd`

## Options

**option window**

- `:options` - open option window

- shows current option

- hit <CR> on a "set" line to execute it

**help**

- `:help 'wrap'` - to see help for 'wrap' option

## Regex

- `.*[]^%/\?~$` - requires `\` escape
- `\<  \>` - patterns that matches beginning or end of word
- `:%s/\([^,]*\), \(.*\)/\2 \1/` - Change "Last, First" to "First Last"

```
                                                \([^,]*\), \(.*\)

The first part between \( \) matches "Last"     \(     \)
    match anything but a comma                    [^,]
    any number of times                               *
matches ", " literally                                   ,
The second part between \( \) matches "First"              \(  \)
    any character                                            .
    any number of times                                       *
```

```
                                                \2 \1

backreferences \2 - second "\( \)"  \1 - first "\( \)"
```

## Help

- `:help index` - all Vim commands
- `:helpgr[ep]` - search help text files

## Steps for Effective Editing

1. While editing, look for repeat and time consuming actions.
1. Find builtin commands to make the actions quicker. Read the user manual, and then docs! (try not to google)
1. Train using the command, do this until muscle memory builds up.

From https://moolenaar.net/habits.html

## Quickfix list

- `:mak[e]` - run make commands and populate quickfix
  - quickfix understands patterns like `src/mobile_api/modules/obsessions.py:346:` in the STDOUT
- `:helpgr[ep]` - search help text files
- `:cnf`, `:cpf` - jump to errors in the next/previous file, `[<C-Q>`, `]<C-Q>`
- run macro q on lines containing "foo"
- `:col[der], :cnew[er]` -- Go to the older/newer quickfix list.

```vim
:grep foo
:cdo normal @q
```

- `:cdo normal .` run repeat/`.` on quickfix

Learned from [code in the hole](https://codeinthehole.com/tips/vim-lists/#quickfix-list)

## Vim spell check quick start

- `:help spell-quickstart`

- `:set spell`

- `]s`  - move to next misspelled word

- `[s`  - move to previous misspelled word

- `zg`  - z good - mark word as a good word

- `zw`  - z good - mark word as a bad word

- `z=`  - correct word

- `1z=` - replace incorrectly spelled word with the first suggest

## Autocomplete

- `Ctrl-x Ctrl-f` - autocomplete file name in insert mode, useful for insert images when writing README

| keys           | function                |
| -------------- | ----------------------- |
| CTRL-X CTRL-F  | file names              |
| CTRL-X CTRL-L  | whole lines             |
| CTRL-X CTRL-K  | words from a dictionary |
| CTRL-X CTRL-\] | tags                    |
| CTRL-X CTRL-V  | Vim command line        |

## Use vim for writing

https://www.naperwrimo.org/wiki/index.php?title=Vim_for_Writers#Tips_from_reddit

https://github.com/preservim/vim-wordy

https://github.com/preservim/vim-lexical

https://github.com/junegunn/goyo.vim

https://github.com/junegunn/limelight.vim

https://github.com/preservim/vim-pencil

https://nickjanetakis.com/blog/vim-is-saving-me-hours-of-work-when-writing-books-and-courses

## vim-markdown plugin

- `:Toc` - create a quickfix vertical window navigable table of contents with the headers

- `:TableFormat` - format the table under the cursor

## Marks

- ``  ` (backtick) `` - jump to marks
- `m{A-Z}` - set marks in any files
- `'0` - location of the cursor when you last exited Vim, `'1` one last...
- `delm[arks] {marks}` - delete the marks for example `delm A-Z`

## Jumps

- `CTRL-O` - Go to \[count\] Older cursor position in jump list
- `CTRL-6` - jump to last edited file, see `:help ctrl-6`
- `<Tab> or CTRL-I` - Go to \[count\] newer cursor

## Change list jumps

- `g;` - jump to last change in current file

## Open files

- `gf` - open file in the same window
- `ctrl-w f` - open file in a new window (see `:help CTRL-W_f`)

## replace character by a new line

Use `\r` not `\n`

## window

- `ctrl-w o` - close all other windows, like `:only`
- `ctrl-w ]` - open tag in another windows

## Temporally Enlarge Quickfix

- `:tab split` - open buffer in new tab
- `:tabc` - close tab

## Working with tabs

- `gt` - next tab
- `gT` - previous tab

## Fugitive Open File From Another Branch

- `Gedit branch-name:path/to/file`

## Links to this note

[Cheat Sheet Writing](cheat-sheet-writing.md)

[Index Cheat Sheet](index-cheat-sheet.md)
