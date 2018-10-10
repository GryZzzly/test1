image Zv2_MS1_p1 = "images/Bob_work/reception/M/scenes/Zv2_MS1/1.jpg"
image Zv2_MS1_p2 = "images/Bob_work/reception/M/scenes/Zv2_MS1/2.jpg"
image Zv2_MS1_p3 = "images/Bob_work/reception/M/scenes/Zv2_MS1/3.jpg"
image Zv2_MS1_p4 = "images/Bob_work/reception/M/scenes/Zv2_MS1/4.jpg"
image Zv2_MS1_p5 = "images/Bob_work/reception/M/scenes/Zv2_MS1/5.jpg"
image Zv2_MS1_p6 = "images/Bob_work/reception/M/scenes/Zv2_MS1/6.jpg"
image Zv2_MS1_p6a = "images/Bob_work/reception/M/scenes/Zv2_MS1/6a.jpg"
image Zv2_MS1_p7 = "images/Bob_work/reception/M/scenes/Zv2_MS1/6a.jpg"
default Zuri_name = "Зури"
label Zv2_MS1_label:
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if Zv2_MS1_ask_boob_office == True:
        scene Zv2_MS1_p1 with dissolve
        $ Zuri_name = "???"
        Zuri "Привет и добро пожаловать в Bayside Business Consultants. Меня зовут Зури. Чем я могу тебе помочь?"
        $ Zuri_name = "Зури"




        scene Zv2_MS1_p2
        if renpy.loadable("patch.rpy"):
            MC "(Вау! Это должно быть папина секретарша! Она очень горячая!)"
            MC "Привет, Зури. Меня зовут [player_name]. Я собирался навестить отца."
            Zuri "И кто твой отец?"
        else:
            MC "(Вау! Это должно быть секретарь Боба! Она очень горячая!)"
            MC "Привет, Зури. Меня зовут [player_name]. Я пришел к Бобу."
            Zuri "А кто такой Боб?"
        MC "Тот, кто управляет этой компанией?"

        scene Zv2_MS1_p3

        Zuri "Ахахаха! Как смешно!"
        Zuri "Позволь мне угадать - ты с одной из этих онлайн-шуток, не так ли?"
        MC "Гмм?"
        Zuri "У тебя есть секретная камера, и ты собираешься унизить босса и выложить онлайн?"
        if renpy.loadable("patch.rpy"):
            MC "Нет. Что ?! Я на самом деле его сын."
        else:
            MC "Нет. Что ?! Я действительно живу с ним."

        scene Zv2_MS1_p1

        Zuri "В самом деле?"
        MC "Да!"
        Zuri "Ох! Извини меня плохую!"
        $ Zv2_MS1_ask_boob_office = False
        jump Zv2_MS1_label2
    if Zv2_MS1_ask_boob_office == False:
        jump Zv2_MS1_label2

label Zv2_MS1_label2:
    if Zv2_MS1_ask_boob_office1 == 3:
        scene Zv2_MS1_p1 with dissolve
        Zuri "Привет и добро пожаловать в Bayside Business Consultants."
        MC "В офисе есть кто-то?"
        scene Zv2_MS1_p4 at pandown3
        if renpy.loadable("patch.rpy"):
            Zuri "Пожалуйста следуй за мной. Я отведу тебя в офис твоего папы."
        else:
            Zuri "Пожалуйста следуй за мной. Я отведу тебя в офис Боба."
        MC "Спасибо."
        jump Zv2_MS1_label3
    if Zv2_MS1_ask_boob_office == False:
        scene Zv2_MS1_p4 at pandown3

        Zuri "В таком случае, пожалуйста, следуй за мной. Я отведу тебя в его офис."
        MC "(Наконец!)"
        MC "Спасибо."
label Zv2_MS1_label3:
    scene Zv2_MS1_p5

    Zuri "Теперь, я должна предупредить тебе - он довольно занят сегодня, так что ты не мог бы оставаться с ним слишком долго."
    Zuri "Сейчас компания переживает очень деликатную реструктуризацию наших контрактов."
    MC "Я вижу. Это не проблема."

    scene Zv2_MS1_p6
    $ renpy.sound.play("sfx/knock_knock.wav")
    "*Стук Стук Стук*"
    $ renpy.music.stop(channel="sound", fadeout=1)
    Zuri "Сэр? К вам посетитель."
    Dad "Кто это?"
    MC "(У нее такая короткая юбка! Может, у меня будет шанс взглянуть на ее трусики?)"
    window hide
    menu:
        "Bend down and peek up her skirt.":
            scene Zv2_MS1_p6a

            MC "(О, очень мило!)"
            MC "(Эти трусики такие тонкие! Они почти ничего не прикрывают!)"
            if renpy.loadable("patch.rpy"):
                MC "(Мне бы хотелось попасть в эту задницу! Но есть большая вероятность того, что это не произойдет - она - секретарь папы!) "
            else:
                MC "(Мне бы хотелось попасть в эту задницу! Но есть большая вероятность того, что это не произойдет - она - секретарь Боба!)"
            jump Zv2_MS1_after_menu
        "Это не стоит риска.":


            if renpy.loadable("patch.rpy"):
                MC "(Мне лучше не рисковать. Если она поймает меня, она, скорее всего, никогда не позволит мне посетить папу снова!)"
            else:
                MC "(Мне лучше не рисковать. Если она поймает меня, она, скорее всего, никогда не позволит мне посетить Боба снова!)"

            scene Zv2_MS1_p7

            Zuri "Это ваш сын, сэр."
            Dad "О! [player_name]! Заходи!"
            Zuri "Продолжайте, сэр. Просто постарайся не отвлекать отца от работы слишком долго, пожалуйста."
            MC "Я буду помнить об этом. Спасибо, Зури."
            Zuri "С удовольствием."
            jump Zv2_MS1_after_menu
label Zv2_MS1_after_menu:
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ Zv2_first_meet = False
    $ bob_office_locked = True
    $ can_hide_windows = False
    jump bob_office_M1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
