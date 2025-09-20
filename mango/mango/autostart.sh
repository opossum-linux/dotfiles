#! /bin/bash
 
set +e

systemctl --user unmask xdg-desktop-portal-wlr &

dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &

dbus-daemon --session --address=unix:path=$XDG_RUNTIME_DIR/bus &

mako &
/usr/lib/xdg-desktop-portal-wlr &
/usr/lib/xfce-polkit/xfce-polkit &
wl-clip-persist --clipboard regular --reconnect-tries 0 &
wl-paste --type text --watch cliphist store &
wlsunset -l 39.9 -L 116.3^C &
swww-daemon

