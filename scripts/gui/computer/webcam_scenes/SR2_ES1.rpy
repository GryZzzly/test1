image SR2_ES1_p1 = "images/web_cam_scenes/SR2_ES1/1.jpg"
image SR2_ES1_p2 = "images/web_cam_scenes/SR2_ES1/2.jpg"
image SR2_ES1_p3 = "images/web_cam_scenes/SR2_ES1/3.jpg"
image SR2_ES1_p4 = "images/web_cam_scenes/SR2_ES1/4.jpg"
image SR2_ES1_p5 = "images/web_cam_scenes/SR2_ES1/5.jpg"
image SR2_ES1_p6 = "images/web_cam_scenes/SR2_ES1/6.jpg"
image SR2_ES1_p7 = "images/web_cam_scenes/SR2_ES1/7.jpg"
image SR2_ES1_p8 = "images/web_cam_scenes/SR2_ES1/8.jpg"
image SR2_ES1_p9 = "images/web_cam_scenes/SR2_ES1/9.jpg"
image SR2_ES1_p10 = "images/web_cam_scenes/SR2_ES1/10.jpg"
image SR2_ES1_p11 = "images/web_cam_scenes/SR2_ES1/11.jpg"
image SR2_ES1_p12 = "images/web_cam_scenes/SR2_ES1/12.jpg"
image SR2_ES1_p13 = "images/web_cam_scenes/SR2_ES1/13.jpg"


image SR2_ES1_Bra_p1 = "images/web_cam_scenes/SR2_ES1/Bra/1.jpg"
image SR2_ES1_Bra_p2 = "images/web_cam_scenes/SR2_ES1/Bra/2.jpg"
image SR2_ES1_Bra_p3 = "images/web_cam_scenes/SR2_ES1/Bra/3.jpg"
image SR2_ES1_Bra_p4 = "images/web_cam_scenes/SR2_ES1/Bra/4.jpg"
image SR2_ES1_Bra_p5 = "images/web_cam_scenes/SR2_ES1/Bra/5.jpg"
image SR2_ES1_Bra_p6 = "images/web_cam_scenes/SR2_ES1/Bra/6.jpg"

image SR2_ES1_Pant_p1 = "images/web_cam_scenes/SR2_ES1/Panties/1.jpg"
image SR2_ES1_Pant_p2 = "images/web_cam_scenes/SR2_ES1/Panties/2.jpg"
image SR2_ES1_Pant_p3 = "images/web_cam_scenes/SR2_ES1/Panties/3.jpg"
image SR2_ES1_Pant_p4 = "images/web_cam_scenes/SR2_ES1/Panties/4.jpg"
image SR2_ES1_Pant_p5 = "images/web_cam_scenes/SR2_ES1/Panties/5.jpg"
image SR2_ES1_Pant_p6 = "images/web_cam_scenes/SR2_ES1/Panties/6.jpg"
image SR2_ES1_Pant_p7 = "images/web_cam_scenes/SR2_ES1/Panties/7.jpg"
image SR2_ES1_Pant_p8 = "images/web_cam_scenes/SR2_ES1/Panties/8.jpg"
image SR2_ES1_Pant_p9 = "images/web_cam_scenes/SR2_ES1/Panties/9.jpg"

