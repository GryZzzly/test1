

default Zv2_MS1_ask_boob_office = True
default Zv2_MS1_ask_boob_office1 = 1
label Zv2_MS1_daymeet_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if Zv2_MS1_ask_boob_office == True:
        scene Zv2_MS1_p1 with dissolve
        $ Zuri_name = "???"
        Zuri "Привет и добро пожаловать в Bayside Business Consultants. Меня зовут Зури. Чем я могу тебе помочь?"
        $ Zuri_name = "Зури"

        scene Zv2_MS1_p2
        if renpy.loadable("patch.rpy"):
            MC "(Вау! Это должно быть папина секретарша! Она очень горячая!)"
            MC "Привет, Зури. Меня зовут [player_name]. Я собирался навестить отца."
            Zuri "И кто твой отец?"
        else:
            MC "(Вау! Это должно быть секретарь Боба! Она очень горячая!)"
            MC "Привет, Зури. Меня зовут [player_name]. Я приешел навестить Боба."
            Zuri "А кто такой Боб?"
        MC "Тот, кто управляет этой компанией?"

        scene Zv2_MS1_p3

        Zuri "Ахахаха! Как смешно!"
        Zuri "Позволь мне угадать - ты с одной из этих онлайн-шуток, не так ли?"
        MC "Гмм?"
        Zuri "У тебя есть секретная камера, и ты собираешься унизить босса и выложить онлайн?"
        if renpy.loadable("patch.rpy"):
            MC "Нет. Что?! Я на самом деле его сын."
        else:
            MC "Нет. Что?! Я действительно живу с ним."

        scene Zv2_MS1_p1

        Zuri "В самом деле?"
        MC "Да!"
        Zuri "Ох! Извини меня плохую!"
        Zuri "Извини, но его сейчас нет в офисе. Он там только по утрам. Пожалуйста, приходи завтра."
        $ Zv2_MS1_ask_boob_office = False
        $ Zv2_MS1_ask_boob_office1 = 3
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump bob_reception_morning1
    if Zv2_MS1_ask_boob_office == False:
        scene Zv2_MS1_p1 with dissolve
        Zuri "Привет и добро пожаловать в Bayside Business Consultants."
        MC "В офисе есть кто-то?"
        Zuri "I'm sorry but nobody is in the office at the moment. He's only there in the mornings. Please come back tomorrow."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump bob_reception_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
