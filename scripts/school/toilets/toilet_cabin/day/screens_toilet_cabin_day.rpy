screen toilet_cabin_day:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Play ("sound", "sfx/toilet cabin.mp3"),Jump("toilets_day1")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
