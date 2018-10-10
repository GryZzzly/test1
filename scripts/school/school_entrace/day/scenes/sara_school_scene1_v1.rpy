image sis_nerdy_school_scene1_v1_p1 = "images/school/school_entrance/day/scenes/sara_scene1_v1/1.jpg"
image sis_nerdy_school_scene1_v1_p2 = "images/school/school_entrance/day/scenes/sara_scene1_v1/2.jpg"
image sis_nerdy_school_scene1_v1_sara = ("images/school/school_entrance/day/scenes/sara_scene1_v1/sara1.png")


label sis_nerdy_school_scene1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 1 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        MC "(Вот она! Интересно, что она делает здесь, одна.)"
        MC "Привет, Сара. Ты занята прямо сейчас?"

        scene sis_nerdy_school_scene1_v1_p2
        Sara "Ой! Привет, [player_name]!"
        Sara "Я ПОЧТИ закончил эту главу - тогда я могу бросить записи в доктора Робертса и отправиться домой."
        MC "Прекрасно! Скоро увидимся."
        $ sis_nerdy_school_scene1_v1_talk += 1
        $ can_sis_nerdy_school_scene1_v1 = False
        $ can_hide_windows = False
        jump school_entrance_day1

    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 2 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        MC "Хейя, Сара. Готова идти?"
        Sara "Еще нет, [player_name]. Я скажу, когда освобожусь."

        scene sis_nerdy_school_scene1_v1_p2
        Sara "Я еще буду здесь, так что, иди займись чем нибуть."
        MC "Хорошо, найду тебя позже."
        Sara "Увидимся!"
        $ sis_nerdy_school_scene1_v1_talk += 1
        $ can_sis_nerdy_school_scene1_v1 = False
        $ can_hide_windows = False
        jump school_entrance_day1


    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 3 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        MC "Привет, Сара, что случилось? Готова идти?"

        scene sis_nerdy_school_scene1_v1_p2
        Sara "Не совсем. У меня все еще урок химии. После этого я буду свободна."
        MC "Хорошо, увидимся дома."
        $ sis_nerdy_school_scene1_v1_talk += 1
        $ can_sis_nerdy_school_scene1_v1 = False
        jump school_entrance_day1

    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 4 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        Sara "(бормотание) ...а затем взять квадратный корень ... получаем ... 12.806…"
        MC "Математика?"
        Sara "Да, да. Она плавит мой мозг!"

        scene sis_nerdy_school_scene1_v1_p2
        MC "Я так понимаю, ты еще не идешь?"
        Sara "Дайте мне еще час или около того, чтобы проверить домашнюю работу."
        MC "Почему ты использываешь коридор вместо библиотеки?"
        Sara "В библиотеке слишком тихо - мне нужен фоновой шум, чтобы сосредоточиться."
        MC "Почему ты не сядешь на стул?"
        Sara "Нет, мне нравится так. Увидимся, [player_name]."
        MC "Увидимся, Сара."
        $ can_sis_nerdy_school_scene1_v1 = False
        jump school_entrance_day1

    if sis_nerdy_school_scene1_v1 == 1 and sis_nerdy_school_scene1_v1_talk == 5 and can_sis_nerdy_school_scene1_v1 == True:

        scene sis_nerdy_school_scene1_v1_p1 with dissolve
        MC "Привет, сексуальная."

        scene sis_nerdy_school_scene1_v1_p2
        Sara "Shush! Y-You can’t say stuff like that in public!"

        menu:
            "Ободрить ее.":

                MC "Не могу не сказать. ты сегодня великолепна!"
                Sara "(... Я становлюсь мокрой, когда он говорит такие комплименты…)"
                Sara "П-прибереги их до дома… Я не хочу, чтобы кто-то еще знал…"
                MC "Увидимся позже ... прекрасная."
                Sara "[player_name]! ха-ха!"
                $ can_sis_nerdy_school_scene1_v1 = False
                $ can_hide_windows = False
                jump school_entrance_day1
            "Don’t embarrass her in school.":


                MC "Да, ты, наверное, права. Я больше этого не скажу."
                Sara "Я ... я не говорил тебе ... больше не говорить ... Просто не публично."
                MC "О, так что ты хочешь, чтобы я сказал, что ты потрясающе красивая?"
                Sara "(Хе-хе!) Нет ... Я не сказала, что…"
                MC "Увидимся, когда приедешь домой."
                Sara "Увидимся [player_name]!"
                $ can_sis_nerdy_school_scene1_v1 = False
                $ can_hide_windows = False
                jump school_entrance_day1

    if can_sis_nerdy_school_scene1_v1 == False:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        show screen school_entrance_day_notclickable
        $ can_hide_windows = False
        MC "Я уже говорил с ней."
        jump school_entrance_day1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
