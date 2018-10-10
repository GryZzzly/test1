image Zv2_MS2_p1 = "images/Bob_work/reception/M/scenes/Zv2_MS2/1.jpg"
image Zv2_MS2_p2 = "images/Bob_work/reception/M/scenes/Zv2_MS2/2.jpg"
image Zv2_MS2_p3 = "images/Bob_work/reception/M/scenes/Zv2_MS2/3.jpg"
image Zv2_MS2_p4 = "images/Bob_work/reception/M/scenes/Zv2_MS2/4.jpg"
image Zv2_MS2_p5 = "images/Bob_work/reception/M/scenes/Zv2_MS2/5.jpg"
image Zv2_MS2_p6 = "images/Bob_work/reception/M/scenes/Zv2_MS2/6.jpg"
image Zv2_MS2_p7 = "images/Bob_work/reception/M/scenes/Zv2_MS2/7.jpg"
image Zv2_MS2_p8 = "images/Bob_work/reception/M/scenes/Zv2_MS2/8.jpg"
image Zv2_MS2_p9 = "images/Bob_work/reception/M/scenes/Zv2_MS2/9.jpg"

default Zv2_MS2_q1 = True
default Zv2_MS2_q2 = True
default Zv2_MS2_q3 = True
default Zv2_MS2_q4 = True
default Zv2_MS2_q5 = False
default Zv2_MS2_q6 = False
default Zv2_MS2_q7 = False
default Zv2_MS2_q8 = False
default Zv2_MS2_q9 = False
default Zv2_MS2_q10 = False
default Zv2_MS2_companyname = 0
default Zv2_MS2_companyname_found = 0
default Zv2_MS2_truth = False
default Zv2_ES1 = False
default Zv2_lie_counter = 0
default Zv2_true_counter = 0
default Zv2_Truth = False
label Zv2_MS2_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if Zv2_Truth == True:
        scene Zv2_MS2_p1 with dissolve

        MC "Привет, Зури!"
        Zuri "О! Привет, [player_name]."

        scene Zv2_MS2_p9

        Zuri "Твоя помощь с этими именами, заработала мне и моей сестре МИЛЛИОНЫ. Мы обе ОЧЕНЬ благодарны за то, что ты сделал для нас."
        MC "Ничего страшного, Зури. Еще раз спасибо за все, что вы сделали для меня."
        jump Zv2_MS2_cancel_label
    else:

        scene Zv2_MS2_p1 with dissolve

        Zuri "ААА! Еще раз здравствуй, [player_name]! Как ты?"
        MC "Я в порядке, Зури. Занята сегодня?"
        Zuri "Я всегда занята."

        jump Zv2_MS2_menu


label Zv2_MS2_menu:
    scene Zv2_MS2_p1
    window hide
    menu:
        "Как долго ты работаешь на папу?" if Zv2_MS2_q1 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q1_label
        "Как долго ты работаешь на Боба?" if Zv2_MS2_q1 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q1_label


        "Где ты познакомилась с папой?" if Zv2_MS2_q2 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q2_label
        "Где ты познакомилась с Бобом?" if Zv2_MS2_q2 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q2_label


        "Каково это-работать на папу? " if Zv2_MS2_q3 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q3_label
        "Каково это работать на Боба? " if Zv2_MS2_q3 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_q3_label


        "{color=#00ff00}Попросить у нее магнитную карточку для папиных офисных дверей.{/color}" if Zv2_MS2_q4 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_magnetcard_label
        "{color=#00ff00}Попросить у нее магнитную карту для дверей от офиса Боба.{/color}" if Zv2_MS2_q4 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_magnetcard_label


        "{color=#00ff00}Спросить ее, когда у папы деловая поездка, или что-то вроде того.{/color}" if Zv2_MS2_q5 == True and renpy.loadable("patch.rpy"):
            jump Zv2_MS2_bobtrip_label
        "{color=#00ff00}Спросить ее, когда у Боба деловая поездка, или еще что-нибудь.{/color}" if Zv2_MS2_q5 == True and not renpy.loadable("patch.rpy"):
            jump Zv2_MS2_bobtrip_label


        "Зури - необычное имя. Откуда ты?" if Zv2_MS2_q6 == True:
            jump Zv2_MS2_zuriname_label

        "Хорошо платит?" if Zv2_MS2_q7 == True:
            jump Zv2_MS2_pay_label

        "{color=#00ff00}Поговорить о предложении Зури.{/color}" if Zv2_MS2_q9 == True:
            jump Zv2_MS2_zuriproposition_label

        "{color=#00ff00}Разговор о названии компании.{/color}" if Zv2_MS2_q10 == True:
            jump Zv2_MS2_companyname1_label
        "Отмена":

            jump Zv2_MS2_cancel_label