image SR2_ES1_Vib_p1 = "images/web_cam_scenes/SR2_ES1/Vibrator/1.jpg"
image SR2_ES1_Vib_p2 = "images/web_cam_scenes/SR2_ES1/Vibrator/2.jpg"
image SR2_ES1_Vib_p3 = "images/web_cam_scenes/SR2_ES1/Vibrator/3.jpg"
image SR2_ES1_Vib_p4 = "images/web_cam_scenes/SR2_ES1/Vibrator/4.jpg"
image SR2_ES1_Vib_p5 = "images/web_cam_scenes/SR2_ES1/Vibrator/5.jpg"
image SR2_ES1_Vib_p6 = "images/web_cam_scenes/SR2_ES1/Vibrator/6.jpg"
image SR2_ES1_Vib_p7 = "images/web_cam_scenes/SR2_ES1/Vibrator/7.jpg"
image SR2_ES1_Vib_p8 = "images/web_cam_scenes/SR2_ES1/Vibrator/8.jpg"
image SR2_ES1_Vib_p9 = "images/web_cam_scenes/SR2_ES1/Vibrator/9.jpg"
image SR2_ES1_Vib_p10 = "images/web_cam_scenes/SR2_ES1/Vibrator/10.jpg"
image SR2_ES1_Vib_p11 = "images/web_cam_scenes/SR2_ES1/Vibrator/11.jpg"
image SR2_ES1_Vib_p12 = "images/web_cam_scenes/SR2_ES1/Vibrator/12.jpg"
image SR2_ES1_Vib_p13 = "images/web_cam_scenes/SR2_ES1/Vibrator/13.jpg"
image SR2_ES1_Vib_p14 = "images/web_cam_scenes/SR2_ES1/Vibrator/14.jpg"
image SR2_ES1_Vib_p15 = "images/web_cam_scenes/SR2_ES1/Vibrator/15.jpg"
image SR2_ES1_Vib_p16 = "images/web_cam_scenes/SR2_ES1/Vibrator/16.jpg"
image SR2_ES1_Vib_p17 = "images/web_cam_scenes/SR2_ES1/Vibrator/17.jpg"
image SR2_ES1_Vib_p18 = "images/web_cam_scenes/SR2_ES1/Vibrator/18.jpg"
image SR2_ES1_Vib_p19 = "images/web_cam_scenes/SR2_ES1/Vibrator/19.jpg"

label SR2_ES1_label:
    hide screen main_deskop_pcv1
    if SR2_ES1 == True:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_ES1_p1 with dissolve

        Sara "Эй, [player_name]! Угадай, кто, наконец то, получил свою веб-камеру!"
        MC "Привет, Сара! Мама знает, что ты пользуешься веб-камерой?"
        Sara "Конечно нет. Она даже не знает, что я на ноутбуке. Хехе!"
        MC "Хаха! Ты непослушная девочка!"

        scene SR2_ES1_p2

        Sara "Как на свободе?"
        MC "Эх, не очень. Я делаю немного работы, и много всякой херни в школе."
        if renpy.loadable("patch.rpy"):
            Sara "По крайней мере, ты можешь идти куда хочешь. Мама меня полностью наказала."
        else:
            Sara "По крайней мере, ты можешь идти куда хочешь. Линда полностью меня наказала."

        scene SR2_ES1_p3

        MC "Надеюсь, наши ночные чаты помогут тебе избавиться от скуки, с которой ты столкнулись."
        Sara "МММ, я тоже на это надеюсь!"
        if renpy.loadable("patch.rpy"):
            MC "Что ты должна сделать, чтобы мама тебя простила?"
        else:
            MC "Что ты должна сделать, чтобы Линда тебя простила?"


        scene SR2_ES1_p4

        Sara "Гррр…."
        Sara "Мы должны говорить об этом?"
        MC "Просто хочу знать, как долго я не смогу нормально общаться с тобой!"

        scene SR2_ES1_p5

        Sara "Она хочет, чтобы я перечитала все книги, которые я изучала в школе в этом году."
        Sara "И затем я должна пересдать все тесты, по которым B и ниже."
        Sara "И, наконец, я должна получить A на следующих двух тестах."

        scene SR2_ES1_p6

        Sara "Посмотри на это дерьмо! Почему я должна изучать поэзию какого-то мертвеца?"
        Sara "Он даже не пишет на нормальном английском!"
        Sara "‟Я смею все, что смеет человек, кто смеет больше, тот не человек. Что, черт возьми, это значит?!"
        MC "Я помню, что мне тоже приходилось изучать Шекспира. Я думаю, это были Ромео и Джульетта."
        Sara "Это так несправедливо! У тебя супер романтическая история - я застряла с Макбетом. Это так ... скучно!"

        scene SR2_ES1_p7
        if renpy.loadable("patch.rpy"):
            Sara "В любом случае! С этого момента я смогу наслаждаться поздними ночными чатами с моим любимым братом!"
        else:
            Sara "В любом случае! С этого момента я смогу наслаждаться поздними ночными чатами с моим любимым другом!"
        Sara "Так что, по крайней мере, у меня есть что-то, что я с нетерпением буду ждать в конце каждого дня!"
        if renpy.loadable("patch.rpy"):
            MC "Разве я не твой единственный брат?"
        else:
            MC "Разве я не твой единственный друг?"
        Sara "Ты ... но даже если бы не был, ты все равно был бы моим любимым."
        MC "(О, она действительно смотрит на меня!)"
        scene SR2_ES1_p8

        MC "Итак, что ты сегодня наденешь?"
        Sara "Оооо, только пижаму. Я собиралась ложиться спать, после нашего разговора."
        MC "Можно посмотреть?"

        scene SR2_ES1_p9

        MC "Без низа?"
        Sara "Сейчас слишком тепло!"
        MC "Отойди назад что бы лучше рассмотреть тебя."

        scene SR2_ES1_p10

        Sara "Так нормально?"
        MC "Идеально! У тебя такие сексуальные ноги! Ты знаешь?"
        Sara "Хехе! Спасибо, [player_name]!"

        scene SR2_ES1_p11

        Sara "Эй! Хочешь увидеть что-то удивительное?"
        MC "Конечно!"
        Sara "Ты должен пообещать не говорить никому, хорошо?"
        MC "Хорошо, я обещаю. (Интересно, о чем она говорит…)"

        scene SR2_ES1_p12

        Sara "Буу!"
        MC "Ммм! Очень хорошо!"
        Sara "Эти трусики немного маленькие - они прикрывают слишком мало."
        Sara "Я не могу носить их в школу в спортивные дни, потому что другие девушки будут видеть, когда мы переодеваемся."
        MC "Они действительно классные!"

        scene SR2_ES1_p13

        Sara "Хаха! Я рада, что тебе нравятся, [player_name]!"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)
        $ menu_q1 = True
        $ menu_q2 = True
        jump SR2_ES1_menu


