image sara_night_sleeping1_v1_p1 = "images/home/sara_room/night/scenes/sleeping1/1.jpg"
image sara_night_sleeping1_v1_p2 = "images/home/sara_room/night/scenes/sleeping1/2.jpg"
image sara_night_sleeping1_v1_p3 = "images/home/sara_room/night/scenes/sleeping1/3.jpg"
image sara_night_sleeping1_v1_p4 = "images/home/sara_room/night/scenes/sleeping1/4.jpg"



label sis_nerdy_night_sleeping1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if can_sis_nerdy_night_sleeping1_v1 == True:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

        scene sara_night_sleeping1_v1_p1 with dissolve
        $ can_hide_windows = True
        MC "(Шепотом) Сара?"
        Sara "…"
        MC "(Шепотом) Ты спишь?"
        MC "(Похоже, она спит. Если я буду осторожен, я мог бы прикоснуться к ней, не разбудив.)"

        scene sara_night_sleeping1_v1_p2
        MC "(Осторожно не… Мне просто нужно снять это одеяло с первого раза.)"
        MC "(Отлично! Вау, я думал, что она будет носить пижаму. Это упрощает!)"
        MC "(Следующий шаг - снять этот бюстгальтер!)"

        scene sara_night_sleeping1_v1_p3
        MC "(Хорошо.)"
        Sara "*храп*"
        MC "(Ох…)"
        MC "(Не просыпайся, не просыпайся…)"

        scene sara_night_sleeping1_v1_p4
        Sara "(зевок!)"
        MC "(Дерьмо! Она начинает просыпаться. Я лучше уйду отсюда.)"
        MC "(По крайней мере, я увидел ее в нижнем белье!)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        scene black
        $ renpy.sound.play("sfx/door_open.mp3")
        $ renpy.pause(1, hard = True)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_sis_nerdy_night_sleeping1_v1 = False
        $ sis_nerdy_night_sleeping1_v1 = 3
        $ sara_room_night_sleeping2 = True
        $ can_hide_windows = False
        jump corridor_night1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
