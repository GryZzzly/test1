image lily_school_day_scene1_v1_p1 = "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/1.jpg"
image lily_school_day_scene1_v1_p2 = "images/school/classroom2/day/scenes/Lily_school_day_scene1_v1/2.jpg"

label lily_school_day_scene1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    scene lily_school_day_scene1_v1_p1 with dissolve
    $ can_hide_windows = True
    Lily "Эй, [player_name]!"
    MC "О, Привет Лили!"
    $ lily_school_day_scene1_v1q1a1 = True
    $ lily_school_day_scene1_v1q1a2 = True
    $ lily_school_day_scene1_v1q1a3 = True
    jump questions_lily_school_day_scene1_v1


label questions_lily_school_day_scene1_v1:

    scene lily_school_day_scene1_v1_p1
    menu:

        "Что случилось?" if lily_school_day_scene1_v1q1a1 == True:

            scene lily_school_day_scene1_v1_p2
            MC "Что случилось?"
            Lily "Эх, сейчас скучно. Я думаю, что я собираюсь улизнуть рано и попытаться пропустить химию."
            MC "Не боишься, что тебя поймают?"
            Lily "Не самое худшее, что может случиться? Мистер Джексон грозится наказать меня, но только грозится!"
            MC "(Вероятно каждый хочет ее наказать. Лили должна быть осторожна!)"
            $ lily_school_day_scene1_v1q1a1 = False
            if lily_school_day_scene1_v1q1a2 == False and lily_school_day_scene1_v1q1a3 == False:
                jump after_questions_lily_school_day_scene1_v1
            else:
                jump questions_lily_school_day_scene1_v1

        "Ты видела мою сестру?" if lily_school_day_scene1_v1q1a2 == True and renpy.loadable("patch.rpy"):

            scene lily_school_day_scene1_v1_p2
            MC "Ты видела мою сестру?"
            Lily "Сару? Конечно, она, вероятно, все еще в коридоре. По крайней мере, вот где я в последний раз видела ее, прежде чем я пришла в класс."
            MC "Спасибо, Лили."
            Lily "Незачто, [player_name]."
            $ lily_school_day_scene1_v1q1a2 = False
            if lily_school_day_scene1_v1q1a1 == False and lily_school_day_scene1_v1q1a3 == False:
                jump after_questions_lily_school_day_scene1_v1
            else:
                jump questions_lily_school_day_scene1_v1

        "Ты видела Сару?" if lily_school_day_scene1_v1q1a2 == True and not renpy.loadable("patch.rpy"):

            scene lily_school_day_scene1_v1_p2
            MC "Ты видела Сару?"
            Lily "Сару? Конечно, она, вероятно, все еще в коридоре. По крайней мере, вот где я в последний раз видела ее, прежде чем я пришла в класс."
            MC "Спасибо, Лили."
            Lily "Незачто, [player_name]."
            $ lily_school_day_scene1_v1q1a2 = False
            if lily_school_day_scene1_v1q1a1 == False and lily_school_day_scene1_v1q1a3 == False:
                jump after_questions_lily_school_day_scene1_v1
            else:
                jump questions_lily_school_day_scene1_v1
        "Что ты делаешь после школы?" if lily_school_day_scene1_v1q1a3 == True:

            scene lily_school_day_scene1_v1_p2
            MC "Что ты делаешь после школы?"
            Lily "Я собираюсь пойти купить новое бикини. Кроме того, у меня нет больших планов."
            Lily "Я хочу найти на что-то действительно ... интересное. Маленькие и тонкие."
            MC "Э-э ... Вау! (Мне бы хотелось, чтобы она была одета так!)"
            $ lily_school_day_scene1_v1q1a3 = False
            if lily_school_day_scene1_v1q1a1 == False and lily_school_day_scene1_v1q1a2 == False:
                jump after_questions_lily_school_day_scene1_v1
            else:
                jump questions_lily_school_day_scene1_v1

label after_questions_lily_school_day_scene1_v1:
    $ lily_bath_event_unlock = True
    $ lily_school_day_scene1_v1 = 3
    $ lily_bath_event_unlock = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump classroom2_day1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
