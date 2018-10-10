image CR2_AS3_p1 = "images/cloth_shop/room1/day/scenes/CR2_AS3/1.jpg"
image CR2_AS3_p2 = "images/cloth_shop/room1/day/scenes/CR2_AS3/2.jpg"
image CR2_AS3_p3 = "images/cloth_shop/room1/day/scenes/CR2_AS3/3.jpg"
image CR2_AS3_p4 = "images/cloth_shop/room1/day/scenes/CR2_AS3/4.jpg"
image CR2_AS3_p5 = "images/cloth_shop/room1/day/scenes/CR2_AS3/5.jpg"
image CR2_AS3_p6 = "images/cloth_shop/room1/day/scenes/CR2_AS3/6.jpg"
image CR2_AS3_p7 = "images/cloth_shop/room1/day/scenes/CR2_AS3/7.jpg"

image CR2_AS3a_p1 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/1.jpg"
image CR2_AS3a_p2 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/2.jpg"
image CR2_AS3a_p3 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/3.jpg"
image CR2_AS3a_p4 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/4.jpg"
image CR2_AS3a_p5 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/5.jpg"
image CR2_AS3a_p6 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/6.jpg"
image CR2_AS3a_p7 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/7.jpg"
image CR2_AS3a_p8 = "images/cloth_shop/room1/day/scenes/CR2_AS3/AfterClening/8.jpg"

default CR2_AS3_clean1 = False
default CR2_AS3_clean2 = False
default CR2_AS3_clean3 = False
default CR2_AS3_clean4 = False
default CR2_AS3_clean5 = False
default CR2_AS3_clean6 = False
default CR2_AS3_clean7 = False
default CR2_AS3_clean_after = False

label CR2_AS3_clean_counter_label:
    $ CR2_AS3_clean_counter += 1
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen cloth_shop_robber_screen

label CR2_AS3_clean_counter_label2:
    $ CR2_AS3_clean_counter += 1
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen cloth_shop_room2_robbery_screen

label CR2_AS3_label:

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_AS3_p1 with dissolve
    $ can_hide_windows = True
    Caroline "*Всхлыпивает*"
    MC "(Что?! Она плачет?)"
    MC "Кэролайн? Ты в порядке?"


    scene CR2_AS3_p2

    MC "(Иисус Христос! Она плачет!)"
    MC "(Что, черт возьми, случилось!?)"
    MC "Эй, я здесь, Кэролайн. Что не так?"

    scene CR2_AS3_p3

    Caroline "Это ... * Всхлыпивает * Все прошло…"
    MC "Что все пропало?"
    Caroline "Мои деньги ... Некоторые из моих акций…"
    MC "Подожди, ты не договариваешь"
    Caroline "Меня ограбили!"

    scene CR2_AS3_p4

    MC "Дерьмо! Все в порядке ... Иди сюда, Кэролайн."
    MC "(Она дрожит, как лист на ветру!)"
    MC "(Я должен что-то сделать, чтобы попытаться успокоить ее.)"

    scene CR2_AS3_p5

    MC "Всё будет хорошо, Кэролайн. Просто сядь и соберись."
    MC "Позволь мне осмотреть магазин, и я посмотрю, что я могу спасти, хорошо?"
    Caroline "Т-Ты не должен делать это..."
    MC "Чушь. Просто устройся поудобнее и расслабься. Позволь мне сделать уборку."

    scene CR2_AS3_p6

    Caroline "Уверен?"
    MC "Честно говоря, просто оставь это мне. Я буду складывать вещи и ставить мебель назад, на свое правильное место."
    Caroline "Спасибо, [player_name]. Ты такой милый."

    scene CR2_AS3_p7

    MC "Ты знаешь, кто мог это сделать?"
    Caroline "Я ... э-э ... я не уверен."
    MC "Скажу тебе, оставь уборку для меня. Ты сообщи о грабеже полицию, хорошо?"
    Caroline "Х-хорошо."
    $ can_map = False
    $ CR2_AS3_clean = True
    $ CR2_AS3 = False
    $ CR2_AS3a = True
    $ can_hide_windows = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music2", loop=True, fadein = 2)
    scene cloth_shop_empty
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen cloth_shop_robber_screen

