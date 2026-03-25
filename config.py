import os
import libqtile.resources
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Group
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

# Put this in in your config.py
from pathlib import Path
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = Path('~/.config/qtile/autostart.sh').expanduser()
    subprocess.run(home)

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == "tk"
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

mod = "mod1"
mod1 = "mod4"
terminal = guess_terminal()

lazy.core.hide_cursor()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod1,], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod1,], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod1,], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod1,], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),  
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "o", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}", lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

groups = [
    Group("1", label="Discord"),
    Group("2", label="Browser"),
    Group("3", label="Cmus"),
    Group("4", label="Comics"),
    Group("5", label="Terminal"),
]

layout_theme = {
    "border_width": 1,
    "margin": 4,
    "border_focus": "#afd787",  # Color for focused window
    "border_normal": "#121212"   # Color for unfocused windows
}


layout_themeno = {
    "border_width": 1,
    "margin": 0,
    "border_focus": "#afd787",  # Color for focused window
    "border_normal": "#121212"   # Color for unfocused windows
}



layouts = [
    #layout.Columns(**layout_theme),
    layout.Max(border_width=0, margin=0),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_themeno),
    # layout.MonadWide(),
    # layout.RatioTile(**layout_theme),
     layout.Tile(**layout_theme),
    #layout.TreeTab(
     #    font = "Ubuntu Bold",
      #   fontsize = 11,
      #   border_width = 0,
      #   bg_color = "#333333",
         #active_bg = "#444444",
      #   active_fg = "555555",
      #   inactive_bg = "#666666",
      #   inactive_fg = "#000000",
      #   padding_left = 8,
      #   padding_x = 8,
      #   padding_y = 6,
      #   sections = ["ONE", "TWO", "THREE"],
      #   section_fontsize = 10,
      #   section_fg = "#888888",
      #   section_top = 15,
      #   section_bottom = 15,
       #  level_shift = 8,
       #  vspace = 3,
       #  panel_width = 240
       #  ),
    # layout.VerticalTile(),
      #layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font = "DepartureMono Nerd Font Mono Bold",
    fontsize=13,
    margin = 0,
    padding=7,
)
extension_defaults = widget_defaults.copy()

logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(padding=6,margin = 4, inactive = '#d6dbe5'),
                widget.Prompt(foreground="#f7b26b"),
                widget.WindowName(foreground="#e6eef6"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Cmus(playing_color="c48ff7", padding=16, fontsize=14),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            30,
            background="#0f172080"
        ),
    ),
]

# Drag floating layouts.


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 12

idle_inhibitors = []  # type: list

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
