image MLR2_MS1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/1.jpg"
image MLR2_MS1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/2.jpg"


image MLR2_MS1_talk_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/1.jpg"
image MLR2_MS1_talk_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/2.jpg"
image MLR2_MS1_talk_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/3.jpg"
image MLR2_MS1_talk_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/4.jpg"
image MLR2_MS1_talk_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/5.jpg"
image MLR2_MS1_talk_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/6.jpg"
image MLR2_MS1_talk_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/7.jpg"
image MLR2_MS1_talk_p8 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Talk/8.jpg"


image MLR2_MS1_kiss_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/1.jpg"
image MLR2_MS1_kiss_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/2.jpg"
image MLR2_MS1_kiss_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/3.jpg"
image MLR2_MS1_kiss_p4a = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/4a.jpg"
image MLR2_MS1_kiss_p4b = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/4b.jpg"
image MLR2_MS1_kiss_p4c = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/4c.jpg"
image MLR2_MS1_kiss_p5a = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/5a.jpg"
image MLR2_MS1_kiss_p5b = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/5b.jpg"
image MLR2_MS1_kiss_p5c = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/5c.jpg"
image MLR2_MS1_kiss_p5d = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/5d.jpg"
image MLR2_MS1_kiss_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Kiss/6.jpg"

image MLR2_MS1_Bob_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Bob/1.jpg"
image MLR2_MS1_Bob_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Bob/2.jpg"
image MLR2_MS1_Bob_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/MLR2_MS1/Bob/3.jpg"

default can_MLR2_MS1_talk = True
default MLR2_MS1_talk_count = 1
default MLR2_MS1_kiss_count = 1
default can_MLR2_MS1_kiss = True
default MLR2_MS1_NS1 = False
default MLR2_MS1_ES3 = False
default MLR2_MS1_BCalendar = False
default MLR2_MS1_visit = 1
label MLR2_MS1_label:
    if MLR2_can_MS1 == False:
        show screen parents_bedroom_morning_notclickable
        MC "Я уже говорил с ней."
        hide screen parents_bedroom_morning_notclickable
        $ can_hide_windows = False
        jump parents_bedroom_morning1
    else:
        $ can_hide_windows = True
        if MLR2_MS1_visit == 2:
            hide screen week_day_viewer
            hide screen time_skip_button
            hide screen day_time_viewer
            hide screen map_button
            scene MLR2_MS1_p2

            Mom "Доброе утро, милый. Что случилось?"
            jump MLR2_MS1_menu
        if MLR2_MS1_visit == 1:
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
            hide screen week_day_viewer
            hide screen time_skip_button
            hide screen day_time_viewer
            hide screen map_button

            scene MLR2_MS1_p1 with dissolve
            if renpy.loadable("patch.rpy"):
                MC "(Черт, мама выглядит горячей в этом черном белье.)"
                MC "Доброе Утро, Мама! Хорошо выглядишь!"
            else:

                MC "(Черт, Линда выглядит горячей в этом черном белье.)"
                MC "Доброе Утро, Линда! Хорошо выглядишь!"



            scene MLR2_MS1_p2

            Mom "Доброе утро, милый. Что случилось?"
            $ MLR2_MS1_visit += 1
            jump MLR2_MS1_menu

