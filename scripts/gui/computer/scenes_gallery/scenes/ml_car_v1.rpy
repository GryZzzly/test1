label mom_car_v1:
    hide screen scenes_gallery
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    scene black
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "(Мама сейчас переодеваеться. Я мог бы подкрасться и подсмотреть!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Линда сейчас переодеваеться. Я мог бы подкрасться и подсмотреть!)"
    scene ml_bedroom_morning_scene5_v1_p1 with dissolve
    MC "(Идеальные формы!)"
    MC "(Черт! У нее невероятная задница. И она выглядит так сексуально на черных высоких каблуках.)"

    scene ml_bedroom_morning_scene5_v1_p2
    MC "(Нет! Она отошла!)"
    MC "(Мне придется подойти ближе, или не увижу больше ничего!)"

    scene ml_bedroom_morning_scene5_v1_p3
    MC "(Похоже, она надевает трусики.)"
    MC "(Я надеялся увидеть ее киску.)"

    scene ml_bedroom_morning_scene5_v1_p4
    MC "(Не плохо! Я могу подсматривать за ней чаще!)"
    MC "(Я, наверное, не должен долго смотреть. Она почти закончила одеваться.)"

    scene ml_bedroom_morning_scene5_v1_p5
    MC "(Она такая потрясающе красивая.)"
    MC "(Похоже, она берет платье из своего шкафа.)"

    scene ml_bedroom_morning_scene5_v1_p6
    MC "(Ладно, она почти закончила - я лучше уйду, прежде чем она заметит, что я подглядываю за ней.)"
    scene ml_bedroom_morning_scene5_v1_p6
    if renpy.loadable("patch.rpy"):
        MC "(Вместо того, чтобы уйти, я мог бы воспользоваться этой возможностью, чтобы поговорить с мамой по поводы работы.)"
        MC "Эй, мам!"
    if not renpy.loadable("patch.rpy"):
        MC "(Вместо того, чтобы уйти, я мог бы воспользоваться этой возможностью, чтобы поговорить с Линдой по поводы работы.)"
        MC "Привет, Линда!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)
    scene ml_bedroom_morning_scene5_v1_p7
    Mom "Привет, сладкий. Я не видела тебя там. Что случилось?"
    if renpy.loadable("patch.rpy"):
        MC "Я разговаривал с папой, и он подумал, что для меня будет лучше зарабатывать деньги самому."
    if not renpy.loadable("patch.rpy"):
        MC "Я разговаривал с Бобом, и он сказал, что для меня будет лучше зарабатывать деньги самому."
    MC "Он сказал, что у тебя есть кое-какая работа для меня?"

    scene ml_bedroom_morning_scene5_v1_p8
    Mom "Хм ... Я не уверена. Я не могу придумать, какую работу я могу тебе предложить."
    MC "Как насчет твоего офисного здания?"
    Mom "Я не уверена."
    if renpy.loadable("patch.rpy"):
        MC "Пожалуйста, мама! Мне действительно нужны деньги. Я не могу просто продолжать умолять папу!"
    if not renpy.loadable("patch.rpy"):
        MC "Пожалуйста, Линда! Мне действительно нужны деньги. Я не могу просто продолжать просить Боба!"

    scene ml_bedroom_morning_scene5_v1_p9
    Mom "Ну, может быть."
    Mom "Есть одна вакансия."
    Mom "Но есть одно условие."

    scene ml_bedroom_morning_scene5_v1_p10
    MC "Замечательно! Какое условие?"
    Mom "Я расскажу тебе позже. Иди за мной."
    MC "Прекрасно!"
    scene black
    $ renpy.sound.play('/sfx/car_start.mp3')
    $ renpy.pause(2, hard = True)

    scene ml_bedroom_morning_scene5_v1_p11
    if renpy.loadable("patch.rpy"):
        MC "Куда мы едем, мам?"
    if not renpy.loadable("patch.rpy"):
        MC "Куда мы едем, Линда?"
    Mom "Еще один поворот и мы приедем. "
    Mom "Это одна из стоянок, рядом с которой я работаю."
    MC "Ага."

    scene ml_bedroom_morning_scene5_v1_p12
    MC "Выглядит довольно пустынно."
    Mom "Никто никогда не приходит сюда, кроме меня."
    Mom "(И отсутствие людей вокруг, важно для того, что я собираюсь сделать.)"

    scene ml_bedroom_morning_scene5_v1_p13
    MC "И что? Каково это условие?"
    Mom "Просто подожди минутку. Мне нужно сначала все спланировать."
    Mom "(Хорошо, ты сможешь. Ты репетировала это в своем уме сто раз!)"

    scene ml_bedroom_morning_scene5_v1_p14
    if renpy.loadable("patch.rpy"):
        MC "Все в порядке, мам? Ты выглядишь немного нервной."
    if not renpy.loadable("patch.rpy"):
        MC "Все в порядке, Линда? Ты выглядишь немного нервной."
    Mom "Я в порядке. Вот что должно произойти."

    scene ml_bedroom_morning_scene5_v1_p15
    Mom "Условие заключается в том, что ты должен просидеть одну минуту как кукла."
    MC "Гм?"
    Mom "Тебе нельзя двигаться. И мы не будем это обсуждать."
    $ ml_bedroom_morning_scene5_v1_label2_menu_q1 = True
    $ ml_bedroom_morning_scene5_v1_label2_menu_q2 = True
    $ ml_bedroom_morning_scene5_v1_label2_menu_q3 = True
    jump ml_bedroom_morning_scene5_v1_label2_menu1r
