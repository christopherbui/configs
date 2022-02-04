# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Autostart
import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

home = os.path.expanduser("~")

mod = "mod1"
terminal = "alacritty"
app_launcher = "rofi -combi-modi drun -font 'Fira Code Nerd Font 18' -show drun -icon-theme 'Papirus' -show-icons -width 48 -theme-str 'element-icon {size:2.8ch;}' -lines 10"
browser = "firefox"
file_manager = "nautilus"
music = "spotify --force-device-scale-factor=1.2"


keys = [
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Rofi
    Key([mod], "space", lazy.spawn(app_launcher)),

    # Lock Screen
    Key([mod],"l", lazy.spawn("betterlockscreen -l --off 60")),

    # Lock Screen + Suspend
    Key([mod], "s", lazy.spawn("betterlockscreen -s")),
    
    # Shutdown
    Key([mod, "shift"], "Delete", lazy.spawn("alacritty -e" + home + "/.config/qtile/shutdown.sh")),

    # Reboot
    Key([mod, "shift"], "r", lazy.spawn("alacritty -e" + home + "/.config/qtile/reboot.sh")),

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 2%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 2%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 1%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 1%-")),
    Key(["control", "shift"], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 1")),

    # Nightlight
    Key([mod], "n", lazy.spawn("redshift -P -O 4900")),
    Key([mod, "shift"], "n", lazy.spawn("redshift -x")),

    # Screenshot
    Key([], "Print", lazy.spawn("gnome-screenshot")),

    # Browser
    Key([mod], "b", lazy.spawn(browser)),

    # File Manager
    Key([mod], "f", lazy.spawn(file_manager)),

    # Text Editor
    Key([mod], "g", lazy.spawn("gedit")),

    # VS Code
    Key([mod], "c", lazy.spawn("code")),

    # Typora
    Key([mod], "t", lazy.spawn("typora")),

    # PDF Reader
    Key([mod], "p", lazy.spawn("evince")),

    # Discord
    Key([mod], "d", lazy.spawn("discord")),

    # Music
    Key([mod], "m", lazy.spawn(music)),

    # Prompt widget
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Switch between windows
    Key([mod], "Tab", lazy.layout.down(), desc="Move focus down"),
    Key([mod, "shift"], "Tab", lazy.layout.up(), desc="Move focus up"),

    # Move windows
    Key([mod], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize windows
    Key([mod, "control"], "h",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # Toggle layouts
    Key([mod, "shift"], "l", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Restart / Shutdown Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = [Group(i) for i in "1234567"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

# Colors
background = "#282828"
foreground = "#ebdbb2"

color={
"black":  "#282828",
"red":    "#fb4934",
"green":  "#b8bb26",
"yellow": "#fabd2f",
"blue":   "#83a598",
"magenta":"#d3869b",
"cyan":   "#8ec07c",
"white":  "#ebdbb2",
}

# Layout defaults
layout_theme = {"border_width":4,
"margin":8,
"border_focus":color["yellow"],
"border_normal":color["black"]}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Stack(**layout_theme, num_stacks=1),
    layout.Floating(**layout_theme),
]

# Widget defaults
widget_defaults = dict(
    font='FiraCode Nerd Font Bold',
    fontsize=18,
    padding=3
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="FiraCode Nerd Font",
                    highlight_method="line",
                    highlight_color=background,
                    rounded=False,
                    padding_x=5,
                    padding_y=4,
                    active=foreground,
                    inactive="#988BA2",
                    this_current_screen_border=color["cyan"],
                    urgent_border=color["red"],
                    disable_drag=True,
                    margin_y=3,
                    spacing=4,
                    use_mouse_wheel=False
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                ),
                widget.CurrentLayoutIcon(
                    scale=0.7
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                ),
                widget.Prompt(
                    foreground=color["green"]
                ),
                widget.Spacer(),
                widget.Clock(
                    format="%H:%M:%S",
                    #format="%H:%M",
                    foreground=color["red"],
                    padding=6
                ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=24
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=34,
                    foreground=foreground
                ),
                widget.WidgetBox(
                    font='FontAwesome5 Free',
                    foreground=color["magenta"],
                    fontsize=20,
                    close_button_location='right',
                    text_closed='',
                    text_open='',
                    widgets=[
                        widget.Memory(
                            foreground=color["magenta"],
                            measure_mem="G",
                            format="{MemUsed:.2f} GB",
                            #mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e htop")},
                            padding=10
                        )
                    ]
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=34,
                    foreground=foreground
                ),
                widget.WidgetBox(
                    font='FontAwesome5 Free',
                    foreground=color["yellow"],
                    fontsize=20,
                    close_button_location='right',
                    text_closed='',
                    text_open='',
                    widgets=[
                        widget.Battery(
                            foreground=color["yellow"],
                            charge_char="",
                            discharge_char="",
                            low_foreground=color["red"],
                            low_percentage=0.25,
                            format="{char} {percent:2.0%}",
                            padding=10
                        )
                    ]
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=34,
                    foreground=foreground
                ),
                widget.WidgetBox(
                    font='FontAwesome5 Free',
                    foreground=color["blue"],
                    fontsize=20,
                    close_button_location='right',
                    text_closed='',
                    text_open='',
                    widgets=[
                        widget.PulseVolume(
                            foreground=color["blue"],
                            padding=10
                        )
                    ]
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=34,
                    foreground=foreground
                ),
                widget.WidgetBox(
                    font='FontAwesome5 Free',
                    foreground=color["green"],
                    fontsize=20,
                    close_button_location='right',
                    text_closed='',
                    text_open='',
                    widgets=[
                        widget.Clock(
                            format="%a %b %d",
                            foreground=color["green"],
                            #mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e /home/alphard/.config/qtile/calendar.sh")},
                            padding=10
                        )
                    ]
                ),
                widget.Sep(
                    linewidth=0,
                    size_percent=60,
                    padding=16,
                    foreground=foreground
                ),
            ],
            32,
            border_width=[4, 4, 4, 4],
            border_color=["000000", "000000", "000000", "000000"],
            background = background + "D9",
            opacity = 1,
            margin=[6, 8, 0, 8]
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
