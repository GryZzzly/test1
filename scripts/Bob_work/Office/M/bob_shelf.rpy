
image bob_shelf_p1 = "/images/Bob_work/office/M/shelf/Shelf1.jpg"
image bob_shelf_p2 = "/images/Bob_work/office/M/shelf/Shelf2.jpg"
image bob_shelf_p3 = "/images/Bob_work/office/M/shelf/Shelf3.jpg"

image bob_sec_p1 = "/images/Bob_work/office/M/scenes/sec/1.jpg"
image bob_sec_p2 = "/images/Bob_work/office/M/scenes/sec/2.jpg"
image bob_sec_p3 = "/images/Bob_work/office/M/scenes/sec/3.jpg"
image bob_sec_p4 = "/images/Bob_work/office/M/scenes/sec/4.jpg"
image bob_sec_p5 = "/images/Bob_work/office/M/scenes/sec/5.jpg"

default bob_secretroom_after_first_visit = False
default shelf_putbook = False
label bob_shelf_label:
    scene bob_shelf_p1
    call screen bob_shelf_scr


screen bob_shelf_scr:
    key "hide_windows" action NullAction()
    if bob_carbook.selected:
        imagebutton:
            xpos 948
            ypos 807
            focus_mask True
            idle "images/Bob_work/office/M/shelf/B1.png"
            hover "images/Bob_work/office/M/shelf/B1_hover.png"
            if clickable == True and day_time ==2:
                action [Play ("sound", "sfx/door_squeak.mp3"),Hide("displayTextScreen"),Jump("bob_shelfopen_label")]
            if clickable == True and day_time ==1:
                action [Hide("displayTextScreen"),Jump("bob_shelfopen_label")]
                unhovered Hide("displayTextScreen")
    if shelf_putbook == True:
        imagebutton:
            xpos 948
            ypos 807
            focus_mask True
            idle "images/Bob_work/office/M/shelf/B1_hover.png"
            hover "images/Bob_work/office/M/shelf/B1_hover.png"

    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_office_M1")]




label bob_shelfopen_label:
    if day_time==1:
        $ clickable = False
        show screen bob_shelf_scr
        MC "Я не могу этого сделать пока кто-то в комнате."
        $ clickable = True
        jump bob_shelf_label
    if day_time==2:
        scene bob_shelf_p1
        $ shelf_putbook = True
        $ inventory.drop(bob_carbook)
        $ bob_carbook.selected = False
        show screen bob_shelf_scr
        $ renpy.pause(0.2,hard= True)
        hide screen bob_shelf_scr
        scene bob_shelf_p2
        $ renpy.pause()
        if bob_secretroom_after_first_visit == False:
            jump bob_secret_room_scene
        else:
            jump bob_secret_room_label


label bob_secret_room_label:
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    scene bob_shelf_p3
    call screen bob_secret_room_scr
label bob_secret_room_leave_label:
    $ inventory.add(bob_carbook)
    $ shelf_putbook = False
    jump bob_office_M1

screen bob_secret_room_scr:
    key "hide_windows" action NullAction()
    if clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("bob_secret_room_leave_label")]


label bob_secret_room_scene:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    MC "Ха?!"
    MC "(Это секретный проход?)"
    if renpy.loadable("patch.rpy"):
        MC "(Зачем, черт возьми, папе нужна скрытая комната?)"
    else:
        MC "(Зачем, черт возьми, Бобу нужна скрытая комната?)"
    MC "(Может быть, он хранит часть своих денег здесь.)"

    scene bob_sec_p1 with dissolve

    MC "Aхххх!"
    MC "Боже! Нет!"

    scene bob_sec_p2

    MC "Его... Это... Он голый!"
    MC "Отвратительно!"

    scene bob_sec_p3

    MC "(Его избивают и относяться как к дерьму…)"
    MC "(Кто-то шантажирует его?)"
    MC "(Нет ... это не имеет смысла. Он не будет хранить данные шантажа в своем кабинете.)"

    scene bob_sec_p4

    MC "(Он, должно быть, в этом замешан.)"
    if renpy.loadable("patch.rpy"):
        MC "(Теперь понятно почему мама относится к нему так плохо…)"
    else:
        MC "(Теперь понятно почему Линда относится к нему так плохо…)"
    MC "(Это объясняет, почему он еще не оставил ее! Ему нравится когда над ним издеваются.)"

    scene bob_sec_p5

    MC "(Некоторые вещи должны оставаться частными. Я просто забуду о том, что я увидел здесь.)"
    if renpy.loadable("patch.rpy"):
        MC "(Это не мое дело. Я бы не хотел, чтобы папа всматривался в мою сексуальную жизнь.)"
    else:
        MC "(Это не мое дело. Я бы не хотел, чтобы Боб следил за моей сексуальной жизнью.)"
    MC "(Таким образом, я не должен шпионить за ним.)"
    $ can_hide_windows = False
    $ bob_secretroom_after_first_visit = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump bob_secret_room_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
