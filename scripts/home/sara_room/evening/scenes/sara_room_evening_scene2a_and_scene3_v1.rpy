image sara_room_evening_scene3_v1_p1 = "images/home/sara_room/evening/scene3_v1/1.jpg"
image sara_room_evening_scene3_v1_p2 = "images/home/sara_room/evening/scene3_v1/2.jpg"
image sara_room_evening_scene3_v1_p3 = "images/home/sara_room/evening/scene3_v1/3.jpg"
image sara_room_evening_scene3_v1_p4 = "images/home/sara_room/evening/scene3_v1/4.jpg"
image sara_room_evening_scene3_v1_p5 = "images/home/sara_room/evening/scene3_v1/5.jpg"
image sara_room_evening_scene3_v1_p6 = "images/home/sara_room/evening/scene3_v1/6.jpg"
image sara_room_evening_scene3_v1_p7 = "images/home/sara_room/evening/scene3_v1/7.jpg"
image sara_room_evening_scene3_v1_p7a = "images/home/sara_room/evening/scene3_v1/7a.jpg"
image sara_room_evening_scene3_v1_p8 = "images/home/sara_room/evening/scene3_v1/8.jpg"
image sara_room_evening_scene3_v1_p9 = "images/home/sara_room/evening/scene3_v1/9.jpg"
image sara_room_evening_scene3_v1_p10 = "images/home/sara_room/evening/scene3_v1/10.jpg"
image sara_room_evening_scene3_v1_p11 = "images/home/sara_room/evening/scene3_v1/11.jpg"
image sara_room_evening_scene3_v1_p12 = "images/home/sara_room/evening/scene3_v1/12.jpg"
image sara_room_evening_scene3_v1_p13 = "images/home/sara_room/evening/scene3_v1/13.jpg"
image sara_room_evening_scene3_v1_p14 = "images/home/sara_room/evening/scene3_v1/14.jpg"
image sara_room_evening_scene3_v1_p15 = "images/home/sara_room/evening/scene3_v1/15.jpg"
image sara_room_evening_scene3_v1_p16 = "images/home/sara_room/evening/scene3_v1/16.jpg"
image sara_room_evening_scene3_v1_p17 = "images/home/sara_room/evening/scene3_v1/17.jpg"


transform pandown1:
    crop (0, 1080, 1920, 2160)
    linear 2 crop (0, 0, 1920, 2160)


