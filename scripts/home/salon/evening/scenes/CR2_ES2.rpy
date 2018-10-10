image CR2_ES2_p1 = "images/home/salon/evening/scenes/CR2_ES2/1.jpg"
image CR2_ES2_p2 = "images/home/salon/evening/scenes/CR2_ES2/2.jpg"
image CR2_ES2_p3 = "images/home/salon/evening/scenes/CR2_ES2/3.jpg"
image CR2_ES2_p4 = "images/home/salon/evening/scenes/CR2_ES2/4.jpg"
image CR2_ES2_p5 = "images/home/salon/evening/scenes/CR2_ES2/5.jpg"
image CR2_ES2_p6 = "images/home/salon/evening/scenes/CR2_ES2/6.jpg"
image CR2_ES2_p7 = "images/home/salon/evening/scenes/CR2_ES2/7.jpg"
image CR2_ES2_p8 = "images/home/salon/evening/scenes/CR2_ES2/8.jpg"
image CR2_ES2_p9 = "images/home/salon/evening/scenes/CR2_ES2/9.jpg"
image CR2_ES2_p10 = "images/home/salon/evening/scenes/CR2_ES2/10.jpg"
image CR2_ES2_p11 = "images/home/salon/evening/scenes/CR2_ES2/11.jpg"
image CR2_ES2_p12 = "images/home/salon/evening/scenes/CR2_ES2/12.jpg"
image CR2_ES2_p13 = "images/home/salon/evening/scenes/CR2_ES2/13.jpg"
image CR2_ES2_p14 = "images/home/salon/evening/scenes/CR2_ES2/14.jpg"


default can1_CR2_MS2 = False
default CR2_ES2_day = 1
default CR2_ES2_q1 = True
default CR2_ES2_q2 = True
default CR2_ES2_q3 = True
default CR2_ES2_q4 = False
default CR2_ES2_q5 = False
default CR2_ES2_q6 = False
default CR2_ES2_q7 = False
default can_CR2_ES2_day2 = False
default can_CR2_ES2_day3 = False
default CR2_ES2_day2_firsttime = True
default CR2_ES2_day3_firsttime = True
default can_CR2_ES2 = True

label CR2_ES2_label:
    if can_CR2_ES2 == False:
        show screen salon_evening_notclickable
        MC "Я не должен беспокоить ее. Она хочет побыть одна."
        jump salon_morning1
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ can_hide_windows = True
        if CR2_ES2_day == 1:
            scene CR2_ES2_p1 with dissolve

            MC "(Кэролайн выглядит очень подавленной. Может, мне стоит пойти и спросить, как у нее дела.)"
            MC "(Я знаю, что я был бы подавлен, если бы я владел бизнесом, который ограбили.)"

            scene CR2_ES2_p2

            MC "(Она даже не заметила, как я подошел. Она должна быть очень глубоко в мыслях.)"
            MC "(Я просто подойду к этому осторожно. Я не хочу расстраивать ее, больше чем есть.)"

            scene CR2_ES2_p3

            MC "Эй, Кэролайн, как ты держишься?"
            Caroline "Привет, [player_name]. У меня все в порядке! Не волнуйся."
            MC "Точно?"

            scene CR2_ES2_p4

            Caroline "Честно. Я в порядке."
            Caroline "Подойди и сядь рядом со мной."
            MC "Хорошо."
            jump CR2_ES2_menu

        if CR2_ES2_day == 2:
            scene CR2_ES2_p1 with dissolve

            MC "(Кэролайн снова на диване с горячим шоколадом.)"
            MC "(Я, наверное, должен проверить ее, чтобы убедиться, что она не чувствует себя слишком подавленной.)"

            scene CR2_ES2_p3

            MC "Эй, это снова я."
            MC "Я подумал, что заскочил узнать, как ты себя чувствуешь."

            scene CR2_ES2_p4

            Caroline "Привет, [player_name]."
            MC "Ты не против, если я присяду рядом с тобой? Или ты бы предпочла провести некоторое время в одиночестве?"
            Caroline "Честно? Я бы предпочла побыть одна. Но не стесняйтесь посидеть со мной несколько минут, если хочешь."
            if CR2_ES2_day2_firsttime == True:
                $ CR2_ES2_q4 = True
                $ CR2_ES2_q5 = True
                $ CR2_ES2_q6 = True
                $ CR2_ES2_day2_firsttime = False
                jump CR2_ES2_menu
        if CR2_ES2_day == 3:
            scene CR2_ES2_p1 with dissolve

            MC "(Она все еще подавлена.)"
            MC "(Похоже, это ограбление серьезно повлияло на нее.)"

            scene CR2_ES2_p3

            MC "Привет, Кэролайн. Как ты себя чувствуешь?"

            scene CR2_ES2_p4

            Caroline "О. Привет, [player_name]."
            MC "Ты была на улице, вообще?"
            Caroline "Нет, мне здесь удобно."
            MC "(Кэролайн должна найти выход из ситуации с ограблением. Она, очевидно, так не волновалась ни разу в своей жизни.)"
            if CR2_ES2_day3_firsttime == True:
                $ CR2_ES2_q7 = True
                $ CR2_ES2_day3_firsttime = False
                jump CR2_ES2_menu
        jump CR2_ES2_menu