label SR2_ES1_menu:
    scene SR2_ES1_p13
    menu:
        "Можешь показать мне свой лифчик?" if menu_q1 == True:

            scene SR2_ES1_Bra_p1

            MC "Теперь ты меня возбуждаешь. Не могла бы ты отйти немного дальше и показать мне свой лифчик?"
            Sara "Мой лифчик?"
            MC "Да, просто немного потяни вниз чтобы я увидел."
            Sara "У нас проблема, [player_name]… Я не могу этого сделать..."

            scene SR2_ES1_Bra_p2

            Sara "На самом деле у меня его нет."
            MC "(Ебена мать! Ее сиськи потрясающие!)"
            Sara "Извини, большинство девушек не пользуются бюстгальтером в постели."

            scene SR2_ES1_Bra_p3

            Sara "Я даже потяну другую сторону рубашки, чтобы доказать это."
            MC "Да, ты должна это сделать!"
            if renpy.loadable("patch.rpy"):
                MC "(Нет ничего лучше, если бы твоя сестра показывала сиськи на камеру!)"

            scene SR2_ES1_Bra_p4

            Sara "Видишь, [player_name]? Без."
            MC "Твои сиськи великолепны, Сара. Мне бы хотелось поцеловать их."
            MC "Ты могла бы поднять немного камеру, чтобы мне было лучше видно?"

            scene SR2_ES1_Bra_p5

            Sara "Конечно, [player_name]."
            Sara "Я очень рада, что они тебе нравятся. Я немного волновалась, что они слишком маленькие."
            MC "Нет, они абсолютно идеальны."

            scene SR2_ES1_Bra_p6

            Sara "Как это?"
            MC "Это великолепно. Боже, они такие задорные!"
            MC "Ты бы выглядела такой горячей в крошечном бикини. Может быть, я заставлю тебя надеть их в бассейн когда-нибудь?"
            Sara "Хехе... Посмотрим. Я не собираюсь ничего обещать!"
            $ menu_q1 = False
            if menu_q1 == False and menu_q2 == False:
                jump SR2_ES1_continue
            else:
                jump SR2_ES1_menu

        "Можешь показать мне свои трусики?" if menu_q2 == True:

            scene SR2_ES1_Pant_p1
            MC "Черт, ты такая сексуальная, Сара."
            Sara "Хехе... Спасибо."
            MC "Серьезно, у меня сйчас такой стояк. Не могла бы ты показать мне немного больше?"
            Sara "Еще немного? О чем ты думаешь?"
            MC "Как насчет того, чтобы показать мне свои трусики?"

            scene SR2_ES1_Pant_p2

            Sara "Конечно. Две секунды - мне просто нужно настроить веб-камеру."
            MC "Не торопись."
            MC "(Это будет здорово!)"

            scene SR2_ES1_Pant_p3

            Sara "Ты видишь меня хорошо с этого ракурса?"
            MC "Да, это прекрасно, Сара. Подойди вперед и подними платье вверх."
            Sara "(Я не знаю, почему я делаю это так охотно для него. Если бы это был какой-нибудь другой парень в моей школе, я бы дрожала от тревоги!)"

            scene SR2_ES1_Pant_p4

            Sara "Вот так [player_name]. Что ты думаешь?"
            MC "МММ! Постой так несколько минут."
            MC "(Я могу рассмотреть ее киску через тонкую розовую ткань!)"
            Sara "Хочешь посмотреть на вид сзади? "
            Sara "(Отлично... я начинаю возбуждаться.)"
            MC "Да пожалуйста!"

            scene SR2_ES1_Pant_p5

            Sara "Вот так."
            MC "Я действительно не вижу многого. Поднимешь рубашку выше?"
            Sara "Ой, прости! Моя вина!"

            scene SR2_ES1_Pant_p6

            Sara "Вот так?"
            MC "Намного лучше! Теперь я все вижу."
            Sara "Хехе…"
            MC "(У нее такая милая маленькая попка!)"

            scene SR2_ES1_Pant_p7

            Sara "Ну? Тебе понравилось?"
            MC "МММ, очень сильно!"
            Sara "В таком случае, позволь мне сделать тебе прощальный подарок."

            scene SR2_ES1_Pant_p8

            MC "Ух ты, у меня голова закружится, если ты будешь так двигать веб-камерой!"
            Sara "Почти готово!"

            scene SR2_ES1_Pant_p9

            Sara "Ты, наверное, не можешь сказать , но я начинаю действительно ... мокнуть под этими трусиками."
            Sara "Что-то в демонстрвции меня на камеру действительно возбуждает."
            MC "Я с нетерпением жду встречи с тобой по вебке без трусиков."
            Sara "Хехе! Я подумаю!"
            $ menu_q2 = False
            if menu_q1 == False and menu_q2 == False:
                jump SR2_ES1_continue
            else:
                jump SR2_ES1_menu



