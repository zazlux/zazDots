#!/usr/bin/bash

# Set background color.
swaybg -i "$HOME/.walls/dark-night.jpg" >/dev/null 2>&1 &

# Launch a panel such as yambar or waybar.
waybar >/dev/null 2>&1 &

dunst >/dev/null 2>&1 &

