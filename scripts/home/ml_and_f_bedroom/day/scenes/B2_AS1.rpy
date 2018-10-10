image B2_AS1_p1 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/1.jpg"
image B2_AS1_p2 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/2.jpg"
image B2_AS1_p3 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/3.jpg"
image B2_AS1_p4 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/4.jpg"
image B2_AS1_p5 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/5.jpg"
image B2_AS1_p6 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/6.jpg"
image B2_AS1_p7 = "/images/home/ml_and_f_bedroom/day/scenes/B2_AS1/7.jpg"

default B2_AS1_day = 1
default B2_AS1_q1 = True
default B2_AS1_q2 = True
default can_B2_AS1_day = True
default bob_payment_money = 0
label B2_AS1_label:
    if B2_AS1_day == 4:
        show screen parents_bedroom_day_notclickable
        Dad "Не сейчас, [player_name]."
        jump parents_bedroom_morning1
    if can_B2_AS1_day == False:
        show screen parents_bedroom_day_notclickable
        Dad "Не сейчас, [player_name]."
        jump parents_bedroom_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene B2_AS1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Привет, пап!"
    else:
        MC "Привет, Боб!"
    Dad "Здравствуй, чемпион. Что готовишь?"

    scene B2_AS1_p2

    MC "Что... готовить?"
    Dad "Это старое выражение ... неважно. Что происходит?"
    jump B2_AS1_menu_label

