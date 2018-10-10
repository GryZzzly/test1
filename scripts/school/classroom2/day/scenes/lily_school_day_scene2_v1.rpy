image lily_school_day_scene2_v1_p1 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/1.jpg"
image lily_school_day_scene2_v1_p2 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/2.jpg"
image lily_school_day_scene2_v1_p3 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/3.jpg"
image lily_school_day_scene2_v1_p3a = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/3a.jpg"
image lily_school_day_scene2_v1_p4 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/4.jpg"
image lily_school_day_scene2_v1_p5 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/5.jpg"
image lily_school_day_scene2_v1_p6 = "images/school/classroom2/day/scenes/Lily_school_day_scene2_v1/6.jpg"

label lily_school_day_scene2_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)

    scene lily_school_day_scene2_v1_p1 with dissolve
    $ can_hide_windows = True
    Lily "О! Привет, [player_name]. Ты проделала весь этот путь сюда, просто чтобы навестить меня?"
    MC "Привет, Лили. Я проходил мимо, решил зайти поздороваться."
    Lily "Я очень рада, что ты пришел. Было немного скучно, пока ты не пришел."

    scene lily_school_day_scene2_v1_p2
    MC "Ха-ха! Думаю, я приму это как комплимент.."
    if renpy.loadable("patch.rpy"):
        Lily "Как твоя сестра? Она оправилась от ее причуда, на днях?"
    if not renpy.loadable("patch.rpy"):
        Lily "Как твой подруга? Она оправилась от ее причуда, на днях?"
    MC "Причуда?"
    Lily "Да-когда она бросила бутылку через комнату."
    MC "О! Да, сейчас она успокоилась.."
    Lily "Приятно слышать."

    scene lily_school_day_scene2_v1_p3
    Lily "Упс! Глупая - я уронила ручку."
    Lily "Ты не мог бы поднять ее?"

    menu:
        "Нагнуться и взять ручку.":
            scene lily_school_day_scene2_v1_p4
            MC "Да, без проблем, Лили."
            MC "(Вот она. Я удивляюсь, почему она не просто наклониться, поднять ее сама, хотя!)"

            scene lily_school_day_scene2_v1_p5
            MC "(Срань господня!)"
            MC "(Лили целенаправленно раздвигает ноги! Я вижу ее трусики.)"
            Lily "Гм!"
            MC "(Охохо…)"

            scene lily_school_day_scene2_v1_p6
            Lily "Ты нашел мою ручку? Или что-то... отвлекает тебя?"
            MC "Н-нет! Вот она."
            Lily "Круто ... Поднимешь или нет?"
            MC "Да, да!"

            scene lily_school_day_scene2_v1_p2
            MC "Я лучше уйду отсюда. Но увидимся, Лили."
            Lily "Увидимся позже, [player_name]."
            jump after_lily_school_day_scene2_v1_choice
        "Отказаться поднимать ручку.":


            scene lily_school_day_scene2_v1_p3a
            MC "Посмотрите! Она под твоей стороной стола. Тебе легче достать ее."
            Lily "Да?"
            MC "Смотри-она ближе к тебе."
            Lily "(Он не понимает? Я пытаюсь показать ему трусики!)"

            Lily "(Он серьезно тупой?! Я даю ему прекрасную возможность! Десятки парней в этой школе будут убивать, чтобы Взглянуть что под моей юпкой!)"
            MC "В любом случае, я лучше уйду. Неотложное дело! Увидимся поже, Лили.."
            Lily "Гррр... Увидимся."
            jump after_lily_school_day_scene2_v1_choice

label after_lily_school_day_scene2_v1_choice:
    $ lily_work_in_progress_v1 = 1
    $ can_lily_work_in_progress = False
    $ lily_school_day_scene1_v1 = 3
    $ lily_school_day_scene2_v1 = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump classroom2_day1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
