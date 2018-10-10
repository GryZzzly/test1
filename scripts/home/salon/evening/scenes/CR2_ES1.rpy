image CR2_ES1_p1 = "images/home/salon/evening/scenes/CR2_ES1/1.jpg"
image CR2_ES1_p2 = "images/home/salon/evening/scenes/CR2_ES1/2.jpg"
image CR2_ES1_p3 = "images/home/salon/evening/scenes/CR2_ES1/3.jpg"
image CR2_ES1_p4 = "images/home/salon/evening/scenes/CR2_ES1/4.jpg"
image CR2_ES1_p5 = "images/home/salon/evening/scenes/CR2_ES1/5.jpg"
image CR2_ES1_p6 = "images/home/salon/evening/scenes/CR2_ES1/6.jpg"
image CR2_ES1_p7 = "images/home/salon/evening/scenes/CR2_ES1/7.jpg"
image CR2_ES1_p8 = "images/home/salon/evening/scenes/CR2_ES1/8.jpg"
image CR2_ES1_p9 = "images/home/salon/evening/scenes/CR2_ES1/9.jpg"
image CR2_ES1_p10 = "images/home/salon/evening/scenes/CR2_ES1/10.jpg"
image CR2_ES1_p11 = "images/home/salon/evening/scenes/CR2_ES1/11.jpg"
image CR2_ES1_p12 = "images/home/salon/evening/scenes/CR2_ES1/12.jpg"


default CR2_ES1_day = 1
default CR2_ES1_q1 = True
default CR2_ES1_q2 = True
default CR2_ES1_q3 = False
default CR2_ES1_q4 = False
default CR2_ES1_q5 = False
default CR2_ES1_q6 = False
default CR2_ES1_q7 = False
default CR2_ES1_q8 = False
default can_CR2_ES1 = True
default can_CR2_ES1_day2 = False
default can_CR2_ES1_day3 = False
default CR2_ES1_day2_firsttime = True
default CR2_ES1_day3_firsttime = True
default CR2_ES1_q1Sara = False
label CR2_ES1_label:
    if can_CR2_ES1 == False:
        show screen salon_evening_notclickable
        MC "Я не должен беспокоить ее. Она хочет побыть одной."
        jump salon_morning1
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ can_hide_windows = True
        if CR2_ES1_day == 1:
            scene CR2_ES1_p1 with dissolve


            MC "(Кэролайн! Похоже, что она проводит день, расслабляясь перед ТВ.)"
            MC "(Давай посмотрим, что она делает.)"

            scene CR2_ES1_p2

            MC "Эй, Кэролайн! Как дела?"
            Caroline "Ох! Привет, [player_name]! Ничего особенного. Просто обращаюсь сама с собой, теперь, когда у меня есть некоторый пасивный доход."
            MC "Замечательно! Работа должна действительно работать на тебя."

            scene CR2_ES1_p3

            Caroline "Это действительно!"
            Caroline "Что я могу сделать для вас?"
            jump CR2_ES1_menu
        if CR2_ES1_day == 2:
            scene CR2_ES1_p1 with dissolve

            MC "(Точно так же, как она сказала - она все еще болтается в гостиной в свободное время.)"
            MC "(Я могу также зайти и сказать привет.)"

            scene CR2_ES1_p2

            MC "Привет снова!"
            Caroline "Здравствуй, [player_name]."
            if CR2_ES1_day2_firsttime == True:
                $ CR2_ES1_q3 = True
                $ CR2_ES1_q4 = True
                $ CR2_ES1_q5 = True
                $ CR2_ES1_day2_firsttime = False
                jump CR2_ES1_menu

        if CR2_ES1_day == 3:
            scene CR2_ES1_p1 with dissolve

            MC "(Я думаю, что это любимый магазин Кэролайн во всем чертовом городе!)"
            MC "(Она куда нибуть ходит кроме работы?!)"

            scene CR2_ES1_p2

            MC "Снова здесь?"
            Caroline "Хаха! Просто делаю маникюр."
            MC "Я никогда пойму, как женщины могут совмещатьстолько работы и следить за своей внешностью!"

            scene CR2_ES1_p3

            Caroline "Итак, что привело тебя сюда?"
            if CR2_ES1_day3_firsttime == True:
                $ CR2_ES1_q6 = True
                $ CR2_ES1_q7 = True
                $ CR2_ES1_q8 = True
                $ CR2_ES1_day3_firsttime = False
                jump CR2_ES1_menu
        jump CR2_ES1_menu

