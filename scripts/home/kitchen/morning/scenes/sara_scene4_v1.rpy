image scene4_v1p1 = "images/home/kitchen/morning/scenes/sara_scene4_v1/1.jpg"
image scene4_v1p2 = "images/home/kitchen/morning/scenes/sara_scene4_v1/2.jpg"
image scene4_v1p3 = "images/home/kitchen/morning/scenes/sara_scene4_v1/3.jpg"
image scene4_v1p3a = "images/home/kitchen/morning/scenes/sara_scene4_v1/3a.jpg"
image scene4_v1p4 = "images/home/kitchen/morning/scenes/sara_scene4_v1/4.jpg"
default first_visit_sister_nerdy_scene4_v1 = 1
default second_visit_sister_nerdy_scene4_v1 = 0
default third_visit_sister_nerdy_scene4_v1 = 0
default fourth_visit_sister_nerdy_scene4_v1 = 0


label sister_nerdy_scene4_v11:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if next_day_sister_nerdy_scene4_v1 == False:
        show screen kitchen_morning_notclickable
        MC "Я уже знаю, кто там."
        jump kitchen_morning1

    if first_sis_nerdy_scene4_v1 == 1 and first_visit_sister_nerdy_scene4_v1 == 1 and next_day_sister_nerdy_scene4_v1 == True:

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Aces High.mp3', channel="music2", loop=True, fadein = 2)

        scene scene4_v1p1
        $ can_hide_windows = True
        MC "(Похоже, я сделал это как раз вовремя.)"
        MC "(Эй, это те трусики, которые я почти украл у сестры!)"
        MC "(У нее есть подходящий бюстгальтер - это должен быть набор, который ей нравится.)"
        MC "(Может быть, завтра осмотрюсь лучше!)"

        $ next_day_sister_nerdy_scene4_v1 = False
        $ first_visit_sister_nerdy_scene4_v1 = 2
        $ second_visit_sister_nerdy_scene4_v1 = 1
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_morning1

    if first_sis_nerdy_scene4_v1 == 1 and next_day_sister_nerdy_scene4_v1 == True and second_visit_sister_nerdy_scene4_v1 == 1:

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Aces High.mp3', channel="music2", loop=True, fadein = 2)

        scene scene4_v1p2
        $ can_hide_windows = True
        MC "(Ммм, еще лучше!)"
        MC "(Черт, у нее такие сексуальные бедра.)"
        MC "(Мне бы хотелось раздвинуть эти булочки и  просто трахнуть ее.)"
        MC "(Давай посмотрим на нее снова в другой раз.)"
        $ next_day_sister_nerdy_scene4_v1 = False
        $ second_visit_sister_nerdy_scene4_v1 = 2
        $ third_visit_sister_nerdy_scene4_v1 = 1
        $ first_sis_nerdy_scene4_v1 += 1
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_morning1

    if first_sis_nerdy_scene4_v1 == 2 and next_day_sister_nerdy_scene4_v1 == True and  third_visit_sister_nerdy_scene4_v1 == 1:

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Aces High.mp3', channel="music2", loop=True, fadein = 2)
        scene scene4_v1p3
        $ can_hide_windows = True
        MC "(Идеальное время! Похоже, она собираеться душ!)"
        MC "(Я почти вижу ее киску отсюда!)"
        if renpy.loadable("patch.rpy"):
            MC "(Боже, пожалуйста! Пусть моя сестра нагнется прямо сейчас!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Боже, пожалуйста! Пусть моя подруга нагнется прямо сейчас!)"

        scene scene4_v1p3a
        Sara "(Да, похоже, я пропустила одно место, когда делала депиляцию.)"
        MC "(Бог есть!)"
        MC "(Черт, она выглядит так туго! Мне очень хотелось бы вставить ей.)"
        MC "(Я бы чувствовал себя удивительно!)"
        $ next_day_sister_nerdy_scene4_v1 = False
        $ fourth_visit_sister_nerdy_scene4_v1 = 1
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_morning1

    if first_sis_nerdy_scene4_v1 == 3 and next_day_sister_nerdy_scene4_v1 == True and fourth_visit_sister_nerdy_scene4_v1 == 1:

        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture_Clean.mp3', channel="music2", loop=True, fadein = 2)
        scene scene4_v1p4
        $ can_hide_windows = True
        Sara "Aх! Aх… Aхх… Mмм… Ooх…"
        MC "(Как раз вовремя! Она мастурбирует!)"
        MC "(Интересно, что она смотрит на телефоне. Может быть, фотка моего члена?)"
        Sara "Oхх… [player_name]! Да…!"
        if renpy.loadable("patch.rpy"):
            MC "(Она должна быть тише, если она не хочет, чтобы мама услышала ее!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Она должна быть тише, если она не хочет, чтобы Линда услышала ее!)"
        $ next_day_sister_nerdy_scene4_v1 = False
        $ fourth_visit_sister_nerdy_scene4_v1 = 1
        $ sis_nerdy_scene4_v1 = False
        $ can_toilet_after_sara_scene4_1 = False
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_morning1



label sister_nerdy_scene4_v1_l_door_locked:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if next_day_sister_nerdy_scene4_v1 == False:
        show screen kitchen_morning_notclickable
        MC "Я уже знаю, кто там."
        jump kitchen_morning1
    show screen kitchen_morning_notclickable
    MC "Закрыто! Интересно, кто там…?"
    MC "Если бы у меня была камера-шпион, я мог бы ее использовать, чтобы увидеть кто за дверью!"
    jump kitchen_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
