


screen bob_entrance_M_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1163
        ypos 294
        focus_mask True
        idle "images/Bob_work/entrance/M/B1.png"
        hover "images/Bob_work/entrance/M/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Приемная")
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("bob_reception_morning1")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 6
        ypos 45
        focus_mask True
        if company_profit == 0:
            idle "images/Bob_work/entrance/M/B2.png"
            hover "images/Bob_work/entrance/M/B2_hover.png"
        if company_profit == 1:
            idle "images/Bob_work/entrance/M/B3.png"
            hover "images/Bob_work/entrance/M/B3_hover.png"
        if company_profit == 2:
            idle "images/Bob_work/entrance/M/B4.png"
            hover "images/Bob_work/entrance/M/B4_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Диаграмма Компании")
            action [Hide("displayTextScreen"),Jump("bob_receptiondiagram")]
            unhovered Hide("displayTextScreen")

    if not "img13_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 593
            ypos 272
            focus_mask True
            idle "images/secret_gallery/Bonus/B13.png"
            hover "images/secret_gallery/Bonus/B13_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img13_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("bob_work_outside_morning1")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
