image caroline_mc_room_morning_scene5_p1 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/1.jpg"
image caroline_mc_room_morning_scene5_p2 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/2.jpg"
image caroline_mc_room_morning_scene5_p3 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/3.jpg"
image caroline_mc_room_morning_scene5_p4 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/4.jpg"
image caroline_mc_room_morning_scene5_p5 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/5.jpg"
image caroline_mc_room_morning_scene5_p6 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/6.jpg"
image caroline_mc_room_morning_scene5_p7 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/7.jpg"
image caroline_mc_room_morning_scene5_p8 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/8.jpg"
image caroline_mc_room_morning_scene5_p9 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/9.jpg"

image caroline_mc_room_morning_scene5_hand_footp1 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/1.jpg"
image caroline_mc_room_morning_scene5_hand_footp2 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/2.jpg"
image caroline_mc_room_morning_scene5_hand_footp3 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/3.jpg"
image caroline_mc_room_morning_scene5_hand_footp4 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/4.jpg"
image caroline_mc_room_morning_scene5_hand_footp5 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/5.jpg"
image caroline_mc_room_morning_scene5_hand_footp6 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/6.jpg"
image caroline_mc_room_morning_scene5_hand_footp7 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/7.jpg"
image caroline_mc_room_morning_scene5_hand_footp8 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/8.jpg"
image caroline_mc_room_morning_scene5_hand_footp9 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/9.jpg"
image caroline_mc_room_morning_scene5_hand_footp9a = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/9a.jpg"
image caroline_mc_room_morning_scene5_hand_footp11 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/11.jpg"
image caroline_mc_room_morning_scene5_hand_footp12 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/12.jpg"
image caroline_mc_room_morning_scene5_hand_footp13 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/13.jpg"
image caroline_mc_room_morning_scene5_hand_footp14 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/14.jpg"
image caroline_mc_room_morning_scene5_hand_footp15 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/15.jpg"
image caroline_mc_room_morning_scene5_hand_footp16 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/16.jpg"
image caroline_mc_room_morning_scene5_hand_footp16a = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/16a.jpg"
image caroline_mc_room_morning_scene5_hand_footp17 = "images/home/mc_room/morning/scenes/caroline_mc_room_morning_scene5/HandFootJob/17.jpg"
image caroline_mc_room_morning_scene5_hand_footp11anim = Movie(play="videos/Caroline-MorningS5-Footjob1.webm", loop = True )
image caroline_mc_room_morning_scene5_hand_footp4anim = Movie(play="videos/Caroline-MorningS5-Handjob1.webm", loop = True )
image caroline_mc_room_morning_scene5_hand_footp6anim = Movie(play="videos/Caroline-MorningS5-Handjob2.webm", loop = True )
label caroline_mc_room_morning_scene5_label:
    hide screen mc_room_day_notclickable
    hide screen mc_room_evening_notclickable
    hide screen mc_room_morning_notclickable
    hide screen mc_room_night_notclickable
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ renpy.pause(3, hard= True)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music1", loop=True, fadein = 2)

    scene caroline_mc_room_morning_scene5_p1 with dissolve
    $ can_hide_windows = True
    Caroline "(Ну ... вот оно. Я все продумала, и я знаю свои недостатки.)"
    Caroline "(Я установлю границы с [player_name] и посмотрю, заинтересован ли он.)"
    Caroline "(Боже ... надеюсь, я поступаю правильно..)"

    scene caroline_mc_room_morning_scene5_p2
    Caroline "[player_name]? Ты не спишь?"
    MC "(Храп…)"
    Caroline "(Он крепко спит. Думаю, это даст мне повод-сломать лед, перед сложным разговором!)"

    scene caroline_mc_room_morning_scene5_p3
    Caroline "БУУ!"
    MC "ААААА!"
    MC "Боже! Ты напугал меня до смерти, Кэролайн! Какого черта?!"

    scene caroline_mc_room_morning_scene5_p4
    Caroline "Ой, да ладно. Ты счастлив видеть меня."

    scene caroline_mc_room_morning_scene5_p4
    MC "Да-но не могла бы ты разбудить меня мягко?"
    MC "Знаешь-может быть, обнять или погладить по плечу..."
    Caroline "Пфф! Это не весело!"

    scene caroline_mc_room_morning_scene5_p5
    Caroline "В любом случае, мне нужно сказать тебе кое-что важное. Так что мне нужно, чтобы ты был в полном сознании."
    MC "Ага?"
    Caroline "Я готова помочь тебе с твоей проблемой ...."
    MC "Ты имеешь в виду мою эрекцию?"

    scene caroline_mc_room_morning_scene5_p6
    Caroline "Да... это. Тем не менее, есть некоторые условия и правила, которые я должна сначала изложить."
    MC "Ну и?"
    Caroline "Мне нужно, чтобы ты пообещал мне что-то, сначала."
    MC "Что-нибудь!"
    Caroline "Ты должен соблюдать эти правила, а не пытаться подталкивать меня, делать что-то, с чем мне неудобно. Это справедливо?"
    MC "Конечно, я так думаю."


    scene caroline_mc_room_morning_scene5_p7
    Caroline "Я с радостью помогу тебе снова используя свои руки или задницу. Но с двумя условиями."
    Caroline "Во-первых, ты начинаешь работать бесплатно, когда мне нужны фотосессии."
    MC "Достаточно справедливо."
    Caroline "Во-вторых, это заканчивается, когда ты находишь себе девушку. С тех пор это ее работа."
    Caroline "Тебя устраивают условия?"
    MC "Да, звучит справедливо."

    scene caroline_mc_room_morning_scene5_p8
    Caroline "Aхх, Я вижу, тебе нужно помочь прямо сейчас."
    MC "Да?"

    scene caroline_mc_room_morning_scene5_p9
    MC "Ой, чёрт! Извини."
    Caroline "Хотите закрепить нашу сделку прямо сейчас?"
    MC "Определенно!"
    Caroline "Давайте начнем. Сними свои трусы."

    scene caroline_mc_room_morning_scene5_hand_footp1
    Caroline "Ну, это было быстро! Сегодня это будет руками."
    MC "Да, давай!"
    Caroline "Хорошо, вот так."

    scene caroline_mc_room_morning_scene5_hand_footp2
    Caroline "Хехе... У тебя такой твердый член. Неужели я так сильно тебя возбуждаю?"
    MC "Любая красивая девушка, если честно."
    Caroline "Значит, ты считаешь меня красивой?"

    scene caroline_mc_room_morning_scene5_hand_footp3
    Caroline "Как тебе это? Я держу твой член слишком сильно?"
    MC "Mммм... Нет, хорошо."
    Caroline "Ладно тогда - я буду продолжать гладить твой, толстый член, как тогда."

    scene caroline_mc_room_morning_scene5_hand_footp4
    Caroline "Ты извращенец. Ты же знаешь, верно?"
    scene caroline_mc_room_morning_scene5_hand_footp4anim
    $ renpy.pause()
    if renpy.loadable("patch.rpy"):
        Caroline "Будь настойчивый по отношению к старшей сестре."
    if not renpy.loadable("patch.rpy"):
        Caroline "Будь настойчивый в отношениях к старому другу."

    scene caroline_mc_room_morning_scene5_hand_footp5
    MC "Ну, кажется, извращенцу, льготы."
    Caroline "Так ты думал обо мне, когда мастурбировал??"
    MC "Что? Я не-"

    scene caroline_mc_room_morning_scene5_hand_footp6
    Caroline "Ты пытаешься сказать мне, что не дрочишь? Это чушь собачья!"
    MC "Конечно, я делаю это... но я не собираюсь просто рассказывать тебе, о чем я мечтаю."
    scene caroline_mc_room_morning_scene5_hand_footp6anim
    $ renpy.pause()
    Caroline "О, хорошо... Может быть, ты откроешься мне, когда-нибудь."

    scene caroline_mc_room_morning_scene5_hand_footp7
    Caroline "Кстати, тебе это нравится? Ты хочешь, чтобы я сделал что-то другое?"
    window hide
    menu:
        "Это потрясающе! Не останавливайся!":

            scene caroline_mc_room_morning_scene5_hand_footp8
            MC "Это удивительно! Не останавливайтесь! Aхх…"
            Caroline "В таком случае я буду использовать обе руки!"
            MC "О, Господи! Я скоро кончу! Ухх!"


            scene caroline_mc_room_morning_scene5_hand_footp9
            if renpy.loadable("patch.rpy"):
                Caroline "Сперма для меня! Для старшей сестры!"
            if not renpy.loadable("patch.rpy"):
                Caroline "Кончай для меня! Сперма для Кэролайн!"
            MC "Ммм! Aххх! Ухх! Да!"
            MC "(У нее удивительные руки!)"

            scene caroline_mc_room_morning_scene5_hand_footp9a
            Caroline "Помни, это длится до тех пор, пока не найдешь себе девушку и ты работаешь бесплатно!"
            Caroline "Приходи ко мне по возможности. Я заказываю новый товар."
            MC "Сделаю, Кэролайн!"
            MC "Фу ... я устал…"
            Caroline "Ну, я ненавижу сообщать плохие новости, но тебе пора вставать."

            $ caroline_mc_room_moenig_scene5 = False
            $ Caroline_points += 1

            $ renpy.pause(3.0, hard=True)
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1
        "Могла бы ты воспользоваться ногами?":



            scene caroline_mc_room_morning_scene5_hand_footp7
            MC "Могла бы ты воспользоваться ногами?"
            Caroline "Н-ногами?"
            MC "Ты сказала, что поможешь мне своими руками или задницей, но мы можем сделать исключение в виде ног?"

            scene caroline_mc_room_morning_scene5_hand_footp11
            Caroline "Конечно."
            Caroline "Честно говоря, моими ограничениями были оральный и вагинальный секс. Я не думала, что ты фетешист."
            Caroline "Я никогда не использовала ноги раньше. Ты должен будешь направить меня немного. Ну как?"
            scene caroline_mc_room_morning_scene5_hand_footp11anim
            $ renpy.pause()

            scene caroline_mc_room_morning_scene5_hand_footp12
            MC "Это хорошо. Продолжай двигать ногами вверх и вниз."
            Caroline "Он чувствует себя немного неловко."
            MC "Не беспокойся об этом - все в порядке."
            MC "Если ты хочешь - ты также можешь попробовать держать мои яйца одной ногой и ласкать мой член другой."

            scene caroline_mc_room_morning_scene5_hand_footp13
            Caroline "Вроде этого?"
            MC "Да, вот так! Ммм…"
            Caroline "(Довольно весело на самом деле!)"

            scene caroline_mc_room_morning_scene5_hand_footp14
            Caroline "Ты скоро кончишь? Мои ноги немного устали."
            MC "Скоро. Если это поможет, ты можешь использовать свою руку."
            Caroline "Так нормально?"
            MC "Абсолютно!"

            scene caroline_mc_room_morning_scene5_hand_footp15
            MC "О Боже... да! ААА…"
            Caroline "О! Ты собираешься кончить!"
            MC "Aхх…"

            scene caroline_mc_room_morning_scene5_hand_footp16
            Caroline "Вот так!"
            MC "Aх! Aхх! Aхххх! МММММММ!"
            MC "Я кончаю!"

            scene caroline_mc_room_morning_scene5_hand_footp16a
            Caroline "О вау... Много спермы!"
            if renpy.loadable("patch.rpy"):
                Caroline "(Я думаю, [player_name] наслаждался этим!)"
            if not renpy.loadable("patch.rpy"):
                Caroline "(Я думаю, [player_name] наслаждался этим!)"
            MC "Фу... Это было невероятно, Кэролайн! Огромное спасибо... (Зевок!)"
            Caroline "Надеюсь, ты не устал! Пора вставать!"

            scene caroline_mc_room_morning_scene5_hand_footp17
            MC "В любом случае, спасибо, Кэролайн. Я наслаждаюсь нашей сделкой!"
            Caroline "Помни, это длится до тех пор, пока не найдешь себе девушку и ты работаешь бесплатно!"
            Caroline "Приходи ко мне по возможности. Я заказываю новый товар."
            MC "Сделаю, Кэролайн!"
            $ caroline_mc_room_moenig_scene5 = False
            $ Caroline_points += 1
            $ renpy.pause(3.0, hard=True)
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
