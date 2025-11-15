#!/bin/sh

feh --bg-scale $( ls ~/Wallpapers/* | rofi -dmenu) &&
notify-send -t -800 "wallpaper changed!!"
