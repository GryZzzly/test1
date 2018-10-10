image ml_morning_salon_scene1_v1_p1 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/1.jpg"
image ml_morning_salon_scene1_v1_p2 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/2.jpg"
image ml_morning_salon_scene1_v1_p3 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/3.jpg"
image ml_morning_salon_scene1_v1_p4 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/4.jpg"
image ml_morning_salon_scene1_v1_p5 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/5.jpg"
image ml_morning_salon_scene1_v1_p6 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/6.jpg"
image ml_morning_salon_scene1_v1_p7 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/7.jpg"
image ml_morning_salon_scene1_v1_p8 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/8.jpg"
image ml_morning_salon_scene1_v1_p9 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/9.jpg"
image ml_morning_salon_scene1_v1_p10 = "images/home/salon/morning/scenes/ml_morning_salon_scene1_v1/10.jpg"

image ml_morning_salon_scene2_v1_p1 = "images/home/salon/morning/scenes/ml_morning_salon_scene2_v1/1.jpg"

image ml_morning_salon_scene3_v1_p1 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/1.jpg"
image ml_morning_salon_scene3_v1_p2 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/2.jpg"
image ml_morning_salon_scene3_v1_p3 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/3.jpg"
image ml_morning_salon_scene3_v1_p4 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/4.jpg"
image ml_morning_salon_scene3_v1_p5 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/5.jpg"
image ml_morning_salon_scene3_v1_p6 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/6.jpg"
image ml_morning_salon_scene3_v1_p7 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/7.jpg"
image ml_morning_salon_scene3_v1_p8 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/8.jpg"
image ml_morning_salon_scene3_v1_p9 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/9.jpg"
image ml_morning_salon_scene3_v1_p10 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/10.jpg"
image ml_morning_salon_scene3_v1_p11 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/11.jpg"
image ml_morning_salon_scene3_v1_p12 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/12.jpg"
image ml_morning_salon_scene3_v1_p13 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/13.jpg"
image ml_morning_salon_scene3_v1_p14 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/14.jpg"
image ml_morning_salon_scene3_v1_p15 = "images/home/salon/morning/scenes/ml_morning_salon_scene3_v1/15.jpg"


screen ml_morning_salon_scenes1to3_v1_screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("ml_morning_salon_scenes1to3_v1_screen"),Jump("salon_morning1")]

