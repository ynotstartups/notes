# Cheat Sheet Ubuntu

## Use dual monitor

`xrandr --output DP1 --primary --auto --right-of eDP1 --output eDP1 --auto`

- `eDP1` is the built-in monitor
- `DP1` or others is the external monitor

Tips:

use `autorandr -s foo` to save the config

## Setup Chinese Input

Inspired by https://leimao.github.io/blog/Ubuntu-Gaming-Chinese-Input/

1. sudo install fcitx and fcitx-pinyin
1. go to ubuntu system settings Language and Region, click `Manage Installed Languages`
1. change input method system from `ibus` to `fcitx 4`
1. run `fcitx-configtool` in command line
1. click `+` to add `pinyin`

Then we can press `Ctrl + Space` to switch to pinyin input!
