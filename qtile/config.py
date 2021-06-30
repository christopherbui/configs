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
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])



mod = "mod1"
terminal = "alacritty"
browser = "firefox"
file_manager = "nautilus"


keys = [
    # Rofi
    Key([mod], "space", lazy.spawn("rofi -combi-modi drun -font 'Fira Code Nerd Font 20' -show combi -icon-theme 'Papirus' -show-icons")),


    # Lock Screen
    Key([mod],"l", lazy.spawn("betterlockscreen -l")),


    # Lock Screen + Suspend
    Key([mod], "s", lazy.spawn("betterlockscreen -s")),

    
    # Shutdown
    Key([mod, "shift"], "Delete", lazy.spawn("shutdown now")),


    # Reboot
    Key([mod, "shift"], "r", lazy.spawn("reboot")),


    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 2%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 2%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),


    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 1%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 1%-")),


    # Nightlight
    Key([mod], "n", lazy.spawn("redshift -P -O 5000")),
    Key([mod, "shift"], "n", lazy.spawn("redshift -x")),


    # Browser
    Key([mod], "b", lazy.spawn(browser)),


    # File Manager
    Key([mod], "f", lazy.spawn(file_manager)),


    # VS Code
    Key([mod], "c", lazy.spawn("code")),


    # Switch between windows
    Key([mod], "Tab", lazy.layout.down(), desc="Move focus down"),
    Key([mod, "shift"], "Tab", lazy.layout.up(), desc="Move focus up"),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod], "Up", lazy.layout.shuffle_up(), desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),


    # Toggle between different layouts as defined below
    Key([mod, "shift"], "l", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "12345"]

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

layout_theme = {"border_width":4,
"margin":10,
"border_focus": "f92672",
"border_normal":"66d9ef"}

layouts = [
    #layout.Columns(border_focus_stack='#d75f5f'),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(**layout_theme),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="SF Pro Display",
                    fontsize=18,
                    highlight_method="block",
                    rounded=False,
                    padding_x=5,
                    padding_y=5,
                    active="#ffffff",
                    inactive="#959595",
                    this_current_screen_border="45d5f0",
                    urgent_border="f92672",
                    disable_drag=True
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                ),
                widget.Prompt(
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="fd971f"
                ),
                widget.WindowName(
                    font="SF Pro Display",
                    fontsize=18,
                    format="  {name}",
                    max_char=50,
                    foreground="ffffff",
                    background="45d5f0"
                ),
                #widget.Spacer(),
                widget.Systray(),
                widget.TextBox(
                    text = "│",
                    fontsize=14,
                    padding=5,
                    foreground="ffffff"
                ),
                widget.TextBox(
                    text="",
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="f92672"
                ),
                widget.CPU(
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="ffffff",
                    format="CPU {load_percent}%"
                ),
                widget.TextBox(
                    text="    ",
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="a6e22e"
                ),
                widget.Memory(
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="ffffff",
                    format="{MemUsed: } /{MemTotal: } MB"
                ),
                widget.TextBox(
                    text="    ",
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="66d9ef"
                ),
                widget.PulseVolume(
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="ffffff"
                ),
                widget.Battery(
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="ffffff",
                    charge_char="",
                    discharge_char="",
                    format="    {char}  {percent:2.0%}"

                ),
                widget.TextBox(
                    text="     ",
                    font="SF Pro Display",
                    fontsize=18,
                    foreground="ae81ff"
                ),
                widget.Clock(
                    font="SF Pro Display",
                    fontsize=18,
                    format="%a  %m/%d/%Y   %H : %M : %S",
                    foreground="ffffff"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                )
            ],
            28,
            background = "#272822",
            opacity = 1
            #margin = [5,12,0,12]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
