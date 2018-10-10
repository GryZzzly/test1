screen therapist_room_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/therapist_room/morning/door1_morning_idle.png"
        hover "images/school/therapist_room/morning/door1_morning_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor3_day1")]
        hovered Show("displayTextScreen", displayText = "Школьный коридор")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 919
        ypos 245
        focus_mask True
        idle "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_scene1_v1_b1.png"
        hover "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_scene1_v1_b1_hover.png"
        action [Hide("displayTextScreen"),Jump("judy_menu_v1_label")]
        hovered Show("displayTextScreen", displayText = "Джуди")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1293
        ypos 300
        focus_mask True
        idle "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_cupboardv1.png"
        hover "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_cupboardv1_hover.png"
        action [Hide("displayTextScreen"),Jump("judy_day_cupboardv1_label")]
        hovered Show("displayTextScreen", displayText = "Шкаф")
        unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
