#! /bin/bash
 
set +e

waybar -c ~/.config/waybar/config.jsonc -s ~/.config/waybar/style.css &

systemctl --user unmask xdg-desktop-portal-wlr &

dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &

dbus-daemon --session --address=unix:path=$XDG_RUNTIME_DIR/bus &

dunst &
/usr/lib/xdg-desktop-portal-wlr &
/usr/lib/xfce-polkit/xfce-polkit &
wlsunset -l 54.9 -L 48.3 &
wl-clip-persist --clipboard regular --reconnect-tries 0 &
wl-paste --type text --watch cliphist store &
waypaper --restore &
lipse -listen &