label CR2_ES2_menu:
    $ can_hide_windows = True
    scene CR2_ES2_p5
    window hide
    menu:
        "{color=#00ff00}Ты знаешь, где я могу найти Виолетту?{/color}" if CR2_ES2_qViolet == True:

            scene CR2_ES2_p9

            MC "Ты знаешь, где я смогу найти Виолетту?"

            scene CR2_ES2_p14

            Caroline "Хмм… Я знаю, что она обычно тусуется в старом темном переулке, в городе."
            Caroline "Вы должен быть осторожен в этом районе."

            scene CR2_ES2_p5

            Caroline "Кстати, почему ты хочешь ее найти? Ты заинтересован в продолжении отношений с ней?"
            MC "Она... случайно оставила немного косметики. Я просто хотел вернуть ее."

            scene CR2_ES2_p6

            Caroline "О, это очень мило с твоей стороны. Передай ей привет от меня! Я не слышала о ней несколько дней."
            MC "(Кэролайн ничего не слышала от Виолетте? . Виолетта, вероятно, чувствует себя слишком виноватой, после ограбления ее друга.)"
            MC "Сделаем, Кэролайн."
            $ CR2_ES2_qViolet = False
            $ dark_alley_unlocked = True
            $ violetV2_scene = True
            $ can1_CR2_MS2 = True
            jump CR2_ES2_menu


        "Я не знал, что тебе нравится кофе." if CR2_ES2_q1 == True:
            scene CR2_ES2_p5

            MC "Я не знал, что тебе нравится кофе, Кэролайн."
            if renpy.loadable("patch.rpy"):
                MC "Каждый раз, когда мы гуляли всей семьей, ты всегда заказывала что-то холодное, например, ананасовый сок."
            else:
                MC "Каждый раз, когда мы встречались, ты всегда заказывала что-то вроде ананасового сока."

            scene CR2_ES2_p6

            Caroline "Потому что это не кофе. Но у тебя очень хорошая память!"
            Caroline "Я приготовила себе горячего шоколада. Хочешь?"
            MC "Конечно, я сделаю глоток."

            scene CR2_ES2_p7

            Caroline "Я немного разочарована, что в доме не было зефира."
            Caroline "Мне нравится, как он тает во рту."
            MC "Да, я знаю, о чем ты."

            scene CR2_ES2_p8

            MC "Глоток!"
            Caroline "Я действительно должна купить крем."
            Caroline "Это было бы идеально…"

            scene CR2_ES2_p9

            MC "На вкус здорово! Спасибо, Кэролайн."
            Caroline "Всегда пожалуйста, [player_name]."
            $ CR2_ES2_q1 = False
            $ can_CR2_ES2_day2 = True
            jump CR2_ES2_menu

        "Ты уверена, что чувствуешь себя хорошо? Ты выглядела немного грустно." if CR2_ES2_q2 == True:
            scene CR2_ES2_p5

            MC "Ты нормально себя чувствуешь? Ты выглядела немного грустно, когда я вошел в комнату."

            scene CR2_ES2_p9

            Caroline "У меня все отлично! Честно говоря - ничего плохого."
            MC "Ты не говоришь мне правду, Кэролайн."

            scene CR2_ES2_p10

            Caroline "Я не умею лгать?"
            MC "Нет, это не так. Скажи мне, что тебя беспокоит. Дело в ограблении, не так ли?"
            Caroline "(Вздох)"

            scene CR2_ES2_p11

            Caroline "Я долго работала над этим магазином.."
            Caroline "Я иногда работала двенадцать часов в день, чтобы запустить его."
            Caroline "А теперь, какой-то тупой грабитель пришел и все мне испортил!"

            scene CR2_ES2_p10

            MC "Все в порядке, Кэролайн. Я понимаю, что ты чувствуешь. Мы пройдем через это, вместе."
            Caroline "(Сопит) Спасибо, [player_name]."
            $ CR2_ES2_q2 = False
            $ can_CR2_ES2_day2 = True
            jump CR2_ES2_menu

        "У тебя есть планы на сегодня?" if CR2_ES2_q3 == True:
            scene CR2_ES2_p5

            MC "У тебя есть какие-либо планы на сегодня?"

            scene CR2_ES2_p13

            Caroline "... не совсем. Я просто собиралась провести день дома, отдыхая."
            MC "Ты не знаешь как отвлечься?"

            scene CR2_ES2_p10

            Caroline "У меня нет денег, чтобы сделать что-то."
            Caroline "Я даже не могу себе позволить купить зефир и сливки для этого горячего шоколада!"
            MC "Все в порядке, Кэролайн. Мы вернем твою жизнь в нужное русло."

            scene CR2_ES2_p10

            Caroline "Спасибо, [player_name]."
            $ CR2_ES2_q3 = False
            $ can_CR2_ES2_day2 = True
            jump CR2_ES2_menu

        "Есть новости от полиции?" if CR2_ES2_q4 == True:
            scene CR2_ES2_p5

            MC "Есть новости от полиции?"
            Caroline "Глоток"

            scene CR2_ES2_p10

            Caroline "Ничего хорошего."
            MC "Дерьмо."
            Caroline "Они сказали мне, что это не был срочный случай для них."
            Caroline "Сегодня утром я позвонила, и они сказали мне, что слишком много времени пройшло с момента инцидента, чтобы они исследовали."
            Caroline "По-видимому, любые доказательства, которые существовали, могли быть подделаны или потеряны."

            scene CR2_ES2_p11

            Caroline "Они сказали, что будут держать мое дело открытым, но он никуда не денется, пока я не назву подозреваемого."
            Caroline "Я имею в виду - почему я должна делать работу полиции?!"
            MC "Дерьмо, я сожалею, что услышал это."
            $ CR2_ES2_q4 = False
            $ can_CR2_ES2_day3 = True
            jump CR2_ES2_menu
        "Когда ты планируешь возвращаться к работе?" if CR2_ES2_q5 == True:
            scene CR2_ES2_p13

            MC "Когда ты планируешь возвращаться к работе?"
            Caroline "Я, отчасти, в безвыходном положении."
            Caroline "Я не могу снабдить свой магазин без денег - и я не могу получить денег от банка, если я не могу представить свидетельства о доходах."

            scene CR2_ES2_p10

            Caroline "Так что, мягко говоря - мне пиздец."
            MC "Дерьмо. Мне жаль это слышать."
            Caroline "Чтобы встать на ноги мне нужно много времени."
            $ CR2_ES2_q5 = False
            $ can_CR2_ES2_day3 = True
            jump CR2_ES2_menu

        "Ты говорила с мамой или Папой об этом ограблении?" if CR2_ES2_q6 == True and renpy.loadable("patch.rpy"):
            jump CR2_ES2_bobtalk

        "Ты говорила с Линдой или Бобом об этом ограбление?" if CR2_ES2_q6 == True and not renpy.loadable("patch.rpy"):
            jump CR2_ES2_bobtalk


        "Как ты себя чувствуешь?" if CR2_ES2_q7 == True:
            scene CR2_ES2_p12

            MC "Как ты себя чувствуешь, Кэролайн?"
            Caroline "Я... не знаю."
            Caroline "Я не чувствую себя подавленной,как пару дней назад."

            scene CR2_ES2_p14

            Caroline "Я думаю, что это то, что они называют, стадия принятия? Хотя, я никогда не изучал психологию, так что я просто угадала."
            MC "(Я ненавижу видеть Кэролайн в таком состоянии. Несколько дней назад она была рады расширить свой бизнес и открыть новые магазины.)"
            MC "(Теперь она была сокращена до, реветьна всех диванах. Тот, кто ограбил ее заслуживает возмездия!)"

            scene CR2_ES2_p9

            MC "Если ты когда-нибудь захочешь поговорить, ты знаешь, что я всегда готов слушать."
            Caroline "Я знаю. Спасибо, [player_name]."
            $ CR2_ES2_q7 = False
            jump CR2_ES2_menu
        "Пока.":


            jump CR2_ES2_bye


