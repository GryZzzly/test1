screen classroom1_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 485
        ypos 162
        focus_mask True
        idle "images/school/classroom1/morning/door1_morning_idle.png"
        hover "images/school/classroom1/morning/door1_morning_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Школьный коридор")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor1_day1")]
            unhovered Hide("displayTextScreen")


    if not "img8_mc_classroom_card" in gallery_photos.storage:
        imagebutton:
            xpos 1893
            ypos 1039
            focus_mask True
            idle "images/secret_gallery/Bonus/MCClassroom Card.png"
            hover "images/secret_gallery/Bonus/MCClassroom Card_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"), addgimage("img8_mc_classroom_card") ,SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
