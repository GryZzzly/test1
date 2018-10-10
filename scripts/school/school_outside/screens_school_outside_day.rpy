screen school_outside_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 561
        ypos 437
        focus_mask True
        idle "images/school/school_outside/morning/door1_morning_idle.png"
        hover "images/school/school_outside/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Школа")
        action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("school_entrance_day1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_outside/morning/door2_morning_idle.png"
        hover "images/school/school_outside/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "В спортзал")
        clicked Jump("gym_day1")
        unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