label CR2_AS3a_label:
    if CR2_AS3_clean_counter <7:
        $ clickable = False
        show screen cloth_shop_robber_screen
        MC "Сначала я должен убрать бардак."
        $ clickable = True
        show screen week_day_viewer
        show screen time_skip_button
        show screen day_time_viewer
        show screen map_button
        show screen new_message_incoming1
        call screen cloth_shop_robber_screen
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
        scene CR2_AS3a_p1 with dissolve
        $ can_hide_windows = True

        MC "Хорошо! Я сделал уборку. Магазин почти вернулся к нормальному виду!"
        Caroline "Огромное спасибо, [player_name]. Ты действительно меня поддержал."
        MC "Я рад помочь. Мы пройдем через это."

        scene CR2_AS3a_p2

        MC "У тебя была возможность позвонить в полицию?"
        Caroline "Да, я сообщила о преступлении. Сейчас у полиции нет никого, кто мог бы приехать срочно, но они говорят, что они будут на связи."
        MC "Не срочно?"

        scene CR2_AS3a_p3

        Caroline "Недостаточно денег было украдено, и никто не был физически ранен. Таким образом, это не срочный случай для них."
        MC "Мдаа."
        Caroline "У меня все еще нет денег, и я не знаю, с чего мне начать ..."

        scene CR2_AS3a_p4


        MC "Все в порядке, Кэролайн. Я буду с тобой, на каждом шагу."
        Caroline "Тебе не нужно это делать. Я знаю, что это мужская работа, но я ... Я даже не плачу тебе."
        if renpy.loadable("patch.rpy"):
            MC "Ты моя сестра. Я уже говорил об этом раньше. Независимо от того, что произойдет, я буду помогать там,где это нужно."
        else:
            MC "Что бы ни случилось, я буду помогать тебе."

        scene CR2_AS3a_p5
        if renpy.loadable("patch.rpy"):
            Caroline "*Всхлыпивает* Огромное спасибо! Ты лучший брат, которого я когда-либо просила о чем-то."
        else:
            Caroline "*Всхлыпивает* Огромное спасибо! Ты лучший человек, которого я когда-либо просила о чем-то."
        MC "(Похоже, я подбодрил ее немного!)"
        MC "(Я не должен отдыхать, хотя-я найду этого грабителя и отомщу ему!)"

        scene CR2_AS3a_p6

        MC "(Я не думаю, что Кэролайн подумала об этом, когда решила обнять меня.)"
        MC "(Ну что ж! Я не собираюсь жаловаться! Вид потрясающий!)"

        scene CR2_AS3a_p7

        Caroline "Еще раз спасибо, [player_name]."
        Caroline "Я не знаю, что бы я делала без тебя, в этой жизни."
        Caroline "Ты мой самый большой, мой единственный источник поддержки."

        scene CR2_AS3a_p8

        MC "Мы пройдем через это вместе, Кэролайн."
        MC "Нам просто нужно взять и сделать все зп один раз. Мы сосредоточимся на том, чтобы привести твой магазина порядок и запустить его."
        MC "Я сосредоточусь на преступной стороне вещей. Хорошо?"
        Caroline "Хорошо, но будь осторожным."

        $ day_time = 3
        $ CR2_AS3a = False
        $ CR2_AS4 = True
        $ CR2_AS5 = True
        $ CR2_MS2 = True
        $ CR2_ES2 = True
        $ cloth_shop_minigame_unlocked = False
        $ CR2_MS1 = False
        $ CR2_ES1 = False
        $ sms2_fromC = True
        $ CR2_AS3_clean_after = True
        $ can_hide_windows = False
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