label Zv2_MS2_q1_label:
    scene Zv2_MS2_p3
    if renpy.loadable("patch.rpy"):
        MC "Как долго ты работаешь на папу, Зури?"
    else:
        MC "Как долго ты работаешь на Боба, Зури?"
    Zuri "Должно быть ... три или четыре месяца?"
    MC "А? Значит, ты здесь новенькая?"

    scene Zv2_MS2_p1

    Zuri "Да, мне очень повезло. Это отличная компания для работы. Намного лучше, чем моя старая работа!"
    MC "Я рад это слышать!"
    $ Zv2_MS2_q1 = False
    jump Zv2_MS2_menu

label Zv2_MS2_q2_label:
    scene Zv2_MS2_p1
    if renpy.loadable("patch.rpy"):
        MC "Где ты встретила папу?"
    else:
        MC "Где ты познакомились с Бобом?"

    scene Zv2_MS2_p4

    Zuri "Интервью было всего пять месяцев назад - но я знала его раньше."
    Zuri "Мы встретились во Франции, на бизнес-конференции в Тулузе. Это было три или четыре года назад."
    MC "Круто. Значит вы давно общаетесь?"

    scene Zv2_MS2_p2

    Zuri "На самом деле, нет. Мы потеряли связь, вскоре после конференции. Только когда я снова встретила его в Нью-Йорке, он сказал мне, что ищет нового секретаря."
    MC "Ну, поздравляю с работой!"
    Zuri "Спасибо!"
    $ Zv2_MS2_q2 = False
    jump Zv2_MS2_menu

label Zv2_MS2_q3_label:
    scene Zv2_MS2_p1
    if renpy.loadable("patch.rpy"):
        MC "Как тебе работать на папу?"
    else:
        MC "Как работаеться на Боба?"

    scene Zv2_MS2_p5

    if renpy.loadable("patch.rpy"):
        Zuri "Мне очень нравится работать на твоего отца. Есть некоторые боссы, которые наваливают работу на своих сотрудников."
        Zuri "Твой отец не такой, он делает много работы сам."
    else:
        Zuri "Мне очень нравится работать на Боба. Есть некоторые боссы, которые наваливают работу на своих сотрудников."
        Zuri "Боб не такой: он много работает сам."
    Zuri "Он приводит пример, и я действительно горжусь тем, что работаю на него."
    $ Zv2_MS2_q3 = False
    jump Zv2_MS2_menu

label Zv2_MS2_magnetcard_label:
    if renpy.loadable("patch.rpy"):
        MC "Привет, Зури. Я разговаривал с папой. Он сказал, что я могу захватить магнитную карту."
    else:
        MC "Привет, Зури. Я поговорил с Бобом. Он сказал, что я могу захватить магнитную карту."
    Zuri "В самом деле?"
    MC "Да, он, вероятно, отправил тебе письмо с объяснением ситуации."

    scene Zv2_MS2_p6

    Zuri "Дай мне проверить…"
    Zuri "Ах! Вот оно что. Ладно, без проблем. Сейчас я тебе его отдам."
    MC "Спасибо, Зури!"

    scene Zv2_MS2_p7
    if renpy.loadable("patch.rpy"):
        Zuri "Твой отец говорил что-нибудь о том, чтобы заказать мне новую карту?"
    else:
        Zuri "Боб сказал что-нибудь о том, чтобы выдать мне новую карту?"
    MC "Да, да. Надеюсь, это не займет слишком много времени."
    Zuri "Все в порядке - я не спешу."
    $ Zv2_MS2_q4 = False
    $ inventory.add(zuri_magentcard )
    jump Zv2_MS2_menu

