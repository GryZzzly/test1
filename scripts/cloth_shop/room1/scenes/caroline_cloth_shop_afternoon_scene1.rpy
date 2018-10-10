image caroline_cloth_shop_afternoon_scene1_p1 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/1.jpg"
image caroline_cloth_shop_afternoon_scene1_p2 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/2.jpg"
image caroline_cloth_shop_afternoon_scene1_p3 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/3.jpg"
image caroline_cloth_shop_afternoon_scene1_p4a = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/4a.jpg"

image caroline_cloth_shop_afternoon_scene1_gotcamerap1 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/Got_camera/1.jpg"
image caroline_cloth_shop_afternoon_scene1_gotcamerap2 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternon_scene1/Got_camera/2.jpg"

label caroline_cloth_shop_afternoon_scene1_label:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_cloth_shop_afternoon_scene1 == True and caroline_cloth_shop_have_camera == 1:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene caroline_cloth_shop_afternoon_scene1_p1 with dissolve
        MC "Вторая половина дня, Кэролайн!"
        Caroline "Привет, [player_name]!"
        Caroline "Идеальный выбор времени - я только что закончила планировать свою идею, чтобы сохранить магазин!"
        MC "Отлично! Чем могу помочь?"

        scene caroline_cloth_shop_afternoon_scene1_p2
        Caroline "Ладно, послушай. У меня есть трехточечный план."
        Caroline "Первое - я собираюсь заказать новый ассортимент косплейных нарядов."
        Caroline "Второе - я собираюсь продавать их, моделируя их и помещая картинки в интернете."


        scene caroline_cloth_shop_afternoon_scene1_p3

        Caroline "Это приводит меня к третьей точке - я тоже начинаю интернет-магазин!"
        Caroline "Это, я надеюсь, увеличит мой годовой оборот достаточно, чтобы получить прибыль."
        MC "Звучит как отличная идея! Что мне нужно делать?"
        Caroline "Ты можешь сделать несколько фотографий меня в костюмах?"
        MC "Конечно!"

        scene caroline_cloth_shop_afternoon_scene1_p4a
        Caroline "Умм ... есть только одна крошечная проблема."
        Caroline "У меня нет камеры."
        MC "Ах... Точно."
        Caroline "Если ты можешь взять ее, вернись, и мы начнем."
        Caroline "Мне нужно продолжить создание своего онлайн-каталога."
        MC "Хорошо, Кэролайн. Я найду камеру."
        $ caroline_cloth_shop_afternoon_scene1 = False
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ caroline_cloth_shop_have_camera = 2
        $ can_hide_windows = False
        jump cloth_shop_open_label
    if caroline_cloth_shop_afternoon_scene1 == False and not camera1 in inventory.items:
        scene caroline_cloth_shop_afternoon_scene1_p1 with dissolve
        Caroline "Хей, [player_name]. Удалось найти камеру?"
        MC "Еще нет."
        $ can_hide_windows = False
        jump cloth_shop_open_label
    if camera1 in inventory.items and caroline_cloth_shop_have_camera == 2:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        scene caroline_cloth_shop_afternoon_scene1_gotcamerap1 with dissolve
        MC "Эй, Кэролайн! Я нашел камеру!"
        Caroline "Удивительно, [player_name]! Это похоже действительно хорошая камера."
        Caroline "Я готова начать делать сеансы моделирования с одеждой, когда ты будетшь готов."

        scene caroline_cloth_shop_afternoon_scene1_gotcamerap2
        Caroline "Ты делаете тяжелую работу - так как насчет того, чтобы выбрать экипировку?"
        Caroline "Попытайся сосредоточиться на получении хороших ракурсов камеры."
        Caroline "Лучшие снимки означают больше продаж, а это означает, что больше денег!"
        $ caroline_cloth_shop_have_camera = 3
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ caroline_morning_scenes_visit = 5
        jump cosplay_menu_label

    if camera1 in inventory.items and caroline_cloth_shop_have_camera == 3:
        if caroline_mc_room_evening_scene2 == True:
            scene caroline_cloth_shop_afternoon_scene1_p4a
            Caroline "[player_name]... Вечером мы должны поговорить конфиденциально, сейчас это не хороший момент для этого."
            $ can_hide_windows = False
            jump cloth_shop_open_label
        scene caroline_cloth_shop_afternoon_scene1_p1
        Caroline "Ой! Привет, [player_name]! Готов к другой фотосессии?"

        menu:
            "Конечно!":

                jump cosplay_menu_label
            "Не сейчас.":
                $ can_hide_windows = False
                jump cloth_shop_open_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
