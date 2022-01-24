# Cheat Sheet Bash

The best tip is to start reading the manual page by use `man` with a program name, such `man ls`.

In vim, you can even use `K` on any bash program to open the manual page, trying pressing K here -> ls.

## Variables

`$?` - last exit code

## Tips

TODO:cut, grep, uniq, sort, ls, use apropos to find command

## Single quote v.s. double quote

Double quote interpolates, single quote doesn't.

So I should use single quote most of the time.

## Check if a directory does not exist

```
if [ -d '/path/to/dir' ]
then
    echo 'Directory /path/to/dir exists.'
else
    echo 'Error: Directory /path/to/dir does not exists.'
fi
```

```
if [ ! -d '/path/to/dir' ]
then
    echo 'Directory /path/to/dir DOES NOT exists.'
    exit 9999 # die with error code 9999
fi
```

## Apt - Advanced Package Tool

`sudo apt update` - check if there are new packages

`sudo apt upgrade` - upgrade packages

## Ranger

[User Guide](https://github.com/ranger/ranger/wiki/Official-user-guide)

`cw` - rename highlighted file

To move file, press `dd`, then navigate to the desired directory and press `p`, files are like text in `ranger`.

`:touch` - create new file

## Minimalistic Software

[Suckless Software](https://suckless.org/rocks/)

## Pipe recently used command to a file

```
history | tail -n 20 | grep git >> ./cheat-sheet-git.md
```

## `pgrep`

grep for process, e.g. `pgrep slack`

`pgrep slack | xargs kill` - kill slack

## `column`

format output to multiple columns

## `sed`

`sed --in-place '/breakpoint()/d' ./**/*.py` - remove all breakpoints from python files

`sed -n 200p foo.md` - print line 200 of file `foo.md`

## Links to this note

[Index Cheat Sheet](index-cheat-sheet.md)