label Zv2_MS2_bobtrip_label:
    scene Zv2_MS2_p1
    if renpy.loadable("patch.rpy"):
        MC "Зури, мне было интересно ... У папы скоро появятся деловые поездки?"
    else:
        MC "Зури, мне было интересно ... У Боба скоро появятся деловые поездки?"
    scene Zv2_MS2_p3

    Zuri "Вероятно? Почему ты хочешь знать?"
    if renpy.loadable("patch.rpy"):
        MC "Мы планируем устроить семейный ужин как-нибудь вечером, и мы хотим убедиться, что он дома в этот время."
    else:
        MC "Я ... мы планируем поужинать как-нибудь вечером, и мы хотим убедиться, что он дома."

    scene Zv2_MS2_p9

    Zuri "О, это очень мило. Я уверена, ему понравится!"
    Zuri "Сейчас я проверю его расписание и скажу, когда он занят…"

    scene Zv2_MS2_p8

    Zuri "Ладно... похоже, он уехал на выходные. Я не вижу других командировок."
    MC "Это прекрасно, Зури! Это все, что мне нужно знать."
    if renpy.loadable("patch.rpy"):
        Zuri "Рада, что смогла помочь. Приятного семейного ужина!"
        MC "(Отлично! Я должен сказать маме, что папа уехал на выходные!)"
    else:
        Zuri "Рада, что смогла помочь. Приятного вам ужина!"
        MC "(Отлично! Я просто должен сообщить Линде, что Боб уехал на выходные!)"

    $ MLR2_MS1_BCalendar = True
    $ Zv2_MS2_q8 = True
    $ Zv2_MS2_q5 = False
    jump Zv2_MS2_menu

label Zv2_MS2_zuriname_label:
    scene Zv2_MS2_p1

    MC "Зури - довольно необычное имя. Откуда ты?"

    scene Zv2_MS2_p2

    Zuri "Необычное? Что ты имеешь в виду?"
    MC "Я не в плохом смысле! Это мило на самом деле!"


    scene Zv2_MS2_p9

    Zuri "ОУ... ты милый. Вообще - то, это французское. Я родилась, недалеко от Марселя."
    MC "Круто! Ты скучаешь по Франции, вообще?"
    Zuri "Иногда... в действительности мне нравится жить здесь."
    $ Zv2_MS2_q6 = False
    jump Zv2_MS2_menu

label Zv2_MS2_pay_label:
    scene Zv2_MS2_p1

    MC "У тебя хорошая заработная плата?"
    scene Zv2_MS2_p3

    Zuri "Хаха! Почему ты думаешь, что я буду говорить о своей зарплате с тобой?"
    if renpy.loadable("patch.rpy"):
        MC "Мне просто интересно, насколько хорошо отец оплачивает свой штат."
    else:
        MC "Мне просто интересно, насколько хорошо Боб оплачивает свой штат."

    Zuri "Позвольте открыть тебе секрет - ни одному работнику в этой компании не платят плохо. Потому так мало людей отсюда уезжают на другую работу."
    $ Zv2_MS2_q7 = False
    jump Zv2_MS2_menu
