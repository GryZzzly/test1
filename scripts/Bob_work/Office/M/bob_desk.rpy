image bob_desk_p1 = "/images/Bob_work/office/M/desk/Desk.jpg"

default car_book_put = False
label bob_desk_label:
    scene bob_desk_p1
    call screen bob_desk_scr


screen bob_desk_scr:
    key "hide_windows" action NullAction()



    imagebutton:
        xpos 0
        ypos 175
        focus_mask True
        idle "images/Bob_work/office/M/desk/B1.png"
        hover "images/Bob_work/office/M/desk/B1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Книги")
            action [Hide("displayTextScreen"),Jump("bob_deskbooks_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 977
        ypos 205
        focus_mask True
        idle "images/Bob_work/office/M/desk/B2.png"
        hover "images/Bob_work/office/M/desk/B2_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Ноутбук")
            action [Hide("displayTextScreen"),Jump("bob_desklaptop_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 558
        ypos 224
        focus_mask True
        idle "images/Bob_work/office/M/desk/B3.png"
        hover "images/Bob_work/office/M/desk/B3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Документы")
            action [Hide("displayTextScreen"),Jump("bob_deskpapers_label")]
            unhovered Hide("displayTextScreen")
    if day_time == 2 and Zv2_MS2_companyname == 1:
        imagebutton:
            xpos 782
            ypos 201
            focus_mask True
            idle "images/Bob_work/office/M/desk/B4.png"
            hover "images/Bob_work/office/M/desk/B4_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Отчеты")
                action [Hide("displayTextScreen"),Jump("bob_deskraports_label")]
                unhovered Hide("displayTextScreen")

    if car_book_put == False and bob_carbook.selected:
        imagebutton:
            xpos 283
            ypos 215
            focus_mask True
            idle "images/Bob_work/office/M/desk/B5.png"
            hover "images/Bob_work/office/M/desk/B6.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Положить книгу")
                action [Hide("displayTextScreen"),Jump("bob_deskcarbookput_label")]
                unhovered Hide("displayTextScreen")

    if car_book_put == True:
        imagebutton:
            xpos 283
            ypos 215
            focus_mask True
            idle "images/Bob_work/office/M/desk/B6.png"
            hover "images/Bob_work/office/M/desk/B6_hover.png"
            if clickable == True:
                hovered Show("displayTextScreen", displayText = "Книга")
                action [Hide("displayTextScreen"),Jump("bob_deskcarbook_label")]
                unhovered Hide("displayTextScreen")
    if Bob_work_minigame == True:
        imagebutton:
            xpos 786
            ypos 316
            focus_mask True
            idle "images/Bob_work/office/M/desk/Minigame.png"
            hover "images/Bob_work/office/M/desk/Minigame_hover.png"
            if clickable == True and day_time == 2:
                hovered Show("displayTextScreen", displayText = "Документы")
                action [Hide("displayTextScreen"),Jump("bob_deskminigame_label")]
                unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 119
        ypos 998
        focus_mask True
        idle "images/Bob_work/office/M/desk/B7.png"
        hover "images/Bob_work/office/M/desk/B7_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Сейф")
            action [Hide("displayTextScreen"),Jump("bob_safe_label")]
            unhovered Hide("displayTextScreen")

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]
label bob_deskbooks_label:
    show screen bob_desk_scr
    $ clickable = False
    if renpy.loadable("patch.rpy"):
        MC "Папины книги."
    else:
        MC "Книги Боба."
    MC "Думаю, у него здесь много свободного времени."
    $ clickable = True
    jump bob_desk_label

label bob_desklaptop_label:
    show screen bob_desk_scr
    $ clickable = False
    if renpy.loadable("patch.rpy"):
        MC "Папин ноутбук. Мне не нужно использовать его."
    else:
        MC "Ноутбук Боба. Мне не нужно использовать его."
    $ clickable = True
    jump bob_desk_label

label bob_deskpapers_label:
    show screen bob_desk_scr
    $ clickable = False
    MC "Только бумаги. Некоторые скучные рабочие вещи."
    $ clickable = True
    jump bob_desk_label


label bob_deskraports_label:

    show screen bob_desk_scr
    $ clickable = False
    $ Zv2_MS2_companyname_found = 1
    MC "Хммм.. Несколько отчетов..."
    MC "Нужно проверить несколько страниц на всякий случай."
    hide screen bob_desk_scr
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(2,hard=True)
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    scene bob_desk_p1
    show screen bob_desk_scr
    $ can_hide_windows = True
    MC "Есть кое-что интересное..."
    MC "Бинго! Это название компании. Я думаю, это то, чего хочет Зури."
    $ clickable = True
    $ can_hide_windows = False
    jump bob_desk_label

label bob_deskcarbookput_label:
    show screen bob_desk_scr
    $ clickable = False
    $ car_book_put = True
    $ inventory.drop(bob_carbook)
    $ bob_carbook.selected = False
    MC "Давай оставим это здесь. Мне это не нужно."
    $ clickable = True
    jump bob_desk_label

label bob_deskcarbook_label:
    show screen bob_desk_scr
    $ inventory.add(bob_carbook)
    $ car_book_put = False
    jump bob_desk_label

label bob_deskminigame_label:
    show screen bob_desk_scr
    $ clickable = False
    if can_Bob_work_minigame == True:
        MC "Окей. Давай немного поработаем! Это должно быть легко."
        $ clickable = True
        hide screen bob_desk_scr
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        jump bob_deskwork_label
    else:
        MC "Завтра, вероятно, будет больше работы."
        $ clickable = True
        jump bob_desk_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