label B2_AS1_menu_label:
    scene B2_AS1_p2
    window hide
    menu:
        "{color=#00ff00}Я отсортировал документы. Не мог бы ты заплатить мне?{/color}" if money_from_bob > 0:
            $ bob_payment_money = 0
            scene B2_AS1_p2
            MC "Я вчера отсортировал документы. Не мог бы ты заплатить мне?"
            Dad "Ах! Хорошая работа, [player_name]! Вот, возьми."
            MC "Спасибо!"
            scene B2_AS1_p5
            Dad "Нет, тебе спасибо! Я ненавижу это делать! "
            Dad "После стольких стало невероятно скучно."
            MC "Хаха!"
            jump B2_AS1_payment

        "Я не знал, что ты куришь." if B2_AS1_day == 1 and B2_AS1_q1 == True:
            scene B2_AS1_p2

            MC "Я не знал, что ты куришь."
            Dad "Не знаю. По крайней мере, не сигареты. Они ужасны для легких."
            MC "Разве сигары такие же плохие?"

            scene B2_AS1_p4

            Dad "Многие так думают, но правда в том, что ты вдыхаешь сигаретный дым."
            MC "Действительно?"

            scene B2_AS1_p6

            Dad "А дым от сыгары втягивается в рот, чтобы попробовать вкус…"

            scene B2_AS1_p7

            Dad "...затем выдыхаеш."
            Dad "Все дело во вкусе, а не в никотине."

            scene B2_AS1_p5

            MC "А? Интересно! Я не знал."
            Dad "Уже знаешь..!"
            $ B2_AS1_q1 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 2
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label

        "Ты слышал о магазине Кэролайн?" if B2_AS1_q2 == True and B2_AS1_day == 1:
            scene B2_AS1_p2

            MC "Ты слышал о магазине Кэролайн?"
            if renpy.loadable("patch.rpy"):
                Dad "О, да! Твоя мама упоминала об этом недавно. Как дела?"
            else:
                Dad "О, да! Линда упоминала об этом. Как дела?"
            MC "Очень хорошо! Она перешла на онлайн-продажи."

            scene B2_AS1_p3

            Dad "Это мечта. Минимальные затраты на аренду и гораздо меньше персонала."
            Dad "Позволь мне сказать тебе кое-что, чемпион. Садись."

            scene B2_AS1_p4

            Dad "Это урок, который я хочу, чтобы ты никогда не забывал."
            MC "Я слушаю."
            Dad "Работать легко. А вот управление персоналом, это сложная часть."
            MC "Действительно?"
            Dad "Ты можешь контролировать работу и отвечать за нее - но сотрудники - люди, и они очень непредсказуемые время от времени."

            scene B2_AS1_p5
            if renpy.loadable("patch.rpy"):
                MC "Спасибо, Пап. Я запомню это!"
            else:
                MC "Спасибо, Боб. Я запомню это!"
            Dad "Молодец."
            $ B2_AS1_q2 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 2
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label


        "Ты выглядишь очень расслабленным!" if B2_AS1_day == 2 and B2_AS1_q1 == True and can_B2_AS1_day == True:

            scene B2_AS1_p2
            MC "Ты выглядишь очень расслабленным!"
            Dad "Я много работаю. Я думаю, что заслуживаю брать небольшой отпуск, время от времени."

            scene B2_AS1_p6

            Dad "И что еще я могу попросить? Это великолепный день. И у меня есть блестящая сигара, и удобный диван."
            MC "Хех... Думаю, ты прав."

            scene B2_AS1_p7

            Dad "Пока ты молод, максимально используй свое свободное время и наслаждайся выходными днями."
            Dad "Ты никогда не сможешь по-настоящему оценить их, пока они не пройдут , но все же попробуй насладиться ими."

            scene B2_AS1_p5

            Dad "Когда ты доживешь до моего возраста, у тебя будет время чтобы отдохнуть."
            Dad "Но каждый становится намного более особенным. Как сейчас."
            Dad "Я могу сидеть сложа руки, поднимать ноги и наслаждаться каждой последней секундой."
            $ B2_AS1_q1 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 3
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label

        "Разве мама не сердится на то, что ты куришь в спальне?" if B2_AS1_day == 2 and B2_AS1_q2 == True and can_B2_AS1_day == True and renpy.loadable("patch.rpy"):
            scene B2_AS1_p1

            MC "Разве мама не сердится на то, что ты куришь в спальне?"

            scene B2_AS1_p7

            Dad "Я только недавно начал. Пара мальчиков порекомендовали их мне на рыбалке."

            scene B2_AS1_p5

            Dad "Мне потребовалось некоторое время, чтобы действительно научиться ценить их."
            MC "Как насчет запаха?"
            Dad "Немного освежителя воздуха и открытое окно."
            Dad "Твоя мама пока не жаловалась, по крайней мере!"
            $ B2_AS1_q2 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 3
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label
        "Разве Линда не злится, что ты куришь сигары в спальне?" if B2_AS1_day == 2 and B2_AS1_q2 == True and can_B2_AS1_day == True and not renpy.loadable("patch.rpy"):
            scene B2_AS1_p1

            MC "Линда не злится, когда ты куришь сигары в спальне?"

            scene B2_AS1_p7

            Dad "Я только недавно начал. Пара мальчиков порекомендовали их мне на рыбалке."

            scene B2_AS1_p5

            Dad "Мне потребовалось некоторое время, чтобы действительно научиться ценить их."
            MC "Как насчет запаха?"
            Dad "Немного освежителя воздуха и открытое окно."
            Dad "Линда пока не жаловалась, по крайней мере!"
            $ B2_AS1_q2 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 3
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label




        "Между тобой и мамой все в порядке? " if B2_AS1_day == 3 and B2_AS1_q1 == True and can_B2_AS1_day == True and renpy.loadable("patch.rpy"):
            scene B2_AS1_p1

            MC "Между тобой и мамой все в порядке?"

            scene B2_AS1_p4

            Dad "Почему ты спрашиваешь?"
            MC "Мне просто любопытно. Ты, кажется, стал немного более далеким, чем обычно."
            Dad "Когда ты будешь в браке столько, сколько мы, ты узнаешь, что есть взлеты и падения."
            Dad "Твоя мать - сложная женщина - одна из причин, по которой я влюбился в нее."


            scene B2_AS1_p3

            Dad "Иногда она становиться замкнутой и должна ‘найти себя’. Я заметил, что лучше всего позволить ей заняться этим и дать ей немного пространства."
            $ B2_AS1_q1 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 4
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label

        "Между тобой и Линдой все в порядке? " if B2_AS1_day == 3 and B2_AS1_q1 == True and can_B2_AS1_day == True and not renpy.loadable("patch.rpy"):
            scene B2_AS1_p1

            MC "Между тобой и Линдой все в порядке?"

            scene B2_AS1_p4

            Dad "Почему ты спрашиваешь?"
            MC "Мне просто любопытно. Ты, кажется, стал немного более далеким, чем обычно."
            Dad "Когда вы будете дружить столько, сколько мы, вы узнаете, что есть взлеты и падения."
            Dad "Линда - сложная женщина - одна из причин, по которым я влюбился в нее."


            scene B2_AS1_p3

            Dad "Иногда она становиться замкнутой и должна ‘найти себя’. Я заметил, что лучше всего позволить ей заняться этим и дать ей немного пространства."
            $ B2_AS1_q1 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 4
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label

        "Есть ли у тебя какие-либо советы для поиска второй половинки?" if B2_AS1_day == 3 and B2_AS1_q2 == True and can_B2_AS1_day == True:
            scene B2_AS1_p1
            if renpy.loadable("patch.rpy"):
                MC "У тебя есть совет, как найти девушку, папа?"
            else:
                MC "У тебя есть совет, как найти девушку, Боб?"

            scene B2_AS1_p2

            Dad "Девушку? Хм…"
            Dad "Поставь себя правильно."

            scene B2_AS1_p3

            Dad "Будь открытым и честным в своих интересах. Если ты геймер, то расскажи об этом."
            Dad "Если ты любишь спорт или фильмы, то будьте откровенны об этом."
            if renpy.loadable("patch.rpy"):
                MC "Но что, если им не нравятся те же вещи, что и мне, папа."
            else:
                MC "Но что, если им не нравятся те же вещи, что и мне, Боб."

            scene B2_AS1_p5

            Dad "Противоположности притягиваются, чемпион."
            Dad "Вопреки тому, что ты можешь поверить, люди не ищут углеродные копии себя, когда они отправляются на свидание."
            Dad "Они ищут людей, которые падают, встают и продолжают идти. Люди, которые принимают жизнь и наслаждаются ею."

            scene B2_AS1_p4

            Dad "Единственное, о чем я должен тебя предупредить, это то, что некоторые увлечения помогут тебе познакомиться с девушками."
            Dad "Если твое хобби - рисование моделей - тогда отправляйся в игровой клуб. Если твое хобби - просмотр фильмов, тогда отправляйся в кинотеатр."
            Dad "Тебе нужно найти ее там. А потом, когда ты там, поздоровайся."
            Dad "Будьте вежлив, представься, будьте очарователен. Вот и все, что нужно сделать."

            scene B2_AS1_p6

            MC "Но, что, если мне откажут?"

            scene B2_AS1_p7

            Dad "Подлизывайся и двигайся дальше. Это произойдет."
            Dad "Ты можешь утешиться тем фактом, что ты сделалл все возможное, ты сделал первый шаг, ты попытался."
            $ B2_AS1_q2 = False
            if B2_AS1_q1 == False and B2_AS1_q2 == False:
                $ B2_AS1_day = 4
                $ B2_AS1_q1 = True
                $ B2_AS1_q2 = True
                $ can_B2_AS1_day = False
                jump B2_AS1_menu_label
            else:
                jump B2_AS1_menu_label
        "Отмена":

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump parents_bedroom_morning1


label B2_AS1_payment:
    if money_from_bob > 0:
        $ inventory.earn(25)
        $ bob_payment_money += 25
        $ money_from_bob -=1
        jump B2_AS1_payment
    else:
        "Ты получишь {color=#00ff00}[bob_payment_money]${/color}."
        jump B2_AS1_menu_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
