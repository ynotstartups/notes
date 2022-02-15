# Cheat Sheet Ubuntu

## Use dual monitor

`xrandr --output DP1 --primary --auto --right-of eDP1 --output eDP1 --auto`

## Setup for office

1. set `Xft.dpi: 144` in `~/.Xresources`
1. `sudo systemctl restart display-manager` - restart xsession
1. `light_set` - set xbacklight