label MLR2_MS1_menu:
    window hide
    menu:

        "{color=#00ff00}Поговорить с мамой.{/color}" if renpy.loadable("patch.rpy") and can_MLR2_MS1_talk == True and MLR2_MS1_talk_count < 4:
            jump MLR2_MS1_talk_label

        "Поговорить с Линдой." if not renpy.loadable("patch.rpy") and can_MLR2_MS1_talk == True and MLR2_MS1_talk_count < 4:
            jump MLR2_MS1_talk_label

        "{color=#00ff00}Попросить поцелуй. {/color}" if can_MLR2_MS1_kiss == True and MLR2_MS1_kiss_count == 1:
            jump MLR2_MS1_kiss_label
        "Попросить поцелуй." if can_MLR2_MS1_kiss == True and MLR2_MS1_kiss_count == 2:
            jump MLR2_MS1_kiss_label

        "{color=#00ff00}Говорить о папе.{/color}" if renpy.loadable("patch.rpy") and MLR2_MS1_NS1 == True:
            jump MLR2_MS1_Bob_label
        "{color=#00ff00}Говорить о Бобе.{/color}" if not renpy.loadable("patch.rpy") and MLR2_MS1_NS1 == True:
            jump MLR2_MS1_Bob_label



        "{color=#00ff00}Говорить о папе.{/color} " if renpy.loadable("patch.rpy") and MLR2_MS1_ES3 == True and can_MLR2_MS1_ES3 == True:
            jump MLR2_MS1_Bob_Trip_label
        "{color=#00ff00}Говорить о Бобе.{/color} " if not renpy.loadable("patch.rpy") and MLR2_MS1_ES3 == True and can_MLR2_MS1_ES3 == True:
            jump MLR2_MS1_Bob_Trip_label


        "Говорить о папе.. (недоступно)" if renpy.loadable("patch.rpy") and MLR2_MS1_ES3 == True and can_MLR2_MS1_ES3 == False:
            jump MLR2_MS1_Bob_Trip_label
        "Говорить о Бобе. (недоступно)" if not renpy.loadable("patch.rpy") and MLR2_MS1_ES3 == True and can_MLR2_MS1_ES3 == False:
            jump MLR2_MS1_Bob_Trip_label





        "{color=#00ff00}Разговоры о папиной поездке.{/color}" if renpy.loadable("patch.rpy") and MLR2_MS1_BCalendar == True and MLR2_MS1_ES3 == 3:
            jump MLR2_MS1_Bob_Trip2_label
        "{color=#00ff00}Разговоры о поездке Боба.{/color}" if not renpy.loadable("patch.rpy") and MLR2_MS1_BCalendar == True and MLR2_MS1_ES3 == 3:
            jump MLR2_MS1_Bob_Trip2_label
        "Bye ":



            jump MLR2_MS1_Cancel_label
