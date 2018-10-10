image bob_statue_p1 = "/images/Bob_work/office/M/Statue.jpg"
image bob_fireplace_p1 = "/images/Bob_work/office/M/Fireplace.jpg"
image bob_tableR_p1 = "/images/Bob_work/office/M/tableR/tableR.jpg"
image bob_tableR_p2 = "/images/Bob_work/office/M/tableR/tableR2.jpg"
image bob_tableL_p1 = "/images/Bob_work/office/M/tableL/tableL.jpg"
image bob_tableL_p2 = "/images/Bob_work/office/M/tableL/tableL2.jpg"
image bob_redstatue_p1 = "/images/Bob_work/office/M/table.jpg"
default bob_carkeys_take = False
default bob_carkeys_put = True

default can_safe_note = False




label bob_statue_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene bob_statue_p1 with dissolve
    $ can_hide_windows = True
    MC "(Я никогда не понимал, почему классические художники решили не лепить головы или руки.)"
    MC "(Я имею в виду, лицо-одна из самых интересных частей любой статуи.)"
    $ can_hide_windows = False
    jump bob_office_M1



label bob_fireplace_label:
    scene bob_fireplace_p1
    call screen bob_fireplace_scr


screen bob_fireplace_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 327
        ypos 433
        focus_mask True
        idle "images/Bob_work/office/M/Fireplace/B1.png"
        hover "images/Bob_work/office/M/Fireplace/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Head Statue")
            action [Hide("displayTextScreen"),Jump("bob_headstatue_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 698
        ypos 25
        focus_mask True
        idle "images/Bob_work/office/M/Fireplace/B2.png"
        hover "images/Bob_work/office/M/Fireplace/B2_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Painting")
            action [Hide("displayTextScreen"),Jump("bob_painting_label")]
            unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1537
        ypos 547
        focus_mask True
        idle "images/Bob_work/office/M/Fireplace/B3.png"
        hover "images/Bob_work/office/M/Fireplace/B3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Statue")
            action [Hide("displayTextScreen"),Jump("bob_statue1_label")]
            unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]
label bob_headstatue_label:
    show screen bob_fireplace_scr
    $ clickable = False
    MC "(Синий мраморный бюст. Он ярко блестит - кто-то отполировал это до совершенства!)"
    MC "(Я почти вижу свое отражение в нем!)"
    $ clickable = True
    jump bob_fireplace_label

label bob_painting_label:
    show screen bob_fireplace_scr
    $ clickable = False

    MC "(В этой картине есть что-то тревожное.)"
    MC "(Это похоже на грязный тротуар. Кто, черт возьми, хотел бы повесить такое в своем офисе?)"

    $ clickable = True
    jump bob_fireplace_label

label bob_statue1_label:
    show screen bob_fireplace_scr
    $ clickable = False
    MC "(Возможно это световой индикатор?)"
    MC "(Или, может быть, это нос человека?)"
    MC "(Боже! Я ненавижу абстрактное искусство.)"
    $ clickable = True
    jump bob_fireplace_label



label bob_tableR_label:
    scene bob_tableR_p1
    call screen bob_tableR_scr