label ml_bedroom_morning_scene5_v1_label2_menu1r:
    scene ml_bedroom_morning_scene5_v1_p14
    menu:
        "Почему? Я не понимаю." if ml_bedroom_morning_scene5_v1_label2_menu_q1 == True:

            MC "Почему? Я не понимаю, почему я должен так делать, чтобы получить работу."
            Mom "Я не прошу тебя понять - просто условие, которое я изложила."

            $ ml_bedroom_morning_scene5_v1_label2_menu_q1 = False
            if ml_bedroom_morning_scene5_v1_label2_menu_q2 == True and ml_bedroom_morning_scene5_v1_label2_menu_q3 == False:
                jump ml_bedroom_morning_scene5_v1_label2_menu_after1r
            else:
                jump ml_bedroom_morning_scene5_v1_label2_menu1r
        "Что будет, если я открою глаза или зашевелюсь? " if ml_bedroom_morning_scene5_v1_label2_menu_q2 == True:

            MC "Что будет, если я открою глаза или зашевелюсь?"
            scene ml_bedroom_morning_scene5_v1_p15
            Mom "Тогда договор аннулируется, и ты не получишь работу."
            MC "Хорошо…"

            $ ml_bedroom_morning_scene5_v1_label2_menu_q2 = False
            if ml_bedroom_morning_scene5_v1_label2_menu_q1 == True and ml_bedroom_morning_scene5_v1_label2_menu_q3 == False:
                jump ml_bedroom_morning_scene5_v1_label2_menu_after1r
            else:
                jump ml_bedroom_morning_scene5_v1_label2_menu1r
        "Что, если у меня возникнут вопросы после минуты?" if ml_bedroom_morning_scene5_v1_label2_menu_q3 == True:

            MC "Что, если у меня возникнут вопросы после минуты?"
            scene ml_bedroom_morning_scene5_v1_p15
            Mom "Ты просто должен сдержать свое любопытство, потому что, если ты зададашь мне какой-либо вопрос о том, что произошло, ты не получишь эту работу."
            if renpy.loadable("patch.rpy"):
                MC "(Гы... мама очень серьезна.)"
            if not renpy.loadable("patch.rpy"):
                MC "(Боже... Линда довольно серьезно относится к этому.)"

            $ ml_bedroom_morning_scene5_v1_label2_menu_q3 = False
            if ml_bedroom_morning_scene5_v1_label2_menu_q1 == True and ml_bedroom_morning_scene5_v1_label2_menu_q2 == False:
                jump ml_bedroom_morning_scene5_v1_label2_menu_after1r
            else:
                jump ml_bedroom_morning_scene5_v1_label2_menu1r
