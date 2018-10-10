image SR2_swimming_card_p1 = "images/home/mc_room/morning/scenes/SR2_swimming_card/1.jpg"
image SR2_swimming_card_p2 = "images/home/mc_room/morning/scenes/SR2_swimming_card/2.jpg"
image SR2_swimming_card_p3 = "images/home/mc_room/morning/scenes/SR2_swimming_card/3.jpg"
image SR2_swimming_card_p4 = "images/home/mc_room/morning/scenes/SR2_swimming_card/4.jpg"
image SR2_swimming_card_p5 = "images/home/mc_room/morning/scenes/SR2_swimming_card/5.jpg"
image SR2_swimming_card_p6 = "images/home/mc_room/morning/scenes/SR2_swimming_card/6.jpg"
image SR2_swimming_card_p7 = "images/home/mc_room/morning/scenes/SR2_swimming_card/7.jpg"
image SR2_swimming_card_p8 = "images/home/mc_room/morning/scenes/SR2_swimming_card/8.jpg"

label SR2_swimming_card_label:
    hide screen mc_room_day_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_morning_notclickable
    hide screen mc_room_night_notclickable
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
    $ renpy.hide("mc_sleep_night_bed", layer="screens")
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    $ renpy.pause(3, hard= True)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)

    MC "(Храп…)"
    $ Sara_name = "???"
    Sara "[player_name]? Ты спишь?"
    $ Sara_name = "Сара"
    MC "(Zzzzzz…)"

    scene SR2_swimming_card_p1 with dissolve

    Sara "[player_name]?"
    MC "(Зевок!)"
    MC "ХММ?"

    scene SR2_swimming_card_p2

    Sara "Ура! Наконец!"
    MC "Да? Сколько времени? Ты никогда не будешь передо мной. Я, должно быть спал."
    Sara "Эй! Много раз я поднимался раньше тебя.!"
    MC "О, правда? Назови мне два раза, когда проснулся раньше меня."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Why_Did_You_Do_It_-_Everet_Almond.mp3', channel="music1", loop=True, fadein = 2)
    scene SR2_swimming_card_p1

    Sara "ЭЭЭ... было то время, когда мы были в отпуске в Испании!"
    MC "Это потому, что таракан заполз в твою постель и разбудил в пять утра!"
    Sara "Я все еще проснулся раньше, так что это все равно считается! И ... ух ... сегодня номер два! Я выигрываю!"
    if renpy.loadable("patch.rpy"):
        MC "(Вздох) Что ты хочешь от меня? Мама говорила тебе вытащить меня из постели?"
    if not renpy.loadable("patch.rpy"):
        MC "(Вздох) Что ты хочешь от меня? Линда сказала тебе вытащить меня из постели?"
    scene SR2_swimming_card_p2

    Sara "Нет, глупый! Я тебе кое-что достала!"
    MC "Ох круто! Что это такое?"

    scene SR2_swimming_card_p3

    Sara "Та-да! Открой!"
    MC "Что это такое?"
    Sara "Просто откройте его!"

    scene SR2_swimming_card_p4

    MC "(Хм, это не кажется слишком тяжелым. Интересно, что это может быть.)"

    MC "(Я попробую встряхнуть его.)"

    "(RATTLE RATTLE)"

    Sara "…"
    Sara "Серьезно? Сколько тебе лет?"
    MC "Давай! Это совершенно естественно хотеть потрясти подарок!"
    Sara "Как скажешь..."

    scene SR2_swimming_card_p5

    Sara "А теперь поторопись и открой. Я не могу ждать все утро!"
    MC "Хорошо, я открою его. Надеюсь здесь не твои трусики!"
    Sara "(О ... звучит непристойно.…)"

    scene SR2_swimming_card_p6

    MC "О! VIP-карты бассейна! Потрясающе!"
    Sara "Да. Они позволяют тебе..."
    MC "Неограниченный доступ?"
    Sara "Правильно.!"
    MC "Это должно было стоить тебе целое состояние, Сара! Откуда у тебя такие деньги?!"

    scene SR2_swimming_card_p4
    if renpy.loadable("patch.rpy"):
        Sara "Я копила то, что мне давал отец."
    else:
        Sara "Я копила то, что мне давал Боб."

    Sara "Я не знала, чего я на самом деле хотела, пока мы не начали ... встречаться."
    Sara "[player_name], Я хочу ходить с тобой в бассейн по выходным, если ты свободен."
    Sara "Вот почему у меня два, чтобы мы могли провести время вместе."

    scene SR2_swimming_card_p7

    MC "О, спасибо тебе огромное, Сара. Это так мило."
    MC "Держи это. Когда-нибудь, когда мы оба свободны, мы можем собраться в бассейн вместе."
    Sara "Действительно?!"
    MC "Конечно!"

    scene SR2_swimming_card_p8

    Sara "Спасибо, [player_name]! Ты самый лучший!"
    Sara "Я собираюсь спуститься вниз и позавтракать. Увидимся, [player_name]."
    MC "Еще раз спасибо, Сара! Увидимся!"
    $ inventory.add(swimming_poll_card)
    $ SR2_weekend_swimming_pool = True
    $ SR2_swimming_card = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
