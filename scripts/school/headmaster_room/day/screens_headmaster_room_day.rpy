screen headmaster_room_day:
    key "hide_windows" action NullAction()



    if not "img20_sec_card" in gallery_photos.storage:
        imagebutton:
            xpos 1905
            ypos 510
            focus_mask True
            idle "images/secret_gallery/Bonus/B20.png"
            hover "images/secret_gallery/Bonus/B20_hover.png"
            if clickable == True:
                action [Hide("displayTextScreen"),addgimage("img20_sec_card"), SetVariable("clickable", False),Show("card_found_alert")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("school_corridor3_morning1")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
