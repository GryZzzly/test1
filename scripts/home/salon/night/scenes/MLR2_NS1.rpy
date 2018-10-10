image MLR2_NS1_p1 = "images/home/salon/night/scenes/MLR2_NS1/1.jpg"
image MLR2_NS1_p2 = "images/home/salon/night/scenes/MLR2_NS1/2.jpg"
image MLR2_NS1_p3 = "images/home/salon/night/scenes/MLR2_NS1/3.jpg"
image MLR2_NS1_p4 = "images/home/salon/night/scenes/MLR2_NS1/4.jpg"
image MLR2_NS1_p5 = "images/home/salon/night/scenes/MLR2_NS1/5.jpg"
image MLR2_NS1_p6 = "images/home/salon/night/scenes/MLR2_NS1/6.jpg"
image MLR2_NS1_p7 = "images/home/salon/night/scenes/MLR2_NS1/7.jpg"
image MLR2_NS1_p8 = "images/home/salon/night/scenes/MLR2_NS1/8.jpg"

image MLR2_NS1_p1a = "images/home/salon/night/scenes/MLR2_NS1/1a.jpg"
image MLR2_NS1_p2a = "images/home/salon/night/scenes/MLR2_NS1/2a.jpg"
default MLR2_NS1_counter = 1
label MLR2_NS1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if MLR2_NS2 == True and MLR2_Sleep == True:
        jump MLR2_NS2_label
    if MLR2_NS1_counter == 2 and MLR2_Sleep == True:
        scene MLR2_NS1_p1 with dissolve
        MC "Интересно, что они делают."
        MC "Сегодня там очень тихо."
        scene MLR2_NS1_p2
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        "*Creeeaaaak*"
        scene MLR2_NS1_p2a
        MC "Хм.. Они спят..."
        MC "Я должен уйти. Я не хочу их будить."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump salon_morning1

    if MLR2_NS1_counter <= 2 and MLR2_Sleep == False:
        scene MLR2_NS1_p1 with dissolve
        MC "Интересно, что они делают."
        MC "Сегодня там очень тихо."
        scene MLR2_NS1_p2
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        "*Creeeaaaak*"
        scene MLR2_NS1_p1a
        if renpy.loadable("patch.rpy"):
            MC "Ах! Это всего лишь папа."
        else:
            MC "Ах! Это всего лишь Боб."
        MC "Я забыл! Мама ждет меня в моей спальне!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump salon_morning1

    if MLR2_NS1_counter == 1 and MLR2_Sleep == True:
        scene MLR2_NS1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            $ Dad_name = "Папа"
        else:
            $ Dad_name = "Боб"
        MC "(Думаю, я слышу, как мама занимается сексом. Это довольно слабо.)"
        MC "(Я могу рискнуть открыть дверь, чтобы проверить.)"

        scene MLR2_NS1_p2
        $ renpy.sound.play("sfx/door_squeak.mp3")
        $ renpy.pause(0.14, hard = True)
        "*Creeeaaaak*"

        Mom "Ох... Ах ... Ах ... …"
        MC "(Да, она определенно занимается сексом!)"

        scene MLR2_NS1_p3
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

        Mom "Ах! ААА! ААА!"
        Dad "Тьфу! Вот и все! Я рад, что ты наслаждаешься!"
        if renpy.loadable("patch.rpy"):
            MC "(Для разнообразия? Мама не должна так сильно наслаждаться сексом с папой.)"
        else:
            MC "(Для разнообразия? Линда не должна так сильно наслаждаться сексом с Бобом.)"

        scene MLR2_NS1_p4

        Mom "О, Господи! О, Господи! Да!"
        MC "(Интересно, если она притворяется?)"
        Mom "Сильнее! Быстрее!"
        Dad "Я иду так быстро, как я могу!"
        Mom "Еби меня сильнее, [player_name]!"
        MC "…"
        MC "(Вот, дерьмо!)"

        scene MLR2_NS1_p5

        Dad "Подождите...?"
        Dad "Ты только что позвонила [player_name]?"
        if renpy.loadable("patch.rpy"):
            MC "(О ебать... Если он узнает, что я сделал вещи с мамой, он убьет меня!)"
        else:
            MC "(О ебать... Если он узнает, что я сделал вещи с Линдой, он убьет меня!)"
        scene MLR2_NS1_p6

        Mom "Тьфу! Почему ты остановился?"
        Dad "Ты только что сказала..."
        Mom "Боже! Ты бесполезен! Я иду спать! Спокойной ночи!"
        Dad "Но я еще не кончил."

        scene MLR2_NS1_p7

        Mom "Уже поздно, и у меня завтра работа."
        Dad "Но-"
        Mom "Иди и смотри порно."
        Dad "(Вздох…)"

        scene MLR2_NS1_p8

        Dad "(Я могу поклясться, она позвонила [player_name])."
        if renpy.loadable("patch.rpy"):
            Dad "(Какого черта она будет думать о нашем сыне, когда мы занимались сексом?)"
        else:
            Dad "(Нахрена ей думать о [player_name], когда мы занимаемся сексом?)"
        Dad "(И почему она была такой сварливой в последнее время?)"
        Dad "(Ну хорошо, время, чтобы загрузиться ноутбук и поиск для некоторых старых добрых фемдом хентай!)"
        $ MLR2_MS1_NS1 = True
        $ MLR2_NS1_counter = 2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump salon_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