label sis_nerdy_evening_scene2a_v1_label:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if sis_nerdy_evening_gamepad_change_scene3_v1 == 0:

        scene sara_room_evening_scene2_v1_p1 with dissolve
        MC "Привет, Сара, ты-"
        Sara "О, привет! Просто поставь на паузу, [player_name]."

        scene sara_room_evening_scene2_v1_p2
        Sara "Хочешь матч-реванш?"
        Sara "Что скажешь? Те же правила? Каждый раз, когда ты умираешь, ты теряешь предмет одежды?"
        MC "(Если я соглашусь, она снова запишет мою задницу ... Мне нужно найти способ гарантировать, что я выиграю.)"
        MC "Нет, не сегодня. Наслаждайтесь остальной частью матча!"

        scene sara_room_evening_scene2_v1_p1
        Sara "Твоя поражение! Увидимся!"

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_sis_nerdy_gamepad_change = 1
        $ can_sis_nerdy_evening_scene1_v1 == False
        jump sister_nerdy_morning1
    if can_sis_nerdy_evening_scene1_v1 == False:
        show sara_room_evening_scene1_v1_after
        $ can_hide_windows = False
        MC "Я уже говорил с ней."
        jump sister_nerdy_morning1
    if sis_nerdy_evening_gamepad_change_scene3_v1 == 1:

        scene sara_room_evening_scene3_v1_p1 with dissolve
        Sara "Я сказал, что фланг ушел! Это правый фланг, ты тупой!"
        MC "(Вау, похоже, что товарищи по команде Сары сегодня не до нуля!)"
        Sara "Грр! Мы проиграли матч из-за вас, ребята! Я ухожу. Спишемся позже!"

        scene sara_room_evening_scene3_v1_p2
        Sara "Ой! Привет, [player_name]! Не видела, чтобы ты стоял там. Что матч-реванш?"
        MC "(Я поменял рабочий контроллер на дешевую версию китайского! Это должно дать мне преимущество, которое мне нужно!)"
        MC "Да, я готов!"

        scene sara_room_evening_scene3_v1_p3
        Sara "Милый! Позволь мне настроить его здесь."
        Sara "Ты хочешь снова играть в Street Brawler VII? Или что-то еще на этот раз?"
        MC "Уличный дракон работает для меня."
        Sara "Круто!"


        scene sara_room_evening_scene3_v1_p4
        Sara "Хе-хе-хе-хе, ты знаешь, что снова проиграешь?"
        MC "Возможно."
        Sara "И ты знаешь наказание за проигрыш?"
        MC "Я снимаю часть одежды."
        Sara "Ага! Теперь давай начнем!"


        $ renpy.music.stop(channel="music2", fadeout=1)
        scene black
        "(Три Минуты Спустя…)"
        $ renpy.pause(2.0)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
        Console "FATALITY!"
        scene sara_room_evening_scene3_v1_p5
        Sara "Ч-ЧТО?! Н-НЕ сейчас!"
        MC "Это один ноль, Сара! Время раздеваться."

        scene sara_room_evening_scene3_v1_p6
        Sara "Н-но я н-не ношу бюстгальтер…"
        MC "Затем джинсовые шорты."
        Sara "Я... Я не ношу любой... * ГМ * либо..."
        MC "Ты не носишь нижнее белье?"
        Sara "Взгляд прочь пока я сниму верх…"

        scene sara_room_evening_scene3_v1_p7
        MC "Хорошо."

        menu:
            "Смотреть, пока она раздевается.":
                window hide
                scene sara_room_evening_scene3_v1_p7a at pandown1
                $ renpy.pause(2.0, hard=True)
                MC "(Ебена мать! Она такая чертовски горячая!)"
                Sara "(Я не могу в это поверить ... это так неловко!)"
                Sara "(Почему я не ношу нижнее белье ?! Я была согласна с победой!)"
                MC "(Хе-хе - этот сломанный контроллер работает как шарм! Она не знает, что, черт возьми, происходит!)"
                jump after_choice_sis_nerdy_evening_scene3
            "Будь честным и пусть Сара раздевается без подглядывания.":


                scene sara_room_evening_scene3_v1_p7
                MC "Хорошо, я не буду смотреть."
                Sara "Спасибо…"
                MC "Ты еще не закончила?"
                Sara "Почти..."
                jump after_choice_sis_nerdy_evening_scene3