label CR2_ES2_bye:
    if CR2_ES2_day == 1:
        scene CR2_ES2_p10

        Caroline "Я предпочла остаться одиночестве."
        Caroline "Хорошо?"

        scene CR2_ES2_p11

        MC "Конечно, Кэролайн. Если тебе что-то нужно, просто позвоните мне?"
        Caroline "Хорошо. Увидимся, [player_name]."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES2 = False
        $ can_hide_windows = False
        jump salon_morning1

    if CR2_ES2_day == 2:
        scene CR2_ES2_p13

        Caroline "Я предпочла бы побыть одна."
        Caroline "Я поговорю с тобой позже, хорошо?"
        MC "Без проблем, Кэролайн. Увидимся."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES2 = False
        $ can_hide_windows = False
        jump salon_morning1
    if CR2_ES2_day == 3:
        scene CR2_ES2_p11

        Caroline "Можно, я побуду одна?"
        MC "Да, без проблем."
        Caroline "Извини, мне нужно подумать."
        MC "Все в порядке, я понимаю. Увидимся позже, Кэролайн."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_CR2_ES2 = False
        $ can_hide_windows = False
        jump salon_morning1


label CR2_ES2_bobtalk:
    scene CR2_ES2_p12
    if renpy.loadable("patch.rpy"):
        MC "Ты сказала маме или папе о грабеже?"
    else:
        MC "Ты уже сказал Линде или Бобу об ограблении?"
    Caroline "Нет! Абсолютно нет."
    MC "Почему?"

    scene CR2_ES2_p10
    if renpy.loadable("patch.rpy"):
        Caroline "Я должна быть независимой успешной дочерью."
    else:
        Caroline "Я должен быть независимой успешной женщиной."
    if renpy.loadable("patch.rpy"):
        Caroline "Я родилась первой, и они оба надеются на меня."
    MC "Разве они не спрашивают, почему ты, не на работе?"

    scene CR2_ES2_p11
    if renpy.loadable("patch.rpy"):
        Caroline "Мама спросила меня, сегодня утром…"
    else:
        Caroline "Линда спросила меня, сегодня утром…"
    MC "Что ты сказала ей?"
    Caroline "Я сказала, что бизнес идет так хорошо, что я позволила себе взять несколько выходных…"

    scene CR2_ES2_p13

    MC "Дерьмо…"
    Caroline "Да, я не должна была так лгать."
    $ CR2_ES2_q6 = False
    $ can_CR2_ES2_day3 = True
    jump CR2_ES2_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
