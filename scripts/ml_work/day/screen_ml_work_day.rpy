screen ml_work_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 234
        ypos 193
        focus_mask True
        idle "/images/ml_work/day/ml_work_door1.png"
        hover "/images/ml_work/day/ml_work_door1_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("ml_work_room1_day1")]
        if clickable == True:
            if renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Офис мамы")
            if not renpy.loadable("patch.rpy"):
                hovered Show("displayTextScreen", displayText = "Офис Линды")
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/LeaveNormal.png"
        hover "images/game_gui/LeaveHover.png"
        if clickable == True:
            action [Play ("sound", "sfx/door_open.mp3"),Hide("displayTextScreen"), Hide("ml_work_day"), Hide("map_button"), Jump("map_label")]
            unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
