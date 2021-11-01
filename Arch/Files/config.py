from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [

    # Move betweens windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Change windows position
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Change windows size
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Apps
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    Key([mod], "m", lazy.spawn("rofi -show run")),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    Key([mod], "b", lazy.spawn("firefox")),

    Key([mod], "s", lazy.spawn("scrot -e \'mv $f ~/Pictures\'")),

    # Toggle layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Close window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Manager options
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile")
]

groups = [Group(i) for i in ["NET", "DEV", "TERM", "ETC"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    'border_focus': '33ccff',
    'border_normal': '042b27',
    'border_width': 2,
    'margin': 5
}

layouts = [
    layout.Columns(**layout_conf),
    layout.Matrix(**layout_conf),
    layout.Max()
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
                    foreground="#67e531",
                    fontsize=37,
                    font='UbuntuMono Nerd Font',
                    padding=-2
                ),
                widget.TextBox(
                    text="",
                    font='UbuntoMono Nerd Font',
                    fontsize=30,
                    foreground="#0f101a",
                    background="#67e531"
                ),
                widget.CheckUpdates(
                    no_update_string="0",
                    background="#67e531",
                    colour_have_updates="#0f101a",
                    colour_no_updates="#0f101a",
                    update_interval=5,
                    custom_command="checkupdates"
                ),
                widget.TextBox(
                    text="",
                    background="#67e531",
                    foreground="#fdab05",
                    fontsize=37,
                    font='UbuntuMono Nerd Font',
                    padding=-2
                ),
                widget.CurrentLayoutIcon(
                    background="#fdab05",
                    foreground="#0f101a",
                    scale=0.7
                ),
                widget.CurrentLayout(
                    background="#fdab05",
                    foreground="#0f101a",
                ),
                widget.TextBox(
                    text="",
                    background="#fdab05",
                    foreground="#d969fc",
                    fontsize=37,
                    font='UbuntuMono Nerd Font',
                    padding=-2
                ),
                widget.TextBox(
                    text="",
                    font='UbuntoMono Nerd Font',
                    fontsize=30,
                    foreground="#0f101a",
                    background="#d969fc"
                ),
                widget.Clock(
                    format='%d/%m/%Y - %H:%M',
                    foreground="#0f101a",
                    background="#d969fc",
                    font='UbuntuMono Nerd Font'
                    ),
                widget.TextBox(
                    text="",
                    background="#d969fc",
                    foreground="#0f101a",
                    fontsize=37,
                    font='UbuntuMono Nerd Font',
                    padding=-2
                ),
                widget.Systray(
                    background="#0f101a"
                ),
                widget.QuickExit(
                    default_text="⏻",
                    countdown_format="{}",
                    countdown_start=4,
                    font='UbuntuMono Nerd Font',
                    fontsize=20,
                    padding=10,
                    background="#0f101a",
                    foreground="#66ccff"
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

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  
    Match(wm_class='makebranch'),  
    Match(wm_class='maketag'),  
    Match(wm_class='ssh-askpass'),  
    Match(title='branchdialog'),  
    Match(title='pinentry'),  
], border_focus='#33ccff')
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wmname = "LG3D"
