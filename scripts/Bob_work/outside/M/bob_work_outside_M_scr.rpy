




screen bob_work_outside_M_scr:

    key "hide_windows" action NullAction()
    imagebutton:
        xpos 966
        ypos 223
        focus_mask True
        idle "images/Bob_work/outside/D/B1_D.png"
        hover "images/Bob_work/outside/D/B1_D_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Приемная")
            action [Hide("displayTextScreen"),Play ("sound", "sfx/door_open.mp3"),Jump("bob_entrance_M1")]
            unhovered Hide("displayTextScreen")


    imagebutton:
        xpos 137
        ypos 296
        focus_mask True
        idle "images/Bob_work/outside/M/B2_M.png"
        hover "images/Bob_work/outside/M/B2_M_hover.png"
        hovered Show("displayTextScreen", displayText = "Автомобиль")
        if clickable == True:
            action [Hide("displayTextScreen"),Jump("bob_car_label")]
            unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
