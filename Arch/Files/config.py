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

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show run")),

    # Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    Key([mod], "b", lazy.spawn("firefox")),

    Key([mod], "s", lazy.spawn("scrot -e \'mv $f ~/Pictures\'"))
]

groups = [Group(i) for i in ["NET", "DEV", "TERM", "ETC"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    'border_focus': '33ccff',
    'border_width': 1,
    'margin': 4
}
#border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4
layouts = [
    layout.Columns(**layout_conf),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntoMono Nerd Font',
    fontsize=20,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground="#f1ffff",
                    background="#0f101a",
                    font='UbuntuMono Nerd Font',
                    fontsize=20,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border="#F07178",
                    this_current_screen_border="#33ccff",
                    this_screen_border="#353c4a",
                    other_current_screen_border="#0f101a",
                    other_screen_border="#0f101a",
                    disable_drag=True
                ),
                widget.WindowName(
                    foreground="#33ccff",
                    background="#0f101a",
                    fontsize=18,
                    font='UbuntuMono Nerd Font',
                    padding=10
                ),
                widget.TextBox(
                    text="",
                    background="#0f101a",
                    foreground="#f3e408",
                    fontsize=37,
                    font='UbuntuMono Nerd Font',
                    padding=-2
                ),
                widget.TextBox(
                    text="",
                    font='UbuntoMono Nerd Font',
                    fontsize=30,
                    foreground="#0f101a",
                    background="#f3e408"
                ),
                widget.CheckUpdates(
                    no_update_string="0",
                    background="#f3e408",
                    colour_have_updates="#0f101a",
                    colour_no_updates="#0f101a",
                    update_interval=5,
                    custom_command="checkupdates"
                ),
                widget.TextBox(
                    text="",
                    background="#f3e408",
                    foreground="#66ccff",
                    fontsize=37,
                    font='UbuntuMono Nerd Font',
                    padding=-2
                ),
                widget.CurrentLayoutIcon(
                    background="#66ccff",
                    foreground="#0f101a",
                    scale=0.7
                ),
                widget.CurrentLayout(
                    background="#66ccff",
                    foreground="#0f101a",
                ),
                widget.TextBox(
                    text="",
                    background="#66ccff",
                    foreground="#ff6600",
                    fontsize=37,
                    font='UbuntuMono Nerd Font',
                    padding=-2
                ),
                widget.TextBox(
                    text="",
                    font='UbuntoMono Nerd Font',
                    fontsize=30,
                    foreground="#0f101a",
                    background="#ff6600"
                ),
                widget.Clock(
                    format='%d/%m/%Y - %H:%M',
                    foreground="#0f101a",
                    background="#ff6600",
                    font='UbuntuMono Nerd Font'
                    ),
                widget.TextBox(
                    text="",
                    background="#ff6600",
                    foreground="#0f101a",
                    fontsize=37,
                    font='UbuntuMono Nerd Font',
                    padding=-2
                ),
                widget.Systray(
                    background="#0f101a"
                ),
                widget.TextBox(
                    text="",
                    font='UbuntuMono Nerd Font',
                    padding=10,
                    fontsize=20,
                    background="#0f101a",
                    foreground="#66ccff",
                )
            ],
            24,
            opacity=0.95
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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
], border_focus='#33ccff')
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"