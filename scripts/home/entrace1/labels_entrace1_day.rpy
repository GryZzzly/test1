label entrace1_day1:
    $ can_hide_windows = False
    hide screen displayTextScreen
    hide screen corridor_day
    hide screen map
    scene entrace1_day
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen entrace1_day
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
