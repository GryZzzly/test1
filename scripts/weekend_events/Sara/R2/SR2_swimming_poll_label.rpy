image SR2_weekend_swimming_pool_p1 = "images/Weekend_Events/Sara/R2/1.jpg"
image SR2_weekend_swimming_pool_p2 = "images/Weekend_Events/Sara/R2/2.jpg"
image SR2_weekend_swimming_pool_p3 = "images/Weekend_Events/Sara/R2/3.jpg"
image SR2_weekend_swimming_pool_p4 = "images/Weekend_Events/Sara/R2/4.jpg"

image SR2_weekend_swimming_pool_background = "images/Weekend_Events/Sara/R2/Map/1.jpg"

default SR2_after_swimming = False
default SR2_after_lemonade = False
default SR2_after_sunbed = False
default SR2_after_waterslide = False
default music_continue = True

label SR2_weekend_swimming_pool_label:
    hide screen mc_room_day_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_morning_notclickable
    hide screen mc_room_night_notclickable
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ week_day = 6
    $ day_time = 2
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ renpy.pause(3,hard = True)
    $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
    scene SR2_weekend_swimming_pool_p1 with dissolve
    $ can_hide_windows = True
    MC "(Хорошо, я изменился и готов плавать.)"
    MC "(Теперь ... где, черт возьми, Сара?)"
    MC "(Сегодня даже не так много работы..)"

    scene SR2_weekend_swimming_pool_p2

    Sara "Привет, [player_name]!"
    MC "Ах!"
    Sara "Прости! Я тебя напугала?"
    MC "Чуточку!"
    Sara "Хехе!"

    scene SR2_weekend_swimming_pool_p3

    Sara "MWAH!"
    MC "(Вау! Я никогда не видел Сару такой головокружительной. Она должна быть счастлива пойти на это свидание со мной.)"
    Sara "Я так рада, что ты здесь!"
    MC "Я тоже, Сара. Ты долго ждала ?"

    scene SR2_weekend_swimming_pool_p4

    Sara "Всего несколько минут."
    Sara "Что ты хочешь делать?"
    MC "Хочешь искупаться в бассейне?"
    Sara "Я не умею плавать.."
    MC "О да, я совсем забыл. Извини."
    $ can_hide_windows = False
    jump swimming_poll_label


label swimming_poll_label:
    hide screen displayTextScreen
    scene SR2_weekend_swimming_pool_background
    if music_continue == True:
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Life of Riley.mp3', channel="music2", loop=True, fadein = 2)
        $ can_map = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    $ music_continue = True
    call screen swimming_poll_scr

screen swimming_poll_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 1097
        ypos 478
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b1.png"
        hover "images/Weekend_Events/Sara/R2/Map/b1_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Плавать с Сарой в бассейне")
            action [Hide("displayTextScreen"),Jump("SR2_swimming_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 725
        ypos 278
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b2.png"
        hover "images/Weekend_Events/Sara/R2/Map/b2_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Пить лимонад")
            action [Hide("displayTextScreen"),Jump("SR2_Lemonade_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1511
        ypos 463
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b3.png"
        hover "images/Weekend_Events/Sara/R2/Map/b3_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Шезлонги")
            action [Hide("displayTextScreen"),Jump("SR2_SunBed_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 15
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b4.png"
        hover "images/Weekend_Events/Sara/R2/Map/b4_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Водная горка")
            action [Hide("displayTextScreen"),Jump("SR2_waterslide_label")]
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 1352
        ypos 297
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b5.png"
        hover "images/Weekend_Events/Sara/R2/Map/b5_hover.png"
        if clickable == True:
            hovered Show("displayTextScreen", displayText = "Джакузи")
            action [Hide("displayTextScreen"),Jump("SR2_jacuzzi_label")]
            unhovered Hide("displayTextScreen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
