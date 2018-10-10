screen parents_bedroom_morning:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_morning1")]

    if ml_bedroom_morning_scene5 == True and ml_can_bedroom_morning_scene5 == True:
        imagebutton:
            xpos 30
            ypos 223
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/ml_b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/ml_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("ml_bedroom_morning_scene5_v1_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Мама")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Линда")
            unhovered Hide("displayTextScreen")



    if ml_bedroom_book_scene == True and ml_points == 1:
        imagebutton:
            xpos 1576
            ypos 551
            focus_mask True
            idle "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/Book_b1.png"
            hover "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/Book_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("ml_bedroom_book_scene_v1_label")]
            hovered Show("displayTextScreen", displayText = "Книга")
            unhovered Hide("displayTextScreen")
    if ml_bedroom_morning_scene6 == True:
        imagebutton:
            xpos 394
            ypos 222
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/ml_b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/ml_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("ml_bedroom_morning_scene6_v1_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Мама")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Линда")
            unhovered Hide("displayTextScreen")
    if moeny_parents_room == True:
        imagebutton:
            xpos 1092
            ypos 656
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/money_b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/money_b1_hover.png"
            action [Hide("displayTextScreen"),Jump("ml_bedroom_morning_money_label")]
            hovered Show("displayTextScreen", displayText = "Деньги")
            unhovered Hide("displayTextScreen")
    if ml_points >=2:
        imagebutton:
            xpos 1087
            ypos 295
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/b1.png"
            hover "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/b1_hover.png"
            action [Hide("displayTextScreen"),Jump("MLR2_MS1_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Мама")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Линда")
            unhovered Hide("displayTextScreen")

screen parents_bedroom_morning_notclickable:

    key "hide_windows" action NullAction()
    if ml_bedroom_morning_scene5 == True and ml_can_bedroom_morning_scene5 == True and ml_bedroom_book_scene == False:
        imagebutton:
            xpos 30
            ypos 223
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene5_v1/ml_b1.png"




    if ml_bedroom_book_scene == True and ml_points == 1:
        imagebutton:
            xpos 1576
            ypos 551
            focus_mask True
            idle "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/Book_b1.png"

    if ml_bedroom_morning_scene6 == True:
        imagebutton:
            xpos 394
            ypos 222
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/ml_b1.png"

    if moeny_parents_room == True:
        imagebutton:
            xpos 1092
            ypos 656
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/money_b1.png"
    if ml_points ==2:
        imagebutton:
            xpos 1087
            ypos 295
            focus_mask True
            idle "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/b1.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