label Zv2_MS2_zuriproposition_label:
    scene Zv2_MS2_p1

    Zuri "Я так понимаю, ты рассмотрел мое предложение."

    scene Zv2_MS2_p2

    Zuri "Я с нетерпением жду твоего ответа. Что это будет такое? "
    window hide
    menu:
        "{color=#00ff00}Да, я помогу вам получить название компании.{/color}":
            scene Zv2_MS2_p3

            MC "Да, я помогу тебе получить название компании."
            Zuri "Блестяще! Огромное спасибо!"
            Zuri "Я обещаю, что ты будешь щедро вознагражден за свою помощь."
            if renpy.loadable("patch.rpy"):
                Zuri "Твой отец всегда выходит из офиса после обеда. Зайди внутрь и найди название компании."
            else:
                Zuri "Боб всегда выходит из офиса после обеда. Зайди внутрь, и там ты найдешь название компании."
            MC "Почему ты не можешь просто обыскать его офис?"
            Zuri "Он установил там несколько камер, так что это слишком рискованно для меня, но он никогда не заподозрит тебя! Или даже то что ты будете обыскивать его офис, когда он будет следить за твоим доступом."
            $ Zv2_MS2_q9 = False
            $ Zv2_MS2_q10 = True
            $ Zv2_MS2_companyname = 1

            jump Zv2_MS2_menu
        "Нет, я не собираюсь помогать с этим.":

            scene Zv2_MS2_p4

            MC "Я думал о предложении... и я бы предпочел не ввязываться."
            Zuri "Мне очень жаль это слышать. Если передумаешь, пожалуйста, вернитесь и поговорите со мной."
            Zuri "Я могла бы сделать что-то дейсвительно стоящее твоего времени."
            jump Zv2_MS2_menu


