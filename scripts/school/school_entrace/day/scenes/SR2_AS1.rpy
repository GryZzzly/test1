image SR2_AS1_p1 = "images/school/school_entrance/day/scenes/SR2_AS1/1.jpg"
image SR2_AS1_p2 = "images/school/school_entrance/day/scenes/SR2_AS1/2.jpg"
image SR2_AS1_p3 = "images/school/school_entrance/day/scenes/SR2_AS1/3.jpg"
image SR2_AS1_p4 = "images/school/school_entrance/day/scenes/SR2_AS1/4.jpg"
image SR2_AS1_p5 = "images/school/school_entrance/day/scenes/SR2_AS1/5.jpg"

label SR2_AS1_label:
    if can_SR2_AS1 == False:
        $ clickable = False
        show screen school_entrance_day
        MC "Я уже говорил с ней.."
        $ clickable = True
        jump school_entrance_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_AS1_p1 with dissolve

        MC "(Это Сара! Похоже, она сосредоточена. Интересно, что может быть такое важное?)"
        MC "Эй, Сара! Что ты читаешь?"
        Sara "…"
        MC "(Кажется, она меня не заметила. Я попробую еще раз.)"
        MC "Привет, Сара!"

        scene SR2_AS1_p2

        Sara "А? Ой! Привет, [player_name]. Что происходит?"
        MC "Что ты читаешь?"
        Sara "О, я просто делаю некоторые последние заметки для теста по истории."
        MC "Какой период вы изучаете?"
        Sara "Сирия во время холодной войны."
        MC "Я помню, как делал этот модуль. Кроме того, это были Сирия и Египет во время холодной войны."

        scene SR2_AS1_p3

        Sara "Вот черт! Ты прав! Я забыла про Египет!"
        MC "Ну, по крайней мере, ты изучала Сирию. Просто сосредоточься на Египте сейчас, и все должно быть в порядке."
        Sara "Я еще ничего не изучала! Я открыла книгу только сегодня утром.!"
        MC "Что?!"

        scene SR2_AS1_p4

        Sara "Я сидела до поздна играя в некоторые игры. Хаха…"
        MC "Но... как насчет теста?"
        Sara "Все будет в порядке?"
        MC "Что такое Объединенная Арабская Республика?"

        scene SR2_AS1_p2

        Sara "Была ли она союзником Сирии и Египта?"
        MC "Это были Сирия и Египет. Они объединились и сформировали единую страну на несколько лет."

        scene SR2_AS1_p5

        Sara "Вот чекнутая. Я облажалась..."
        MC "(Это совсем не похоже на Сару! Она была лучшей в своем классе.!)"
        MC "(Думаю, она просто отвлеклась на видеоигры. Ей действительно нужно вернуться на трассу и сосредоточиться. Надеюсь, она пройдет этот тест.)"
        MC "Удачи тебе, наверное. Надеюсь, все пойдет хорошо."
        Sara "(Глоток) Спасибо, [player_name]."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ can_SR2_AS1 = False
        jump school_entrance_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
