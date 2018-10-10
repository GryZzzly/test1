screen school_corridor3_day:
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_corridor3/morning/door1_morning_idle.png"
        hover "images/school/school_corridor3/morning/door1_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Кабинет терапевта")
        clicked Jump("therapist_room_day1")
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_corridor3/morning/door2_morning_idle.png"
        hover "images/school/school_corridor3/morning/door2_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Школьный коридор")
        clicked Jump("school_corridor1_day1")
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_corridor3/morning/door3_morning_idle.png"
        hover "images/school/school_corridor3/morning/door3_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Комната директора")
        clicked Jump("headmaster_room_day1")
        unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
