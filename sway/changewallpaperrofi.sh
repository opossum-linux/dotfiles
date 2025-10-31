#!/bin/sh

swaybg -i $( ls ~/Pictures/Wallpapers/* | rofi -dmenu) &&
notify-send -t -800 "wallpaper changed!!"
