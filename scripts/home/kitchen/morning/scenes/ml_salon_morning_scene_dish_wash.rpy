image ml_morning_salon_scene2_v1_p2 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/2.jpg"
image ml_morning_salon_scene2_v1_p3 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/3.jpg"
image ml_morning_salon_scene2_v1_p4 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/4.jpg"
image ml_morning_salon_scene2_v1_p5 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/5.jpg"
image ml_morning_salon_scene2_v1_p6 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/6.jpg"
image ml_morning_salon_scene2_v1_p7 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/7.jpg"

label ml_salon_morning_scene_dish_wash_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_morning_salon_scene2_v1_p2 with dissolve
    $ can_hide_windows = True
    MC "(Продолжим...)"
    MC "(Они, должно быть, остались с прошлого вечера.)"

    scene ml_morning_salon_scene2_v1_p3
    if renpy.loadable("patch.rpy"):
        MC "(Интересно, почему мама не положила их посудомоечную машину.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Интересно, почему Линда не положила их посудомоечную машину.)"
    MC "(Так или иначе это - последнее.)"
    MC "(Это хорошие вещи, но я могу опоздать в школу!)"

    scene ml_morning_salon_scene2_v1_p4
    Mom "Благодарю так много сделал для меня!"
    Mom "Ты не представляешь, как много роботы по дому ты мне помагаешь."
    if renpy.loadable("patch.rpy"):
        MC "Да, это не проблема. Рад помочь, мама."
    if not renpy.loadable("patch.rpy"):
        MC "Да, это не проблема. Рад помочь, Линда."

    scene ml_morning_salon_scene2_v1_p5
    if renpy.loadable("patch.rpy"):
        Mom "Твой отец ужасен, когда дело доходит до рутины."
    if not renpy.loadable("patch.rpy"):
        Mom "Боб ужасен, когда дело доходит до домашних дел."
    Mom "Никогда не кладет свою одежду в стирку. Никогда не моет свою тарелку после еды."
    Mom "Ты настоящий мужчина."

    scene ml_morning_salon_scene2_v1_p6
    MMC "(Настоящий мужчина?!)"
    if renpy.loadable("patch.rpy"):
        MC "(Действие мамы очень...)"
    if not renpy.loadable("patch.rpy"):
        MC "(Действие Линды очень ...)"
    MC "(Может быть, это связано с ее гормонами или еще чем-то?)"
    MC "(Девушки странные…)"

    scene ml_morning_salon_scene2_v1_p7
    Mom "(сопение…)"
    Mom "(Ммм ... Бог ... он так хорошо пахнет.)"
    Mom "(Я хотела бы просто лечь голой рядом с ним и обнимать его всю ночь)"
    Mom "(Дерьмо! Я снова слишком вовлечена в свои фантазии.)"


    scene black
    Mom "Тебе пора в школу! Поторопись! Пора двигаться дальше!"
    MC "Да, я просто вытирал тарелки"
    Mom "Нет времени!"
    MC "Хорошо, я пойду! (Что на нее нашло?)"
    $ ml_can_salon_morning_scene_dish_wash = 3
    $ ml_salon_morning_visit = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump kitchen_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
