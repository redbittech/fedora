##IMPORTS##

from libqtile import bar
from libqtile import widget
from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import os
import subprocess


mod = "mod4"
terminal = "alacritty"


##KEYBINDS##

keys = [
    # Window behaviour    
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),

    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    
    # Program/PC behaviour
    
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    Key([mod, "Shift"], "p", lazy.spawn("systemctl poweroff"), desc = "Shutdown pc"),
    
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    Key([mod, "Shift"], "z", lazy.spawn(os.path.expanduser("~/.config/qtile/Scripts/i3lock")), desc="Lock screen using i3lock"),
    
    Key([mod, "Shift"], "f", lazy.spawn("pcmanfm")),
    
    Key([mod], "f", lazy.spawn("alacritty -e ranger"), desc="Open file manager in terminal"),
    
    Key([mod], "w", lazy.spawn("firefox https://duckduckgo.com")),
    
    Key([mod], "v", lazy.spawn("pavucontrol")),
    
    Key([mod], "m", lazy.spawn("alacritty -e cmus")),

    Key([mod, "Shift"], "e", lazy.spawn("alacritty -e nvim")),

    Key([mod], "F3", lazy.spawn("amixer -c 0 -q set Master 3dB+")),
   
    Key([mod], "F2", lazy.spawn("amixer -c 0 -q set Master 3dB-")),
    
    Key([mod], "F1", lazy.spawn("amixer -c 0 -q set Master toggle")),
    
    Key([mod], "F12", lazy.spawn("brightnessctl s 10%+")),
    
    Key([mod], "F11", lazy.spawn("brightnessctl s 10%-")),

]
   
##GROUPS##

groups = [Group(i) for i in "123456"]
	
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

##LAYOUT##

layouts = [
	# layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(border_focus=["#9ff6f7"], border_normal=["#505c6e"], border_width=2, margin=8),
    # layout.Matrix(),
    layout.MonadTall(border_focus=["#9ff6f7"], border_normal=["#505c6e"], border_width=2, border_margin=8),
    layout.Max(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

##BAR##

screens = [
    Screen(
        wallpaper = "~/Wallpapers/049.png",
        wallpaper_mode = "fill",
        top=bar.Bar(
            [

		widget.CurrentLayout(
			# background = ["#2e2246"],
			scale = 0.75,
			font  = "FiraCode Nerd Font, Regular",
		),

        widget.GroupBox(
            fontsize = 14,
            margin_x = 15,
            margin_y = 4,
            borderwidth = 0,
            font = "FiraCode Nerd Font, Regular",
            # background = ["#2e2246"],
		    # active = ["#b643a0"],
            inactive = ["#555555"],
            block_highlight_text_color = ["#056abe"],
            rounded = True,
            disable_drag = True,

        ),

        widget.Prompt(
            fontsize = 12,
            font = "FiraCode Nerd Font, Regular",
            cursor = True,
            cursor_color = '056abe',
            record_history = True,
            max_history = 20,
            ignore_dups_history = True,
        ),


        widget.Spacer(
            length = 350,

        ),

        widget.WindowName(
            fontsize = 12,
            font = "FiraCode Nerd Font, Regular",

        ),
		
		widget.Battery(
			# background = ["#2e2246"],
			# foreground = ["#59a6f6"],
			padding = 3,
			charge_char = '󰂄',
			discharge_char = '󰂀',
			empty_char = '󰂃',
			full_char = '󰁹',
			format = '{char} {percent:2.0%}',
			update_interval = 60,
			font = "FiraCode Nerd Font, Regular",
            		fontsize = 12,
		),

		widget.Volume(
			# background = ["#2e2246"],
			# foreground = ["#6970c1"],
			padding = 7,
			fmt = 'Volume: {}',
			channel = 'Master',
			font = "FiraCode Nerd Font, Regular",
			limit_max_volume = True,
		),

		widget.Net(
			# background = ["#2e2246"],
			# foreground = ["#d0d1f3"],
			format = '⬆ {up} ⬇ {down}',
			prefix = 'M',
			padding = 3,
			disconnected = 'N/A', 
			update_interval = 10,
			font = "FiraCode Nerd Font, Regular",

		),		

        widget.Clock(
            format = "%H:%M",
            fontsize = 12,
            padding = 10,
            # background = ["#2e2246"],
            font = "FiraCode Nerd Font, Regular",
        ),

                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
            ],
            24,
            margin = [2, 2, 2 ,2],
            background = ["#111111"]
        ),
    ),
]

##MOUSE BEHAVIOUR##

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True 
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


@hook.subscribe.startup_once
def autostart():
   # chmod +x ~/.config/qtile/autostart.sh
   path = os.path.expanduser('~/.config/qtile/autostart.sh')
   subprocess.call([path])



# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

