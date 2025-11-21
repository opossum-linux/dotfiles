#!/bin/sh

wal -i $( ls ~/Wallpapers/* | rofi -dmenu) &&
notify-send -t -800 "wallpaper changed!!"
