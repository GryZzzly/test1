image ml_workR2_AS1_p1 = "/images/ml_work/room1/scenes/ml_workR2_AS1/1.jpg"
image ml_workR2_AS1_p2 = "/images/ml_work/room1/scenes/ml_workR2_AS1/2.jpg"
image ml_workR2_AS1_p3 = "/images/ml_work/room1/scenes/ml_workR2_AS1/3.jpg"
image ml_workR2_AS1_p4 = "/images/ml_work/room1/scenes/ml_workR2_AS1/4.jpg"
image ml_workR2_AS1_p5 = "/images/ml_work/room1/scenes/ml_workR2_AS1/5.jpg"
image ml_workR2_AS1_p6 = "/images/ml_work/room1/scenes/ml_workR2_AS1/6.jpg"
image ml_workR2_AS1_p7 = "/images/ml_work/room1/scenes/ml_workR2_AS1/7.jpg"
image ml_workR2_AS1_p8 = "/images/ml_work/room1/scenes/ml_workR2_AS1/8.jpg"
image ml_workR2_AS1_p9 = "/images/ml_work/room1/scenes/ml_workR2_AS1/9.jpg"


label ml_workR2_AS1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_workR2_AS1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Привет мама!"
    else:
        MC "Привет, Линда!"
    Mom "Добрый день, милый. Ты здесь для работы??"
    MC "Да, у тебя есть что-нибудь для меня?"

    scene ml_workR2_AS1_p2

    Mom "Просто убира, если тебе нравится."
    MC "Конечно. Я начну сейчас."
    Mom "Спасибо, дорогой! Вернешься и сообщишь мне, когда закончишь."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump work_minigame_R2_room1_label


label after_ml_workR2_AS1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    $ inventory.earn(25)
    $ renpy.pause(3, hard = True)


    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_workR2_AS1_p3 with dissolve

    MC "Хорошо, я поубирал!"
    MC "У тебя ДЕЙСТВИТЕЛЬНО грязные сотрудники! Разве они не знают, что такое чистота? ха-ха!"
    Mom "Да, есть пара мужчин, которые являются полными неряхами. Я бы уволила их, но они знают свое дело."
    MC "Итак ... теперь, когда я закончил, возможно, мы могли бы…"

    scene ml_workR2_AS1_p4

    Mom "Прости, милый. Сегодня я очень занята."
    Mom "Видишь эту папку?"
    MC "Да?"
    Mom "Мне потребуется время на обработку. И после этой, у меня есть еще пять таких."

    scene ml_workR2_AS1_p5

    MC "Ой, Господи. Это звучит жестко."
    MC "Могу я помочь тебе?"
    Mom "Спасибо за предложение. Но если ты не квалифицированный бухгалтер, я не могу позволить тебе работать с ними."
    MC "О, справедливо, тогда. Ну, если я могу что-то сделать, просто дай знать, ладно?"

    scene ml_workR2_AS1_p6

    Mom "Подойди, милый! Не выгляди так уныло. Как только мы проходим через налоговый сезон, тогда у меня будет МНОГО свободного времени для тебя."
    Mom "Я буду занята еще не долго. Обещаю!"

    scene ml_workR2_AS1_p7

    Mom "Тем временем просто позволь своему воображению блуждать с мыслями обо всех грязных вещах, которые я сделаю тебе."
    MC "(Срань господня! У меня накопилось много фантазий!)"
    MC "(Я буду доволен когда она освободится!)"

    scene ml_workR2_AS1_p8

    Mom "Во всяком случае, можешь идти, а я займусь делом."
    Mom "Увидимся позже. Люблю тебя милый."
    if renpy.loadable("patch.rpy"):
        MC "Увидимся позже, мама. Люблю тебя тоже!"
    else:
        MC "Увидимся позже, Линда. Люблю тебя тоже!"
    $ ml_workR2_AS1 = False
    $ can_ml_workR2 = False
    $ ml_workR2_AS2 = True
    $ day_time = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
