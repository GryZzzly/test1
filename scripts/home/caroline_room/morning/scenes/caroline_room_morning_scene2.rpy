image caroline_room_morning_scene2_p1 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/1.jpg"
image caroline_room_morning_scene2_p2 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/2.jpg"
image caroline_room_morning_scene2_p3 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/3.jpg"
image caroline_room_morning_scene2_p4 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene2/4.jpg"

label caroline_room_morning_scene2_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_can_room_morning_scenes == False:
        show screen caroline_room_morning_not_clickable
        MC "Я уже говорил с ней."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    scene caroline_room_morning_scene2_p1 with dissolve

    MC "(Кэролайн сказала, что я мог бы прийти и поговорить с ней в любое время.)"
    MC "(Я думаю, это не мешало бы общаться с кем-то, кроме моего терапевта.)"
    MC "(Кроме того, Кэролайн, как правило, торчит в нижнем белье, когда в своей спальне.)"

    scene caroline_room_morning_scene2_p2
    MC "Эм, привет Кэролайн. Помнишь, ты сказала, что я могу прийти и поболтать..."
    Caroline "Я сожалею, [player_name]. Я знаю, что обещала, но... "
    Caroline "...Я просто не могу сейчас."
    MC "Все хорошо?"

    scene caroline_room_morning_scene2_p3
    Caroline "…"
    MC "Кэролайн?"
    MC "(Она не может свободно общаться, но, по крайней мере, я могу посмотреть на ее задницу.)"

    scene caroline_room_morning_scene2_p4
    Caroline "Извините, [player_name]. Я сейчас под большим давлением."
    MC "Ты не упеваешь из-за этих тяжелых учебников?"
    Caroline "Нет, это мой магазин. Я... Я не могу сбалансировать финансы."
    Caroline "Слушай, ты не мог бы оставить меня одну на некоторое время??"
    Caroline "Я знаю, я обещала тебе, что буду здесь, чтобы поболтать, но сейчас я не в состоянии."
    MC "Прости, Кэролайн. Я дам вам немного пространства."
    $ caroline_can_room_morning_scenes = False
    $ caroline_morning_scenes_visit = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
