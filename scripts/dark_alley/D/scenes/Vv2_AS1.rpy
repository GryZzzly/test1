

image Vv2_AS1_p1 = "/images/dark_alley/D/scenes/Vv2_AS1/1.jpg"
image Vv2_AS1_p2 = "/images/dark_alley/D/scenes/Vv2_AS1/2.jpg"
image Vv2_AS1_p3 = "/images/dark_alley/D/scenes/Vv2_AS1/3.jpg"
image Vv2_AS1_p4 = "/images/dark_alley/D/scenes/Vv2_AS1/4.jpg"
image Vv2_AS1_p5 = "/images/dark_alley/D/scenes/Vv2_AS1/5.jpg"
image Vv2_AS1_p6 = "/images/dark_alley/D/scenes/Vv2_AS1/6.jpg"
image Vv2_AS1_p7a = "/images/dark_alley/D/scenes/Vv2_AS1/7a.jpg"
image Vv2_AS1_p7b = "/images/dark_alley/D/scenes/Vv2_AS1/7b.jpg"
image Vv2_AS1_p8 = "/images/dark_alley/D/scenes/Vv2_AS1/8.jpg"
image Vv2_AS1_p8a = "/images/dark_alley/D/scenes/Vv2_AS1/8a.jpg"
image Vv2_AS1_p8b = "/images/dark_alley/D/scenes/Vv2_AS1/8b.jpg"
image Vv2_AS1_p8c = "/images/dark_alley/D/scenes/Vv2_AS1/8c.jpg"
image Vv2_AS1_p8d = "/images/dark_alley/D/scenes/Vv2_AS1/8d.jpg"
image Vv2_AS1_p8e = "/images/dark_alley/D/scenes/Vv2_AS1/8e.jpg"
image Vv2_AS1_p8f = "/images/dark_alley/D/scenes/Vv2_AS1/8f.jpg"
image Vv2_AS1_p8g = "/images/dark_alley/D/scenes/Vv2_AS1/8g.jpg"
image Vv2_AS1_p8h = "/images/dark_alley/D/scenes/Vv2_AS1/8h.jpg"
image Vv2_AS1_p8i = "/images/dark_alley/D/scenes/Vv2_AS1/8i.jpg"
image Vv2_AS1_p8j = "/images/dark_alley/D/scenes/Vv2_AS1/8j.jpg"
image Vv2_AS1_p9 = "/images/dark_alley/D/scenes/Vv2_AS1/9.jpg"
image Vv2_AS1_p10 = "/images/dark_alley/D/scenes/Vv2_AS1/10.jpg"
image Vv2_AS1_p11 = "/images/dark_alley/D/scenes/Vv2_AS1/11.jpg"
image Vv2_AS1_p12 = "/images/dark_alley/D/scenes/Vv2_AS1/12.jpg"
image Vv2_AS1_p13 = "/images/dark_alley/D/scenes/Vv2_AS1/13.jpg"
image Vv2_AS1_p14 = "/images/dark_alley/D/scenes/Vv2_AS1/14.jpg"
image Vv2_AS1_p15 = "/images/dark_alley/D/scenes/Vv2_AS1/15.jpg"
default V_points = 1
default Dwayne_name = "Дуэйн"
default player_name1 = "{color=#3366FF}[player_name]{/color}"
label Vv2_AS1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene Vv2_AS1_p1 with dissolve
    $ can_hide_windows = True
    MC "(Это похоже на область, которую Кэролайн описала мне, чтобы проверить...)"
    MC "(Выглядит как Виолетта! Интересно, с кем она.)"
    MC "(Я не могу противостоять ему - он сделает из меня дерьмо в драке!)"
    MC "(Я вернусь и посмотрю, что происходит…)"

    scene Vv2_AS1_p2


    Violet "Я-я сожалею, Дуэйн."
    Dwayne "Извините. Что происходит?"
    Violet "Н-Нет… *шмыгает носом*"

    scene Vv2_AS1_p3

    Dwayne "Ты мне должна. Никогда этого не забывай."
    Violet "Я не буду, Дуэйн."
    Dwayne "Я попросил тебя сделать ОДНУ простую вещь для меня."
    Dwayne "Одна простая вещь!"

    scene Vv2_AS1_p4

    Dwayne "И моя глупая чертова сестра не может даже получить это право!"
    Dwayne "Я должен просто здать тебя в полицию прямо сейчас! Хотела бы ты сидеть в тюрьме, как я? хм?!"
    Violet "Нет!"

    scene Vv2_AS1_p5

    Violet "Ооох!"
    Dwayne "В следующий раз, вам лучше ограбить магазин, в котором чертовски много денег!"
    Dwayne "Как я должен заплатить картелю за это дерьмо?! Аа?!"

    scene Vv2_AS1_p6

    Violet "P-Пожалуйста! Больше нет!"
    Dwayne "Дура. Чертовка. Сука."
    window hide
    menu:
        "Вмешаться, чтобы помочь Виолетте. Ты должен спасти ее!":
            scene Vv2_AS1_p8

            MC "(Ебать! Он убьет ее! Я не могу просто стоять на месте и смотреть!)"
            MC "(Мне ударить его?)"
            window hide
            menu:
                "Ударить его!":
                    scene Vv2_AS1_p8b

                    MC "Хяаааххх!"
                    Dwayne "Тьфу!"
                    MC "Оставь её в покое!"
                    MC "(Получи ублюдок!)"
                    jump Vv2_AS1_q1
                "Пнуть его!":
                    scene Vv2_AS1_p8a

                    MC "Привет! Оставь ее в покое!"
                    "*Шмяк*"
                    Dwayne "Ооох!"
                    jump Vv2_AS1_q1
        "Stay out of it! This guy would murder you!":

            scene Vv2_AS1_p7a

            "*БУХ*"
            Violet "Ааай!"
            Dwayne "Arrgh! Ты заставил меня повредить мой гребаный кулак."

            scene Vv2_AS1_p7b

            Dwayne "Бери реальные деньги в следующий раз."
            Dwayne "Если ты снова испортишь, тогда ты будешь сама платить за картель."
            Dwayne "Я уверен, что они сбивают несколько грандиозных долгов за месяц, позволяя им использовать твое тело."
            Violet "Н-нет! пожалуйста!"
            Dwayne "Тогда принеси мне остальную часть денег."

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
            jump Vv2_AS1_continue




