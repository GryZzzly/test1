label school_outside_day1:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen school_entrace_day
    hide screen gym_day
    hide screen map
    scene school_outside_day
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen school_outside_day
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
