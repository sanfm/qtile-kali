import os
#import re
import subprocess
#import socket
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
#terminal = guess_terminal()
terminal = "qterminal"
myBrowser = "firefox"
myFileManager = "thunar"
home = os.path.expanduser('~')

# Font and font size for arrow char
arrowFontSize = 45
selectFont = "FiraCode Nerd Font"



keys = [
    Key([mod], "b",
        lazy.spawn(myBrowser),
        desc='Launch Web Browser'
        ),
    Key([mod], "f",
        lazy.spawn(myFileManager),
        desc='Launch File Manager'
        ),
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc='Launch Terminal'
        ),
    Key([mod, "shift", "control"], "l",
        lazy.spawn("betterlockscreen -l"),
        desc="Lock screen"
        ),
    Key([mod, "control"], "p",
        lazy.spawn("" + home + "/.local/bin/powermenu"),
        desc="Launch Power menu"
        ),
    Key([mod], "d",
        lazy.spawn("rofi -show drun"),
        desc="Launch Rofi menu"
        ),
        
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    # Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
               }

layouts = [
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme)
    # Try more layouts by unleashing below layouts.
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
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




colors = [["#282a36", "#282a36"],	# panel background
          ["#434758", "#434758"],	# background for current screen tab
          ["#ffffff", "#ffffff"],	# font color for group names
          ["#ff5555", "#ff5555"],	# background color for layout widgets
          ["#000000", "#000000"],	# background color for other screen tabs
          ["#A77AC4", "#A77AC4"],	# dark green gradiant for other screen tabs
          ["#50fa7b", "#50fa7b"],	# background color for network widget
          ["#7197E7", "#7197E7"],	# background color for pacman widget
          ["#9AEDFE", "#9AEDFE"],	# background color for cmus widget
          ["#000000", "#000000"],	# background color for clock widget
          ["#434758", "#434758"],]	# background color for systray widget


widget_defaults = dict(
    #font="sans",
    font = selectFont,
    fontsize=20,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
            	widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[2],
                       background = colors[0]
                       ),
                #widget.CurrentLayout(),
                widget.GroupBox(
			            #font = "Ubuntu Bold",
                       	#fontsize = 9,
                       	margin_y = 3,
                       	margin_x = 0,
                       	padding_y = 5,
                       	padding_x = 5,
                       	borderwidth = 1,
                       	active = colors[2],
                       	inactive = colors[2],
                       	rounded = False,
                       	#highlight_color = colors[5],
                       	highlight_method = "block",
                       	this_current_screen_border = colors[5],
                       	this_screen_border = colors[1],
                       	other_current_screen_border = colors[0],
                       	other_screen_border = colors[0],
                       	foreground = colors[2],
                       	background = colors[0]
                	),
                widget.Prompt(),
                widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.WindowName(
                	foreground = colors[5],
                	background = colors[0],
                	padding = 5
                	),
                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                widget.Systray(),
                widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[5],
                       padding = -7,
                       #fontsize = 37
                       fontsize = arrowFontSize
                       ),
                widget.TextBox(
                       #text = '〖〗',
                       #text = '【】',
                       text = '',
                       background = colors[5],
                       foreground = colors[2],
                       padding = 5,
                       fontsize = 16
                       ),
                widget.CurrentLayout(
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                    ),
                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[7],
                       padding = -7,
                       #fontsize = 37
                       fontsize = arrowFontSize
                       ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Net(
                       interface = "eth0",
                       format = ': {down} ↓↑ {up}',
                       foreground = colors[2],
                       background = colors[7],
                       padding = 5
                       ),
		widget.TextBox(
                       text = '',
                       background = colors[7],
                       foreground = colors[5],
                       padding = -7,
                       #fontsize = 37
                       fontsize = arrowFontSize
                       ),
                widget.KeyboardLayout(
                       foreground = colors[2],
                       background = colors[5],
                       fmt = 'Keyboard: {}',
                       padding = 5
                       ),
                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[7],
                       padding = -7,
                       #fontsize = 37
                       fontsize = arrowFontSize
                       ),
                widget.Clock(
                       foreground = colors[2],
                       background = colors[7],
                       format = "%A, %B %d - %H:%M "
                       ),
                widget.TextBox(
                       text = '',
                       background = colors[7],
                       foreground = colors[5],
                       padding = -7,
                       #fontsize = 37
                       fontsize = arrowFontSize
                       ),
                widget.QuickExit(
		       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
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
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup
def autostart():
    #home = os.path.expanduser('/home/kali/.config/qtile/autostart.sh')
    home = os.path.expanduser('/home/kali/.config/qtile/autostart.sh')
    subprocess.run([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
