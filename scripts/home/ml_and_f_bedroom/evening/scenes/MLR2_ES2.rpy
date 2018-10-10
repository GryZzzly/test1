image MLR2_ES2_p1 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/1.jpg"
image MLR2_ES2_p2 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/2.jpg"
image MLR2_ES2_p3 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/3.jpg"
image MLR2_ES2_p4 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/4.jpg"
image MLR2_ES2_p5 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/5.jpg"
image MLR2_ES2_p6 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/6.jpg"
image MLR2_ES2_p7 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/7.jpg"
image MLR2_ES2_p8 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/8.jpg"
image MLR2_ES2_p9 = "images/home/ml_and_f_bedroom/evening/scenes/MLR2_ES2/9.jpg"

label MLR2_ES2_label:
    $ renpy.music.stop(channel="music2", fadeout=1)

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(3,hard = True)
    scene MLR2_ES2_p1 with dissolve
    $ can_hide_windows = True
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    Mom "Буу!"
    MC "Aхх!"
    if renpy.loadable("patch.rpy"):
        MC "Господи, ты напугала меня, мам!"
    else:
        MC "Господи, ты напугала меня, Линда!"

    scene MLR2_ES2_p2

    Mom "Ну... это.. пробирайся в мою комнату!"
    MC "Эээ... я думаю..."
    Mom "Ты должно быть уже скучаешь по мне."

    scene MLR2_ES2_p3
    if renpy.loadable("patch.rpy"):
        MC "Хаха! Конечно, мам. Я люблю проводить время с тобой."
    else:
        MC "Хаха! Конечно, Линда. Я люблю проводить время с тобой."
    Mom "Ты такой милый."
    Mom "Я просто толкну тебя обратно на кровать. Сними джинсы и.."
    $ renpy.sound.play('/sfx/phone_ringing.wav', loop=False)
    "Звонок Звонок! Звонок Звонок!"
    $ renpy.sound.stop(channel="sound")
    scene MLR2_ES2_p4

    MC "Гм?"
    $ renpy.sound.play('/sfx/phone_ringing.wav', loop=False)
    "Звонок Звонок! Звонок Звонок!"
    $ renpy.sound.stop(channel="sound")
    Mom "Блин - это мой телефон. Погоди. Я буду через минуту."

    scene MLR2_ES2_p5

    Mom "Вообще-то ... ты можешь выйти? Это рабочий звонок. Извини."
    if renpy.loadable("patch.rpy"):
        MC "Конечно, Мам. Не проблема."
    else:
        MC "Конечно, Линда. Не проблема."
    MC "(А? Интересно, что заставило ее так быстро передумать.)"

    scene MLR2_ES2_p6

    Mom "Привет, Джуди. Что случилось?"
    "…"
    Mom "Угу. Сейчас не лучшее время."


    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
    scene MLR2_ES2_p7

    MC "(Джуди? Интересно, это та же Джуди, что и мой терапевт?)"
    Mom "Да, конечно. Сделка все еще продолжается."
    "…."
    Mom "Конечно, мы можем встретиться снова за кофе скоро."

    scene MLR2_ES2_p8

    Mom "Как насчет тебя? Книга идет хорошо?"
    "...."
    Mom "Писательский блок? Мне жаль это слышать."
    "…"

    scene MLR2_ES2_p9

    Mom "Конечно. Я обещала, что помогу тебе.."
    Mom "Не беспокойся, Джуди. Я дам вам несколько идей."
    "...."
    Mom "Созвонимся позже!"
    MC "(Чёрт, она почти закончила. Я лучше уйду, чтобы она не подумала, будто я подслушал ее!)"
    $ can_ml_workR2_AS2 = True
    $ MLR2_ES2 = False
    $ day_time = 4
    $ judy_q2 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump salon_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
