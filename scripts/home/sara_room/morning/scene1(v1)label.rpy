image scene1_v1p1 = "images/home/sara_room/morning/Scene1_v1/1.jpg"
image scene1_v1p2 = "images/home/sara_room/morning/Scene1_v1/2.jpg"
image scene1_v1p3 = "images/home/sara_room/morning/Scene1_v1/3.jpg"
image scene1_v1p4 = "images/home/sara_room/morning/Scene1_v1/4.jpg"
image after_sis_nerdy_scene1_v1p1 = "images/home/sara_room/morning/Scene1_v1/after_sara_scene1.png"


label scene1_v1:
    $ renpy.music.stop(channel="music2", fadeout=2)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene scene1_v1p1 with dissolve
    $ can_hide_windows = True
    MC "(Сара поглощена одной из своих видеоигр!)"
    MC "(Если она не спешит, она будет опаздывать на свой первый урок.)"
    MC "Эй, ты почти готова пойти?"

    scene scene1_v1p2

    MC "(Да, я не думаю, что она услышала меня, в наушниках.)"
    MC "Привет! Сара!"
    Sara "Да ?! Ой! Привет, [player_name]!"
    MC "Ты кричишь!"
    Sara "Что случилось?"
    MC "Нам нужно ехать в школу через пять минут!"

    scene scene1_v1p3
    Sara "Все в порядке, я сделаю это как ... пару минут."
    MC "Мы оба знаем, что это не правдаe."
    MC "Я могу ЧЕТКО сказать, ты только что начала раунд!"

    scene scene1_v1p4
    if renpy.loadable("patch.rpy"):
        Sara "Все, иди [player_name]! Ты не мой папа! Хехе!"
    if not renpy.loadable("patch.rpy"):
        Sara "Все, иди [player_name]! Ты не Боб! Хехе!"
    Sara "Почему тебя волнует, если я немного опоздаю в школу? В любом случае, я почти лучшая в классе."
    MC "Почти? Разве ты не был топ, два года назад? Ты сползаешь, Сара."

    scene scene1_v1p2
    Sara "Grr ... Отлично! Я иду."
    Sara "Скажи ... О миссис Селии, на днях..."

    scene scene1_v1p3
    MC "Я бы не хотел говорить об этом."
    Sara "Ой, извини. я понимаю."
    MC "Нет, тебе не нужно извиняться. Ты была права - я должен был слушать твои советы."
    MC "Я постараюсь сделать это в будущем, я обещаю."

    scene scene1_v1p4
    Sara "Хочешь вместе ходить в школу?"
    MC "Тебе нужно торопиться! Я был готов уехать в течение последних десяти минут!"
    $ sis_nerdy_scene1_v1= 2
    $ after_sis_nerdy_scene1_v1 = 2
    $ next_day = False
    $ can_morning_sara_scenes = False
    $ renpy.music.stop(channel="music1", fadeout=2)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump sister_nerdy_morning1

label after_sis_nerdy_scene1_v1:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show after_sis_nerdy_scene1_v1p1
    $ can_hide_windows = False
    MC "Я уже говорил с ней.."
    jump sister_nerdy_morning1

label next_day_after_sis_nerdy_scene1_v1:
    $ renpy.music.stop(channel="music2", fadeout=2)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene scene1_v1p1 with dissolve
    $ can_hide_windows = True
    MC "(Вздох ... Компьютерные игры снова?!)"
    MC "(Ее оценки будут продолжать опускатся, если она не будет заставлять себя.)"
    MC "(И даже если она получит хорошие оценки; какой работодатель захочет ленивого работника, который всегда опаздывает?)"

    scene scene1_v1p2
    MC "Сара! Ты опаздываешь СНОВА!"
    Sara "Просто ... еще пять минут. Я почти заработала свой ежедневный бонус!"
    MC "Не можеши ли ты это сделать, когда вернешься домой, после школы?"
    Sara "Ммм…"

    scene scene1_v1p3
    Sara "Но если я сейчас не открою ящик для добычи, мне будет интересно, что в нем ВСЕ ДЕНЬ!"
    Sara "Я просто буду отвлечена в школе и не узнаю ничего. Поэтому мне действительно нужно забрать это сейчас."
    MC "Это ... страшное оправдание. Ты знаешь?"
    Sara "Хе-хе, да…"
    $ scene1_v1q1a1 = True
    $ scene1_v1q1a2 = True
    $ scene1_v1q1a3 = True
    jump scene1_v1q1
label scene1_v1q1:
    scene scene1_v1p4
    menu:
        "Ты сделала домашнюю работу?" if scene1_v1q1a1 == True:

            MC "Ты хотя бы сделала домашнее задание?"
            Sara "Да! Большинство из…"
            MC "Что ты имеешь в виду, большинство из ?!"
            Sara "Расслабься! Я могу закончить это в школьной библиотеке, за обедом."
            $ scene1_v1q1a1 = False
            jump scene1_v1q1

        "Во сколько ты легла спать прошлой ночью?" if scene1_v1q1a2 == True:

            MC "В какое время ты легла спать прошлой ночью?"
            Sara "Умм ... Давай посмотрим ... Я сыграла три матча ... затем еще два захвата флагов…"
            Sara "2 ночи!"
            MC "2 ночи?!"
            Sara "Хе-хе, да. Я немного устала…"
            MC "(Ей действительно нужно ложиться спать раньше.)"
            $ scene1_v1q1a2 = False
            jump scene1_v1q1

        "{color=#00ff00}До чего-нибудь захватывающего сегодня?{/color}" if scene1_v1q1a3 == True:

            MC "Сегодня ты занята чем-нибудь захватывающим?"
            Sara "Нет, ничего интересного не планировалось. Я, вероятно, просто буду болтаться с Лили."
            Sara "Как насчет тебя?"
            MC "Помимо медленного стремления вернуть себе чувство собственного достоинства и вернуть свою жизнь в нужное русло?"
            Sara "Ты слишком драматичный."
            MC "Это драматично на самом деле."
            Sara "Действительно? Боже мой, может быть, я не должна была пропускать урок английской литературы."
            MC "Ты пропустила литературу?!"
            $ scene1_v1q1a3 = False
            jump after_scene1_v1q1

label after_scene1_v1q1:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene scene1_v1p4
    Sara " Ой! Посмотрите на время-я лучше быстро оденусь! Я могу опоздать!"
    $ sis_nerdy_scene1_v1 = 3
    $ after_sis_nerdy_scene1_v1 = 3
    $ drawer_sis_nerdy = 1
    $ can_morning_sara_scenes == False
    $ can_sara_scene3_v1 = False
    $ next_day = False
    $ renpy.music.stop(channel="music1", fadeout=2)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2, fadeout=2)
    $ can_hide_windows = False
    jump corridor_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