label SR2_ES1_continue:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
    scene SR2_ES1_Vib_p1

    MC "(Она все еще выглядит довольно подавленной после того, как ее закрыли в комнате.)"
    MC "(Посмотрим, смогу ли я отвлечь ее мыслей...)"
    MC "Тебе понравился вибратор, который я тебе купил?"

    scene SR2_ES1_Vib_p2

    Sara "А? О да, это действительно хорошо."
    MC "Ты часто ним пользуешься?"
    Sara "Почти каждый день! Иногда несколько раз. Я представляю себе что это твой член прижимается к моей киске."
    MC "Ты все еще сидишь в своей комнате?"

    scene SR2_ES1_Vib_p3

    Sara "Да, это прямо здесь. Я прячу его в ящике стола."
    MC "Да, это прямо здесь. Я прячу его в ящике стола?"
    Sara "Что?"
    MC "Я хотел бы посмотреть, как ты пользуешься. Можешь сделать это для меня?"

    scene SR2_ES1_Vib_p4

    Sara "Я... Наверное…"
    MC "(Ууу! Это будет здорово!)"
    Sara "Ты должен пообещать ... не смеяться, хорошо?"
    MC "Почему я должен смеяться?"
    Sara "Я издаю	... много звуков, когда использую его."
    MC "Я не буду смеяться, обещаю."

    scene SR2_ES1_Vib_p5

    Sara "(Глубокий вдох) Окей…"
    Sara "Я только сниму свои трусики…"
    Sara "(Я не могу поверить, что делаю это на камеру…)"

    scene SR2_ES1_Vib_p6
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*Buzzzzz*"
    Sara "Oooх…"
    MC "(Я слышу вибратор, и похоже, что Сара только что нашла свой клитор!)"
    MC "(Жаль, что я ничего не вижу, хотя…)"
    MC "Сара, можешь приблизить веб-камеру, чтобы я мог видеть?"

    scene SR2_ES1_Vib_p7

    Sara "МММ! Угу! Конечно! ААА…"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*Buzzzzzzzz*"
    Sara "Ох ... черт…"
    MC "(Та девушка в секс шопе была права! Сильная вибрация!)"

    scene SR2_ES1_Vib_p8

    Sara "Ты видишь?"
    MC "Да! Твоя киска выглядит потрясающе!"
    MC "Я мог бы просто нырнуть прямо туда и лизать тебя часами."
    Sara "[player_name]!"
    MC "Подними его немного вверх. Я хочу посмотреть как ты мастурбируешь."

    scene SR2_ES1_Vib_p9
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*Buzzzz*"
    Sara "Ах ... Ах.... ААА!"
    MC "(Похоже, что Сара сейчас проводит время своей жизни!)"

    scene SR2_ES1_Vib_p10

    Sara "МММ! Да! МММ!"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*BUZZZZ*"
    MC "Каково это, Сара?"

    scene SR2_ES1_Vib_p11

    Sara "МММ! Это оооочень.... офигительно!"
    Sara "Тьфу! Это как - аххх-тепло глубоко в моем животе! МММ!"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*BUZZZ*"
    Sara "Боже ... это так интенсивно ...  ААА!"
    MC "Я хочу, чтобы ты кончила, Сара."

    scene SR2_ES1_Vib_p12

    Sara "Боже! Да! Я кончаю! Я КОНЧАЮ!"
    Sara "Хммммм!!! Ахххххх!"
    MC "(Вау! Она дрожит и дрожит! Я никогда не видел, чтобы девушка кончала так интенсивно!)"

    scene SR2_ES1_Vib_p13
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music2", loop=True, fadein = 2)
    $ renpy.sound.play("sfx/knock_knock.wav")
    "*СТУК СТУК*"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    "*BUZZZ*"
    Sara "Блядь!"

    $ Mom_name = "???"

    Mom "Сара? Что там происходит?"
    if renpy.loadable("patch.rpy"):
        $ Mom_name = "Линда"
    else:
        $ Mom_name = "Мама"

    MC "(Вот дерьмо!)"
    MC "Быстро! Выключи вибрацию и брось его под свою кровать!"

    scene SR2_ES1_Vib_p14

    Mom "Сара! Я сказала тебе учиться! Ты снова тратишь время на эти онлайн-игры, не так ли?"
    if renpy.loadable("patch.rpy"):
        Sara "Н-Нет, М-Мама!"
    else:
        Sara "Н-Нет, Л-Линда!"

    Mom "Не лги мне, юная леди!"

    scene SR2_ES1_Vib_p15

    Sara "Хух!"
    "*СТУК*"
    Mom "Возьми себя в руки и..."

    scene SR2_ES1_Vib_p16

    Mom "Почему ты не носишь трусики?!"
    if renpy.loadable("patch.rpy"):
        Sara "Я ... Э ... мама!"
    else:
        Sara "Я... э... - Линда!"
    Mom "О Боже мой! Это были стоны, я слышала их из твоей комнаты!"

    scene SR2_ES1_Vib_p17

    Mom "Ты смотрела порно?!"
    if renpy.loadable("patch.rpy"):
        Sara "Мама, я..."
    else:
        Sara "Линда, я..."
    Mom "Вот именно. Будешь без ноутбука. Выключи его, сейчас же."

    scene SR2_ES1_Vib_p18
    if renpy.loadable("patch.rpy"):
         Sara "Но, Мама!"
    else:
        Sara "Но, Линда!"
    Mom "Сейчас, Сара! Я сказала, выключи свой ноутбук!"
    Sara "*Сопит* Ладно…"

    scene SR2_ES1_Vib_p19

    Mom "Подожди, это твоя вебка?"
    Mom "Ты занималась киберсексом с мальчиками?!"
    MC "(Ой, бля!)"
    Sara "Н-нет! Красный свет означает что она выключена!"
    Mom "ААА... Согласна."
    Sara "*Сопит*"
    Mom "Клянусь Богом! Будешь сидеть тут в течение года, если твои оценки не улучшатся, юная леди."

    $ sara_webcam_online = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False

    $ SR2_AS4 = False
    $ SR2_ES1 = False
    $ SR2_AS5 = True
    $ day_time = 4
    $ sms6_sara = True
    jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
