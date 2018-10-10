image Bobv2_MS1_p1 = "images/Bob_work/office/M/scenes/Bobv2_MS1/1.jpg"
image Bobv2_MS1_p2 = "images/Bob_work/office/M/scenes/Bobv2_MS1/2.jpg"
image Bobv2_MS1_p3 = "images/Bob_work/office/M/scenes/Bobv2_MS1/3.jpg"
image Bobv2_MS1_p4 = "images/Bob_work/office/M/scenes/Bobv2_MS1/4.jpg"
image Bobv2_MS1_p5 = "images/Bob_work/office/M/scenes/Bobv2_MS1/5.jpg"
image Bobv2_MS1_p6 = "images/Bob_work/office/M/scenes/Bobv2_MS1/6.jpg"
image Bobv2_MS1_p7 = "images/Bob_work/office/M/scenes/Bobv2_MS1/7.jpg"
image Bobv2_MS1_p8 = "images/Bob_work/office/M/scenes/Bobv2_MS1/8.jpg"
image Bobv2_MS1_p9 = "images/Bob_work/office/M/scenes/Bobv2_MS1/9.jpg"
image Bobv2_MS1_p10 = "images/Bob_work/office/M/scenes/Bobv2_MS1/10.jpg"

default Bobv2_MS1_q1 = True
default Bobv2_MS1_first_talk = True
default Bobv2_MS1_q2 = True
default Bobv2_MS1_q3 = False
default Bobv2_MS1_q4 = False
default Bobv2_MS1_q5 = False
default Bob_work_minigame = False
default Zv2_MS2 = False
default can_Zv2_MS2_q = False
default can2_Zv2_MS2_q = True
default bob_give_money_first_time = True
label Bobv2_MS1_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Feelin Good.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene Bobv2_MS1_p1 with dissolve
    if Bobv2_MS1_first_talk == True:
        if renpy.loadable("patch.rpy"):
            MC "Доброе утро, папа!"
        else:
            MC "Доброе утро, Боб!"
        Dad "Привет, чемпион. Что привело тебя в мой офис?"
        MC "Ничего. Просто подумал заскочить поздороваться."

        scene Bobv2_MS1_p2
        if renpy.loadable("patch.rpy"):
            Dad "Ну, я никогда не откажусь от визита моего любимого сына!"
            MC "Я твой единственный сын."
        else:
            Dad "Ну, я никогда не откажусь от визита моего любимого соседа по комнате!"
            MC "Я твой единственный сосед по комнате."
        Dad "И таким образом, мой любимый."
        $ Bobv2_MS1_first_talk = False

        jump Bobv2_MS1_menu
    else:
        if renpy.loadable("patch.rpy"):
            MC "Доброе утро, папа!"
        else:
            MC "Доброе утро, Боб!"

        Dad "Привет, [player_name]"
        MC "Что случилось?"
        Dad "О, Господи! Ничего важного. Такой же день, как всегда."

        jump Bobv2_MS1_menu


