label teacher_room1_morning1:
    $ can_hide_windows = False
    if day_time == 1:
        jump teacher_room1_morning2
    if day_time == 2:
        jump teacher_room1_day1

label teacher_room1_morning2:
    $ can_hide_windows = False
    hide screen displayTextScreen
    scene teacher_room1_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen teacher_room1_morning_notclickable
    call screen teacher_room1_morning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
