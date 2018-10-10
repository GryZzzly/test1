image SR2_AS2_p1 = "images/school/classroom2/day/scenes/SR2_AS2/1.jpg"
image SR2_AS2_p2 = "images/school/classroom2/day/scenes/SR2_AS2/2.jpg"
image SR2_AS2_p3 = "images/school/classroom2/day/scenes/SR2_AS2/3.jpg"
image SR2_AS2_p4 = "images/school/classroom2/day/scenes/SR2_AS2/4.jpg"
image SR2_AS2_p5 = "images/school/classroom2/day/scenes/SR2_AS2/5.jpg"
image SR2_AS2_p6 = "images/school/classroom2/day/scenes/SR2_AS2/6.jpg"


label SR2_AS2_label:
    if can_SR2_AS2 == False:
        $ clickable = False
        show screen classroom2_day
        MC "Я уже говорил с ней.."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_AS2_p1 with dissolve

        MC "Эй, Сара! Как дела?"
        Sara "Привет, [player_name]! Не слишком хорошо, честно говоря."

        scene SR2_AS2_p2
        if renpy.loadable("patch.rpy"):
            Sara "Мама привела меня на рассвете в школу. А потом, как только я вернусь домой, она заставит меня учить весь вечер!"
        else:
            Sara "Линда привела меня на рассвете в школу. А потом, как только я вернусь домой, она заставит меня учить весь вечер!"
        Sara "Я больше не могу читать эти учебники! Это сводит меня с ума!"
        $ menu_q1 = True
        $ menu_q2 = True
        $ menu_q3 = True
        jump SR2_AS2_menu

label SR2_AS2_menu:
    scene SR2_AS2_p2

    menu:
        "Может, тебе стоило просто учиться, а не играть в видеоигры?" if menu_q1 == True:

            MC "Может, тебе стоило учиться, а не играть в видеоигры?"
            scene SR2_AS2_p3

            Sara "МММ…. И ты тоже!"
            if renpy.loadable("patch.rpy"):
                Sara "Это именно то, что сказала мама."
            else:
                Sara "Это именно то, что сказала Линда."
            MC "Может быть, она права?"
            Sara "Боже ... Я такая глупая! Глупая, глупя, Сара!"
            MC "(Боже, она гнобит себя, довольно сильно.)"

            scene SR2_AS2_p4

            MC "(Я должен успокоить ее-я не могу видеть ее такой.)"
            MC "Эй, не волнуйся, Сара. Ты вернешся в нужное русло с учебой!"
            MC "Ты одна из самых умных людей, которых я знаю. Нам просто нужно вернуть тебя в седло. Тогда ты снова будешь первой в классе!"

            scene SR2_AS2_p5

            Sara "Спасибо, [player_name]. Я ценю это."
            Sara "Всякий раз, когда я получаю мои оценки резервного копирования, мы будем играть в видео-игры вместе. Договорились?"
            MC "Договорились."
            $ menu_q1 = False
            if menu_q1 == False and menu_q2 == False and menu_q3 == False:
                jump SR2_AS2_cantinue
            else:
                jump SR2_AS2_menu

        "Ты пыталась поговорить с мамой о предоставлении тебе свободы снова?" if menu_q2 == True and renpy.loadable("patch.rpy"):
            scene SR2_AS2_p1

            MC "Ты пробовала поговорить с мамой о возврате некоторых свобод?"
            MC "Возможно, она успокоится и даст тебе время исправиться?"

            scene SR2_AS2_p2

            Sara "Нет, я уже это пробовала. Я практически убедила ее, чтобы у меня есть час «времени», прежде чем я лягу спать."
            MC "Как это получилось??"
            Sara "Гибельно. Я никогда не видел ее такой яростной."
            MC "(Ну, Сара позаботилась о себе, сама.)"
            $ menu_q2 = False
            if menu_q1 == False and menu_q2 == False and menu_q3 == False:
                jump SR2_AS2_cantinue
            else:
                jump SR2_AS2_menu


        "Ты пробовала поговорить с Линдой о предоставлении тебе свободы снова?" if menu_q2 == True and not renpy.loadable("patch.rpy"):
            scene SR2_AS2_p1

            MC "Ты пробовала поговорить с Линдой о возвращении некоторых свобод?"
            MC "Может быть, она успокоится и даст тебе перерыв, для разнообразия?"

            scene SR2_AS2_p2

            Sara "Нет, я уже пробовала это. Я практически умоляла ее дать мне час «моего времени», прежде чем я лягу спать."
            MC "Как все прошло?"
            Sara "Катастрофически. Я никогда раньше не видел ее такой яростной.."
            MC "(Ну, Сара как-то сама это устроила..)"
            $ menu_q2 = False
            if menu_q1 == False and menu_q2 == False and menu_q3 == False:
                jump SR2_AS2_cantinue
            else:
                jump SR2_AS2_menu

        "У тебя есть свободное время?" if menu_q3 == True:

            MC "У вас есть свободное время, вообще?"
            Sara "Если считать перерыв и обед в школе, то да, у меня в общей сложности сорок пять минут."
            MC "О, Боже..."

            scene SR2_AS2_p3

            Sara "Я знаю. Это отстой!"
            Sara "Худшая часть этого - мои друзья все выходят и веселятся! Я застрял в доме с книгами и домашним заданием!"
            MC "Ммм… Разве ты не проводила большинство ночей в доме, играя в видеоигры?"

            scene SR2_AS2_p6

            Sara "Это... не актуально."
            MC "(Я уверен, что это очень важно. Нет смысла спорить с ней, прямо сейчас. Она изучает болезненный урок.)"
            if renpy.loadable("patch.rpy"):
                MC "Хорошо. Просто попробуй и сделай все возможное, чтобы снова вернуть свои оценки к максимуму. Хорошо? Если не для мамы, тогда сделай это для меня."
            else:
                MC "Хорошо. Просто попробуй и сделай все возможное, чтобы снова вернуть свои оценки к максимуму. Хорошо? Если не для Линды, тогда сделай это для меня."

            scene SR2_AS2_p5

            Sara "Это действительно утомительно! Но я попытаюсь, [player_name]."
            MC "Спасибо, Сара."
            $ menu_q3 = False
            if menu_q1 == False and menu_q2 == False and menu_q3 == False:
                jump SR2_AS2_cantinue
            else:
                jump SR2_AS2_menu


label SR2_AS2_cantinue:
    scene SR2_AS2_p5

    MC "Я думаю, что найду тебя позже."
    Sara "Подожди, прежде чем ты уйдешь ... я могу прокрасться в твою комнату сегодня вечером?"
    if renpy.loadable("patch.rpy"):
        MC "Мама разрешит это? Я думал, ты наказана."
    else:
        MC "Линда позволит это сделать? Я думал, ты наказана."

    scene SR2_AS2_p6

    Sara "Я. Вот почему я сказала подкрасться!"
    MC "Aхх…"
    Sara "Я хотел поговорить с тобой о... некоторых вещах, которые я не могу... сказать вслух в классе."
    if renpy.loadable("patch.rpy"):
        MC "Не проблема. Приходи, когда освободишься. Просто убедись, что мама тебя не видит.!"
    else:
        MC "Не проблема. Приходи, когда освободишься. Просто убедись, что Линда тебя не видит.!"
    Sara "Круто! Увидимся, [player_name]."
    MC "Увидимся, Сара. ."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ can_SR2_AS2 = False
    $ SR2_NS1 = True
    $ S_N_inbed = False
    jump classroom2_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
