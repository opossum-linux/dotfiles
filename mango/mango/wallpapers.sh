#!/bin/sh

swww img $( ls ~/Pictures/Wallpapers/* | wofi --show dmenu) &&
notify-send -t -800 "wallpaper changed!!"
