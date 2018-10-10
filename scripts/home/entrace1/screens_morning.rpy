screen entrace_morning:
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/map_button_idle.png"
        hover "images/game_gui/map_button_idle.png"
        clicked [Show("map"), Hide("map_button")]
        hovered Show("displayTextScreen", displayText = "door")
        unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
