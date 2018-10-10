screen caroline_room_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_evening1")]

    if caroline_room_evening_scene4 == True and Caroline_points == 1:
        imagebutton:
            xpos 1167
            ypos 347
            focus_mask True
            idle "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/caroline_b1.png"
            hover "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_evening_scene4_label")]
            hovered Show("displayTextScreen", displayText = "Кэролайн")
            unhovered Hide("displayTextScreen")
    if caroline_room_evening_scene4 == 3 and Caroline_points == 1:
        imagebutton:
            xpos 1167
            ypos 347
            focus_mask True
            idle "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/caroline_b1.png"
            hover "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/caroline_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("caroline_room_evening_scene4_label")]
            hovered Show("displayTextScreen", displayText = "Кэролайн")
            unhovered Hide("displayTextScreen")


screen caroline_room_evening_not_clickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"

    if caroline_room_evening_scene4 == True:
        imagebutton:
            xpos 1167
            ypos 347
            focus_mask True
            idle "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/caroline_b1.png"

    if caroline_room_evening_scene4 == 3:
        imagebutton:
            xpos 1167
            ypos 347
            focus_mask True
            idle "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/caroline_b1.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