label ml_bedroom_morning_scene5_v1_label2_menu_after1r:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_bedroom_morning_scene5_v1_p16
    MC "Хорошо - я готов."
    Mom "Минута начинается сейчас. Помни, никаких разговоров, движений или вопросов после."

    scene ml_bedroom_morning_scene5_v1_p17
    MC "(Раз... Два ... Три…)"
    MC "(Она просто положила руку мне на плечо. Ничего особенного…)"
    MC "(Семь ... Восемь ... Девять…)"

    scene ml_bedroom_morning_scene5_v1_p18
    Mom "(Боже ... Он такой красивый.)"
    Mom "(Я должна поцеловать его. Это может быть мой единственный шанс.)"
    if renpy.loadable("patch.rpy"):
        Mom "(Надеюсь, он ничего не скажет отцу об этом.)"
    if not renpy.loadable("patch.rpy"):
        Mom "(Надеюсь, он ничего не скажет Бобу об этом.)"

    scene ml_bedroom_morning_scene5_v1_p19
    Mom "(Вот так ... сейчас или никогда!)"
    MC "(Тринадцать ... Четырнадцать ... Пятнадцать…)"
    MC "(Что она делает?)"

    scene ml_bedroom_morning_scene5_v1_p20
    MC "(О МОЙ БОГ!)"
    scene ml_bedroom_morning_scene5_v1_p20anim with dissolve
    if renpy.loadable("patch.rpy"):
        MC "(Мама целуется со мной!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Линда целуется со мной!)"
    MC "(Я чувствую ее язык во рту, и все такое!)"

    scene ml_bedroom_morning_scene5_v1_p21
    MC "(Я ... Я потерял счет. Было двадцать или тридцать?)"
    scene ml_bedroom_morning_scene5_v1_p21anim with dissolve
    Mom "(Почему я сказала только минуту? Я могла бы сказать две или три…)"
    Mom "(Я желаю, чтобы этот момент длился вечно. Эта мечта сбывается прямо сейчас.)"

    scene ml_bedroom_morning_scene5_v1_p22
    if renpy.loadable("patch.rpy"):
        Mom "(Если я подумаю об этом, когда его отец трахнет меня сегодня вечером, я могла бы даже изминить кульминацию.)"
    if not renpy.loadable("patch.rpy"):
        Mom "(Если я подумаю об этом, когда Боб трахнет меня сегодня вечером, я могла бы даже изминить кульминацию.)"
    Mom "(Я должна сдерживать себя ... но прямо сейчас, я могу просто разорвать одежду [player_name] и трахуть его на сидении автомобиля.)"

    scene ml_bedroom_morning_scene5_v1_p23
    Mom "(Я должна знать, тяжело ли ему. И наслаждаеться ли он так же, как и я…)"
    Mom "(Я просто пошевелю рукой, а затем уберу.)"

    scene ml_bedroom_morning_scene5_v1_p24
    Mom "(Он встал! В этом нет никаких сомнений.)"
    Mom "(Я также чувствую, что у него довольно большой член.)"
    Mom "(Если бы я могла почувствовать его глубоко внутри моей киски!)"
    MC "(Черт возьми! Она взяла меня за член?! Она сделала это нарочно?) "
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)
    scene ml_bedroom_morning_scene5_v1_p25
    Mom "Хорошо, минута закончилась."
    Mom "(Вау... это было... что-то.)"
    MC "Я могу сейчас говорить?"
    Mom "Да, но ты не можешь говорить о том, что случилось."

    scene ml_bedroom_morning_scene5_v1_p26
    MC "Ох... Ладно…"
    if renpy.loadable("patch.rpy"):
        MC "(Зачем ей это делать? Я не понимаю... она моя мать.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Зачем ей это делать? Я не понимаю.)"
    MC "(Я имею в виду, если она влюблена в меня, или что? Но это не имеет смысла.)"
    if renpy.loadable("patch.rpy"):
        MC "(Если миссис Селия не хотела встречаться со мной, как моя собственная мама может быть заинтересована?)"
    if not renpy.loadable("patch.rpy"):
        MC "(Если миссис Селия не хотела встречаться со мной, как она можеть быть заинтересована?)"

    scene ml_bedroom_morning_scene5_v1_p27
    Mom "ГМ... Я работаю в здании, прямо напротив этой парковки."
    Mom "Если ты зайдешь завтра днем, я устрою тебя на работу."
    if renpy.loadable("patch.rpy"):
        MC "Спасибо, Мам."
    if not renpy.loadable("patch.rpy"):
        MC "Спасибо, Линда."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
