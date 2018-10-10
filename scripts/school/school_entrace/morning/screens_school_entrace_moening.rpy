screen school_entrance_morning:
    imagebutton:
        xpos 215
        ypos 254
        focus_mask True
        idle "images/school/school_entrance/morning/door1_morning_idle.png"
        hover "images/school/school_entrance/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Выход из школы")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_outside_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1651
        ypos 152
        focus_mask True
        idle "images/school/school_entrance/morning/door2_morning_idle.png"
        hover "images/school/school_entrance/morning/door2_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Коридор")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_morning1")]
            unhovered Hide("displayTextScreen")


    imagebutton:
        xpos 1259
        ypos 232
        focus_mask True
        idle "images/school/school_entrance/morning/school_entrance_locker_morning.png"
        hover "images/school/school_entrance/morning/school_entrance_locker_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Шкафчик")
            action [Hide("displayTextScreen"),Jump("school_lockerv1_morning_label")]
            unhovered Hide("displayTextScreen")

    if not "img6_exit_school_corridor_card" in gallery_photos.storage:
        imagebutton:
            xpos 944
            ypos 259
            focus_mask True
            idle "images/secret_gallery/Bonus/ExitSchoolCorridor Card.png"
            hover "images/secret_gallery/Bonus/ExitSchoolCorridor Card_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), addgimage("img6_exit_school_corridor_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                hovered Show("displayTextScreen", displayText = "Секретная карта")
                unhovered Hide("displayTextScreen")

    if not "img23_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 738
            ypos 522
            focus_mask True
            idle "images/secret_gallery/Bonus/B23.png"
            hover "images/secret_gallery/Bonus/B23_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img23_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
