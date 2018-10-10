image ML_morning_scene0_v1_p1 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/1.jpg"
image ML_morning_scene0_v1_p2 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/2.jpg"
image ML_morning_scene0_v1_p3 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/3.jpg"
image ML_morning_scene0_v1_p4 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/4.jpg"
image ML_morning_scene0_v1_p5 = "/images/home/corridor/morning/scenes/ML_morning_scene0_v1/5.jpg"

label ML_morning_scene0_v1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene ML_morning_scene0_v1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "(Ха, это необычно. Это офисный костюм мамы.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Ха, это необычно. Это офисный костюм Линды.)"
    MC "(Обычно она не одевается и не выходит последнее время.)"
    scene ML_morning_scene0_v1_p2 at pandown3
    $ renpy.pause(2)
    MC "(Ее ноги выглядят действительно хорошо, хотя…)"
    MC "(Подождите - что я думаю?!)"
    MC "(С тех пор, как она поцеловала меня в засос, эти непристойные мысли о ней продолжают ползти мне в голову.)"
    MC "(Возможно, я должен просто поговорить с ней об этом, лицом к лицу?)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    scene ML_morning_scene0_v1_p3
    Mom "Oh! You startled me there, [player_name]!"
    Mom "Я как раз собиралась отправиться на работу."
    Mom "Что с тобой? Что-то придумал?"
    MC "Гм… Да-да, на самом деле - я хотел поговорить с тобой об этом… ммм… О недавнем поцелуе."

    scene ML_morning_scene0_v1_p4
    Mom "О, это ... Ха-ха ... Это было ... ничего."
    MC "Это было ... просто ... Это был первый раз, когда я когда-либо целовал девушку."
    Mom "Ой, прости. Иди сюда."

    scene ML_morning_scene0_v1_p5
    Mom "Извините, Ты тогда был такой грустный. И я хотела попытаться сделать моего мальчика счастливым."
    Mom "Наверное, я немного эмоциональна и испортила момент."
    Mom "Можешь ли ты простить меня?"
    if renpy.loadable("patch.rpy"):
        MC "Да, мама. Все в порядке."
    if not renpy.loadable("patch.rpy"):
        MC "Да, Линда. Все в порядке."
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ salon_ml_first_visit = True
    $ ml_salon_morning_visit = 1
    $ ml_can_salon_morning_scene = False
    $ ml_can_salon_morning_scene2 = False
    $ can_hide_windows = False
    jump salon_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
