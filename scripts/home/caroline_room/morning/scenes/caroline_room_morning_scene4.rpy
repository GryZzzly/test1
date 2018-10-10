image caroline_room_morning_scene4_p1 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/1.jpg"
image caroline_room_morning_scene4_p2 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/2.jpg"
image caroline_room_morning_scene4_p3 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene4/3.jpg"

label caroline_room_morning_scene4_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if caroline_room_morning_scene4 == False:
        show screen caroline_room_morning_not_clickable
        MC "Я уже говорил с ней."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_room_morning_scene4_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "(Кэролайн на своем телефоне, но похоже, что она просто пишет сообщение.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Кэролайн на своем телефоне, но похоже, что она просто переписывается.)"
    MC "(Надеюсь, она в лучшем настроении, теперь, когда я немного помог!)"
    MC "Привет, Кэролайн!"


    scene caroline_room_morning_scene4_p2
    Caroline "Ой! Привет, [player_name]!"
    Caroline "Еще раз спасибо помощь в магазине."
    Caroline "Слишком рано говорить, получаю ли я прибыль - но я определенно видела больше клиентов, просматривающих товар."
    Caroline "Интернет-магазин тоже начал снимать."

    scene caroline_room_morning_scene4_p3
    Caroline "Большое тебе спасибо за все, что ты сделал!"
    if renpy.loadable("patch.rpy"):
        Caroline "Ты лучший младший брат во всем мире!"
    if not renpy.loadable("patch.rpy"):
        Caroline "Ты лучший друг во всем мире!"
    MC "Благодарю, Кэролайн!"

    scene caroline_room_morning_scene4_p2
    Caroline "Если ты хочешь снова навестить меня на работе, я уверена, что смогу чаще использовать твою помощь."
    Caroline "Просто скажи, когда свободен."
    MC "Нет проблем! Я уверен, что ты увидишь меня снова, скоро."
    $ caroline_room_morning_scene4 = 6
    $ caroline_can_room_morning_scenes = False
    $ caroline_room_morning_scene4 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