label MLR2_MS1_talk_label:
    if MLR2_MS1_talk_count == 1:
        scene MLR2_MS1_talk_p1
        if renpy.loadable("patch.rpy"):
            MC "Ничего особенного, мам. Я просто зашел, поздороваться."
        else:
            MC "Ничего особенного, Линда. Я просто зашел, поздороваться."
        Mom "ОУ, это любезно с твоей стороны."
        Mom "Хочешь кофе? Я думаю, что есть еще в чайнике."

        scene MLR2_MS1_talk_p2

        MC "Нет, спасибо."
        Mom "Как обстоят дела с Сарой? Вы гуляете вместе?"

        scene MLR2_MS1_talk_p3
        if Sara_points >=2:

            MC "(Вот черт! Она ни за что не должна узнать, что мы с Сарой встречаемся...)"
            MC "(Нужно быстро придумать оправдание..)"
            MC "Да, мы тусовались вместе... Я понял, что проводил мало времени с Сарой, когда был моложе, поэтому я пытаюсь компенсировать это сейчас."

            scene MLR2_MS1_talk_p2

            Mom "О, это очень мило. Я рада, что вы хорошо ладите."
        if Sara_points ==1:

            MC "Приключения? Я хочу."
            MC "Это просто была постоянная работа в школе."

            scene MLR2_MS1_talk_p4
            if renpy.loadable("patch.rpy"):
                Mom "Тебе стоит подумать о том, чтобы проводить больше времени со своей младшей сестрой. Она действительно интересуется тобой?"
                MC "Знаю-знаю. Я просто очень занят сейчас, мама."
            if not renpy.loadable("patch.rpy"):
                Mom "Тебе стоит подумать о том, чтобы проводить больше времени с Сарой. Она действительно интересуется тобой?"
                MC "Знаю-знаю. Я просто очень занят сейчас, Линда."
        $ MLR2_MS1_talk_count = 2
        $ can_MLR2_MS1_talk = False
        jump MLR2_MS1_menu

    if MLR2_MS1_talk_count == 2:
        scene MLR2_MS1_talk_p1
        if renpy.loadable("patch.rpy"):
            MC "Занята, как обычно, мам?"
        if not renpy.loadable("patch.rpy"):
            MC "Занята, как обычно, Линда.."
        MC "Как я вижу, постельная работа?"

        scene MLR2_MS1_talk_p6

        Mom "Ха-ха! Ты поймал меня. Да, я просто проверяю наши европейские счета."
        MC "Что-нибудь интересное?"

        scene MLR2_MS1_talk_p8

        Mom "Нет, если ты заинтересован правилами внутреннего рынка Европейского союза."
        MC "Ну, я не думаю нет."

        scene MLR2_MS1_talk_p2

        Mom "Говоря о работое Кэролайн кажется открыла перспективный магазин."
        Mom "Надеюсь, ты не слишком отвлекаешь ее, когда посещаешь ее магазин."
        if Caroline_points >= 2:

            MC "(Ох! )Я надеюсь она не догадалась о наших странных отношениях"
            MC "Я ... Э ... Нет! Нет, я не отвлекаю ее."
            MC "Во всяком случае, она отвлекает меня!"

            scene MLR2_MS1_talk_p8

            Mom "А? Что это значит?"
            MC "(Блядь!)"
            MC "Я ... э-э ... я имею в виду ... она отвлекает ... вдохновляет меня, чтобы начать ... собственный бизнес."

            scene MLR2_MS1_talk_p4

            Mom "Тогда хорошо…"
            Mom "Я думаю, это нормально, если ты не слишком беспокоишь ее."
            MC "(Ху! Уклонился от пули!)"

        if Caroline_points == 1:

            MC "Честно? Я слишком занят, чтобы реально помочь ей в этом."
            Mom "Это понятно. Ваши школьные исследования действительно на первом месте."
            MC "Да, это правда."

        scene MLR2_MS1_talk_p1

        Mom "Я знаю, что вы оба заняты, но старайтесь находить время друг для друга."
        Mom "Друзья приходят и уходят - но твои братья и сестры остаются с нами на всю свою жизнь."
        if renpy.loadable("patch.rpy"):
            MC "Окей мам. Я буду иметь это в виду."
        if not renpy.loadable("patch.rpy"):
            MC "Хорошо, Линда. Я буду иметь это в виду."

        $ MLR2_MS1_talk_count = 3
        $ can_MLR2_MS1_talk = False
        jump MLR2_MS1_menu

    if MLR2_MS1_talk_count == 3:
        scene MLR2_MS1_talk_p1
        if renpy.loadable("patch.rpy"):
            MC "Э-э, я в порядке. Немного беспокоился о папе, если честно."
        else:
            MC "Э-э, я в порядке. Честно говоря, был немного обеспокоен Бобом."
        scene MLR2_MS1_talk_p4

        Mom "Волновался? Что-то случилось? Он что-то сказал тебе?"
        MC "Нет! Нет! Еще … я просто не взволнован по поводу того, чтобы не попасться."
        Mom "Ну, я не думаю, что у тебя есть повод, чтобы быть взволнованными."
        Mom "Если мы..."

        "((Бинго! Одно новое письмо!))"

        scene MLR2_MS1_talk_p7

        Mom "Извините, это мне. Мы можем поговорить позже?"
        if renpy.loadable("patch.rpy"):
            MC "Конечно, Мама."
        else:
            MC "Конечно, Линда."
        $ MLR2_MS1_talk_count = 4
        $ can_MLR2_MS1_talk = False
        jump MLR2_MS1_menu