label Vv2_AS1_q1:
    scene Vv2_AS1_p8c

    Dwayne "А? О, посмотри Виолетта. У тебя есть свой собственный белый рыцарь."
    Dwayne "Похоже, я должен проучить етого парня."
    MC "Я сказал, оставь ее!"

    scene Vv2_AS1_p8d

    "*Удар*"

    MC "Оой!"
    MC "(Блядь!)"

    scene Vv2_AS1_p8e

    MC "Оооуу..."
    MC "(Иисус Христос... Моя голова…)"

    scene Vv2_AS1_p8f

    Dwayne "Я не знаю, чем ты думал, пытаясь взять меня, ты, кусок дерьма."
    Dwayne "Пришло время поставить тебя на свое место."
    MC "Ахх…."

    scene Vv2_AS1_p8g

    Dwayne "В гребаном мусоре."
    MC "Эй! Остановить! Отпусти меня!"
    MC "Аххх!"

    scene Vv2_AS1_p8h

    Dwayne "Ебаный панк. В настоящее время они не уважают никого."
    MC "Ооой…."
    Dwayne "Я вернусь за остальными деньгам позже, Виолетта. Не забывай."

    scene Vv2_AS1_p8i

    MC "(Он еще не ушел?)"
    MC "(Почти…)"
    MC "(Этот ублюдок, вероятно, зделал мне чертовски черный глаз! Он бьет, как ебаный грузовик!)"

    scene Vv2_AS1_p8j
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)


    MC "О, Боже ... Виолетта…"
    MC "(Она в порядке ?! Я должен пойти и проверить…)"
    MC "(Надеюсь, что мудак не навредил ей!)"
    jump Vv2_AS1_continue


