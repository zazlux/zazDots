#!/bin/bash

if [[ $(pidof swaybg) ]]; then
  pkill swaybg
fi

wal -q -n --iterative -i ~/Pictures/niribg

notify-send -i "$(< "${HOME}/.walls")" "Theme Changed"

if [[ $(pidof waybar) ]]; then
  killall -SIGUSR2 waybar
fi

swaybg -m fill -i "$(< "${HOME}/.walls")"

/home/void/.config/mako/update-theme.sh

niri msg action do-screen-transition --delay-ms 300

