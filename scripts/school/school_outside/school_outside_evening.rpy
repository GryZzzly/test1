label school_outside_evening1:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen school_entrace_evening
    hide screen gym_evening
    hide screen corridor_evening
    hide screen map
    scene school_outside_evening
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen school_outside_evening
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
