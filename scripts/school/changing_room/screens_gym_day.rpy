screen changing_room_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/changing_room/morning/door1_morning_idle.png"
        hover "images/school/changing_room/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Тренажерный зал")
        clicked Jump("gym_day1")
        unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
