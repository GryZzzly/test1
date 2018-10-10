image neighboor_spy_v1_p2 = "images/home/mc_room/morning/scenes/neighboor_spy/2.jpg"
image neighboor_spy_v1_p3 = "images/home/mc_room/morning/scenes/neighboor_spy/3.jpg"
image neighboor_spy_v1_p4 = "images/home/mc_room/morning/scenes/neighboor_spy/4.jpg"
image neighboor_spy_v1_p5 = "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"
image neighboor_spy_v1_p6 = "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
image neighboor_spy_v1_p7 = "images/home/mc_room/morning/scenes/neighboor_spy/7.jpg"
image neighboor_spy_v1_p8 = "images/home/mc_room/morning/scenes/neighboor_spy/8.jpg"

image mc_spy_morning = "images/home/mc_room/morning/scenes/neighboor_spy/SpyingMorningAfternoon.png"
image mc_spy_evening = "images/home/mc_room/morning/scenes/neighboor_spy/SpyingEvening.png"
image mc_spy_night = "images/home/mc_room/morning/scenes/neighboor_spy/SpyingNight.png"

image neighboor_spy_v1_p5and6_animation:
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

    0.40
    function play_effect
    "images/home/mc_room/morning/scenes/neighboor_spy/6.jpg"
    0.40
    "images/home/mc_room/morning/scenes/neighboor_spy/5.jpg"

define Neighbor2 = Character("???", color="#66CC33")
define Neighbor1 = Character("???", color="#CC00CC")
init -1 python:
    def play_effect(trans, st, at):
        renpy.play("sfx/slap.mp3", channel="sound")
label neighboor_spy_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if binoculars.selected:
        if day_time == 1:
            show screen mc_room_morning_notclickable
        if day_time == 2:
            show screen mc_room_day_notclickable
        if day_time == 3:
            show screen mc_room_evening_notclickable
        if day_time == 4:
            show screen mc_room_night_notclickable
        menu:
            "Шпионить за соседом справа.":

                if day_time == 2:
                    $ renpy.show("mc_spy_morning", layer="screens")
                    $ renpy.music.stop(channel="music2", fadeout=1)
                    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
                    MC "Окей. Посмотрим, есть ли что-нибудь интересное."
                    MC "Ах! Да! что-то происходит!"

                    hide screen mc_room_day_notclickable
                    $ renpy.hide("mc_spy_morning", layer="screens")
                    scene neighboor_spy_v1_p2 with dissolve
                    $ can_hide_windows = True
                    Neighbor1 "Ты была очень плохой девочкой! Тебя нужно наказать!"
                    Neighbor2 "Нет! Пожалуйста, нет! Я обещаю, что буду стараться в школе!"
                    Neighbor1 "Ты знаешь, сколько раз уже обещала мне это?"
                    Neighbor2 "На этот раз будет по-другому!! "
                    Neighbor1 "Я был слишком мягок с тобой, с самого начала! "
                    Neighbor2 "… "

                    scene neighboor_spy_v1_p3
                    Neighbor2 "Я не смогу сидеть несколько дней, снова!"
                    Neighbor1 "Ты должна была подумать об этом раньше!"
                    Neighbor2 "Я была! Я часами училась! Но я говорю тебе, что учитель математики ненавидит меня!"
                    Neighbor1 "*Вздох* Оправдание за оправданием."
                    Neighbor1 "Кажется, на этот раз тебе нужен лучший пример того, что я сделаю, если ты не начнешься учиться должным образом!"

                    scene neighboor_spy_v1_p4
                    Neighbor2 "(Боже! Почему?? Почему я?? Эта чертова шлюха, Селия! Тупая стерва!)"
                    Neighbor1 "Пожалуйста, не нужно меня ненавидеть - я делаю это для твоего же блага."
                    Neighbor2 "(Я уверен, что ты знаешь... Почему ты не можешь просто поверить мне!?)"

                    scene neighboor_spy_v1_p5
                    Neighbor2 "(О, нет! Это начнется через минуту!)"
                    Neighbor1 "Вот он приходит!"
                    $ renpy.sound.play("sfx/slap.mp3", channel="sound")

                    scene neighboor_spy_v1_p6
                    Neighbor2 "ААА!!! Нет!!"
                    Neighbor1 "Пожалуйста, молчи! Справься с этим, как женщина!"

                    scene neighboor_spy_v1_p5and6_animation
                    $ renpy.pause(6, hard= True)

                    scene neighboor_spy_v1_p7
                    Neighbor2 "Хватит! Хватит уже! УМОЛЯЮ ТЕБЯ! Н-Нет!"
                    Neighbor1 "*Вздох* Прекрасно."

                    scene neighboor_spy_v1_p8
                    Neighbor1 "Теперь пришло время извиниться за плохое поведение."
                    Neighbor1 "Ты знаешь, что должна сделать, не так ли?"
                    Neighbor2 "*Snip* Да… "
                    Neighbor1 "Затем встань и сразу в спальню. У меня также есть свои потребности."
                    Neighbor2 "*Snip* Окей… "
                    scene mc_room_day
                    show screen mc_room_day_notclickable
                    $ renpy.show("mc_spy_morning", layer="screens")
                    MC "Черт... Они пошли в другую комнату…."
                    MC "Мне серьезно нужно за ними проследить! "
                    MC "Я мог бы поговорить с ней в школе или пойти к ним и сказать привет, так как я их сосед."
                    $ renpy.hide("mc_spy_morning", layer="screens")
                    $ Neighboor_spy_mc_room = False
                    $ neighboor_unlocked = True
                    $ renpy.music.stop(channel="music1", fadeout=1)
                    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                    $ can_hide_windows = False
                    jump mc_room_morning1
                else:



                    if day_time == 1:
                        $ renpy.show("mc_spy_morning", layer="screens")


                    if day_time == 3:
                        $ renpy.show("mc_spy_evening", layer="screens")


                    if day_time == 4:
                        $ renpy.show("mc_spy_night", layer="screens")


                    MC "Окей. Посмотрим, есть ли что-нибудь интересное."
                    MC "Хм ... Ничего. Ну, может быть, в другое время дня."
                    $ renpy.hide("mc_spy_morning", layer="screens")
                    $ renpy.hide("mc_spy_night", layer="screens")
                    $ renpy.hide("mc_spy_evening", layer="screens")
                    $ can_hide_windows = False
                    jump mc_room_morning1
            "Назад.":
                $ can_hide_windows = False
                jump mc_room_morning1


    if not binoculars.selected:
        if day_time == 1:
            show screen mc_room_morning_notclickable
        if day_time == 2:
            show screen mc_room_day_notclickable
        if day_time == 3:
            show screen mc_room_evening_notclickable
        if day_time == 4:
            show screen mc_room_night_notclickable
        $ renpy.hide("mc_spy_morning", layer="screens")
        $ renpy.hide("mc_spy_night", layer="screens")
        $ renpy.hide("mc_spy_evening", layer="screens")
        MC "Это-просто окно..., с хорошим видом на моего соседа. Но они слишком далеко, чтобы увидеть что-нибудь глазами."
        $ can_hide_windows = False
        jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
