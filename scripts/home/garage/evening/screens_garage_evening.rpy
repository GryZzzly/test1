screen garage_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/garage/morning/Garage_door_exit_idle.png"
        hover "images/home/garage/morning/Garage_door_exit_hover.png"
        if clickable == True and MLR2_ES3 == False:

            hovered Show("displayTextScreen", displayText = "Вход")
            action [Play ("sound", "sfx/garage door.mp3"),Jump("entrance2_evening1")]
            unhovered Hide("displayTextScreen")
        if clickable == True and MLR2_ES3 == True:
            hovered Show("displayTextScreen", displayText = "Вход")
            action [Hide("displayTextScreen"),Jump("MLR2_ES3_cantleave_label")]
            unhovered Hide("displayTextScreen")

    if not "img1_garage_card" in gallery_photos.storage:
        imagebutton:
            xpos 1130
            ypos 460
            focus_mask True
            idle "images/secret_gallery/Bonus/Garage SecretCard.png"
            hover "images/secret_gallery/Bonus/Garage SecretCard_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Секретное фото")
                action [Hide("displayTextScreen"),addgimage("img1_garage_card"), Jump("garage_card")]
                unhovered Hide("displayTextScreen")

    if not "img21_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 502
            ypos 882
            focus_mask True
            idle "images/secret_gallery/Bonus/B21.png"
            hover "images/secret_gallery/Bonus/B21_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img21_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if not "img22_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1616
            ypos 192
            focus_mask True
            idle "images/secret_gallery/Bonus/B22.png"
            hover "images/secret_gallery/Bonus/B22_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img22_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")

    if MLR2_ES3 == True:
        imagebutton:
            xpos 613
            ypos 468
            focus_mask True
            idle "images/home/garage/morning/b1.png"
            hover "images/home/garage/morning/b1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Автомобиль")
                action [Hide("displayTextScreen"),Jump("MLR2_ES3_label")]
                unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
