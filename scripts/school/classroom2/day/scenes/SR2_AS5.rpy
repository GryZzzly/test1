image SR2_AS5_p1 = "images/school/classroom2/day/scenes/SR2_AS5/1.jpg"
image SR2_AS5_p2 = "images/school/classroom2/day/scenes/SR2_AS5/2.jpg"
image SR2_AS5_p3 = "images/school/classroom2/day/scenes/SR2_AS5/3.jpg"
image SR2_AS5_p4 = "images/school/classroom2/day/scenes/SR2_AS5/4.jpg"
image SR2_AS5_p5 = "images/school/classroom2/day/scenes/SR2_AS5/5.jpg"
image SR2_AS5_p6 = "images/school/classroom2/day/scenes/SR2_AS5/6.jpg"
image SR2_AS5_p7 = "images/school/classroom2/day/scenes/SR2_AS5/7.jpg"



label SR2_AS5_label:
    if can_SR2_AS5 == False:
        $ clickable = False
        show screen classroom2_day
        MC "Я уже говорил с ней."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True

        scene SR2_AS5_p1 with dissolve

        Sara "Хаха!"
        MC "(Приятно видеть, как она смеется для разнообразия. Интересно, что она читает.)"
        Sara "Овен... ты будешь..."

        scene SR2_AS5_p2

        MC "Эй, Сара! Что случилось?"
        Sara "Привет, [player_name]!"
        MC "Что ты там читаешь?"
        Sara "Просто какой-то глупый мусор."

        scene SR2_AS5_p3

        MC "Сейчас посмотрю."
        Sara "Поверь, тебе это не будет интересно."
        MC "Говорит ли это «Знаки зодиака»?"

        scene SR2_AS5_p4

        Sara "Да, это все о том, чтобы предсказать, с кем вы должны соответствовать, на основе вашего знака звезды."
        MC "Я не знал, что ты увлекаешься астрологией и звездными знаками.."
        Sara "Это не столько Звездный знак, сколько ... я не верю в эту чушь. Это просто немного забавно."
        MC "Зачем читаешь тогда?"

        scene SR2_AS5_p5

        Sara "Честно? Это будет действительно чистое ночное небо, в течение следующих нескольких дней…"
        Sara "Я вроде как хотела сходить с тобой в городскую башню."
        MC "О, это так мило с твоей стороны. Я бы с удовольствием пошел."

        scene SR2_AS5_p4

        Sara "Это не имеет значения. Этого больше не происходит."
        MC "А? Причина?"
        if renpy.loadable("patch.rpy"):
            Sara "Мама наказала меня, помнишь? Мне нельзя выходить из дома.."
        else:
            Sara "Линда наказала меня, помнишь? Мне нельзя выходить из дома.."

        menu:
            "Как насчет того, чтобы подкрасться на крышу гаража вместе и посмотреть на звезды дома?":
                scene SR2_AS5_p5

                MC "Как насчет того, чтобы подкрасться к крыше гаража и посмотреть на звезды сегодня вечером?"

                scene SR2_AS5_p6

                Sara "Ты серьезно?"
                MC "Да!"
                Sara "Да! Да! Да! Давай сделаем это! Я так рада!"

                jump SR2_AS5_continue
            "Все в порядке, Сара. Нам придется подождать, пока ты больше не будешь наказана. Когда-нибудь мы увидим звезды вместе.":

                scene SR2_AS5_p4

                MC "Мне очень жаль, Сара. Нам просто придется подождать, пока ты больше не будешь под домашним арестом.."
                MC "Я обещаю, мы когда-нибудь вместе пойдем в городскую башню, чтобы посмотреть на звезды."
                Sara "(Вздох…)"

                scene SR2_AS5_p6

                Sara "Вообще-то, держись! У меня есть идея!"
                Sara "Как насчет того, чтобы подняться на крышу гаража сегодня вечером и посмотреть на звезды оттуда?"
                MC "Да! Это отличная идея!"

                jump SR2_AS5_continue

label SR2_AS5_continue:
    scene SR2_AS5_p7

    Sara "Это будет потрясающе, [player_name]! Не могу дождаться! Я так рада!"
    MC "Где ты хочешь встретиться?"
    if renpy.loadable("patch.rpy"):
        Sara "Я ускользну из своей спальни после того, как мама уснет. Тогда встретимся в гараже.?"
    else:
        Sara "Я ускользну из своей спальни после того, как Линда уснет. Тогда встретимся в гараже.?"
    MC "Звучит здорово! Увидимся там вечером.."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False

    $ can_SR2_AS5 = False
    $ SR2_NS3 = True
    $ S_N_inbed = False
    jump classroom2_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