screen bob_tableR_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 640
        ypos 458
        focus_mask True
        idle "images/Bob_work/office/M/tableR/B1.png"
        hover "images/Bob_work/office/M/tableR/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Открыто")
            action [Play ("sound", "sfx/drawer_op.wav"),Hide("displayTextScreen"),Jump("bob_tableRopen_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]


label bob_tableRopen_label:
    $ renpy.pause(0.2,hard= True)
    scene bob_tableR_p2
    call screen bob_tableRopen_scr

screen bob_tableRopen_scr:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]


label bob_tableL_label:
    scene bob_tableL_p1
    call screen bob_tableL_scr

screen bob_tableL_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 705
        ypos 425
        focus_mask True
        idle "images/Bob_work/office/M/tableL/B1.png"
        hover "images/Bob_work/office/M/tableL/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Открыто")
            action [Play ("sound", "sfx/drawer_op.wav"),Hide("displayTextScreen"),Jump("bob_tableLopen_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]


label bob_tableLopen_label:
    $ renpy.pause(0.2,hard = True)
    scene bob_tableL_p2
    call screen bob_tableLopen_scr

screen bob_tableLopen_scr:
    key "hide_windows" action NullAction()
    if bob_safenote not in inventory.items and day_time == 2 and Zv2_MS2_companyname == 2 and can_safe_note == True:
        imagebutton:
            xpos 850
            ypos 561
            focus_mask True
            idle "images/Bob_work/office/M/tableL/B2.png"
            hover "images/Bob_work/office/M/tableL/B2_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Примечание к сейфу")
                action [Hide("displayTextScreen"),Jump("bob_safenote_label")]
                unhovered Hide("displayTextScreen")
    if bob_safenote in inventory.items and bob_safenote.selected and day_time == 2 and Zv2_MS2_companyname == 2 and can_safe_note == True:
        imagebutton:
            xpos 850
            ypos 561
            focus_mask True
            idle "images/Bob_work/office/M/tableL/B3.png"
            hover "images/Bob_work/office/M/tableL/B3_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Put Safe Note")
                action [Hide("displayTextScreen"),Jump("bob_safenoteput_label")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]


label bob_safenote_label:
    $ clickable = False
    show screen bob_tableLopen_scr
    MC "Хммм... код сейфа. Не очень мудро, оставить его лежать здесь. Кто-то может найти его."
    $ inventory.add(bob_safenote)
    $ clickable = True
    jump bob_tableLopen_label

label bob_safenoteput_label:
    $ clickable = False
    show screen bob_tableLopen_scr
    $ inventory.drop(bob_safenote)
    MC "Оставим это здесь."

    $ bob_safenote.selected = False
    $ clickable = True
    jump bob_tableLopen_label

label bob_redstatue_label:
    scene bob_redstatue_p1
    call screen bob_redstatue_scr

screen bob_redstatue_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 466
        ypos 62
        focus_mask True
        idle "images/Bob_work/office/M/B10.png"
        hover "images/Bob_work/office/M/B10_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Красная статуя")
            action [Hide("displayTextScreen"),Jump("bob_redstatue2_label")]
            unhovered Hide("displayTextScreen")
    if bob_carkeys_take == False and day_time == 1:
        imagebutton:
            xpos 1024
            ypos 512
            focus_mask True
            idle "images/Bob_work/office/M/B1.png"
            hover "images/Bob_work/office/M/B1_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Ключи от машины")
                action [Hide("displayTextScreen"),Jump("bob_carkeys_label")]
                unhovered Hide("displayTextScreen")
    if bob_carkeys_put == False and bob_carkeys.selected:
        imagebutton:
            xpos 1024
            ypos 512
            focus_mask True
            idle "images/Bob_work/office/M/B2.png"
            hover "images/Bob_work/office/M/B1.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Положить ключи от машины")
                action [Hide("displayTextScreen"),Jump("bob_carkeys_put_label")]
                unhovered Hide("displayTextScreen")
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]


label bob_redstatue2_label:
    $ clickable = False
    show screen bob_redstatue_scr
    MC "(Это очень круто! Похоже, что это сделано из красного стекла, или, может быть, даже нефрита!)"
    MC "(Она должно быть кошка? Или, может быть, пантера?)"
    $ clickable = True
    jump bob_redstatue_label

label bob_carkeys_label:
    show screen bob_redstatue_scr
    $ clickable = False
    MC "О! Это - ключи от папиной машины. Но почему там два? Другой должно быть запасной?"
    $ inventory.add(bob_carkeys)
    $ bob_carkeys_take = True
    $ clickable = True
    $ bob_carkeys_put = False
    $ bob_carkeys.selected = False
    jump bob_redstatue_label

label bob_carkeys_put_label:
    show screen bob_redstatue_scr
    $ clickable = False
    $ inventory.drop(bob_carkeys)
    $ bob_carkeys_take = False
    $ bob_carkeys_put = True
    $ active_item = None
    $ bob_carkeys.selected = False
    if renpy.loadable("patch.rpy"):
        MC "Нужно вернуть папины ключи."
    else:
        MC "Нужно вернуть ключи Боба."
    $ clickable = True
    jump bob_redstatue_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