label Vv2_AS1_continue:

    scene Vv2_AS1_p9
    MC "Эй ,Виолетта?"
    Violet "…"
    MC "Виолетта? Ты меня слышишь?"

    scene Vv2_AS1_p10

    Violet "Ахх!"
    MC "Привет! Это просто я! Это просто я!"
    MC "Дуэйн ушел."
    Violet "О, черт!…"
    MC "Позвольте мне помочь тебе встать на ноги."

    scene Vv2_AS1_p10

    Violet "Спасибо, что помог мне."
    MC "Это не проблема, я бы сделал то же самое для и для других."
    Violet "Ты хороший человек."

    scene Vv2_AS1_p11

    Violet "Я ... думаю, это означает, что ты знаешь, что я ограбила Кэролайн."
    MC "Да, я знаю!"
    Violet "Пожалуйста, не говори ей. Она единственный друг, которому я действительно доверяю..."
    Violet "Я верну ей деньги обратно - как-нибудь. обещаю."
    $ menu_q1 = True
    $ menu_q2 = True
    jump Vv2_AS1_menu

label Vv2_AS1_menu:
    window hide
    scene Vv2_AS1_p11
    menu:
        "Почему этот мудак избивал тебя?" if menu_q1 == True:
            scene Vv2_AS1_p11

            MC "Почему этот мудак избивал тебя?"

            scene Vv2_AS1_p13

            Violet "Боже ... Я была глупа. Несколько лет я провожу контрабанду наркотиков для бывшего бойфренда."
            Violet "У этого парня, Дуэйна, есть достаточно доказательств, чтобы посадить меня в тюрьму. В обмен на то, что он не скажет полиции, он заставляет меня делать для него ужасные задания. Как, наприме, ограбить магазин Кэролайн."
            MC "Боже…"
            $ menu_q1 = False
            if menu_q2 == True and menu_q1 == True:
                jump Vv2_AS1_continue2
            else:
                jump Vv2_AS1_menu

        "Кто был тем придурком?" if menu_q2 == True:
            scene Vv2_AS1_p11

            MC "Кто был тем придурком?"
            if renpy.loadable("patch.rpy"):
                Violet "Это - мой брат, Дуэйн. Он был в тюрьме четыре, возможно пять лет. "
            else:
                Violet "Это - мой друг, Дуэйн. Он был в тюрьме четыре, возможно пять лет. "
            Violet "Я не скучала по нему вообще. Но теперь он вернулся, не изменившись."
            MC "Он избивал тебя раньше?"
            Violet "Избиения были ежедневными. Я привыкла к ним, не волнуйся."

            $ menu_q2 = False
            if menu_q2 == True and menu_q1 == True:
                jump Vv2_AS1_continue2
            else:
                jump Vv2_AS1_menu

label Vv2_AS1_continue2:
    scene Vv2_AS1_p14

    Violet "Ойй…"
    MC "Ты в порядке?"
    Violet "Просто немного болит. Мне нужно идти домой и лечь."
    MC "Я могу тебе помочь?"

    scene Vv2_AS1_p15

    Violet "Н-нет, мне не нужна твоя помощь. Я могу справиться с этим сама."
    MC "Ты уверена?"
    Violet "Просто ... Просто сосредоточься на заботе о Кэролайн, хорошо?"
    MC "(Эта девушка действительно нуждается в большей помощи, чем она позволяет. Что-то нужно сделать о Дуэйном...)"
    $ violetV2_scene = False
    $ violet_scene2 = True
    $ V_points = 2
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump dark_alley_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