label MLR2_MS1_kiss_label:

    if renpy.loadable("patch.rpy"):
        MC "Могу я поцеловать тебя, мама?"
    else:
        MC "Могу я поцеловать тебя, Линда?"
    scene MLR2_MS1_kiss_p1
    Mom "Конечно, милый. Ты не должен спрашивать?"
    MC "Я не должен?"
    Mom "Нисколько. Я хочу, чтобы ты поцеловал меня."
    Mom "Вы можете делать что угодно, касающееся меня. Хотите дотронуться до моей задницы или схватить мои сиськи, вперед!"
    Mom "Действуй уверенно. Девушки любят это."
    MC "Мне можно не спрашивать разрешения?"
    Mom "Конечно можно. Я разрешаю тебе."

    scene MLR2_MS1_kiss_p2

    Mom "А теперь заткнись и поцелуй меня."
    if renpy.loadable("patch.rpy"):
        MC "(Ладно, похоже, мама действительно хочет, чтобы я вел себя более доминирующе в этих отношениях.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Похоже, Линда действительно хочет, чтобы я вел себя более доминирующе в этих отношениях.)"

    MC "(Или, может быть, просто более уверенно? Я никогда не встречался с девушкой раньше.)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)

    scene MLR2_MS1_kiss_p3

    Mom "Mмм…"
    MC "Mмм!"
    MC "(Интересно, если я должен быть более уверенним, я могу попытаться взять ее за сиськи или задницу, пока мы целуемся?)"
    window hide
    menu:
        "Взять ее за грудь.":
            scene MLR2_MS1_kiss_p5a
            if renpy.loadable("patch.rpy"):
                MC "(Я сожму сиськи мамы и посмотрю, как она наслаждается.)"
            if not renpy.loadable("patch.rpy"):
                MC "(Я сожму сиськи Линды и посмотрю, как она наслаждается.)"
            MC "(У нее хорошая грудь - моя бедная сестра не унаследовала эти гены!)"

            scene MLR2_MS1_kiss_p5b

            MC "(Теперь мои руки покоятся на ее груди. Время сильнее сжать)"
            MC "(Я слышал, что у девочек очень чувствительная грудь-интересно, будет ли мама чувствовать удовольствие, если я буду сжимать их, пока я с ней целуюсь?)"

            scene MLR2_MS1_kiss_p5c

            Mom "Mммммм!"
            MC "(Вот и ответ на вопрос!)"
            Mom "(Да! Похоже, он наконец-то обрел немного уверенности!)"
            jump after_menu_MLR2_MS1_kiss
        "Взять ее за задницу.":

            scene MLR2_MS1_kiss_p4a

            MC "(Давай схватим ее за задницу и посмотрим, как она реагирует.)"
            MC "(На ней нет штанов, так что у меня есть отличная возможность почувствовать ее попку.)"

            scene MLR2_MS1_kiss_p4b

            Mom "Mмм!"
            MC "(Похоже, ей это нравится! Давай сожмем крепче!)"
            Mom "(Да! Похоже, он наконец-то начинает понимать, как обращаться с женщиной!)"

            scene MLR2_MS1_kiss_p4c

            Mom "Oooххммммм!"
            MC "(Да, я в восторге от этого багатства! Захватить ее задницу было правильным решением!)"
            jump after_menu_MLR2_MS1_kiss

label after_menu_MLR2_MS1_kiss:
    scene MLR2_MS1_kiss_p5d

    MC "Mмм…"
    Mom "Mмм!"
    Mom "(О, Боже ... Если я продолжу это, я потеряю все утро!)"

    scene MLR2_MS1_kiss_p6

    Mom "Ладно, пора остановиться. Ха-ха! У меня есть работа."
    Mom "Ты можешь быть ОЧЕНЬ отвлекающими?"
    MC "Сожалею. Виноват. Ха-ха!"
    Mom "Помни, что я сказала, хорошо? Ты должен быть более уверенным со мной."
    Mom "Делайте то, что хочешь - но если не уверен, пожалуйста, спроси. Здоровые сексуальные отношения основаны на открытости и честности."
    Mom "(Какой-то отличный совет от друга прямо!)"
    if renpy.loadable("patch.rpy"):
        MC "Окей мам. Спасибо, что сказала."
    if not renpy.loadable("patch.rpy"):
        MC "Ладно, Линда. Спасибо, что сказала."
    $ can_MLR2_MS1_kiss = False
    if MLR2_MS1_kiss_count == 1:
        $ MLR2_ES1 = True
        $ MLR2_MS1_kiss_count = 2
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
        jump MLR2_MS1_menu
    $ MLR2_MS1_kiss_count = 2
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    jump MLR2_MS1_menu

