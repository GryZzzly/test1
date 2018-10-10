screen salon_night:
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/night/door1_night_idle.png"
        hover "images/home/salon/night/door1_night_hover.png"
        hovered Show("displayTextScreen", displayText = "Коридор")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("corridor_night1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/night/door2_night_idle.png"
        hover "images/home/salon/night/door2_night_hover.png"
        hovered Show("displayTextScreen", displayText = "Кухня")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("kitchen_night1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/night/door3_night_idle.png"
        hover "images/home/salon/night/door3_night_hover.png"
        if renpy.loadable("patch.rpy"):
            hovered Show("displayTextScreen", displayText = "Спальня родителей")
        if not renpy.loadable("patch.rpy"):
            hovered Show("displayTextScreen", displayText = "Гостинная")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("parents_bedroom_night1")]
        unhovered Hide("displayTextScreen")
    if ml_ml_and_f_bedroom_night_scene_v1 == True and ml_mc_room_night_scene3 == False and ml_points == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/salon/night/door3_night_idle.png"
            hover "images/home/salon/night/door3_night_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Спальня родителей")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Гостинная")
            action [Hide("displayTextScreen"),Jump("ml_ml_and_f_bedroom_night_scene_v1_label")]
            unhovered Hide("displayTextScreen")
    if ml_ml_and_f_bedroom_night_scene_v1 == False and ml_can_ml_and_f_bedroom_night_scene_v1 == False and ml_mc_room_night_scene3 == False and ml_points == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/salon/night/door3_night_idle.png"
            hover "images/home/salon/night/door3_night_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Спальня родителей")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Гостинная")
            action [Hide("displayTextScreen"),Jump("ml_ml_and_f_bedroom_night_scene_v1_label")]
            unhovered Hide("displayTextScreen")
    if MLR2_NS1 == True  and ml_points >= 2:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/salon/night/door3_night_idle.png"
            hover "images/home/salon/night/door3_night_hover.png"
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Спальня родителей")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Гостинная")
            action [Hide("displayTextScreen"),Jump("MLR2_NS1_label")]
            unhovered Hide("displayTextScreen")

    if slon_money == True:
        imagebutton:
            xpos 1402
            ypos 464
            focus_mask True
            idle "images/home/salon/night/Money Salon Night.png"
            hover "images/home/salon/night/Money Salon Night_hover.png"
            hovered Show("displayTextScreen", displayText = "Деньги")
            action [Hide("displayTextScreen"),Jump("salon_money_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 529
        ypos 140
        focus_mask True
        idle "images/home/salon/night/paint_b1.png"
        hover "images/home/salon/night/paint_b1_hover.png"
        hovered Show("displayTextScreen", displayText = "Картина")
        action [Hide("displayTextScreen"),Jump("salon_paint_label")]
        unhovered Hide("displayTextScreen")

screen salon_night_notclickable:
    imagebutton:
        xpos 529
        ypos 140
        focus_mask True
        idle "images/home/salon/night/paint_b1.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/night/door1_night_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/night/door2_night_idle.png"
        hover "images/home/salon/night/door2_night_hover.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/salon/night/door3_night_idle.png"



    if slon_money == True:
        imagebutton:
            xpos 1402
            ypos 464
            focus_mask True
            idle "images/home/salon/night/Money Salon Night.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
