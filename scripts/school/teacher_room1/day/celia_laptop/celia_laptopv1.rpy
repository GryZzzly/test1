image celia_laptopv1_p1 = "images/school/teacher_room1/morning/celia_laptopv1/1.jpg"
image celia_laptopv1_p1a = "images/school/teacher_room1/morning/celia_laptopv1/1a.jpg"
image celia_laptopv1_p2 = "images/school/teacher_room1/morning/celia_laptopv1/2.jpg"
image celia_laptopv1_p3 = "images/school/teacher_room1/morning/celia_laptopv1/3.jpg"
image celia_laptopv1_p4 = "images/school/teacher_room1/morning/celia_laptopv1/4.jpg"
image celia_laptopv1_p5 = "images/school/teacher_room1/morning/celia_laptopv1/5.jpg"

label celia_day_laptopv1_label:
    scene celia_laptopv1_p1
    $ celia_laptopv1_password = renpy.input ("Enter Password", "" )
    $ renpy.sound.play('/sfx/mouse_click.mp3', loop=False)
    if celia_laptopv1_password == "Ossa36":
        MC "(Да! Пароль принят!)"
        MC "(Давай посмотрим, смогу ли я смутить ее каким-либо образом!)"
        jump celia_password_correct_v1
    else:
        MC "(Блядь! Пароль неверен.)"
        jump teacher_room1_day1

label celia_password_correct_v1:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    MC "(Давай посмотрим ... оценки? Электронные письма? Руководства по содержанию курса?)"
    MC "(Возможно, в письмах что-то интересное…)"
    MC "(Планирование курса ... Встречи родителей и учителей ... Ух ... это все скучно.)"
    MC "(Думаю, я мог бы просто повысить свои оценки, пока я здесь.)"

    scene celia_laptopv1_p2 with dissolve
    MC "(Подождите ... Подождите! Это не папка для записи классов!)"
    MC "(Мэддокс $2000? Английский $4400?)"
    MC "(Вы шутите! Миссис Селия продает оценки?!)"

    scene celia_laptopv1_p3
    MC "(Да! Это материал высшего качества!)"
    MC "(Она не будет доставать меня больше!)"
    MC "(Я лучше сфотографирую.)"

    scene celia_laptopv1_p4
    $ renpy.sound.play("sfx/photo_take.wav")
    MC "(И... Мне нужно, придумать твердый план, но по крайней мере у меня есть все доказательства, какие понадобятся.)"

    scene celia_laptopv1_p5
    MC "(Берегись, миссис Селия, я иду за тобой.!)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_celia_laptopv1 = False
    $ Judy_scene1_v1 = 1
    $ can_hide_windows = False
    jump teacher_room1_day1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