label Zv2_MS2_companyname1_label:
    if Zv2_MS2_companyname == 1:
        scene Zv2_MS2_p2

        Zuri "Оно у тебя есть? Есть название компании?"
        window hide
        menu:
            "Нет, пока нет.":

                MC "Нет, у меня его еще нет."
                Zuri "Пожалуйста, поторопись получить его!"
                jump Zv2_MS2_menu

            "{color=#00ff00}Да.{/color}" if Zv2_MS2_companyname_found == 1:
                MC "Yes, I have it."

                scene Zv2_MS2_p5

                Zuri "Отлично! Я знала, что могу доверять тебе! Как называется?"
                window hide
                menu:
                    "{color=#00ff00}Говорить правду.{/color}":
                        MC "Компания называется Charterhouse Investments."
                        Zuri "Потрясающе! Пожалуйста, приходи ко мне домой сегодня вечером, и я позабочусь, чтобы ты получил награду."
                        $ Zv2_MS2_companyname = 2
                        $ Zv2_ES2 = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_true_counter += 1
                        jump Zv2_MS2_menu
                    "{color=#f00}Солгать.{/color}":

                        MC "Компания называется Beerhouse Investments."
                        Zuri "Удивительно! Сегодня вечером я снова жду тебя дома, для вознаграждения."
                        $ Zv2_MS2_companyname = 2
                        $ Zv2_ES2 = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_lie_counter += 1
                        jump Zv2_MS2_menu
    if Zv2_MS2_companyname == 2:
        scene Zv2_MS2_p2

        Zuri "Привет, [player_name]! "
        Zuri "Ну? Удалось получить второе название компании?"
        window hide
        menu:
            "Нет, пока нет.":
                MC "Нет, у меня его еще нет."
                Zuri "Ты очень помог с первым именем. Пожалуйста, получи его как можно скорее для меня."
                jump Zv2_MS2_menu

            "{color=#00ff00}Да.{/color}" if Zv2_MS2_companyname_found == 2:
                MC "Да, оно у меня есть. Это было написано на записке в сейфе."

                scene Zv2_MS2_p5

                Zuri "Отлично! Ты доказываешь, что ты блестящий актив! Как называется вторая компания?"
                window hide
                menu:
                    "{color=#00ff00}Говорить правду.{/color}":
                        MC "Вторая компания торгует под названием Jakarta Legal Procurements."
                        Zuri "Блестяще! Как прежде, приезжай ко мне, и я удостоверюсь, что ты получил ознаграждение."
                        $ Zv2_MS2_companyname = 3
                        $ Zv2_ES3 = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_true_counter += 1
                        jump Zv2_MS2_menu
                    "{color=#f00}Солгать.{/color}":

                        MC "Название компании… Indian Railway and Infrastructure Investments."
                        Zuri "Блестяще! Как прежде, приезжай ко мне, и я удостоверюсь, что ты получил ознаграждение."
                        $ Zv2_MS2_companyname = 3
                        $ Zv2_ES3 = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_lie_counter += 1
                        jump Zv2_MS2_menu

    if Zv2_MS2_companyname == 3:

        scene Zv2_MS2_p9

        Zuri "[player_name]! Готов?"
        MC "А? Что ты имеешь в виду?"
        Zuri "Работа! Мы еще не закончили.. Я уверена, что ты хочешь... больше?"
        MC "*Глоток* Каков план?"

        scene Zv2_MS2_p2

        Zuri "Третье и последнее название компании будет сложнее получить."
        Zuri "Это полная тайна - единственный человек, который знает, это твой отец. И он нигде это не записывает."
        Zuri "Вот почему ты мне нужен. Мне нужно, чтобы ты поговорил с ним и попросил дать тебе имя. Понимаешь?"
        MC "Я понял. Посмотрим, что я смогу сделать."

        $ Zv2_MS2_companyname = 4
        jump Zv2_MS2_menu

    if Zv2_MS2_companyname == 4:
        scene Zv2_MS2_p5
        if renpy.loadable("patch.rpy"):
            Zuri "Ну? Ты получил последнее имя от своего отца?"
        else:
            Zuri "Ну? Ты получил последнее имя от Боба?"
        window hide
        menu:
            "Нет, пока нет.":
                MC "Нет, у меня его еще нет. Это оказалось сложнее, чем я думал."
                Zuri "Пожалуйста, продолжай. Очень важно, чтобы мы получили это имя."
                jump Zv2_MS2_menu

            "{color=#00ff00}Да.{/color}" if Zv2_MS2_companyname_found == 3:
                MC "Да, у меня есть."

                scene Zv2_MS2_p5

                Zuri "Прекрасно! Я знала, что могу доверять тебе! Какое?"
                window hide
                menu:
                    "{color=#00ff00}Говорить правду.{/color}":
                        MC "Заключительная компания - Nottingham Legal and Commercial Incorporated."
                        Zuri "Ты просто потрясающий! Боже! Я могу поцеловать тебя прямо сейчас! Пожалуйста, приходи ко мне домой сегодня вечером, и я тебя отблагодарю."
                        $ Zv2_MS2_companyname = False
                        $ Zv2_ES3a = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_true_counter += 1
                        jump Zv2_MS2_menu
                    "{color=#f00}Соврать.{/color}":


                        MC "Название компании… Manchester Aviation and Aeronautics Engineering."
                        Zuri "Ты просто потрясающий! Боже! Я могу поцеловать тебя прямо сейчас! Пожалуйста, приходи ко мне домой сегодня вечером, и я тебя отблагодарю."
                        $ Zv2_MS2_companyname = False
                        $ Zv2_ES3a = True
                        $ zuri_inhome = True
                        $ Zv2_MS2_q10 = False
                        $ Zv2_lie_counter += 1
                        jump Zv2_MS2_menu



label Zv2_MS2_cancel_label:
    if Zv2_MS2_q8 == True:
        scene Zv2_MS2_p1

        Zuri "Подождите - прежде чем ты уйдешь, [player_name]."
        Zuri "Хотели бы ты приехать в мой дом сегодня вечером?"
        MC "А? Зачем?"
        Zuri "О, да ладно. Симпатичная девушка просит тебя приехать к ней. Как можно сказать нет?"

        scene Zv2_MS2_p6

        Zuri "Просто дай мне .. Хм .. Ах!"

        scene Zv2_MS2_p7

        Zuri "Это мой адрес."
        MC "Это ...свидание?"

        scene Zv2_MS2_p9

        Zuri "Ха-ха! Просто приходи и узнай сам."
        $ Zv2_MS2_q8= False
        $ Z_home_unlocked = True
        $ Zv2_ES1 = True
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump bob_reception_morning1
    else:
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump bob_reception_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
