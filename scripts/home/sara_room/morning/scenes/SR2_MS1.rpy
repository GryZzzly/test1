image SR2_MS1_p1 = "images/home/sara_room/morning/SR2_MS1/1.jpg"
image SR2_MS1_p2 = "images/home/sara_room/morning/SR2_MS1/2.jpg"
image SR2_MS1_p3 = "images/home/sara_room/morning/SR2_MS1/3.jpg"
image SR2_MS1_p4 = "images/home/sara_room/morning/SR2_MS1/4.jpg"
image SR2_MS1_p5 = "images/home/sara_room/morning/SR2_MS1/5.jpg"
image SR2_MS1_p6 = "images/home/sara_room/morning/SR2_MS1/6.jpg"
image SR2_MS1_p7 = "images/home/sara_room/morning/SR2_MS1/7.jpg"
image SR2_MS1_p8 = "images/home/sara_room/morning/SR2_MS1/8.jpg"

label SR2_MS1_label:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen sister_nerdy_morning_notclickable

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)

    MC "Сара, уже почти пора идти в школу. Ты готова?"
    Sara "…"
    MC "Сара?"
    hide screen sister_nerdy_morning_notclickable
    scene SR2_MS1_p1 with dissolve
    $ can_hide_windows = True

    MC "Сара?"
    Sara "Zzz…"
    MC "(Она только что уснула за своим столом?)"

    scene SR2_MS1_p2

    MC "Эй, Сара, у тебя есть пять минут, пока мы не вышли в школу."
    Sara "Mмм…"
    MC "Сара, ты должна проснуться!"

    scene SR2_MS1_p3

    Sara "Хмм?"
    MC "(Господи, она выглядит измученной! Она заболела или что?)"
    MC "С тобой все в порядке, Сара? Ты плохо выглядишь."
    Sara "Нет... я в порядке. Я хороший. Не волнуйся."

    scene SR2_MS1_p4

    MC "Ты уверена? Ты выглядишь полностью измотанной!"
    Sara "Я ... не думаю, что я лег спать прошлой ночью. Последнее, что я помню, это скрежетание в интернете с моим кланом... я, должно быть, задремала во время рейда."
    MC "Тогда это все объясняет.. "
    Sara "Ух, мне нужно идти в школу сегодня?"
    if renpy.loadable("patch.rpy"):
        MC "Если ты пропустишь урок, мама взбесится."
    else:
        MC "Если ты пропустишь урок, Линда взбесится."

    scene SR2_MS1_p5

    Sara "(Вздох) Ты прав."
    MC "Иди и прими душ. Увидимся в школе."
    Sara "Хорошо ... (Зевок!) Увидимся там, [player_name]."

    scene SR2_MS1_p6

    MC "Сара, следи за дв..."
    $ renpy.sound.play("sfx/door_hit.wav")
    "*Стук*"
    Sara "Oй!"
    MC "(Ну, я думаю, это один из способов разбудить кого-то!)"

    scene SR2_MS1_p7

    MC "Ты в порядке?"
    Sara "Да, у меня нос не кровоточит. Я в порядке."
    MC "Ты в наушниках - смотри не пойди с ними в душ!"

    scene SR2_MS1_p8

    Mom "ВЫ ДВОЕ ГОТОВЫ? ВЫ ОПОЗДАЕТЕ В ШКОЛУ!"
    if renpy.loadable("patch.rpy"):
        Sara "(Зевок!) Да, Мам! Я почти готова…"
    else:
        Sara "(Зевок!) Да, Линда! Я почти готова…"
    Sara "Хорошо, я собираюсь принять душ. Я могу опоздать на несколько минут на занятия."
    MC "Увидимся позже, Сара!"
    MC "(Я надеюсь, что эти ночные игры, не слишком сильно влияют на ее оценки…)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SR2_MS1 = False
    $ SR2_MS2 = True
    $ can_SR2_MS2 = False
    $ SR2_bath = True
    jump sister_nerdy_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
