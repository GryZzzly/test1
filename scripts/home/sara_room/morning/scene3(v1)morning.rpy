image scene3_v1p1 = "images/home/sara_room/morning/Scene3_v1/1.jpg"
image scene3_v1p2 = "images/home/sara_room/morning/Scene3_v1/2.jpg"
image scene3_v1p3 = "images/home/sara_room/morning/Scene3_v1/3.jpg"
image scene3_v1p4 = "images/home/sara_room/morning/Scene3_v1/4.jpg"
image scene3_v1p5 = "images/home/sara_room/morning/Scene3_v1/5.jpg"
image scene3_v1p6 = "images/home/sara_room/morning/Scene3_v1/6.jpg"
image scene3_v1p7 = "images/home/sara_room/morning/Scene3_v1/7.jpg"
image scene3_v1pdrawer = "images/home/sara_room/morning/Scene3_v1/drawer_sara.png"

label sis_nerdy_scene3_v1:
    hide screen displayTextScreen
    hide screen corridor_morning
    scene SisterNerdy_morning
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    call screen sister_nerdy_morning

label scene3_v1drawer:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    MC "(Да, никаких признаков Сары. Интересно, где она.)"
    MC "(Подумай об этом ... если ее не вокруг, я мог бы взять любопытную вещь в ее шкафе. Может, у нее там что-то интересное спрятанное?)"
    $ drawer_sis_nerdy = 2
    jump sister_nerdy_morning1

label sis_nerdy_scene3_1_v1:
    $ renpy.music.stop(channel="music2", fadeout=2)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene scene3_v1p1 with dissolve
    $ can_hide_windows = True
    MC "(Посмотрим, что можно найти здесь..)"
    MC "(Большинство девочек ее возраста начали употреблять алкоголь. Возможно, она могла бы спрятать его здесь.)"
    scene black
    $ renpy.sound.play('/sfx/Drawer open.mp3', loop=False)
    $ renpy.pause(2)
    $ renpy.sound.stop(channel="sound")
    MC "(Скучно ... Хлам ... Мусор…)"
    MC "(Сколько макияжа нужна одной девушке?!)"
    MC "(Вау! Стоп!)"
    scene scene3_v1p2
    if renpy.loadable("patch.rpy"):
        MC "(Пара трусиков Сары?)"
    if not renpy.loadable("patch.rpy"):
        MC "(Пара трусиков Сары?)"
    MC "(Я могу стащить их в мою комнату, прежде чем она возвратится.)"
    MC "(Подождите - почему я даже подумываю сделать что-то подобное ?! Этот глупый терапевт вкладывает в голову извращенные идеи!)"
    MC "(Я, наверное, должен просто вернуть их обратно.)"

    scene scene3_v1p3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Aces High.mp3', channel="music2", loop=True, fadein = 2)
    Sara "УГМС!"
    Sara "[player_name]? Что ты делал в моем нижнем белье?"
    MC "(ТВОЮ МАТЬ!)"
    MC "(Мне нужно придумать что-то, чтобы оправдаться…)"
    window hide
    menu:
        "Положить трусики в ящик и уйти, не сказав ни слова.":

            scene scene3_v1p4
            MC "(Чем меньше я говорю, тем лучше. Может быть, если я поступлю так, как будто ничего странного не происходит, тогда Сара подумает, что я просто убираю или собираю стирку?)"
            MC "(Да, это лучший способ справиться с этим.)"
            Sara "[player_name]! Что ты делаешь с моим..."

            scene scene3_v1p6
            Sara "Да?!"
            Sara "(Ч-что ?! Он просто уронил мои трусики и ушел?)"
            MC "(Ха-ха! Успешно справился! Теперь она думает, что я просто собираю стирку!)"
            Sara "(Должно быть, это был блеф, что он собирал стирку?)"
            MC "(Нет, она никогда не подумает, что я собираюсь украсть ее трусики и рылся в них!)"
            Sara "(Черт ... мысль о том, что он крадет мои трусики и роеться в них, довольно горячая)"

            scene scene3_v1p7
            Sara "Действительно ... действительно ... горяч..."
            Sara "(Ему, должно быть, действительно понравились эти трусики, если вынул их из ящика.)"
            Sara "(Интересно, могу ли я его удивить?)"
            jump after_scene3_v1_ch1
        "Солгать и заявить, что ты нашел их лежащими на полу.":


            scene scene3_v1p4
            MC "(Я просто должен сказать ей, что я вошел в ее комнату и нашел ее трусики, лежащие на полу.)"
            MC "(Ты можешь сделать это, [player_name]. Обдумай, затем развернись и уверенно объясни, что произошло.)"
            MC "(Сара, я вошел в твою комнату, увидел твои трусики, лежащие на полу, и поднял их.)"
            Sara "[player_name]?"
            MC "(Сара, я вошла в твою комнату, увидела твои трусики, лежащие на полу.)"
            Sara "[player_name]! Что ты делаешь?!"
            MC "(Сара, я зашел в твою комнату, увидел твои трусики, лежащие на-)"
            Sara "[player_name]! Ответь мне!"

            scene scene3_v1p5
            MC "Сара, я пришел в твою комнату положить трусики!"
            Sara "Что?!"
            MC "Н-нет! Я пришел в твои трусики - я имею в виду, я пришел на твой пол!"
            Sara "Ч-что ?!"
            MC "(О, черт! Я вернул это! Мне нужно сделать глубокий вдох и начать снова.)"
            MC "Я вошел в твою ... комнату. Я увидел твои трусики, лежащие на полу. Затем я поднял их, чтобы положить в ящик."
            MC "Вот, возьми их обратно!"

            scene scene3_v1p6
            MC "(Иисус Христос! Это было почти так же плохо, как мой опыт с миссис Селией!)"
            MC "(Почему я не могу просто общаться с людьми должным образом!)"

            scene scene3_v1p7
            Sara "(Хехе! Это было действительно смешно видя как [player_name] волновался.)"
            Sara "(Я должна признаться, хотя - мысль о том, что он использует мои трусики и кончает в них, действительно горячая.)"
            Sara "(Только одна мысль заставляет меня мокреть.)"
            jump after_scene3_v1_ch1


label after_scene3_v1_ch1:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
    $ drawer_sis_nerdy = 3
    $ sis_nerdy_evening_scene2_v1 = 1
    $ day_time += 1
    $ sis_nerdy_scene4_v1 = 1
    $ first_sis_nerdy_scene4_v1 = 1
    $ can_sms1_from_sara = 1
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    $ can_hide_windows = False
    jump sister_nerdy_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
