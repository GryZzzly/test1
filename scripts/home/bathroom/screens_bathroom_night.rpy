screen bathroom_night:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/door_open.mp3"),Jump("kitchen_night1")]
        hovered Show("displayTextScreen", displayText = "Кухня")
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 393
        ypos 401
        focus_mask True
        idle "images/home/bathroom/morning/scenes/bath_event/bath_night_b2.png"
        hover "images/home/bathroom/morning/scenes/bath_event/bath_night_b2_hover.png"
        action [Hide("displayTextScreen"),Jump("bath_event_label")]
        hovered Show("displayTextScreen", displayText = "Ванная")
        unhovered Hide("displayTextScreen")

screen bathroom_night_notclickable:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"

    imagebutton:
        xpos 393
        ypos 401
        focus_mask True
        idle "images/home/bathroom/morning/scenes/bath_event/bath_night_b2.png"
        hover "images/home/bathroom/morning/scenes/bath_event/bath_night_b2_hover.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
