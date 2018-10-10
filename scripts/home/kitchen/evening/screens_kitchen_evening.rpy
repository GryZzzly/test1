screen kitchen_evening:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door1_evening_idle.png"
        hover "images/home/kitchen/evening/door1_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Гостинная")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("salon_evening1")]
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door2_evening_idle.png"
        hover "images/home/kitchen/evening/door2_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Вход")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("entrance2_evening1")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door3_evening_idle.png"
        hover "images/home/kitchen/evening/door3_evening_hover.png"
        hovered Show("displayTextScreen", displayText = "Ванная")
        action [Play ("sound", "sfx/door_open.mp3"),Jump("bathroom_evening1")]
        unhovered Hide("displayTextScreen")

    if ml_evening_bathroom_scene_v1 == True and ml_points == 1:
        if camera.selected:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/evening/door3_evening_idle.png"
                hover "images/home/kitchen/evening/door3_evening_hover.png"
                hovered Show("displayTextScreen", displayText = "Ванная")
                action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_scene_v1_label")]
                unhovered Hide("displayTextScreen")
        else:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/morning/door3_morning_idle.png"
                hover "images/home/kitchen/morning/door3_morning_hover.png"
                hovered Show("displayTextScreen", displayText = "Ванная")
                action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_locked_scene_v1_label")]
                unhovered Hide("displayTextScreen")
    if ml_evening_bathroom_scene_v1 == False and ml_can_evening_bathroom_scene_v1 == False and ml_points == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/evening/door3_evening_idle.png"
            hover "images/home/kitchen/evening/door3_evening_hover.png"
            hovered Show("displayTextScreen", displayText = "Ванная")
            action [Hide("displayTextScreen"),Jump("ml_evening_bathroom_scene_v1_label")]
            unhovered Hide("displayTextScreen")
    if MLR2_ES1 == True and ml_points == 2:
        imagebutton:
            xpos 637
            ypos 330
            focus_mask True
            idle "images/home/kitchen/evening/scenes/MLR2_ES1/b1.png"
            hover "images/home/kitchen/evening/scenes/MLR2_ES1/b1_hover.png"
            action [Hide("displayTextScreen"),Jump("MLR2_ES1_label")]
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Мама")
            else:
                hovered Show("displayTextScreen", displayText = "Линда")
            unhovered Hide("displayTextScreen")

screen kitchen_evening_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door1_evening_idle.png"

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door2_evening_idle.png"


    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/home/kitchen/evening/door3_evening_idle.png"


    if ml_evening_bathroom_scene_v1 == True and ml_points == 1:
        if camera.selected:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/evening/door3_evening_idle.png"

        else:
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                idle "images/home/kitchen/morning/door3_morning_idle.png"

    if ml_evening_bathroom_scene_v1 == False and ml_can_evening_bathroom_scene_v1 == False and ml_points == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/home/kitchen/evening/door3_evening_idle.png"
    if MLR2_ES1 == True and ml_points == 2:
        imagebutton:
            xpos 637
            ypos 330
            focus_mask True
            idle "images/home/kitchen/morning/scenes/MLR2_ES1/b1.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
