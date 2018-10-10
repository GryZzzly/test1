image SR2_MS2_p1 = "images/home/sara_room/morning/SR2_MS2/1.jpg"
image SR2_MS2_p2 = "images/home/sara_room/morning/SR2_MS2/2.jpg"
image SR2_MS2_p3 = "images/home/sara_room/morning/SR2_MS2/3.jpg"
image SR2_MS2_p4 = "images/home/sara_room/morning/SR2_MS2/4.jpg"
image SR2_MS2_p5 = "images/home/sara_room/morning/SR2_MS2/5.jpg"
image SR2_MS2_p6 = "images/home/sara_room/morning/SR2_MS2/6.jpg"
image SR2_MS2_p7 = "images/home/sara_room/morning/SR2_MS2/7.jpg"
image SR2_MS2_p8 = "images/home/sara_room/morning/SR2_MS2/8.jpg"

label SR2_MS2_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen sister_nerdy_morning_notclickable
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)

    Mom "Нет смысла лгать мне, Сара. Отчет пришел сегодня по почте ."
    Sara "Wh-What?!"
    if renpy.loadable("patch.rpy"):
        MC "(А? Звучит так, будто мама и Сара поссорились. Я должен проверить это и узнать, что происходит.)"
    else:
        MC "(А? Похоже, Линда и Сара поссорились. Я должен проверить это и узнать, что происходит.)"

    hide screen sister_nerdy_morning_notclickable
    $ can_hide_windows = True
    scene SR2_MS2_p1 with dissolve
    Mom "Ты всегда был отличницей. Итак, представьте мое удивление, когда я открываю твою карточку отчета, и вижу множество D, E и даже F!"
    Mom "Я имею в виду, серьезно - как это у тебя двойка по истории?!"
    if renpy.loadable("patch.rpy"):
        Sara "Мама, я"
    else:
        Sara "Линда, я"

    scene SR2_MS2_p2

    Mom "Это совершенно неприемлемо. Ты знаешь, что происходит с учениками, которые плохо учатся в школе? Они не учатся в хороших колледжах."
    Mom "Ты хочешь пойти в хороший колледж, не так ли?"
    if renpy.loadable("patch.rpy"):
        Sara "Да, Мама."
    else:
        Sara "Д-Да, Линда."

    scene SR2_MS2_p3

    Mom "Возможно, тогда ты можешь дать мне какое-то объяснение, для этих совершенно ужасных результатов."
    Sara "Я... не знаю…"
    Mom "Как часто ты училась в течение последних нескольких месяцев?"
    Sara "Так же, как всегда"
    Mom "Не обманывай меня, Сара!"

    scene SR2_MS2_p4

    Mom "Я знаю, что это такое-ты проводишь все свое время, играя в эту глупую онлайн-игру."
    Mom "Ну с этого момента тебе запрещено."
    Sara "Что?!"
    if renpy.loadable("patch.rpy"):
        Mom "Нет компьютерных игр, не выходить с друзьями, и не висеть с братом."
    else:
        Mom "Нет компьютерных игр, не выходить с друзьями, и не висеть с [player_name]."

    scene SR2_MS2_p5

    Sara "(Сопит!)"
    Mom "Это бесполезно, молодая леди. Если тебе нельзя доверять, свое собственное образование, тогда мне придется отменить твои привилегии."
    Mom "Ты должна оставаться в своей спальне и учиться. Я позвоню тебе, когда придет время обедать. Но после этого ты вернешься в свою комнату и продолжишь."
    Sara "Это несправедливо! (Рыдает!)"

    scene SR2_MS2_p6

    Mom "Я не спрашиваю, требуется тебе неделя или десять недель. Ты будешь пересматривать и пересдавать каждый экзамен, пока не выйдешь, ПО КРАЙНЕЙ МЕРЕ B, в каждом."
    Mom "Это ясно?"
    Sara "…"
    Mom "Я спросила, ясно?!"
    if renpy.loadable("patch.rpy"):
        Sara "(Сопит) Да, Мама."
    else:
        Sara "(Сопит) Д-Да, Линда."

    scene SR2_MS2_p7

    Mom "Ой, [player_name]! Я не видела, чтобы ты там стоял."
    MC "С Сарой все в порядке?"
    Mom "С ней все будет хорошо. Она просто решила играть в видеоигры, а не учиться. Она собирается учиться, очень ценный урок, в ближайшие дни."
    MC "Может быть, я мог бы помочь ей учиться?"

    scene SR2_MS2_p8

    Mom "Прости, милый. Я знаю, ей очень нравится тусоваться с тобой, но я не могу позволить ей отвлекаться."
    Mom "Пока она не подтянет каждый предмет крайней мере до B, до тех пор не выйдет никуда."
    MC "Я могу пойти и поговорить с ней, по крайней мере?"
    Mom "Нет, дай ей немного пространства. Вы всегда можете общаться в школе."
    if renpy.loadable("patch.rpy"):
        MC "(Gee… Мама сейчас очень жестко относится к Саре.)"
    else:
        MC "(Gee… Линда очень жестко относится к Саре.)"
    MC "(Опять же, Сара, вероятно, должна была действительно учиться. Она выучила большую часть этого, сама.)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SR2_MS2 = False
    $ SR2_grounded = True
    $ SR2_AS1 = False
    $ SR2_AS2 = True
    $ day_time = 2
    jump corridor_morning1



label SR2_grounded_label:
    $ clickable = False

    if day_time == 1:
        show screen corridor_morning

    if day_time == 2:
        show screen corridor_day
    if day_time == 3:
        show screen corridor_evening

    if renpy.loadable("patch.rpy"):
        MC "Я не могу войти внутрь. Мама просила меня не делать этого."
    else:
        MC "Я не могу войти внутрь. Мама просила меня не делать этого."
    $ clickable = True
    jump corridor_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
