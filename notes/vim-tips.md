# Vim Tips

## Vim spell check quick start

`:help spell-quickstart`

`:set spell`

`]s`  - move to next misspelled word
`[s`  - move to previous misspelled word
`zg`  - z good - mark word as a good word
`zw`  - z good - mark word as a bad word
`z=`  - suggest correctly spelled word
`1z=` - replace incorrectly spelled word with the first suggest

## Autocomplete

`Ctrl-x Ctrl-f` - autocomplete file name in insert mode, useful for insert images when writing README

## Use vim for writing

https://www.naperwrimo.org/wiki/index.php?title=Vim_for_Writers#Tips_from_reddit

https://github.com/preservim/vim-wordy

https://github.com/preservim/vim-lexical

https://github.com/junegunn/goyo.vim

https://github.com/junegunn/limelight.vim

https://github.com/preservim/vim-pencil

https://nickjanetakis.com/blog/vim-is-saving-me-hours-of-work-when-writing-books-and-courses

## vim-markdown plugin

`:Toc` - create a quickfix vertical window navigable table of contents with the headers

`:TableFormat` - format the table under the cursor

## Marks

`` ` (backtick)`` - jump to marks

`m{A-Z}` - set marks in any files

`'0` - location of the cursor when you last exited Vim, `'1` one last...

`delm[arks] {marks}` - delete the marks for example `delm A-Z`

## Jumps

`CTRL-O` - Go to [count] Older cursor position in jump list

`CTRL-6` - jump to last edited file, see `:help ctrl-6`

`<Tab> or CTRL-I` - Go to [count] newer cursor

## Change list jumps

`g;` - jump to last change in current file

## Open files

`gf` - open file in the same window
`ctrl-w f` - open file in a new window (see `:help CTRL-W_f`)

## defaultdict

`from collections import defaultdict`