label CR2_ES1_menu:
    scene CR2_ES1_p3
    window hide
    menu:
        "Я искал тебя." if CR2_ES1_q1 == True:
            scene CR2_ES1_p3

            MC "Я искал тебя."

            scene CR2_ES1_p4

            Caroline "О, да? Как ты понял, что я буду в салоне красоты."
            MC "Просто - ты заботишся о своей внешности, а твой бизнес зарабатывает деньги."
            MC "Я сложил два и два вместе, и сделал вывод, что ты будешь в салоне красоты."
            Caroline "Это чушь собачья. Ты случайно столкнулся со мной, не так ли?"


            scene CR2_ES1_p5

            MC "Ахаха! Ты меня достала!"
            Caroline "Я знала это!"
            $ CR2_ES1_q1 = False
            $ CR2_ES1_q2 = False
            $ can_CR2_ES1_day2 = True
            jump CR2_ES1_menu_cancel

        "Как продвигается работа?" if CR2_ES1_q3 == True:
            scene CR2_ES1_p3

            MC "Как на работе?"
            Caroline "Продажи процветают. На самом деле, самая большая проблема, с которой я сейчас сталкиваюсь, - это получение запаса, доставленного мне достаточно быстро."
            MC "О да?"

            scene CR2_ES1_p6

            Caroline "Серьезно - я заказываю в кучу одежды - и прежде чем я могу показать их, они продаються онлайн!"
            MC "Это Потрясающе, Кэролайн! Поздравляю!"


            scene CR2_ES1_p8

            Caroline "Ха-ха! Это большой стресс."
            Caroline "Клянусь - эти ленивые дни - единственное, что держит меня в здравом уме!"
            MC "Не давите на себя слишком сильно!"
            $ CR2_ES1_q3 = False
            $ can_CR2_ES1_day3 = True
            jump CR2_ES1_menu

        "Ты говорила с Сарой?" if CR2_ES1_q4 == True:
            scene CR2_ES1_p3

            MC "Ты говорила с Сарой?"

            scene CR2_ES1_p9

            Caroline "Это... немного грустно. У нас с Сарой никогда не было общих интересов."
            MC "В самом деле?"
            Caroline "Мне не нравятся видеоигры, и я не занимаюсь тем, что она."
            MC "Хммм..."

            scene CR2_ES1_p3

            Caroline "Мы все еще здороваемся друг с другом. Но это не похоже на то, что у нас был бы глубокий женский разговор."
            MC "Да, я понимаю."
            $ CR2_ES1_q4 = False
            $ CR2_ES1_q1Sara = True
            $ can_CR2_ES1_day3 = True
            jump CR2_ES1_menu

        "Какие планы относительно бизнеса?" if CR2_ES1_q5 == True:
            scene CR2_ES1_p4

            MC "Какие планы относительно бизнеса?"
            Caroline "Я не знаю."

            scene CR2_ES1_p7

            Caroline "Честно говоря, я сейчас немного перегружена. Я все еще ТОЛЬКО сотрудник!"
            Caroline "Может быть, когда-нибудь я займусь разработкой собственной линии одежды? Или открою цепочку магазинов."

            scene CR2_ES1_p8

            Caroline "Однако сейчас я сосредоточена на том, чтобы мой магазин оставался прибыльным."
            $ CR2_ES1_q5 = False
            $ can_CR2_ES1_day3 = True
            jump CR2_ES1_menu

        "Я хотел поговорить о сделке, которую мы заключили." if CR2_ES1_q6 == True:
            scene CR2_ES1_p10

            MC "Я хотел поговорить о сделке, которую мы заключили."
            Caroline "Что?!"
            MC "Сделка, котор..."

            scene CR2_ES1_p6

            Caroline "Тише! Не при людях."
            MC "Ну, давай! Никто нас не слышит."
            Caroline "Я НЕ говорю об этом с тобой посреди гостиной!"
            MC "Прекрасно! Поговорим позже."
            $ CR2_ES1_q6 = False
            jump CR2_ES1_menu

        "Мама и папа ссоряться?" if CR2_ES1_q7 == True and renpy.loadable("patch.rpy"):
            jump CR2_ES1_menu_bobfight
        "Линда и Боб ссоряться?" if CR2_ES1_q7 == True and not renpy.loadable("patch.rpy"):
            jump CR2_ES1_menu_bobfight


        "У тебя есть совет, как найти девушку?" if CR2_ES1_q8 == True:
            scene CR2_ES1_p4

            MC "Кэролайн, мне было интересно-есть ли у вас какие-либо советы для поиска подруги?"
            Caroline "Конечно. С какой частью у тебя проблема?"
            MC "Это все."

            scene CR2_ES1_p7

            Caroline "Ха-ха! Тогда хорошо!"
            Caroline "Давай начнем с основ."

            scene CR2_ES1_p5

            Caroline "Убедись что ты мытый, носишь чистую одежду, и заботишься о своей внешности."
            Caroline "После этого поработай над своей уверенностью. Люди любят уверенных."

            scene CR2_ES1_p11

            Caroline "Просто подойди к девушке, которая тебе нравится, положи руку ей на плечо и спроси, можешь ли ты купить ей кофе."
            Caroline "Это так просто."

            scene CR2_ES1_p10

            MC "Это не сработало с миссис Селией."
            Caroline "Это потому, что она была твоим учителем! Есть определенные границы, которые ты должен соблюдать."

            scene CR2_ES1_p12

            Caroline "Не обращай на это слишком много внимания. Это придет со временем."
            Caroline "Просто сосредоточься на том, что тебе нравится."
            $ CR2_ES1_q8 = False
            jump CR2_ES1_menu
        "Пока.":


            if CR2_ES1_q1Sara == True:
                scene CR2_ES1_p10

                Caroline "Так что насчёт тебя и Сары? Я видела вас двоих гулявших вместе, дольше обычного."
                window hide
                menu:
                    "Мы довольно близки.":
                        scene CR2_ES1_p5

                        MC "Сара и я всегда были довольно близки. "
                        Caroline "Да, тебе повезло!"
                        $ CR2_ES1_q1Sara = False
                        jump CR2_ES1_menu_cancel
                    "Я не чувствую никакой связи с ней.":

                        scene CR2_ES1_p6

                        MC "Я не чувствую никакой связи с Сарой.."
                        MC "Я не знаю, возможно, это возрастное, но у нас, похоже, не так много общего."
                        Caroline "Ой, мне жаль это слышать. Надеюсь, она повзрослеет в ближайшие годы."
                        MC "Да, я тоже на это надеюсь."
                        $ CR2_ES1_q1Sara = False
                        jump CR2_ES1_menu_cancel

                    "У нас с Сарой кровосмесительные отношения." if Sara_points >= 2:
                        scene CR2_ES1_p10

                        MC "Да, у нас с Сарой были кровосмесительные отношения."
                        Caroline "[player_name]!"

                        scene CR2_ES1_p5

                        Caroline "Хаха! У тебя больное чувство юмора!"
                        MC "(Если бы только она знала правду!)"
                        $ CR2_ES1_q1Sara = False
                        jump CR2_ES1_menu_cancel
            else:
                jump CR2_ES1_menu_cancel