label MLR2_MS1_Bob_label:
    scene MLR2_MS1_talk_p2
    if renpy.loadable("patch.rpy"):
        MC "Можем ли мы поговорить о папе?"
    else:
        MC "Можем ли мы поговорить о Бобе?"
    Mom "Хмм? Конечно, что у него?"
    MC "Это о вас ... занимающихся сексом каждую ночь."

    scene MLR2_MS1_talk_p4
    Mom "О верно..."
    Mom "Это заставляет ревновать, что я все еще с ним сплю?"

    window hide
    menu:
        "Нет, совсем нет.":


            scene MLR2_MS1_talk_p4

            MC "Честно говоря, меня это совсем не беспокоит."

            scene MLR2_MS1_talk_p8
            if renpy.loadable("patch.rpy"):
                Mom "Так что ... это не беспокоит тебя, что я занимаюсь сексом с мужем ... но ты хотел поговорить об этом?"
            else:
                Mom "Так что ... это не беспокоит тебя, что я занимаюсь сексом с Бобом ... но ты хотел поговорить об этом?"
            MC "Ухх…"
            Mom "Ты нас видишь?"
            MC "Вроде…"

            scene MLR2_MS1_talk_p2

            Mom "В любом случае, ты говоришь, что не беспокоишься, но я не собираюсь снова заниматься с ним сексом."
            Mom "Я не знаю, успокоишся ты или нет."
            MC "Действительно? Почему?"
            Mom "Мы просто не трахаемся, как раньше."
            jump after_menu_MLR2_MS1_Bob_label
        "Да, это действительно так.":


            scene MLR2_MS1_talk_p4

            MC "Да, это действительно заставляет меня чувствовать... я не знаю."
            Mom "Ревновать?"
            MC "Да, наверное."

            scene MLR2_MS1_talk_p2

            Mom "Ну, в этом случае я могу обещать не сделать что-либо некоторое время."
            Mom "Но мы не можем оставить это как нерешенную проблему навсегда."
            MC "Да, я понимаю."
            Mom "Хорошо. Это показывает реальную зрелость, с твоей стороны."
            jump after_menu_MLR2_MS1_Bob_label
        "Это не беспокоит меня слишком.":

            scene MLR2_MS1_talk_p2

            MC "Честно? Это не беспокоит меня слишком сильно."

            scene MLR2_MS1_talk_p8

            Mom "Действительно?"
            MC "Может быть, немного - но не достаточно, чтобы расстраивать меня."
            Mom "Хммм…"

            scene MLR2_MS1_talk_p2

            Mom "Я могу попробовать не заниматься с ним сексом и посмотреть, как ты себя чувствуешь."
            Mom "Очевидно, что это не может продолжаться вечно, и нам нужно будет его пересмотреть. Но это может помочь тебе решить, чего ты хочешь."
            if renpy.loadable("patch.rpy"):
                MC "Спасибо, мама."
            else:
                MC "Спасибо, Линда."
            jump after_menu_MLR2_MS1_Bob_label

label after_menu_MLR2_MS1_Bob_label:
    scene MLR2_MS1_talk_p8

    Mom "И последнее..."
    if renpy.loadable("patch.rpy"):
        Mom "Откуда ты знаешь, что я все еще занимаюсь сексом с твоим отцом? Наши отношения не такие страстные в последнее время."
    else:
        Mom "Как ты узнал, что я все еще занимаюсь сексом с Бобом? Наши отношения не так уж велики в последнее время."
    MC "Я ... мм…"
    Mom "Ты шпионил за нами, не так ли?"
    MC "Ах... я... ЭМ... просто догадка!"

    scene MLR2_MS1_talk_p4

    Mom "Угу. Конечно."
    $ MLR2_MS1_NS1 = 3
    $ MLR2_NS2 = True
    jump MLR2_MS1_menu