label Bobv2_MS1_menu:
    scene Bobv2_MS1_p2
    window hide
    menu:
        "{color=#00ff00}Я уладил документы. Не мог бы ты заплатить мне?{/color}" if money_from_bob > 0:
            $ bob_payment_money = 0
            if bob_give_money_first_time == True:
                scene Bobv2_MS1_p1
                MC "Я уладил документы. Не мог бы ты заплатить мне?"
                scene Bobv2_MS1_p2
                Dad "Ах! Хорошая работа, [player_name]! Вот, возьми."
                MC "Благодарю!"
                Dad "Нет, я благодарю тебя! Ненавижу это делать!"
                scene Bobv2_MS1_p7
                Dad "После стольких раз это стало невероятно скучно."
                MC "Хаха!"
                Dad "Я буду более чем счастлив, если ты начнешь делать это регулярно."
                if renpy.loadable("patch.rpy"):
                    MC "Без проблем, папа."
                else:
                    MC "Без проблем, Боб."
                $ bob_give_money_first_time = False
                jump bob_work_money_give

            if bob_give_money_first_time == False:
                scene Bobv2_MS1_p1
                MC "Я вчера отсортировал документы. Не мог бы ты заплатить мне?"
                scene Bobv2_MS1_p7
                Dad "Снова!?"
                Dad "Блестяще! Вот, возьми."
                Dad "(Теперь у меня будет больше времени, чтобы читать книги!)"
                if renpy.loadable("patch.rpy"):
                    MC "Спасибо, Папа."
                else:
                    MC "Спасибо, Боб."
                jump bob_work_money_give



        "{color=#00ff00}У тебя есть для меня работа?{/color}" if Bobv2_MS1_q1 == True:
            scene Bobv2_MS1_p2

            MC "Мне было интересно, есть ли у тебя работа, с которой я мог бы помочь."

            scene Bobv2_MS1_p3

            Dad "Ты хочешь, чтобы тебе заплатили, я полагаю?"
            MC "Да, я вроде как надеялся."
            Dad "Если подумать, мне обычно нужны документы, отсортированные во второй половине дня. Я всегда в доме в это время, так что ты можешь работать здесь, если хочешь."

            scene Bobv2_MS1_p10

            Dad "Документы для сортировки всегда будут лежать на моем столе после того, как я уйду."
            MC "Насколько это будет сложно?"

            scene Bobv2_MS1_p7

            Dad "Сложно? Хаха! Совсем нет! Просто сопоставьте документы с соответствующим номером."
            MC "Как насчет компенсации?"
            Dad "Всякий раз, когда ты заканчиваешь работу, приходи ко мне."
            Dad "Помни, что я здесь только утром!"
            MC "Я должен ждать еще один день для оплаты?"
            Dad "Хаха! Нетерпение-очень плохая привычка, [player_name]."
            Dad "Ты также можешь найти меня дома во второй половине дня. Я быть в своей спальне курить вкусные сигары."
            MC "Гмм!"
            Dad "Не суди!"
            Dad "Я курю только рекреационно, а не с пристрастием."
            MC "Да... (Каждый зависимый человек, вероятно, говорит так...)"
            $ Bob_work_minigame = True
            $ Bobv2_MS1_q1 = False
            jump Bobv2_MS1_menu

        "{color=#00ff00}Не мог бы ты дать мне ключ-карту от офиса?{/color}" if Bobv2_MS1_q2 == True:
            scene Bobv2_MS1_p2

            MC "Могу ли я получить ключ-карту от офиса?"

            scene Bobv2_MS1_p3

            Dad "Да... это будет проблемой. У меня есть только один - и он мне нужен каждый день."
            MC "О. Ничего."

            scene Bobv2_MS1_p8

            Dad "Нет, подожди здесь одну минуту. У меня есть идея."
            Dad "Иди к Зури и попроси ее ключ-карту. Она имеет те же уровни доступа, что и я."
            MC "Благодарю. Но что насчет нее?"

            scene Bobv2_MS1_p7

            Dad "Я просто закажу ей новую."
            if renpy.loadable("patch.rpy"):
                MC "Круто. Спасибо папа! Я пойду и поговорю с Зури."
            else:
                MC "Круто. Спасибо, Боб! Я пойду и поговорю с Зури."
            $ bob_office_locked = False
            $ Bobv2_MS1_q2 = False
            $ Zv2_MS2 = True
            $ can_Zv2_MS2_q = True
            jump Bobv2_MS1_menu
        "{color=#00ff00}Спросить о названии компании.{/color}" if Zv2_MS2_companyname == 4 and Zv2_MS2_companyname_found == 2:
            scene Bobv2_MS1_p1
            if renpy.loadable("patch.rpy"):
                MC "Эй, папа, я знаю, что ты супер инвестор. Можешь дать мне совет?"
            else:
                MC "Эй, Боб, я знаю, что ты супер инвестор. Можешь дать мне совет?"
            Dad "Конечно, что ты хочешь знать, чемпион?"
            MC "Я знаю, что у всех крупных инвесторов есть компании, которые, как они знают, будут очень хорошо работать на рынке. Вроде как, коммерческая тайна."
            scene Bobv2_MS1_p2
            Dad "Ха-ха! Да, это правда."
            MC "Ну? Есть ли у тебя?"
            Dad "Конечно."
            MC "Круто! Как она называется?"
            scene Bobv2_MS1_p4

            Dad "Извини - коммерческая тайна. Я не могу сказать, пока мы не закроем сделку."
            if renpy.loadable("patch.rpy"):
                MC "Да ладно, папа! Я никому не расскажу. Я просто хочу узнать больше о бизнесе!"
            else:
                MC "О, давай, Боб! Я никому не расскажу. Я просто хочу узнать больше о бизнесе!"
            MC "Честно говоря, я думаю о том, чтобы участвовать в этом, когда вырасту!"
            scene Bobv2_MS1_p2
            Dad "Действительно?"
            MC "Да!"
            Dad "Хмм... В таком случае... я полагаю."
            Dad "Хорошо! У меня есть совет от члена Совета Европы. "
            Dad "Он сказал мне, что Nottingham Legal and Commercial Incorporated получает крупный контракт на железнодорожную сеть из Португалии в Германию. Мы говорим о многомиллиардном контракте!"
            MC "Вау!"
            MC "(Вот что мне нужно знать!)"
            if renpy.loadable("patch.rpy"):
                MC "Я поговорю с тобой об этом позже, папа."
            else:
                MC "Я поговорю с тобой об этом позже, Боб."
            Dad "Нет проблем! Увидимся!"
            $ Zv2_MS2_companyname_found = 3

            jump Bobv2_MS1_menu


        "Спросить папу, знает ли он о сестре-близнеце Зури. " if Bobv2_MS1_q4 == True and renpy.loadable("patch.rpy"):
            jump Bobv2_MS1_zurisuri_label
        "Спросить Боба, знает ли он о сестре-близнеце Зури. " if Bobv2_MS1_q4 == True and not renpy.loadable("patch.rpy"):
            jump Bobv2_MS1_zurisuri_label


        "{color=#00ff00}Спросить папу, как продвигается работа.{/color}" if Bobv2_MS1_q5 == True and renpy.loadable("patch.rpy"):
            jump Bobv2_MS1_work_label
        "{color=#00ff00}Спросить Боба, как идет работа.{/color}" if Bobv2_MS1_q5 == True and not renpy.loadable("patch.rpy"):
            jump Bobv2_MS1_work_label
        "Отмена":

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump bob_office_M1



