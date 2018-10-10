screen school_outside_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 561
        ypos 437
        focus_mask True
        idle "images/school/school_outside/morning/door1_morning_idle.png"
        hover "images/school/school_outside/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Школа (Закрыта)")
        action [Play ("sound", "sfx/door_locked.mp3"),Jump("school_outside_morning1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_outside/morning/door2_morning_idle.png"
        hover "images/school/school_outside/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "В тренажерный зал (закрыт)")
        action Jump("school_outside_morning1")
        unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