label MLR2_MS1_Bob_Trip_label:
    scene MLR2_MS1_Bob_p1

    MC "Ты помнишь, о чем мы говорили в машине?"
    Mom "Мы много о чем говорили."

    if renpy.loadable("patch.rpy"):
        MC "О том, что мы проводим больше романтического времени вместе."
    else:
        MC "О том, что мы проводим больше романтического времени вместе."
    MC "Также в ту ночь. Где ты поймал меня в своей комнате, и мы сделали ... некоторые ... вещи ..."
    Mom "Я знаю... Он всегда был рядом... Остановить нас."

    scene MLR2_MS1_Bob_p2
    if renpy.loadable("patch.rpy"):
        Mom "Если подумать... у меня есть идея. Сможешь ли ты проникнуть на рабочее место твоего отца и проверить его календарь?"
    else:
        Mom "Если подумать... у меня есть идея. Сможешь ли ты проникнуть на рабочее место Боба и проверить его календарь?"
    MC "Зачем?"
    Mom "Мы можем узнать, когда он отправится в другую командировку."
    MC "Ааа! И тогда у нас будет время для себя!"

    scene MLR2_MS1_Bob_p3

    Mom "Бинго!"
    MC "Почему ты не можешь сделать это?"
    if renpy.loadable("patch.rpy"):
        Mom "Он просто подозрительный. Когда брак медленно терпит неудачу-такие вещи, как проверка расписания твоего партнера, становится предупреждающим знаком."
    else:
        Mom "Он просто подозрителен. Когда дружба медленно терпит неудачу-такие вещи, как проверка расписания твоего друга, становится предупреждающим знаком."
    Mom "А потом, когда он уедет, у нас будет замечательная двуспальная кровать.."
    Mom "Так ты сделаешь это, милый?"
    MC "Конечно!"
    Mom "Идеально! Ты помнишь, где он работает?"
    MC "Это большое здание под пляжем?"
    Mom "Да."
    MC "Я позабочусь об этом. Обещаю."

    scene MLR2_MS1_kiss_p2

    MC "(Вау! Это появилось из ниоткуда!)"
    Mom "Mwah!"

    scene MLR2_MS1_Bob_p3

    Mom "Ладно, мне нужно успокоиться и сконцентрироваться. Мне нужно работать."
    MC "Тогда я не буду тебя отвлекать!"
    Mom "Хаха! Ты всегда меня отвлекаешь, милый."
    $ MLR2_MS1_ES3 = 3

    $ Bob_workplace_unlocked = True
    $ Bob_v2_scenes = True
    jump MLR2_MS1_menu

label MLR2_MS1_Bob_Trip2_label:
    scene MLR2_MS1_talk_p1
    if renpy.loadable("patch.rpy"):
        MC "Мама! Хорошие новости! Папа скоро уедет в командировку!"
    else:
        MC "Мама! Хорошие новости! Скоро Боб отправляется в командировку!"
    Mom "Отлично! Как скоро?"
    MC "В эти выходные!"

    scene MLR2_MS1_Bob_p3

    Mom "Блестяще! Я не могу дождаться!"
    Mom "Хорошо, так вот план. Ты придешь ко мне в спальню, как только он уйдет."
    Mom "Тогда мы проведем ночь, занимаясь любовью в моей постели!"
    Mom "Я не чувствовала такого возбуждения с тех пор, как была подростком!"

    scene MLR2_MS1_Bob_p2

    MC "Если я принесу тебе подарок или презент?"
    Mom "Просто немного красного вина. Это было бы прекрасно."

    scene MLR2_MS1_Bob_p3
    if renpy.loadable("patch.rpy"):
        MC "Хорошо, мама. Я удостоверюсь, что сделал это."
    else:
        MC "Хорошо, Линда. Я удостоверюсь, что сделал это."
    Mom "Ура! Это будет лучшая ночь в моей жизни!"
    MC "(Ой! Я никогда не видел никого так возбужденного как сейчас. Она, как ребенок на Рождество!)"
    $ MLR2_MS1_BCalendar = 3
    $ MLR2_weekend_event = True
    jump MLR2_MS1_menu

label MLR2_MS1_Cancel_label:
    scene MLR2_MS1_p2

    Mom "Итак, ты хочешь, чтобы я пришла в твою комнату вечером?"

    window hide
    menu:
        "Да":

            MC "Да, пожалуйста!"
            Mom "Хорошо, увидимся сегодня вечером, дорогой."

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ MLR2_Sleep = False
            $ MLR2_can_MS1 = False
            $ can_hide_windows = False
            jump parents_bedroom_morning1
        "Не сегодня.":

            MC "Не сегодня. Я немного устал, мам."
            Mom " Это нормально. Я понимаю. Надеюсь, завтра ты передумаешь."
            $ MLR2_Sleep = True
            $ MLR2_can_MS1 = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump parents_bedroom_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
