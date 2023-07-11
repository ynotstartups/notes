# How To Use Vim For Markdown

## Use prose linter

- install prose linter write-good globally
- use plugin ale to display errors

## Vim shortcut to autocorrect wrongly spell word

```vim
" leader z to autocorrect words and move cursor to the end of the word
nnoremap <silent> <leader>z 1z=<CR>g;e
```

Use builtin `zg` to mark good and bad words

## plasticboy/vim-markdown

- for syntax highlight in code block e.g.

```python
print("hello world")
```

- for `gx` to open link

[test](https://github.com/plasticboy/vim-markdown)

## vim-surround shortcuts

```vim
" `code`
let b:surround_{char2nr("c")} = "`\r`"
" **bold**
let b:surround_{char2nr("b")} = "**\r**"
" link
let b:surround_{char2nr("l")} = "[\r]()"
" _italic_
let b:surround_{char2nr("i")} = "_\r_"
```

## Bash Alias

```bash
vmarkdown() {
    cd ~/Documents/personal-docs/messages || exit

    vim "$(date --iso-8601=minutes)".md
}

vslack() {
    cd ~/Documents/personal-docs/messages || exit

    vim "$(date --iso-8601=minutes)".slack
}
```

## Custom text-object

`al` - to represent a link