label Bobv2_MS1_zurisuri_label:
    scene Bobv2_MS1_p1
    if renpy.loadable("patch.rpy"):
        MC "Привет, пап. Знаешь ли ты, что у Зури есть сестра-близнец?"
    else:
        MC "Привет, Боб. Знаешь ли ты, что у Зури есть сожитель?"
    scene Bobv2_MS1_p7

    Dad "В самом деле?"
    MC "Да, девушка по имени Сури."
    Dad "Странно. Я никогда не слышал, чтобы она говорила о ней."

    scene Bobv2_MS1_p5
    if renpy.loadable("patch.rpy"):
        Dad "Как ты узнал, что у нее есть сестра-близнец?"
    else:
        Dad "Как ты узнал, что у нее есть сожитель?"
    MC "Я ... э-э ... Она упомянула это мне в вестибюле."

    scene Bobv2_MS1_p3

    Dad "Да ... Хорошо. Хорошо для нее."
    $ Bobv2_MS1_q4 = False
    jump Bobv2_MS1_menu

label Bobv2_MS1_work_label:
    scene Bobv2_MS1_p2
    if renpy.loadable("patch.rpy"):
        MC "Как идет работа, папа?"
    else:
        MC "Как идет работа, Боб?"
    if Zv2_true_counter > 1:
        scene Bobv2_MS1_p9
        Dad "О, боже. Жаль, что ты спросил. Вся компания облажалась."
        MC "(Ой-ой…)"
        Dad "Прибыль - это погружение с носом в красный цвет, и штаб-квартира корпорации находится на моей заднице, требуя знать, почему."
        Dad "Я собираюсь работать вдое больше, чтобы удержать это корабль на плаву."
        if renpy.loadable("patch.rpy"):
            MC "Дерьмо! Мне жаль это слышать, папа."
        else:
            MC "Дерьмо! Мне жаль это слышать, Боб."

    if Zv2_lie_counter > 1:

        Dad "Я рад, что ты спросил! Вещи действительно возвращаются!"
        Dad "Знаешь - рынок никогда не восстановиться после аварии 2009 года. Но посмотри - вот мы здесь. И судя по всему, мы собираемся опубликовать рекордную прибыль!"
        if renpy.loadable("patch.rpy"):
            MC "Поздравляю, Папа!"
        else:
            MC "Поздравляю, Боб!"
        Dad "Если все пойдет по плану, я должен, наконец, снова получить свой годовой бонус!"

    $ Bobv2_MS1_q5 = False
    $ Bob_v3_scenes = True
    show workinprogress2

    "Это конец текущего содержимого этой версии для этого персонажа."

    hide workinprogress2
    jump Bobv2_MS1_menu

label bob_work_money_give:
    if money_from_bob > 0:
        $ inventory.earn(25)
        $ bob_payment_money += 25
        $ money_from_bob -=1
        jump bob_work_money_give
    else:
        "Ты получишь {color=#00ff00}[bob_payment_money]${/color}."
        jump Bobv2_MS1_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
