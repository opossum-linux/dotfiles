#!/bin/sh

swaybg -i $( ls ~/Documents/Wallpapers/* | rofi -dmenu) &&
notify-send -t -800 "wallpaper changed!!"
