image SR2_AS4_p1 = "images/school/classroom2/day/scenes/SR2_AS4/1.jpg"
image SR2_AS4_p2 = "images/school/classroom2/day/scenes/SR2_AS4/2.jpg"
image SR2_AS4_p3 = "images/school/classroom2/day/scenes/SR2_AS4/3.jpg"
image SR2_AS4_p4 = "images/school/classroom2/day/scenes/SR2_AS4/4.jpg"
image SR2_AS4_p5 = "images/school/classroom2/day/scenes/SR2_AS4/5.jpg"
image SR2_AS4_p6 = "images/school/classroom2/day/scenes/SR2_AS4/6.jpg"

label SR2_AS4_label:
    if can_SR2_AS4 == False:
        $ clickable = False
        show screen classroom2_day
        MC "Я уже говорил с ней."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_AS4_p1 with dissolve

        MC "(Там Сара-приятно видеть, как она улыбается для разнообразия.)"
        MC "Эй, Сара! Сегодня ты выглядишь в лучшем настроении!"
        Sara "Привет, [player_name]. Да, я чувствую себя немного лучше."

        scene SR2_AS4_p2

        MC "Я рад это слышать. Становится ли обучение легче?"
        Sara "О Боже, нет. Это все еще ад!"
        MC "Почему ты так счастлива??"
        Sara "(Шепотом) Я просто думала о том, чтобы лежать рядом с тобой ночью. Это было так чудесно просто лежать с моей головой на груди, слушая, как бьется твое сердце."
        Sara "Я никогда в жизни не чувствовал себя более спокойно."
        MC "О, это так мило с твоей стороны. Мне тоже нравилось обнимать тебя по ночам."


        $ menu_q1 = True
        $ menu_q2 = True
        $ menu_q3 = True
        $ menu_q4 = True
        $ menu_q5 = True
        $ menu_ask = 0
        jump SR2_AS4_menu


label SR2_AS4_menu:
    scene SR2_AS4_p5
    Sara "Итак, зачем ты пришел навестить меня?"
    menu:
        "Как проходит учеба?" if menu_q1 == True:
            scene SR2_AS4_p3

            MC "Как продвигается твое обучение? Твои оценки улучшились?"
            Sara "Ух, мы должны поговорить об этом?"
            MC "Чем скорее ты вернешь свои оценки в нужное русло, тем скорее я снова проведу с тобой больше времени!"

            scene SR2_AS4_p5

            Sara "Я знаю. Я знаю... Просто ... каждый раз, когда ты говоришь об этом, это напоминает мне, что я была очень ленивой."
            MC "Хорошо, я постараюсь не поднимать эту тему снова. Просто ... постарайся повысить свои оценки, хорошо? Я не хочу, чтобы ты вечно был наказана."
            Sara "Я постараюсь вернуться на правильный путь, как только смогу, я обещаю."
            $ menu_q1 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "Тебе понравилось, как я использую вибратор?" if menu_q2 == True:
            scene SR2_AS4_p5

            MC "Тебе понравилось, как я использую вибратор?"

            scene SR2_AS4_p3

            Sara "Да, типа того. Это было просто ... очень чувствительно."
            Sara "Я полагаю, что это потому, что я никогда не делала ничего подобного раньше, поэтому мое тело не полностью привыкло к этому."

            scene SR2_AS4_p4

            Sara "Но не волнуйся - я буду следить, чтобы использовать его очень регулярно."
            Sara "Когда-нибудь, ты сможешь использовать его на мне, так долго, как схочешь."
            MC "Я с нетерпением жду этого!"
            $ menu_q2 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "Какая твоя любимая тема?" if menu_q3 == True:
            scene SR2_AS4_p5

            MC "Я не думаю, что я когда-либо спрашивал: какая твоя любимая тема?"
            Sara "В школе?"
            MC "Да."
            Sara "Хм ... честно говоря, в последнее время я вообще не интересуюсь ничем."
            Sara "Прежде чем я действительно попала в видеоигры, мне нравилась математика. Было приятно знать, что твой ответ был правильным или неправильным - у вас не было оттенков серого, как в истории или английской литературы."
            $ menu_q3 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "Я просто хотел зайти и сказать спасибо за удивительный минет." if SR2_NS2_blow_ch == True and menu_q4 == True:
            scene SR2_AS4_p3

            MC "Я просто хотел сказать спасибо за удивительный минет."
            Sara "[player_name]! Мы на занятиях! Кто-то может нас услышать..."
            MC "Все разговаривают друг с другом-никто не будет слушать."
            MC "Я просто должен был прийти и сказать тебе, что это было потрясающе. Твоя техника была великолепна. И то, как ты проглотил его в конце... Боже ... это было так чертовски здорово."

            scene SR2_AS4_p4

            Sara "Серьезно? Тебе так понравилось.?"
            MC "О да."
            Sara "МММ, думаю, тогда мне придется сделать еще один. В следующий раз я попробую взять твой член глубже в рот. Тебе бы это понравилось?"
            MC "Это было бы здорово!"
            $ menu_q4 = False
            $ menu_q5 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "Тот футфетиш, который ты мне сделала, был ооочень хорош!" if SR2_NS2_foot_ch == True and menu_q5 == True:
            scene SR2_AS4_p5

            MC "Я просто хотел заскочить и сказать, что футджоб, который ты мне сделала, был ооочень хорош."
            Sara "Правда? Тебе понравилось? Это был мой первый раз, поэтому я не была уверена, что делаю это правильно."
            MC "Поверь мне, ты была великолепна!"

            scene SR2_AS4_p6

            Sara "Ура! Я думаю, что это окупилось тогда!"
            MC "А? Что окупилось?"

            scene SR2_AS4_p4

            Sara "Учимся у лучшего преподавателя!"
            MC "Хаха! Ты очень милая."
            Sara "Я также провела несколько часов, ища секс-техники в интернете. Я старалась учить себя как можно больше."
            MC "Серьезно? Ты узнала какие-либо новые трюки?"
            Sara "О, да! Но я-то знаю, а ты узнаешь!"
            $ menu_q4 = False
            $ menu_q5 = False
            $ menu_ask += 1
            if menu_q1 == False and menu_q2 == False and menu_q3 == False and menu_q4 == False and menu_q5 == False:
                jump SR2_AS4_continue
            else:
                jump SR2_AS4_menu

        "Пропустить вопросы." if menu_ask >= 2:
            jump SR2_AS4_continue


label SR2_AS4_continue:
    scene SR2_AS4_p5

    MC "Ладно, мне лучше идти прямо сейчас. Было приятно увидеть тебя сегодня, Сара. ."
    Sara "Подожди - прежде чем ты уйдешь ... как ты думаешь, мы могли бы общаться на веб-камеру в этот вечер?"
    Sara "Я ограничена своей комнатой, но мама не забрала мой ноутбук, чтобы мы могли поговорить об этом."
    MC "Да, конечно. Увидимся вечером.."

    scene SR2_AS4_p6

    Sara "Ура! Я с нетерпением жду этого!"
    MC "Отлично! Увидимся, Сара!"
    Sara "Увидимся, [player_name]!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ can_SR2_AS4 = False
    $ S_inv_webcam = True
    $ SR2_ES1 = True

    $ menu_q1 = False
    $ menu_q2 = False
    $ menu_q3 = False
    $ menu_q4 = False
    $ menu_q5 = False
    $ menu_ask = 0
    jump classroom2_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
