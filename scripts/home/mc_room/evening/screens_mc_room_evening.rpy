screen mc_room_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/evening/door1_evening_idle.png"
        hover "images/home/mc_room/evening/door1_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Коридор")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/evening/bed_evening_idle.png"
        hover "images/home/mc_room/evening/bed_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Кровать")
        clicked Jump("day_time_changer")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1453
        ypos 412
        focus_mask True
        idle "images/home/mc_room/evening/pc_idle.png"
        hover "images/home/mc_room/evening/pc_hover.png"
        hovered Show("displayTextScreen", displayText = "Компьютер")
        action [Play ("sound", "sfx/mouse_click.mp3"),Hide("displayTextScreen"),Jump("computer_menu")]
        unhovered Hide("displayTextScreen")

    if not "img4_mc_room_card" in gallery_photos.storage:
        imagebutton:
            xpos 23
            ypos 906
            focus_mask True
            idle "images/secret_gallery/Bonus/MCBedroom SecretCard.png"
            hover "images/secret_gallery/Bonus/MCBedroom SecretCard_hover.png"
            action [Hide("displayTextScreen"), addgimage("img4_mc_room_card") ,Jump("mc_room_card")]
            hovered Show("displayTextScreen", displayText = "Секретная карта")
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1493
        ypos 319
        focus_mask True
        idle "images/home/mc_room/evening/s_gallery.png"
        hover "images/home/mc_room/evening/s_gallery_hover.png"
        hovered Show("displayTextScreen", displayText = "Секретная Галерея")
        action [Hide("displayTextScreen"), Show("secret_gallery"),]
        unhovered Hide("displayTextScreen")

    if Neighboor_spy_mc_room == True:
        imagebutton:
            xpos 384
            ypos 227
            focus_mask True
            idle "images/home/mc_room/evening/window_evening.png"
            hover "images/home/mc_room/evening/window_evening_hover.png"
            hovered Show("displayTextScreen", displayText = "Окно")
            action [Hide("displayTextScreen"), Jump("neighboor_spy_v1_label"),]
            unhovered Hide("displayTextScreen")
    if caroline_mc_room_evening_scene2 == True:
        imagebutton:
            xpos 735
            ypos 227
            focus_mask True
            idle "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/caroline_b1.png"
            hover "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/caroline_b1_hover.png"
            hovered Show("displayTextScreen", displayText = "Кэролайн")
            action [Hide("displayTextScreen"), Jump("caroline_mc_room_evening_scene2_label"),]
            unhovered Hide("displayTextScreen")
    if caroline_mc_room_evening_scene3 == True and caroline_mc_room_can_evening_scene3 == True:
        imagebutton:
            xpos 717
            ypos 217
            focus_mask True
            idle "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/caroline_b1.png"
            hover "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/caroline_b1_hover.png"
            hovered Show("displayTextScreen", displayText = "Кэролайн")
            action [Hide("displayTextScreen"), Jump("caroline_mc_room_evening_scene3_label"),]
            unhovered Hide("displayTextScreen")

    if inventory.money < 10:
        imagebutton:
            xpos 14
            ypos 670
            focus_mask True
            idle "images/home/mc_room/evening/b1.png"
            hover "images/home/mc_room/evening/b1_hover.png"
            hovered Show("displayTextScreen", displayText = "Деньги")
            action [Hide("displayTextScreen"), Jump("money_less10"),]
            unhovered Hide("displayTextScreen")
screen mc_room_evening_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/evening/door1_evening_idle.png"
        hover "images/home/mc_room/evening/door1_evening_hover.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/mc_room/evening/bed_evening_idle.png"
        hover "images/home/mc_room/evening/bed_evening_hover.png"


    imagebutton:
        xpos 1453
        ypos 412
        focus_mask True
        idle "images/home/mc_room/evening/pc_idle.png"
        hover "images/home/mc_room/evening/pc_hover.png"

    if not "img4_mc_room_card" in gallery_photos.storage:
        imagebutton:
            xpos 23
            ypos 906
            focus_mask True
            idle "images/secret_gallery/Bonus/MCBedroom SecretCard.png"
            hover "images/secret_gallery/Bonus/MCBedroom SecretCard_hover.png"


    imagebutton:
        xpos 1493
        ypos 319
        focus_mask True
        idle "images/home/mc_room/evening/s_gallery.png"
        hover "images/home/mc_room/evening/s_gallery_hover.png"


    if Neighboor_spy_mc_room == True:
        imagebutton:
            xpos 384
            ypos 227
            focus_mask True
            idle "images/home/mc_room/evening/window_evening.png"
            hover "images/home/mc_room/evening/window_evening_hover.png"
    if caroline_mc_room_evening_scene2 == True:
        imagebutton:
            xpos 735
            ypos 227
            focus_mask True
            idle "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/caroline_b1.png"
    if caroline_mc_room_evening_scene3 == True and caroline_mc_room_can_evening_scene3 == True:
        imagebutton:
            xpos 717
            ypos 217
            focus_mask True
            idle "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/caroline_b1.png"

    if inventory.money < 10:
        imagebutton:
            xpos 14
            ypos 670
            focus_mask True
            idle "images/home/mc_room/evening/b1.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
