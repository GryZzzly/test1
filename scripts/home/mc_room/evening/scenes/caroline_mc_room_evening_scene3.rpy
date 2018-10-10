image caroline_mc_room_evening_scene3_p1 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/1.jpg"
image caroline_mc_room_evening_scene3_p2 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/2.jpg"
image caroline_mc_room_evening_scene3_p3 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/3.jpg"
image caroline_mc_room_evening_scene3_p4 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/4.jpg"
image caroline_mc_room_evening_scene3_p5 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/5.jpg"
image caroline_mc_room_evening_scene3_p6 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/6.jpg"
image caroline_mc_room_evening_scene3_p7 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/7.jpg"
image caroline_mc_room_evening_scene3_p8 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/8.jpg"
image caroline_mc_room_evening_scene3_p9 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/9.jpg"
image caroline_mc_room_evening_scene3_p10 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/10.jpg"
image caroline_mc_room_evening_scene3_p11 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/11.jpg"
image caroline_mc_room_evening_scene3_p12 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/12.jpg"
image caroline_mc_room_evening_scene3_p13 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/13.jpg"
image caroline_mc_room_evening_scene3_p14 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/14.jpg"
image caroline_mc_room_evening_scene3_p15 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/15.jpg"
image caroline_mc_room_evening_scene3_p16 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/16.jpg"
image caroline_mc_room_evening_scene3_p17 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/17.jpg"
image caroline_mc_room_evening_scene3_p18 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/18.jpg"
image caroline_mc_room_evening_scene3_p19 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/19.jpg"
image caroline_mc_room_evening_scene3_p20 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/20.jpg"
image caroline_mc_room_evening_scene3_p21 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/21.jpg"
image caroline_mc_room_evening_scene3_p22 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/22.jpg"
image caroline_mc_room_evening_scene3_p23 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/23.jpg"
image caroline_mc_room_evening_scene3_p24 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/24.jpg"
image caroline_mc_room_evening_scene3_p25 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/25.jpg"
image caroline_mc_room_evening_scene3_p25a = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/25a.jpg"
image caroline_mc_room_evening_scene3_p26 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/26.jpg"
image caroline_mc_room_evening_scene3_p27 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/27.jpg"
image caroline_mc_room_evening_scene3_p28 = "images/home/mc_room/evening/scenes/caroline_mc_room_evening_scene3/28.jpg"

