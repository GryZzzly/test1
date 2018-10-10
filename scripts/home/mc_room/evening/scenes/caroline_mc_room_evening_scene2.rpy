image caroline_mc_room_evening_scene2_p1 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/1.jpg"
image caroline_mc_room_evening_scene2_p2 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/2.jpg"
image caroline_mc_room_evening_scene2_p3 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene2/3.jpg"


label caroline_mc_room_evening_scene2_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_mc_room_evening_scene2_p1 with dissolve
    $ can_hide_windows = True
    MC "Кэролайн? Прошу прощения за сегодня."
    MC "Я сделаю все для тебя, клянусь. Если ты просто да.."
    Caroline "Тише."

    scene caroline_mc_room_evening_scene2_p2
    Caroline "Я та, кто должен извиняться."
    MC "Ты?"
    Caroline "Это совершенно нормально - и, возможно, даже здорово - для парня твоего возраста."
    Caroline "И, честно говоря, мой наряд не мог заставить подумать о другом."
    MC "(Да, она права!)"

    scene caroline_mc_room_evening_scene2_p3
    Caroline "Итак, извините, [player_name]. Мы друзья?"
    MC "Да, мы друзья."
    MC "И для протокола... Мне тоже жаль."
    Caroline "Ой! И пока я не забыла - я придумала небольшой сюрприз для тебя."

    scene caroline_mc_room_evening_scene2_p2
    MC "Ой, ты   не должна делать это."
    Caroline "Поверь. Я думаю, тебе понравится!"
    Caroline "Увидимся, [player_name]."
    MC "Увидимся, Кэролайн!"
    $ caroline_mc_room_evening_scene2 = False
    $ caroline_mc_room_evening_scene3 = True
    $ caroline_mc_room_can_evening_scene3 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
