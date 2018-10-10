image CR2_AS5_p1 = "images/cloth_shop/room1/day/scenes/CR2_AS5/1.jpg"
image CR2_AS5_p2 = "images/cloth_shop/room1/day/scenes/CR2_AS5/2.jpg"
image CR2_AS5_p3 = "images/cloth_shop/room1/day/scenes/CR2_AS5/3.jpg"
image CR2_AS5_p4 = "images/cloth_shop/room1/day/scenes/CR2_AS5/4.jpg"
image CR2_AS5_p5 = "images/cloth_shop/room1/day/scenes/CR2_AS5/5.jpg"
image CR2_AS5_p6 = "images/cloth_shop/room1/day/scenes/CR2_AS5/6.jpg"


default CR2_AS5_q1 = True
default CR2_AS5_q2 = True
default CR2_AS5_q3 = True
default CR2_AS5_q4 = True
label CR2_AS5_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_AS5_p1
    $ can_hide_windows = True
    MC "(Я думаю, ее ноутбук украли...)"
    MC "(Я думаю, что у нее не осталось денег.)"

    scene CR2_AS5_p2

    MC "Эй, Кэролайн."

    scene CR2_AS5_p3

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    Caroline "Ах! [player_name]! "
    Caroline "Ты меня испугал!"

    scene CR2_AS5_p4

    MC "Ха-ха!"
    Caroline "Что-то не так?"
    MC "Нет. Я только заметил, что магазин открыт."
    Caroline "В настоящий момент это не похоже на то, что есть причина закрыть его."
    jump CR2_AS5_menu


label CR2_AS5_menu:
    scene CR2_AS5_p4
    window hide
    menu:
        "Кто тебе разрешил брать этот ноутбук? " if CR2_AS5_q1 == True:
            scene CR2_AS5_p5
            MC "Кто тебе разрешил брать этот ноутбук? Ты вернула свои деньги?"
            if renpy.loadable("patch.rpy"):
                Caroline "Нет ... Это ноутбук Мамы. Я только взяла его."
            else:
                Caroline "Нет ... Это ноутбук Линды. Я только взяла его."
            if renpy.loadable("patch.rpy"):
                MC "Мама знает?"
            else:
                MC "Знает ли Линда?"
            Caroline "Н-Нет..."
            Caroline "Я верну его ей сегодня. Мне нужно было всего пару часов."
            MC "Хорошо. я понимаю."
            $ CR2_AS5_q1 = False
            if CR2_AS5_q2 == False and CR2_AS5_q1 == False:
                jump CR2_AS5_continue
            else:
                jump CR2_AS5_menu


        "Что делаешь?" if CR2_AS5_q2 == True:
            scene CR2_AS5_p6
            Caroline "Я проверяю все входящие поставки. "
            Caroline "У меня есть хорошие новости и некоторые плохие новости для тебя. Какой из них ты хочешь услышать первой?"
            jump CR2_AS5_menu_g_b
label CR2_AS5_menu_g_b:

    window hide
    menu:
        "Хорошо." if CR2_AS5_q3 == True:
            Caroline "Есть одна партия, которую я уже оплатила! Поэтому у меня появятся новые клиенты для нового каталога."
            MC "Это хорошо. Я все еще могу быть твоим фотографом."
            Caroline "Да.. Нет..."
            MC "Что?"
            $ CR2_AS5_q3 = False
            if CR2_AS5_q4 == True:
                jump CR2_AS5_menu_g_b
            if CR2_AS5_q3 == False and CR2_AS5_q4 == False:
                $ CR2_AS5_q2 = False
            if CR2_AS5_q2 == False and CR2_AS5_q1 == False and CR2_AS5_q3 == False and CR2_AS5_q4 == False:
                jump CR2_AS5_continue
            if CR2_AS5_q1 == True:
                jump CR2_AS5_menu

        "Плохо" if CR2_AS5_q4 == True:
            scene CR2_AS5_p5
            Caroline "Плохая новость заключается в том, что в новом каталоге будут костюмы для мужчин и женщин."
            MC "Я думаю ... Я знаю, где это происходит..."
            Caroline "Да. Мы оба будем носить костюмы, которые оставляют нам потребность еще одном фотографе."
            Caroline "Но не нужно паниковать. У меня есть время, чтобы найти кого-то."
            $ CR2_AS5_q4 = False
            if CR2_AS5_q3 == True:
                jump CR2_AS5_menu_g_b
            if CR2_AS5_q3 == False and CR2_AS5_q4 == False:
                $ CR2_AS5_q2 = False
            if CR2_AS5_q2 == False and CR2_AS5_q1 == False and CR2_AS5_q3 == False and CR2_AS5_q4 == False:
                jump CR2_AS5_continue
            if CR2_AS5_q1 == True:
                jump CR2_AS5_menu

label CR2_AS5_continue:
    scene CR2_AS5_p1
    if renpy.loadable("patch.rpy"):
        Caroline "О нет! Время! Мама скоро вернется домой!"
    else:
        Caroline "О нет! Время! Линда скоро вернется домой!"
    Caroline "Давай! Выключай!"
    if renpy.loadable("patch.rpy"):
        MC "Тебе лучше поторопиться. Мама будет действительно безумна, если она заметит, что ее ноутбука."
    else:
        MC "Тебе лучше поторопиться. Линда будет действительно безумна, если она заметит, что ее ноутбук отсутствует."
    Caroline "я знаю!"
    Caroline "Я должна был закончить некоторое время назад! Но на рабочем столе было слишком много инцест-историй, и это затрудняло загрузку файлов!"
    MC "(Что!?)"
    Caroline "Интересно, для чего они были!?"
    MC "М-может быть, какой-то вирус..."
    MC "Хорошо.. А-в любом случае.. Увидимся."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ day_time = 3
    $ CR2_AS5 = False
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
