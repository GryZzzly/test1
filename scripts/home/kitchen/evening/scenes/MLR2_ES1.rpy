image MLR2_ES1_p1 = "images/home/kitchen/evening/scenes/MLR2_ES1/1.jpg"
image MLR2_ES1_p2a = "images/home/kitchen/evening/scenes/MLR2_ES1/2a.jpg"
image MLR2_ES1_p2aa = "images/home/kitchen/evening/scenes/MLR2_ES1/2aa.jpg"
image MLR2_ES1_p2aaa = "images/home/kitchen/evening/scenes/MLR2_ES1/2aaa.jpg"
image MLR2_ES1_p2b = "images/home/kitchen/evening/scenes/MLR2_ES1/2b.jpg"
image MLR2_ES1_p2bb = "images/home/kitchen/evening/scenes/MLR2_ES1/2bb.jpg"
image MLR2_ES1_p2bbb = "images/home/kitchen/evening/scenes/MLR2_ES1/2bbb.jpg"
image MLR2_ES1_p3 = "images/home/kitchen/evening/scenes/MLR2_ES1/3.jpg"
image MLR2_ES1_p4 = "images/home/kitchen/evening/scenes/MLR2_ES1/4.jpg"
image MLR2_ES1_p5 = "images/home/kitchen/evening/scenes/MLR2_ES1/5.jpg"
image MLR2_ES1_p6 = "images/home/kitchen/evening/scenes/MLR2_ES1/6.jpg"
image MLR2_ES1_p7 = "images/home/kitchen/evening/scenes/MLR2_ES1/7.jpg"
image MLR2_ES1_p8 = "images/home/kitchen/evening/scenes/MLR2_ES1/8.jpg"
image MLR2_ES1_p9 = "images/home/kitchen/evening/scenes/MLR2_ES1/9.jpg"


label MLR2_ES1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene MLR2_ES1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "(Похоже, мама моет посуду. Вероятно, она не заметила, что я на кухне.)"
    else:
        MC "(Похоже, Линда моет посуду. Вероятно, она не заметила, что я на кухне.)"
    MC "(Хммм… Это может быть мой шанс доказать, насколько уверен я могу быть с ней.)"
    MC "(Может схватить ее за задницу? Наверное это слишком.)"
    MC "(Полагаю, я могу обнять ее за талию?)"

    window hide
    menu:
        "Взять маму за задницу." if renpy.loadable("patch.rpy"):
            jump MLR2_ES1_grab_ass

        "Взять Линду за задницу." if not renpy.loadable("patch.rpy"):
            jump MLR2_ES1_grab_ass

        "Обнять маму за талию." if renpy.loadable("patch.rpy"):
            jump MLR2_ES1_waist
        "Обнять Линду за талию." if not renpy.loadable("patch.rpy"):
            jump MLR2_ES1_waist


label MLR2_ES1_grab_ass:
    scene MLR2_ES1_p2a

    MC "(Ну ... Надеюсь, ей понравится, шлепок по заднице!)"
    MC "(Формы, как всегда! У нее отличная задница!)"
    MC "(Хмм… она, кажется, не реагирует…)"

    scene MLR2_ES1_p2aa

    Mom "Не сейчас. У меня нет настроения."
    Mom "Кроме того, я уже говорила тебе я занята!"
    Mom "Тебе нечем занятся?"
    MC "Извини! Виноват!"

    scene MLR2_ES1_p2aaa

    Mom "Что?! Вот дерьмо!"
    if renpy.loadable("patch.rpy"):
        Mom "Извини, я думала, что это твой отец!"
        MC "Прости мама. Я.."
    else:
        Mom "Извини, я думала, что ты Боб!"
        MC "Извини, Линда. Я.."
    Mom "Нет, не извиняйся! Ты ни в чем не виноват!"
    Mom "Сожалею. Этот ублюдок просто, ВСЕГДА ищете секса, даже когда не закончил роботу по дому, которую я ему задала!"
    jump after_menu_MLR2_ES1_label


label MLR2_ES1_waist:
    scene MLR2_ES1_p2b

    MC "(Я думаю, стоит обнять ее за талию. Это намного романтичнее, чем просто схватить ее за задницу!)"
    MC "(Давай посмотрим, что получиться…)"

    scene MLR2_ES1_p2bb

    Mom "Не сейчас. У меня нет настроения."
    Mom "Кроме того, я уже говорила тебе я занята!"
    Mom "Тебе нечем занятся?"
    MC "Извини! Виноват!"

    scene MLR2_ES1_p2bbb

    Mom "Что?! Вот дерьмо!"
    if renpy.loadable("patch.rpy"):
        Mom "Извини, я думала, что это твой отец!"
        MC "Прости мама. Я.."
    else:
        Mom "Извини, я думала, что ты Боб!"
        MC "Извини, Линда. Я.."
    Mom "Нет, не извиняйся! Ты ни в чем не виноват!"
    Mom "Сожалею. Этот ублюдок просто, ВСЕГДА ищете секса, даже когда не закончил роботу по дому, которую я ему задала!"
    jump after_menu_MLR2_ES1_label



label after_menu_MLR2_ES1_label:
    scene MLR2_ES1_p3

    Mom "Слушай, мне действительно очень жаль, [player_name]."
    Mom "Мы можем продолжить с того момента, когда я закричала?"
    MC "Мм … уверен."

    scene MLR2_ES1_p4

    Mom "Если я не ошибаюсь, я наклонилась так."
    Mom "Иди поиграй с моей попкой. Я тебе разрешаю."
    if renpy.loadable("patch.rpy"):
        MC "Спасибо, мама!"
    else:
        MC "Спасибо, Линда!"
    MC "(Вау, у нее отличная задница!)"

    scene MLR2_ES1_p5

    Mom "Ммм… Это все. Ты можешь сжать ее немного сильнее."
    MC "(Черт, она отлично смотрится в этих узких джинсах!)"

    scene MLR2_ES1_p6

    Mom "ААА... Тебе нравиться, не так ли, [player_name]?"
    MC "Конечно! Ха-ха!"
    Mom "Ну, если тебе так нравится, тогда, может быть, мы должны установить некоторые правила."

    scene MLR2_ES1_p7

    MC "Правила? Каие?"
    Mom "Позвольте мне подумать ... Хм…"
    Mom "Ну, тебе явно нравится касаться моего тела. Итак, как насчет сделки?"

    scene MLR2_ES1_p8

    MC "Сделка?"
    Mom "Ты можешь прикосаться к моему телу столько, сколько захочешь."
    MC "Звучит хорошо!"

    scene MLR2_ES1_p9

    Mom "И взамен я прикасаюсь к тебе всякий раз, когда захочу, до тех пор, пока я хочу."
    Mom "Ну как?"
    MC "О, да. Я с нетерпением жду этого!"
    Mom "Ммм ... Я тоже."

    $ day_time = 4
    $ MLR2_ES1 = False
    $ MLR2_ES2 = True
    $ can_MLR2_ES2 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump kitchen_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