label CR2_ES1_menu_cancel:
    if CR2_ES1_day == 2:
        scene CR2_ES1_p11

        Caroline "Дай мне досмотреть программу. Увидимся позже."

        scene CR2_ES1_p12

        Caroline "Будь любезен, хорошо?"
        MC "Не волнуйся, буду! Увидимся позже, Кэролайн!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES1 = False
        $ can_hide_windows = False
        jump salon_morning1
    if CR2_ES1_day == 3:

        scene CR2_ES1_p12
        Caroline "Время доделать маникюр. Увидимся, [player_name]."
        MC "Пока, Кэролайн!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES1 = False
        $ can_hide_windows = False
        jump salon_morning1
    else:
        scene CR2_ES1_p12
        Caroline "Позвольте мне закончить просмотр. Увидимся позже."
        MC "Пока, Кэролайн."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES1 = False
        $ can_hide_windows = False
        jump salon_morning1

label CR2_ES1_menu_bobfight:
    scene CR2_ES1_p9
    if renpy.loadable("patch.rpy"):
        MC "Мама и папа ссоряться?"
    else:
        MC "AРина и Боб ссоряться?"
    Caroline "Почему ты так думаешь?"
    MC "Просто показалось ... напряженность между ними."
    Caroline "Они проходят через взлеты и падения."

    scene CR2_ES1_p4

    Caroline "Насколько я помню, у этих двоих всегда были хорошие и плохие моменты.."
    Caroline "В конце концов, они всегда справлялись. Я не вижу причин, почему этот плохой момент должен быть другим."
    MC "Да, надеюсь ты права."
    $ CR2_ES1_q7 = False
    $ can_hide_windows = False
    jump CR2_ES1_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