image caroline_mc_room_evening_scene3_p14anim = Movie(play="videos/Caroline-EveningS3-Violet2.webm", loop = True )
image caroline_mc_room_evening_scene3_p21anim = Movie(play="videos/Caroline-EveninS3-3.webm", loop = True )
image caroline_mc_room_evening_scene3_p24anim = Movie(play="videos/Caroline-EveninS3-2.webm", loop = True )
label caroline_mc_room_evening_scene3_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_mc_room_evening_scene3_p1 at pandown3
    $ can_hide_windows = True
    MC "О! Привет, Кэролайн. Что ты делаешь в моей комнате?"
    MC "И кто это?"
    Caroline "Привет [player_name]! Я хочу, чтобы ты познакомился с Виолеттой!"
    Violet "Привет."
    Caroline "Я обещала тебе сюрприз - так Виолетта собирается помочь тебе снять часть стресса, который я создала."

    scene caroline_mc_room_evening_scene3_p2
    MC "Ты привела проститутку в мою спальню!?"
    Violet "Что?!"
    Caroline "Ахахахах! Боже мой! Прости, Виолетта!"

    scene caroline_mc_room_evening_scene3_p3
    Violet "Да пошёл ты! Я не какая-то шлюха!"
    Violet "Кэролайн договорилась со мной-она должна поможет мне, если я помогу тебе расслабиться."
    MC "Да? Как? Массаж?"

    scene caroline_mc_room_evening_scene3_p4
    Caroline "Она не проститутка. Она одна из моих подруг."
    Caroline "Я договорилась с ней-я помогу ей в обмен на то, что она сейчас сделает."
    MC "Что сделает?"

    scene caroline_mc_room_evening_scene3_p5
    Caroline "Ты серьезно? Она ублажает тебя!"
    MC "ОЙ!"
    MC "Прости, Виолетта! Я не понял."
    Caroline "Теперь я оставлю вас вдвоем. Повеселись!"

    scene caroline_mc_room_evening_scene3_p6 at pandown3
    Violet "Увидимся позже, Кэролайн. Подойди ко мне, [player_name]."
    MC "Что ты собираешься делать?"
    MC "Хочу... секс? Или анал?"

    scene caroline_mc_room_evening_scene3_p7
    Violet "Все будет немного не так."
    Violet "Я лягу на кровати и позволю тебе трахнуть мой рот."
    MC "Замечательно!"

    scene caroline_mc_room_evening_scene3_p8
    Violet "Что ж? Ты готов? У меня есть место для разгона."
    MC "Уверена!"
    if renpy.loadable("patch.rpy"):
        MC "Какую сделку вы заключили, кстати?"
    if not renpy.loadable("patch.rpy"):
        MC "Какую сделку вы заключили с Сарой, кстати?"
    Violet "Она мне должна. Я, в конечном итоге заставляю ее сосать одного из моих друзей-мужчин, просто для оценки."

    scene caroline_mc_room_evening_scene3_p9
    Violet "Хорошо - давайте начнем веселье."
    Violet "Поначалу тебе покажется сложно."
    MC "(Она ДЕЙСТВИТЕЛЬНО сексуальна! У Кэролайн хороший вкус на друзей!)"
    MC "(Посмотрим, насколько она распутная!)"

    scene caroline_mc_room_evening_scene3_p10
    Violet "Aхх…."
    MC "Oooх…"
    MC "(Я чувствую ее язык, облизывающий кончик моего члена.)"
    MC "(Она явно делала минет не один раз.)"

    scene caroline_mc_room_evening_scene3_p11
    MC "(Фотографировать для Кэролайн, должно быть одно из лучших решений, которые я сделал в течение всего года!)"
    MC "(Я никогда не думал, что это закончится минетом от шлюхи!)"

    scene caroline_mc_room_evening_scene3_p12
    Violet "А, Ну вот и все. Теперь мы можем начать."
    MC "Я знаю, что ты сказали быстрый минет, могу я трахнуть тебя в между сисек?"
    Violet "(Вздыхает) Хорошо."

    scene caroline_mc_room_evening_scene3_p13
    MC "Потрясающие! "
    Violet "Мне нужно держать грудь вместе?"
    MC "Могла бы?"
    Violet "Конечно."

    scene caroline_mc_room_evening_scene3_p14
    Violet "Так нормально?"
    MC "Гораздо лучше!"
    scene caroline_mc_room_evening_scene3_p14anim with dissolve
    $ renpy.pause()
    MC "(Я чувствую ее теплую грудь, обернутую вокруг моего члена!)"

    scene caroline_mc_room_evening_scene3_p15 with dissolve
    Violet "(Тьфу! Сколько времени этот маленький болван собирается это делать?)"
    Violet "(Я думаю, мои сиськи достаточно хороши, но возможно я должна буду помочь ему?)"

    scene caroline_mc_room_evening_scene3_p16
    MC "OOOХХХ!"
    MC "(Черт побери! Она облизывает мою задницу! Я никогда не предполагал, что это будет настолько чувствительно!)"
    MC "(Дерьмо! Если она продолжит, я кончу раньше минета!)"

    scene caroline_mc_room_evening_scene3_p17
    MC "(Я постараюсь потерпеть некоторое время - он чувствует себя потрясающе!)"
    Violet "(Время сжать мои груди немного ближе друг к другу. Посмотрим, сможет ли он кончить, прежде чем я перейду к минету.)"
    MC "Aхх… Oхх…"

    scene caroline_mc_room_evening_scene3_p18
    MC "Господи, да! ААА... Ебать!"
    Violet "(Пора повертеть языком еще быстрее.)"
    MC "Aхххх! OХ! OХ OХ!!!"

    scene caroline_mc_room_evening_scene3_p19
    MC "(Между ее грудью и языком, лижущим мою задницу я чувствую, что я собираюсь кончить!)"
    MC "(я должен прекратить это. Пора перейти к минету!)"
    MC "Хорошо, ээ - достаточно. Я хочу, чтобы ты взяла в рот."
    Violet "Тьфу! Хорошо."

    scene caroline_mc_room_evening_scene3_p20
    Violet "(Сосет сосет)"
    MC "Oooхх - вот это познания!"
    MC "(Я больше не могу сдерживаться. Мне нужен минет!)"

    scene caroline_mc_room_evening_scene3_p21
    Violet "ФУУУХХХ!"
    scene caroline_mc_room_evening_scene3_p21anim with dissolve
    Violet "(Черт! Я не ожидал, что он засунет свой член в мой рот так глубоко!)"
    MC "Ooo да!"

    scene caroline_mc_room_evening_scene3_p22
    MC "Черт, ты отличный сосеш. Ты знаешь?"
    Violet "(Это всего лишь комплимент, который девушка хочет услышать от парня, которого она только что встретила…)"
    Violet "Mммм…."

    scene caroline_mc_room_evening_scene3_p23
    MC "Aхх, ебать ... Я скоро кончу!"
    Violet "(По крайней мере, он предупредил меня. Это больше, чем я могу сказать про любого из моих бывших.)"

    scene caroline_mc_room_evening_scene3_p24
    MC "Aх! Ох! Да!"
    Violet "(Shlurp)"
    scene caroline_mc_room_evening_scene3_p24anim with dissolve
    Violet "(Сосет, сосет)"
    MC "Я кончаю!"

    scene caroline_mc_room_evening_scene3_p25
    MC "Открой пошире!"
    MC "Aхх! Да!"
    Violet "(Я все больше убеждаюсь, что долг Кэролайн будет того стоить!)"

    scene caroline_mc_room_evening_scene3_p25a
    MC "Ухх! Aхххх!"
    MC "(пыхтит... ) Oooхх…."
    MC "Тебе нужно куда то сплюнуть?"
    Violet "(Глоток!)"
    MC "Или ти можешь сделать и так."

    scene caroline_mc_room_evening_scene3_p26
    Violet "Итак, Кэролайн рассказывала мне, у тебя стоит, глядя на нее. Это правда?"
    MC "Э-э ... Да, но это не полная история."
    Violet "Какова история тогда?"
    MC "Она была одета в сексуальный костюм. У парней нет никакого контроля над его членом, в такой ситуации. Поэтому я не могу сказать, что это моя вина."
    Violet "Эх ... справедливо."
    Violet "Еще один вопрос - тебе больше нравлюсь я или Кэролайн??"

    scene caroline_mc_room_evening_scene3_p27
    if renpy.loadable("patch.rpy"):
        MC "Давай я не буду отвечать. Она моя сестра."
    if not renpy.loadable("patch.rpy"):
        MC "Давай я не буду отвечать. Она мой друг."
    Violet "Уверена, что ты можешь!"
    MC "(Вздох…) Ты горячая, но... Кэролайн больше мне по вкусу. Она действительно великолепна."

    scene caroline_mc_room_evening_scene3_p28
    Caroline "(Вздох!)"
    if renpy.loadable("patch.rpy"):
        Caroline "([player_name] на самом деле.... Я не просто одела этот костюм!)"
    if not renpy.loadable("patch.rpy"):
        Caroline "(Мой друг на самом деле … привлекает меня. Я не просто одела этот костюм!)"
    Caroline "(Какого черта я должна сейчас делать? Будет ли это правильно, чтобы он продолжал фотографировать меня? Или это просто мучает его?)"
    $ caroline_mc_room_evening_scene3 = False
    $ violet_bath_event_unlock = True
    $ unlock_caroline_closth_shop_afternoon_scene3 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
