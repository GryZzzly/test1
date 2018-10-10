
default can_ml_workR2_AS2_talk = True
default can_ml_workR2_AS2 = False

label ml_workR2_AS2_label:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_workR2_AS1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "После обеда, мама! Я пришел немного поработать."
    else:
        MC "После обеда, Линда! Я пришел немного поработать."
    if can_ml_workR2_AS2 == False and can_ml_workR2_AS2_talk == True:
        Mom "Прости, милый. У меня сегодня нет работы для тебя."
        MC "Хорошо."
        Mom "Приходи в другой день."
        MC "Нет проблем."
        Mom "Теперь позволь мне закончить эту глупую работу, и у меня бедет немного яснее голова."
        MC "Хорошо."
        if renpy.loadable("patch.rpy"):
            MC "(Хм .. Мама кажется очень занятой.. Может быть, я должен посетить ее вечером, чтобы сделать ей расслабляющий массаж, после работы?)"
        else:
            MC "(Хм .. Линда кажется очень занятой.. Может быть, я должен посетить ее вечером, чтобы сделать ей расслабляющий массаж, после работы?)"
        $ can_ml_workR2_AS2_talk = False
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump ml_work_room1_day1
    if can_ml_workR2_AS2 == False and can_ml_workR2_AS2_talk == False:
        Mom "Прости, милый. У меня сегодня нет работы для тебя."
        MC "Хорошо."
        Mom "Приходи в другой день."
        MC "Хорошо."
        Mom "Теперь позволь мне закончить эту глупую работу, и у меня бедет немного яснее голова."
        MC "Хорошо."
        if renpy.loadable("patch.rpy"):
            MC "(Хм .. Мама кажется очень занятой.. Может быть, я должен посетить ее вечером, чтобы сделать ей расслабляющий массаж, после работы?)"
        else:
            MC "(Хм .. Линда кажется очень занятой.. Может быть, я должен посетить ее вечером, чтобы сделать ей расслабляющий массаж, после работы?)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump ml_work_room1_day1
    else:


        Mom "Привет, милый. Займешся уборкой?"
        MC "Конечно, без проблем."

        scene ml_workR2_AS1_p2

        Mom "Огромное спасибо. Я буду работать здесь. Просто скажи, когда закончишь."
        if renpy.loadable("patch.rpy"):
            MC "Окей мам!"
        else:
            MC "Хорошо, Линда!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump work_minigame_R2room2_label

label after_ml_workR2_AS2_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    $ inventory.earn(25)
    $ renpy.pause(3, hard = True)


    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_workR2_AS1_p3 with dissolve

    MC "Иииии… я все сделал!"
    Mom "Хорошая работа-мой персонал действительно ценит, приходя в аккуратный офис утром."
    Mom "(И, надеюсь, этого будет достаточно, чтобы закрыть разговоры об их профсоюзах!)"

    scene ml_workR2_AS1_p4

    Mom "У меня сегодня хорошие новости - я почти готова. Это последние документы!"
    MC "Потрясающие!"
    MC "(Надо надеяться, это означает, скоро я смогу остаться с ней наедине!)"

    scene ml_workR2_AS1_p5

    MC "Когда ты закончишь?"
    Mom "Скоро. Просто дай мне время до вечера."
    MC "О, круто. Каковы твои планы на вечер?"

    scene ml_workR2_AS1_p6

    Mom "Ну ... Я думала о том, чтобы взять тебя с собой в великолепный маленький ресторан на дальнем конце города."
    Mom "Это итальянское место - одно из лучших в городе. Тебе понравится еда."
    Mom "Я никогда не смогу заставить твоего отца пойти туда. Он никогда не интересовался, ничем, кроме американских гамбургеров."
    Mom "(У меня больше культуры в мизинце, чем у жирного идиота во всем его чертовом теле!) "

    scene ml_workR2_AS1_p8

    Mom "Итак, что ты скажешь? Заинтересованный?"
    MC "Определенно!"

    scene ml_workR2_AS1_p9

    Mom "Отлично! В таком случае, встретимся в гараже. "
    Mom "Увидимся вечером. Пожалуйста, не опаздывай."
    if renpy.loadable("patch.rpy"):
        MC "Я не буду - не волнуйся, мама!"
    else:
        MC "Я не буду - не волнуйся, Линда!"

    if MLR2_ES1 == True:
        $ MLR2_ES1 = False

    $ can1_MLR2_ES1 = True
    $ ml_workR2_AS2 = False
    $ day_time = 3
    $ MLR2_ES3 = True
    $ can_map = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump garage_evening1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
