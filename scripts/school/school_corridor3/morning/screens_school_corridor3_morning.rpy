screen school_corridor3_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 472
        ypos 124
        focus_mask True
        idle "images/school/school_corridor3/morning/door1_morning_idle.png"
        hover "images/school/school_corridor3/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Кабинет терапевта")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("therapist_room_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 672
        ypos 0
        focus_mask True
        idle "images/school/school_corridor3/morning/door2_morning_idle.png"
        hover "images/school/school_corridor3/morning/door2_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "школьный коридор")
            clicked Jump("school_corridor1_morning1")
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1322
        ypos 122
        focus_mask True
        idle "images/school/school_corridor3/morning/door3_morning_idle.png"
        hover "images/school/school_corridor3/morning/door3_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Комната директора")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("headmaster_room_morning1")]
            unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