label after_choice_sis_nerdy_evening_scene3:

    scene sara_room_evening_scene3_v1_p8
    MC "(Ее соски довольно жесткие! Она должна тайно наслаждаться этим!)"
    Console "РАУНД 2! БОРЬБА!"
    Sara "На этот раз я собираюсь побить твою задницу!"
    MC "О, да? Ты действительно так думаешь?"
    Sara "Проклятье! Я нажала X три раза! Почему он не работал?!"
    Console "C-C-COMBO BREAKER!"

    scene sara_room_evening_scene3_v1_p9
    Console "FATALITY! ИГРОК 2 ВЫИГРЫВАЕТ!"
    Sara "НЕЕЕЕТ!"
    MC "Даааа!"
    Sara "Никоим образом! Это не может происходить!"
    MC "Ты знаешь правила, Сара! Время снимать эти джинсовые шорты!"
    MC "Или ... ты могла бы просто снять обувь."

    scene sara_room_evening_scene3_v1_p10
    MC "На самом деле! Давай заключим сделку - еще один раунд. Внезапные правила смерти."
    Sara "Что ты имеешь в виду?"
    MC "Если ты побеждаешь, я снимаю ВСЕ. Если я побеждаю, хотя … тогда ты должна раздеться абсолютно полностью."
    MC "По рукам?"
    Sara "… По рукам."

    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    "(Через тридцать секунд…)"
    $ renpy.pause(2.0)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music2", loop=True, fadein = 2)

    scene sara_room_evening_scene3_v1_p11
    Sara "AAAAAAХХХХХХ!!!"
    Sara "(ЧТО ПРОИСХОДИТ?! Почему я больше не люблю видеоигры?!)"
    MC "Сара проиграла. Время снимать!"

    scene sara_room_evening_scene3_v1_p12
    Sara "Фу ... Отлично. Я разденусь на кровати."
    Sara "Не фотографируй, хотя!"
    MC "Это немного лицемерно!"
    Sara "У меня ... у меня больше нет этой фотографии. Я ... ЭМ ... удалила ее!"
    MC "(Она лжет ... у нее определенно все еще есть фотография моего члена!)"

    scene sara_room_evening_scene3_v1_p13
    MC "Ладно, никаких фотографий. Но я все равно хочу увидеть все твое тело."
    Sara "(Залпом) Конечно."
    Sara "(Я не могу поверить, что я проиграла... Я думала, что это будет просто простой способ увидеть член [player_name] снова.)"
    Sara "(Боже ... что я скажу Лили, если она спросит, что случилось??!)"

    scene sara_room_evening_scene3_v1_p14
    MC "(Вау! Там ее киска! Я вижу капюшон ее клитора, высунув верх.)"
    MC "(Она не лгала, когда говорила, что у нее нет трусиков. Была ли она серьезно, что она уверена, что она собирается побеждать ?! ха-ха!)"
    Sara "Ну? Я-это достаточно?"

    scene sara_room_evening_scene3_v1_p15
    MC "Норм, полностью голая - довольно сексуальный вид."
    Sara "С-сексуальный?"
    MC "Я просто дразню тебя."

    scene sara_room_evening_scene3_v1_p16
    Sara "П-подожди ты не можешь просто сказать что-то подобное и уйти…"
    MC "Да?"
    Sara "Д……  я уверена?"

    scene sara_room_evening_scene3_v1_p17
    MC "Конечно, ты прекрасна. Я бы с удовольствием играл в стриптиз-игры с тобой, если бы мы не были..!"
    Sara "Я ... я думаю…"
    MC "Во всяком случае, я позволю тебе снова одеться. До встречи, Сара."
    MC "И для записи, ты очень красивая."
    Sara "Спасибо..."
    $ day_time +=1
    $ sis_nerdy_evening_scene2a_v1 = 3
    $ sis_nerdy_evening_scene1_v1 = 1
    $ can2_mc_sara_night_scene1_v1 = True
    $ can1_sis_nerdy_school_scene3_v1 = True
    $ sis_nerdy_evening_scene1_v1 = 3
    $ can_lily_scene = False
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump corridor_night1

label sis_nerdy_evening_gamepad_change_scene3_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if broken_gamepad.selected and can_sis_nerdy_gamepad_change == 1:
        show sara_room_evening_scene1_v1_after
        $ can_hide_windows = False
        MC "Я не могу сделать это, пока она рядом."
        jump sister_nerdy_evening1
    else:
        show sara_room_evening_scene1_v1_after
        $ can_hide_windows = False
        MC "Это ее Контролер. Что я должен делать с ним, чтобы выиграть в следующий раз?"
    jump sister_nerdy_evening1


label sis_nerdy_evening_gamepad_change_scene3_v1_label_can:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = False
    if day_time == 1:
        show screen sister_nerdy_morning_notclickable
        if broken_gamepad.selected and can_sis_nerdy_gamepad_change == 1:
            $ inventory.drop(broken_gamepad)
            MC "Геймпад изменен."
            $ sis_nerdy_evening_gamepad_change_scene3_v1 = 1
            $ can_sis_nerdy_gamepad_change = 3
            jump sister_nerdy_morning1
        else:
            MC "Это ее Контролер. Что я должен делать с ним, чтобы выиграть в следующий раз?"
            jump sister_nerdy_morning1
    if day_time == 2:
        show screen sister_nerdy_day_notclickable
        if broken_gamepad.selected and can_sis_nerdy_gamepad_change == 1:
            $ inventory.drop(broken_gamepad)
            MC "Геймпад изменен."
            $ sis_nerdy_evening_gamepad_change_scene3_v1 = 1
            $ can_sis_nerdy_gamepad_change = 3
            jump sister_nerdy_morning1
        else:
            MC "Это ее Контролер. Что я должен делать с ним, чтобы выиграть в следующий раз?"
            jump sister_nerdy_morning1

    if day_time == 4:
        show screen sister_nerdy_night_notclikcable
        if broken_gamepad.selected and can_sis_nerdy_gamepad_change == 1:
            $ inventory.drop(broken_gamepad)
            MC "Геймпад изменен."
            $ sis_nerdy_evening_gamepad_change_scene3_v1 = 1
            $ can_sis_nerdy_gamepad_change = 3
            jump sister_nerdy_morning1
        else:
            MC "Это ее Контролер. Что я должен делать с ним, чтобы выиграть в следующий раз?"
            jump sister_nerdy_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
