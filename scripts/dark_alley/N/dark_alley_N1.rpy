

label dark_alley_N1:
    hide screen displayTextScreen
    scene dark_alley_Nbg
    $ can_map = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    $ can_hide_windows = False
    call screen dark_alley_N_scr
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
