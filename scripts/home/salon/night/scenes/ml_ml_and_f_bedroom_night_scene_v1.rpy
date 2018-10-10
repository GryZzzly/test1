image ml_ml_and_f_bedroom_night_scene1_v1_p1 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/1.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p2 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/2.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p3 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/3.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p4 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/4.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p5 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/5.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p6 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/6.jpg"
image ml_ml_and_f_bedroom_night_scene1_v1_p7 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene1_v1/7.jpg"

image ml_ml_and_f_bedroom_night_scene2_v1_p1 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene2_v1/1.jpg"
image ml_ml_and_f_bedroom_night_scene2_v1_p2 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene2_v1/2.jpg"
image ml_ml_and_f_bedroom_night_scene2_v1_p3 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene2_v1/3.jpg"
image ml_ml_and_f_bedroom_night_scene2_v1_p4 = "images/home/salon/night/scenes/ml_ml_and_f_bedroom_night_scene2_v1/4.jpg"

screen ml_ml_and_f_bedroom_night_scene_v1_screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("ml_ml_and_f_bedroom_night_scene_v1_screen"),Jump("salon_night1")]

label ml_ml_and_f_bedroom_night_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if ml_ml_and_f_bedroom_night_visit_scene_v1 == 1 and ml_can_ml_and_f_bedroom_night_scene_v1 == True:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        scene ml_ml_and_f_bedroom_night_scene1_v1_p1 with dissolve
        $ Dad_name = "???"
        Dad "(Тьфу! Да!)"

        if renpy.loadable("patch.rpy"):
            MC "(Похоже, мои родители занимаются сексом.)"
            MC "(Может, я воспользуюсь этим шансом, чтобы заглянуть к маме!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Похоже, Линда и Боб занимаются сексом.)"
            MC "(Может, я воспользуюсь этим шансом, чтобы заглянуть к Линде?)"
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        scene ml_ml_and_f_bedroom_night_scene1_v1_p2
        MC "(Черт ... надеюсь, они не слышали, как открывалась дверь!)"
        Dad "О! ААА!"
        MC "(Видимо, нет!)"
        if renpy.loadable("patch.rpy"):
            $ Dad_name = "Папа"
        if not renpy.loadable("patch.rpy"):
            $ Dad_name = "Боб"

        scene ml_ml_and_f_bedroom_night_scene1_v1_p3
        Dad "О да, вот и все!"
        Dad "Ох, дерьмо..."
        if renpy.loadable("patch.rpy"):
            MC "(Ха, это только папа стонет.)"
        if not renpy.loadable("patch.rpy"):
            MC "(Ха, это только Боб стонет.)"
        Dad "Подожди, я получу свой стояк обратно. Просто дай мне минутку, и я войду снова!"
        Mom "Хм ... без проблем, дорогой."

        scene ml_ml_and_f_bedroom_night_scene1_v1_p4
        if renpy.loadable("patch.rpy"):
            MC "(Похоже, маме ... скучно?)"
        if not renpy.loadable("patch.rpy"):
            MC "(Похоже, Линде ... скучно?)"
        MC "(Нет! С чего бы ей скучать, занимаясь сексом?!)"
        MC "(Это не имеет смысла…)"

        scene ml_ml_and_f_bedroom_night_scene1_v1_p5

        if renpy.loadable("patch.rpy"):
            MC "(Похоже, маму больше интересует ее книга. Интересно, что это?)"
            MC "(Папа, вероятно, даже не знает или не заботится сейчас.)"
        if not renpy.loadable("patch.rpy"):
            MC "(Похоже, Линду больше интересует ее книга. Интересно, что это такое?)"
            MC "(Боб, вероятно, даже не знает или не заботится сейчас.)"
        scene ml_ml_and_f_bedroom_night_scene1_v1_p6
        Dad "ААА! О да, вот и все! Тьфу!"
        Dad "Ты чувствуешь это, дорогая?"
        Mom "МММ хмм... "
        Mom "(Зевок!)"

        scene ml_ml_and_f_bedroom_night_scene1_v1_p7
        MC "(Это должно быть одна, чертовски хорошая книга, если она умеет читать ее в середине секса!)"
        MC "(Я должен проверить, что это.)"
        MC "(В любом случае, мне лучше улизнуть, пока меня не поймали!)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ ml_can_ml_and_f_bedroom_night_scene_v1 = False
        $ ml_ml_and_f_bedroom_night_visit_scene_v1 = 2
        $ ml_bedroom_book_scene = True
        $ can_hide_windows = False
        jump salon_night1
    if ml_ml_and_f_bedroom_night_visit_scene_v1 == 2 and ml_can_ml_and_f_bedroom_night_scene_v1 == True:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        scene ml_ml_and_f_bedroom_night_scene2_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "(Интересно, мама снова будет читать.)"
        if not renpy.loadable("patch.rpy"):
            MC "(Интересно, Линда снова будет читать.)"
        MC "(По крайней мере, я увижу ее сиськи!)"
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        scene ml_ml_and_f_bedroom_night_scene2_v1_p2
        MC "(Черт! К черту эту дверь! Кто-то должен смазать эти петли!)"

        scene ml_ml_and_f_bedroom_night_scene2_v1_p3
        Dad "Боже Мой!!! Оооо да! Вот и все!"
        Dad "Возьми мой член! ААА!"
        Mom "(Snoooooorrreee)"
        MC "(Она ... спит ... ?)"

        scene ml_ml_and_f_bedroom_night_scene2_v1_p4
        if renpy.loadable("patch.rpy"):
            MC "(Черт возьми! Мама заснула во время секса!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Черт возьми! Линда на самом деле заснула во время секса!)"
        MC "(И она даже не полностью разделась.)"
        MC "(Я не знал, что у нее такая ужасная сексуальная жизнь.)"
        Dad "ААА! Я кончаю!"
        if renpy.loadable("patch.rpy"):
            MC "(Ой-ой! Мне лучше убраться отсюда, пока папа не закончил!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Ой-ой! Мне лучше убраться отсюда, пока Боб не закончил!)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ ml_can_ml_and_f_bedroom_night_scene_v1 = False
        $ ml_ml_and_f_bedroom_night_visit_scene_v1 = 2
        $ ml_ml_and_f_bedroom_night_scene_v1 = True
        $ can_hide_windows = False
        jump salon_night1

    if ml_can_ml_and_f_bedroom_night_scene_v1 == False:
        $ can_hide_windows = False
        show screen salon_night
        show screen ml_ml_and_f_bedroom_night_scene_v1_screen
        MC "Это слишком рискованно. Я должен оставить их в покое."
        jump salon_night1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
