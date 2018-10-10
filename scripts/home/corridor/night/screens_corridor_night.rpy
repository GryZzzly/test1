screen corridor_night:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 937
        ypos 195
        focus_mask True
        idle "images/home/corridor/night/painting_B1.png"
        hover "images/home/corridor/night/painting_B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Картина")
            action [Hide("displayTextScreen"),Jump("painting_corridor_label")]
            unhovered Hide("displayTextScreen")
    if caroline_door_open == True:
        imagebutton:
            xpos 178
            ypos 167
            focus_mask True
            idle "images/home/corridor/night/door1_night_idle.png"
            hover "images/home/corridor/night/door1_night_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Спальня Кэролайн")
                action [Play ("sound", "sfx/door_open.mp3"),Jump("caroline_room_night1")]
                unhovered Hide("displayTextScreen")
    if caroline_door_open == False:
        imagebutton:
            xpos 178
            ypos 167
            focus_mask True
            idle "images/home/corridor/night/door1_night_idle.png"
            hover "images/home/corridor/night/door1_night_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Спальня Кэролайн")
                action [Hide("displayTextScreen"),Play ("sound", "sfx/door_locked.mp3"),Jump("caroline_room_locked_label")]
                unhovered Hide("displayTextScreen")
    if caroline_spare_key.selected and caroline_door_open == False:
        imagebutton:
            xpos 178
            ypos 167
            focus_mask True
            idle "images/home/corridor/night/door1_night_idle.png"
            hover "images/home/corridor/night/door1_night_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Спальня Кэролайн")
                action [SetVariable ("caroline_door_open", True),Play ("sound", "sfx/door_open.mp3"),Jump("caroline_room_night1")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 640
        ypos 224
        focus_mask True
        idle "images/home/corridor/night/door2_night_idle.png"
        hover "images/home/corridor/night/door2_night_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Моя спальня")
            action [Play ("sound", "sfx/door_open.mp3"),Jump("mc_room_night1")]
            unhovered Hide("displayTextScreen")
    if sara_door_open == True:
        imagebutton:
            xpos 1279
            ypos 200
            focus_mask True
            idle "images/home/corridor/night/door3_night_idle.png"
            hover "images/home/corridor/night/door3_night_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Спальня Сары")
                action [Play ("sound", "sfx/door_open.mp3"),Jump("sister_nerdy_night1")]
                unhovered Hide("displayTextScreen")
    if sara_door_open == False:
        imagebutton:
            xpos 1279
            ypos 200
            focus_mask True
            idle "images/home/corridor/night/door3_night_idle.png"
            hover "images/home/corridor/night/door3_night_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Спальня Сары")
                action [Play ("sound", "sfx/door_locked.mp3"),Hide("displayTextScreen"),Jump("sis_nerdy_door_locked")]
                unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1660
        ypos 0
        focus_mask True
        idle "images/home/corridor/night/door4_night_idle.png"
        hover "images/home/corridor/night/door4_night_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Гостинная")
            action [Jump("salon_night1")]
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/LeaveNormal.png"
            hover "images/game_gui/LeaveHover.png"
            action [Play ("sound", "sfx/door_open.mp3"),Jump("entrace_night1")]

screen corridor_night_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 937
        ypos 195
        focus_mask True
        idle "images/home/corridor/night/painting_B1.png"
    if caroline_door_open == True:
        imagebutton:
            xpos 178
            ypos 167
            focus_mask True
            idle "images/home/corridor/night/door1_night_idle.png"
    if caroline_door_open == False:
        imagebutton:
            xpos 178
            ypos 167
            focus_mask True
            idle "images/home/corridor/night/door1_night_idle.png"
    imagebutton:
        xpos 640
        ypos 224
        focus_mask True
        idle "images/home/corridor/night/door2_night_idle.png"
    if sara_door_open == True:
        imagebutton:
            xpos 1279
            ypos 200
            focus_mask True
            idle "images/home/corridor/night/door3_night_idle.png"
    if sara_door_open == False:
        imagebutton:
            xpos 1279
            ypos 200
            focus_mask True
            idle "images/home/corridor/night/door3_night_idle.png"
    imagebutton:
        xpos 1660
        ypos 0
        focus_mask True
        idle "images/home/corridor/night/door4_night_idle.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