label ml_morning_salon_scenes1to3_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if ml_can_salon_morning_scene_dish_wash == True and ml_can_salon_morning_scene == False:
        show screen salon_morning
        show screen ml_morning_salon_scenes1to3_v1_screen
        MC "Мне нужно помыть посуду."
        jump salon_morning1
    if ml_can_salon_morning_scene == False:
        show screen salon_morning
        show screen ml_morning_salon_scenes1to3_v1_screen
        MC "Я уже говорил с ней."
        jump salon_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    if ml_salon_morning_visit == 1 and ml_can_salon_morning_scene == True:
        scene ml_morning_salon_scene1_v1_p1 with dissolve
        Television "...находятся в высокой скорости преследования с тремя мужчинами в масках."
        Television "Автомобиль угнали с парковки местного банка."

        if renpy.loadable("patch.rpy"):
            MC "(Похоже, мама смотрит утренние новости.)"
            scene ml_morning_salon_scene1_v1_p2
            MC "Доброе Утро, мама!"
        if not renpy.loadable("patch.rpy"):
            MC "(Похоже, Линда смотрит утренние новости.)"

            scene ml_morning_salon_scene1_v1_p2
            MC "Доброе Утро, Линда!"
        Mom "Доброе утро, [player_name]. Ты куда?"
        MC "Это школьный день, помнишь?"
        Mom "О! Правда."
        Mom "У тебя еще есть время. Подойди и посиди со мной некоторое время."
        MC "Ну ладно."

        scene ml_morning_salon_scene1_v1_p3
        MC "У меня есть только несколько минут - я не могу остаться слишком долго, или я..."
        Mom "Я знаю-ты опоздаешь на занятия."
        Mom "Я преподам тебе очень важный урок. Тот, который ты должен был узнать много лет назад."
        if renpy.loadable("patch.rpy"):
            Mom "Никогда не позволяй работе стать на пути семейного времени."
        if not renpy.loadable("patch.rpy"):
            Mom "Никогда не позволяй работе стать на пути семейного времени."

        scene ml_morning_salon_scene1_v1_p4
        if renpy.loadable("patch.rpy"):
            Mom "Даже если это всего несколько минут перед телевизором со своим сыном."
        if not renpy.loadable("patch.rpy"):
            Mom "Даже если всего за несколько минут перед телевизором со мной, перед школой."
        MC "Э... Хорошо. Я запомню."
        Mom "Пожалуйста. Твои собственные дети будут благодарить за это когда-нибудь."

        scene ml_morning_salon_scene1_v1_p5
        if renpy.loadable("patch.rpy"):
            MC "(Ебена мать! Мама не носит бюстгальтер!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Ебена мать! Линда не носит бюстгальтер!)"
        MC "(Но почему?!)"
        MC "(Она наклоняется так близко, что я почти чувствую ее левый сосок!)"
        Mom "...и я больше никогда не совершу эту ошибку."

        scene ml_morning_salon_scene1_v1_p6
        Mom "Ты слушаешь, [player_name]?"
        MC "А?! О! Да!"
        Mom "Давай я тебя поцелую, пока ты не ушел."

        scene ml_morning_salon_scene1_v1_p7
        MC "(Ох ... она собирается...)"
        MC "(О, это просто в щеку. Мое сердце начало биться сильнее!)"
        if renpy.loadable("patch.rpy"):
            MC "(Может быть, я больше не анализирую вещи? Возможно, это поцелуй любящей матери?)"
        if not renpy.loadable("patch.rpy"):
            MC "(Может быть, я больше не анализирую вещи? Возможно, это поцелуй любящего друга?)"
        MC "(Я должен перестать воспроизводить это в своем уме.)"

        scene ml_morning_salon_scene1_v1_p8
        MC "(А?! Она поворачивает мне голову!)"
        MC "(Что мне делать?!)"
        if renpy.loadable("patch.rpy"):
            MC "(Я не могу поцеловать ее в ответ вот так-она моя мать! Это слишком интимно!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Я не могу поцеловать ее в ответ вот так-она моя подруга! Это слишком интимно!)"
        scene ml_morning_salon_scene1_v1_p9
        Mom "Mмм…"
        MC "(Она кусает мою нижнюю губу!)"
        MC "(Вот именно - никаких шансов это просто обычный поцелуй перед окном.)"

        scene ml_morning_salon_scene1_v1_p10
        Mom "(Ой, бля! Я почти сделала это снова!)"
        Mom "Мне... мне нужно спешить на работу. Увидимся вечером!"
        if renpy.loadable("patch.rpy"):
            MC "Увидимся позже, мам…"
        if not renpy.loadable("patch.rpy"):
            MC "Увидимся позже, Линда…"
        Mom "(Может, мне повезло, и я отменила поцелуй, пока он не заподозрил?)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ ml_salon_morning_visit = 2
        $ ml_can_salon_morning_scene = False
        $ ml_can_salon_morning_scene2 = False
        jump salon_morning1
    if ml_salon_morning_visit == 2 and ml_can_salon_morning_scene == True:

        scene ml_morning_salon_scene2_v1_p1 with dissolve
        Mom "Доброе утро, [player_name]."
        if renpy.loadable("patch.rpy"):
            MC "Привет, мам."
        if not renpy.loadable("patch.rpy"):
            MC "Привет, Линда."
        Mom "Собираешься отправиться в школу?"
        MC "Через несколько минут."
        Mom "У тебя есть время помыть посуду?"
        menu:
            "Да":

                MC "Конечно, без проблем."
                Mom "Спасибо! Ты такой милый."
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_can_salon_morning_scene = False
                $ ml_can_salon_morning_scene_dish_wash = True
                jump salon_morning1
            "Нет":

                if renpy.loadable("patch.rpy"):
                    MC "Прости, Мам. Я немного тороплюсь. Я не могу позволить себе опаздывать."
                    Mom "Не волнуйся, я достану их позже. Приятного дня!"
                    MC "Спасибо, Мам!"
                if not renpy.loadable("patch.rpy"):
                    MC "Прости, Линда. Я немного тороплюсь. Я не могу позволить себе опаздывать."
                    Mom "Не волнуйся, я достану их позже. Приятного дня!"
                    MC "Спасибо, Линда!"
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_can_salon_morning_scene = False
                jump salon_morning1

    if ml_salon_morning_visit == 3 and ml_can_salon_morning_scene == True:
        scene ml_morning_salon_scene3_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "Доброе Утро, мама! Я сейчас иду в школу."
        if not renpy.loadable("patch.rpy"):
            MC "Доброе Утро, Линда! Я сейчас иду в школу."
        Mom "Подожди - пока не уходи!"

        scene ml_morning_salon_scene3_v1_p2
        Mom "Посиди со мной немного."
        MC "Я не хочу опоздать."
        Mom "Ты не опоздаешь - всего несколько минут."
        MC "Окей."

        scene ml_morning_salon_scene3_v1_p3
        Mom "Тебе нравиться кто-то из девушек?"

        menu:
            "Я видел несколько симпатичных.":

                scene ml_morning_salon_scene3_v1_p4
                MC "Я видел несколько симпатичных девушек."
                Mom "Оооо, я надеюсь, ты не превратишься в одного из тех плейбоев, которые гоняются за всеми девушками!!"
                if renpy.loadable("patch.rpy"):
                    MC "Мама!"
                if not renpy.loadable("patch.rpy"):
                    MC "Линда!"
                Mom "Хе-хе, я просто дразню тебя."
                scene ml_morning_salon_scene3_v1_p5
                Mom "Ты знаешь, что независимо от того, что ты делаешь, я всегда буду гордиться своим мальчиком."
                if renpy.loadable("patch.rpy"):
                    MC "Хаха! Ты заставляешь меня краснеть, мама."
                if not renpy.loadable("patch.rpy"):
                    MC "Хаха! Ты заставляешь меня краснеть, Линда."
                MC "(Она кажется ... другой сегодня. Интересно, что на нее нашло.)"

                scene ml_morning_salon_scene3_v1_p6
                if renpy.loadable("patch.rpy"):
                    MC "МММ ... Мама?"
                if not renpy.loadable("patch.rpy"):
                    MC "Мм ... Линда?"
                Television "Следующий - латте делает тебя толстым? Barry McSwindon расследует."
                Mom "(Медленно делает это... я собираюсь переместить мою руку, прямо к его промежности и посмотреть, как он реагирует.)"

                scene ml_morning_salon_scene3_v1_p7
                Television "Правда, Барри-выпивая более пятидесяти латте в день, значительно повышает риск ожирения."
                Television "Но, Соня-кто, черт возьми, пьет пятьдесят чашек кофе в день?!"
                Television "Это не то, что я пытаюсь сделать, Барри."
                if renpy.loadable("patch.rpy"):
                    MC "(Мама выглядит поглощенной своим шоу ... я не думаю, что она обращает внимание на то, что она делает.)"
                if not renpy.loadable("patch.rpy"):
                    MC "(Линда выглядит поглощенной своим шоу ... я не думаю, что она обращает внимание на то, что она делает.)"
                scene ml_morning_salon_scene3_v1_p8
                MC "(ХММ?!)"
                Television "Типичный латте из StarFucks содержит 190 калорий. Если вы умножите это на пятьдесят-"
                Television "Иисус, Блядь, Христос, Соня! Ты упускаешь смысл!"

                scene ml_morning_salon_scene3_v1_p9
                if renpy.loadable("patch.rpy"):
                    MC "М-Мама! Твоя рука!"
                if not renpy.loadable("patch.rpy"):
                    MC "Л-Линда! Твоя рука!"
                Mom "А? Оппс! Прости, я пыталась схватить тебя за руку. Я думала, ты держишь ее на коленях."
                Mom "Я должна была посмотреть."

                scene ml_morning_salon_scene3_v1_p10
                MC "Почему ты хотела схватить меня за руку?"
                Mom "Вот, позволь мне показать."

                scene ml_morning_salon_scene3_v1_p11
                MC "Что?!"
                Mom "Ты чувствуешь, что?"
                MC "Да, но я не думаю, что должен!"
                Mom "Мое сердцебиение."
                MC "О! Правда."

                scene ml_morning_salon_scene3_v1_p12
                Mom "Ты чувствуешь, как быстро он бьется?"
                Mom "Это только возле тебя. Ты для меня особенный."
                if renpy.loadable("patch.rpy"):
                    MC "М-Мама…"
                if not renpy.loadable("patch.rpy"):
                    MC "Л-Линда…"
                scene ml_morning_salon_scene3_v1_p13
                Mom "Всегда помни мое сердцебиение, и ты будете знать, как много ты значишь для меня."
                Mom "Я действительно люблю тебя, [player_name]."
                if renpy.loadable("patch.rpy"):
                    MC "Я буду, мам."
                if not renpy.loadable("patch.rpy"):
                    MC "Я буду, Линда."
                MC "(Что на нее нашло сегодня? Я никогда не видел ее такой эмоциональной прежде.)"

                scene ml_morning_salon_scene3_v1_p14
                Mom "Хорошо, тебе лучше попасть в школу. Я задерживаю тебя."
                if renpy.loadable("patch.rpy"):
                    MC "Все в порядке, мам."
                if not renpy.loadable("patch.rpy"):
                    MC "Все в порядке, Линдa."
                Mom "Ну, мне все равно надо идти. Увидимся позже."

                scene ml_morning_salon_scene3_v1_p15
                if renpy.loadable("patch.rpy"):
                    MC "Пока, мам. Увидимся…"
                if not renpy.loadable("patch.rpy"):
                    MC "Пока, Линда. Увидимся…"
                MC "(Она ведет себя очень странно в последнее время. Интересно, если есть что-то, что она не говорит мне.)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_salon_morning_visit = 4
                $ ml_can_salon_morning_scene = False
                $ ml_morning_salon_scene_active = False
                $ ml_kitchen_morning_scene = True
                $ ml_can_kitchen_morning_scene4 = False
                jump salon_morning1
            "Только одна прямо сейчас.":
                scene ml_morning_salon_scene3_v1_p4
                MC "Я вроде как положил глаз на одну прямо сейчас."
                Mom "О... ты делаешь?"
                MC "Да. Ты в порядке?"
                Mom "О, да! Я в порядке! Я..."
                scene ml_morning_salon_scene3_v1_p5
                Mom "Ты знаешь, что независимо от того, что ты делаешь, я всегда буду гордиться своим мальчиком."
                if renpy.loadable("patch.rpy"):
                    MC "Хаха! Ты заставляешь меня краснеть, мама."
                if not renpy.loadable("patch.rpy"):
                    MC "Хаха! Ты заставляешь меня краснеть, Линда."
                MC "(Она кажется ... другой сегодня. Интересно, что на нее нашло.)"

                scene ml_morning_salon_scene3_v1_p6
                if renpy.loadable("patch.rpy"):
                    MC "МММ ... Мама?"
                if not renpy.loadable("patch.rpy"):
                    MC "Мм ... Линда?"
                Television "Следующий-латте делает тебя толстым? Barry McSwindon расследует."
                Mom "(Медленно делает это... я собираюсь переместить мою руку, прямо к его промежности и посмотреть, как он реагирует.)"

                scene ml_morning_salon_scene3_v1_p7
                Television "Правда, Барри-выпивая более пятидесяти латте в день, значительно повышает риск ожирения."
                Television "Но, Соня-кто, черт возьми, пьет пятьдесят чашек кофе в день?!"
                Television "Это не то, что я пытаюсь сделать, Барри."
                if renpy.loadable("patch.rpy"):
                    MC "(Мама выглядит поглощенной своим шоу ... я не думаю, что она обращает внимание на то, что она делает.)"
                if not renpy.loadable("patch.rpy"):
                    MC "(Линда выглядит поглощенной своим шоу ... я не думаю, что она обращает внимание на то, что она делает.)"
                scene ml_morning_salon_scene3_v1_p8
                MC "(Хмм?!)"
                Television "Типичный латте из StarFucks содержит 190 калорий. Если вы умножите это на пятьдесят-"
                Television "Иисус, Блядь, Христос, Соня! Ты упускаешь смысл.!"

                scene ml_morning_salon_scene3_v1_p9
                if renpy.loadable("patch.rpy"):
                    MC "М-Мама! Твоя рука!"
                if not renpy.loadable("patch.rpy"):
                    MC "Л-Линда! Твоя рука!"
                Mom "А? Оппс! Прости, я пыталась схватить тебя за руку. Я думала, ты держишь ее на коленях."
                Mom "Я должна был посмотреть."

                scene ml_morning_salon_scene3_v1_p10
                MC "Почему ты хотела схватить меня за руку?"
                Mom "Вот, позволь мне показать тебе."

                scene ml_morning_salon_scene3_v1_p11
                MC "Что?!"
                Mom "Ты чувствуешь, что?"
                MC "Да, но я не думаю, что должен!"
                Mom "Мое сердцебиение."
                MC "О! Правда."

                scene ml_morning_salon_scene3_v1_p12
                Mom "Ты чувствуешь, как быстро он бьется возле тебя?"
                Mom "Это только возле тебя. Ты для меня особенный."
                if renpy.loadable("patch.rpy"):
                    MC "М-Мама…"
                if not renpy.loadable("patch.rpy"):
                    MC "Л-Линда…"
                scene ml_morning_salon_scene3_v1_p13
                Mom "Всегда помни мое сердцебиение, и ты будете знать, как много ты значишь для меня."
                Mom "Я действительно люблю тебя, [player_name]."
                if renpy.loadable("patch.rpy"):
                    MC "Я буду, мам."
                if not renpy.loadable("patch.rpy"):
                    MC "Я буду, Линда."
                MC "(Что сегодня стало с ней? Я никогда не видел, чтобы она действовала эмоционально.)"

                scene ml_morning_salon_scene3_v1_p14
                Mom "Ладно, тебе лучше пойти в школу. Я заставлю тебя опоздать."
                if renpy.loadable("patch.rpy"):
                    MC "Все в порядке, мам."
                if not renpy.loadable("patch.rpy"):
                    MC "Все в порядке, Линда."
                Mom "Ну, мне все равно нужно идти. Увидимся позже."

                scene ml_morning_salon_scene3_v1_p15
                if renpy.loadable("patch.rpy"):
                    MC "Пока, Мам. Увидимся…"
                if not renpy.loadable("patch.rpy"):
                    MC "Пока, Линда. Увидимся…"
                MC "(Она ведет себя очень странно в последнее время. Интересно, есть ли что-то, что она мне не говорит.)"

                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_salon_morning_visit = 4
                $ ml_can_salon_morning_scene = False
                $ ml_morning_salon_scene_active = False
                $ ml_kitchen_morning_scene = True
                $ ml_can_kitchen_morning_scene4 = False
                jump salon_morning1
            "Нет, я бы предпочел побыть один какое-то время.":
                scene ml_morning_salon_scene3_v1_p4
                MC "Нет, я бы предпочла побыть одной какое-то время. Особенно после этой неловкой ситуации с миссис Селией."
                Mom "Хорошо."
                MC "Хорошо?"
                Mom "ЭЭ… Я имею в виду, это хорошо, что ты ... делаешь все медленно и восстанавливаешься."
                MC "Ах, да."

                scene ml_morning_salon_scene3_v1_p5
                Mom "Ты знаешь, что независимо от того, что ты делаешь, я всегда буду гордиться своим мальчиком."
                if renpy.loadable("patch.rpy"):
                    MC "Хаха! Ты заставишь меня покраснеть, мам."
                if not renpy.loadable("patch.rpy"):
                    MC "Хаха! Ты заставишь меня покраснеть, Линда."
                MC "(Она кажется ... другой сегодня. Интересно, что на нее нашло.)"

                scene ml_morning_salon_scene3_v1_p6
                if renpy.loadable("patch.rpy"):
                    MC "МММ ... Мама?"
                if not renpy.loadable("patch.rpy"):
                    MC "Мм ... Линда?"
                Television "Следующий-латте делает тебя толстым? Barry McSwindon расследует."
                Mom "(Медленно делает это... я собираюсь переместить мою руку, прямо к его промежности и посмотреть, как он реагирует.)"

                scene ml_morning_salon_scene3_v1_p7
                Television "Правда, Барри-выпивая более пятидесяти латте в день, значительно повышает риск ожирения."
                Television "Но, Соня-кто, черт возьми, пьет пятьдесят чашек кофе в день?!"
                Television "Это не то, что я пытаюсь сделать, Барри."
                if renpy.loadable("patch.rpy"):
                    MC "(Мама выглядит поглощенной своим шоу ... я не думаю, что она обращает внимание на то, что она делает.)"
                if not renpy.loadable("patch.rpy"):
                    MC "(Линда выглядит поглощенной своим шоу ... я не думаю, что она обращает внимание на то, что она делает.)"
                scene ml_morning_salon_scene3_v1_p8
                MC "(ХММ?!)"
                Television "Типичный латте из StarFucks содержит 190 калорий. Если вы умножите это на пятьдесят-"
                Television "Иисус, Блядь, Христос, Соня! Ты упускаешь смысл!"

                scene ml_morning_salon_scene3_v1_p9
                if renpy.loadable("patch.rpy"):
                    MC "М-Мама! Твоя рука!"
                if not renpy.loadable("patch.rpy"):
                    MC "Л-Линда! Твоя рука!"
                Mom "А? Оппс! Прости, я пыталась схватить тебя за руку. Я думала, ты держишь ее на коленях."
                Mom "Я должна была посмотреть."

                scene ml_morning_salon_scene3_v1_p10
                MC "Почему ты хотела схватить меня за руку?"
                Mom "Вот, позволь мне показать тебе."

                scene ml_morning_salon_scene3_v1_p11
                MC "Что?!"
                Mom "Ты чувствуешь, что?"
                MC "Да, но я не думаю, что должен!"
                Mom "Мое сердцебиение."
                MC "Да."

                scene ml_morning_salon_scene3_v1_p12
                Mom "Ты чувствуешь, как быстро он бьется возле тебя?"
                Mom "Это только возле тебя. Ты для меня особенный."
                if renpy.loadable("patch.rpy"):
                    MC "М-Мама…"
                if not renpy.loadable("patch.rpy"):
                    MC "Линда…"
                scene ml_morning_salon_scene3_v1_p13
                Mom "Всегда помните мое сердцебиение, и ты будешь знать, как много ты значишь для меня."
                Mom "Я действительно люблю тебя, [player_name]."
                if renpy.loadable("patch.rpy"):
                    MC "Я буду, мам."
                if not renpy.loadable("patch.rpy"):
                    MC "Я буду, Линда."
                MC "(Что на нее нашло сегодня? Я никогда не видел ее такой эмоциональной.)"

                scene ml_morning_salon_scene3_v1_p14
                Mom "Ладно, тебе лучше пойти в школу. Я заставлю тебя опоздать."
                if renpy.loadable("patch.rpy"):
                    MC "Все в порядке, мам."
                if not renpy.loadable("patch.rpy"):
                    MC "Все в порядке, Линда."
                Mom "Ну, мне все равно нужно идти. Увидимся позже."

                scene ml_morning_salon_scene3_v1_p15
                if renpy.loadable("patch.rpy"):
                    MC "Пока, Мам. Увидимся…"
                if not renpy.loadable("patch.rpy"):
                    MC "Пока, Линда. Увидимся…"
                MC "(Она ведет себя очень странно в последнее время. Интересно, есть ли что-то, что она мне не говорит.)"
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ ml_salon_morning_visit = 4
                $ ml_can_salon_morning_scene = False
                $ ml_morning_salon_scene_active = False
                $ ml_kitchen_morning_scene = True
                $ ml_can_kitchen_morning_scene4 = False
                jump salon_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
