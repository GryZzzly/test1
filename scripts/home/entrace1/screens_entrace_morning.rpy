screen entrace1_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrace1/morning/Entrance_door_morning_idle.png"
        hover "images/home/entrace1/morning/Entrance_door_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Вход в дом")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_morning1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/entrace1/morning/entrance_path_morning_idle.png"
        hover "images/home/entrace1/morning/entrance_path_morning_hover.png"
        hovered Show("displayTextScreen", displayText = "Вход")
        action [Jump("entrance2_morning1")]
        unhovered Hide("displayTextScreen")

    if not "img3_home_entrance_card" in gallery_photos.storage:
        imagebutton:
            xpos 1843
            ypos 607
            focus_mask True
            idle "images/secret_gallery/Bonus/EntranceHouse SecretCard.png"
            hover "images/secret_gallery/Bonus/EntranceHouse SecretCard_hover.png"
            action [Hide("displayTextScreen"), addgimage("img3_home_entrance_card") ,Jump("home_entrance_card")]
            hovered Show("displayTextScreen", displayText = "Секретная карта")
            unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
