image d_ml_and_f_bedroom_mornig_scene_v1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/1.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/2.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/3.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/4.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/5.jpg"
image d_ml_and_f_bedroom_mornig_scene_v1_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/d_ml_and_f_bedroom_mornig_scene_v1/6.jpg"

screen d_ml_and_f_bedroom_mornig_scene_v1_screen:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("d_ml_and_f_bedroom_mornig_scene_v1_screen"),Jump("parents_bedroom_morning1")]
label d_ml_and_f_bedroom_mornig_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if d_ml_and_f_bedroom_mornig_scene_visit == 4 and d__can_ml_and_f_bedroom_mornig_scene == True:
        show screen parents_bedroom_day_notclickable
        show screen d_ml_and_f_bedroom_mornig_scene_v1_screen
        if not renpy.loadable("patch.rpy"):
            $ Dad_name = "Боб"
        Dad "Не сейчас, [player_name]."
        jump parents_bedroom_morning1
    if d__can_ml_and_f_bedroom_mornig_scene == False:
        show screen parents_bedroom_day_notclickable
        show screen d_ml_and_f_bedroom_mornig_scene_v1_screen
        Dad "Не сейчас, [player_name]."
        jump parents_bedroom_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Aces High.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True
    if d_ml_and_f_bedroom_mornig_scene_visit == 1 and d__can_ml_and_f_bedroom_mornig_scene == True:
        if not renpy.loadable("patch.rpy"):
            $ Dad_name = "Боб"
        scene d_ml_and_f_bedroom_mornig_scene_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "ГМ... Эй, Пап, ты сейчас занят?"
        if not renpy.loadable("patch.rpy"):
            MC "ГМ... Эй Боб, ты занят?"
        Dad "Хмм?"

        scene d_ml_and_f_bedroom_mornig_scene_v1_p2
        Dad "О! Привет, чемпион! Ну что, клюет?"
        MC "А?"
        Dad "Что за клев? Это то, что вы, молодые говорите не так ли?"
        MC "Ум... Уверен."

        scene d_ml_and_f_bedroom_mornig_scene_v1_p5
        Dad "Что ты хотел то?"

        menu:
            "{color=#00ff00}Можешь дать мне немного денег?{/color}":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                if renpy.loadable("patch.rpy"):
                    MC "Вообще-то, у меня не хватает денег, пап. Не мог бы ты одолжить мне немного?"
                if not renpy.loadable("patch.rpy"):
                    MC "У меня не хватает наличных, Боб. Не мог бы ты одолжить мне немного?"
                Dad "Хаха! Ты потратили все свои деньги, гуляя с девушками, не так ли?"
                Dad "Сейчас я посмотрю…"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p4
                Dad "Хорошо, вот, пожалуйста. Не трать все сразу!"
                if renpy.loadable("patch.rpy"):
                    MC "Спасибо, Папа!"
                if not renpy.loadable("patch.rpy"):
                    MC "Спасибо, Боб!"
                "+15$"
                $ inventory.earn(15)
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ d_ml_and_f_bedroom_mornig_scene_visit = 2
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
            "Как обстоят дела на работе?":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                MC "Как обстоят дела на работе?"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p6
                Dad "О, боже. С чего начать?!"
                Dad "Эмили, из отдела кадров, только что уволили за продажу частных медицинских данных."
                Dad "Поэтому сейчас я должен провести целую оценку рисков по всему Восточному филиалу компании!"
                MC "Ох, звучит грубо!"
                MC "(Я понятия не имею, как он вообще работает…)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
            "У тебя что-то веселое планируеться?":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                MC "У тебя что-то веселое планируеться?"
                if renpy.loadable("patch.rpy"):
                    Dad "Ничего особенного сегодня. Я помогу твоей маме пропылесосить позже."
                if not renpy.loadable("patch.rpy"):
                    Dad "Ничего особенного сегодня. Я, вероятно, помогу Линде пылесосить."
                Dad "Однако завтра я собираюсь пойти на лекцию о ловле рыбы нахлыстом."
                MC "Э... Вау! Звучит... интересно."
                Dad "Я знаю! На самом деле, знаешь ли ты, что в Тихом океане водиться семь разных видов лосося!"
                MC "Увлекательно. (Боже, лучше выбраться отсюда или изменить тему, прежде чем он продолжмт про рыбалку.)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1

    if d_ml_and_f_bedroom_mornig_scene_visit == 2 and d__can_ml_and_f_bedroom_mornig_scene == True:
        scene d_ml_and_f_bedroom_mornig_scene_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "Эй, пап!"
        if not renpy.loadable("patch.rpy"):
            MC "Эй, Боб!"
        scene d_ml_and_f_bedroom_mornig_scene_v1_p2
        Dad "Привет, чемпион. Что случилось?"
        menu:
            "Как ты на самом деле работаешь?":

                scene d_ml_and_f_bedroom_mornig_scene_v1_p2
                MC "Я только что понял, что на самом деле не знаю, как ты работаешь."
                Dad "Серьезно? Я оценщик рисков компании."
                scene d_ml_and_f_bedroom_mornig_scene_v1_p3
                Dad "Это моя работа - путешествовать по различным сайтам и принимать меры для минимизации риска."
                Dad "Я также отвечаю за управление нашими страховыми полисами для Eastern Business Centres."
                MC "(Черт ... Зачем я спросил.)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
            "{color=#00ff00}Можешь дать мне еще денег?{/color}":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p3
                if renpy.loadable("patch.rpy"):
                    MC "Могу ли я взять еще немного денег, папа?"
                if not renpy.loadable("patch.rpy"):
                    MC "Могу ли я взять еще немного денег, Боб?"
                Dad "Что случилось с деньгами, которые я давал тебе?"
                MC "Ээ ... Мне пришлось потратить их на ... предметы первой необходимости."
                Dad "Черт, школы сегодня дорожают!"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p4
                Dad "У меня не было шанса поехать в банкомат, так что это все, что у меня есть сейчас."
                if renpy.loadable("patch.rpy"):
                    MC "Спасибо папа."
                if not renpy.loadable("patch.rpy"):
                    MC "Спасибо, Боб."
                Dad "Нет проблем, чемпион."
                "+15$"
                $ inventory.earn(15)
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ d_ml_and_f_bedroom_mornig_scene_visit = 3
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
            "Как прошла лекция по рыбалке?":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p3
                MC "Итак, как лекция о рыбалке?"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                Dad "Ты должен был быть там! Это было невероятно!"
                MC "(О Боже ... Я его снова зацепил.)"
                "(Пятнадцать минут спустя…)"
                scene black
                $ renpy.pause()
                scene d_ml_and_f_bedroom_mornig_scene_v1_p2
                Dad "И это был только приглашенный оратор!"
                MC "(Теперь у меня есть шанс окончательно изменить тему беседы!)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1

    if d_ml_and_f_bedroom_mornig_scene_visit == 3 and d__can_ml_and_f_bedroom_mornig_scene == True:
        scene d_ml_and_f_bedroom_mornig_scene_v1_p1 with dissolve
        if renpy.loadable("patch.rpy"):
            MC "Привет папа!"
        if not renpy.loadable("patch.rpy"):
            MC "Привет боб!"
        Dad "Привет, чемпион!"
        scene d_ml_and_f_bedroom_mornig_scene_v1_p2
        Dad "Что я могу сделать для тебя?"
        menu:
            "{color=#00ff00}Могу ли я одолжить еще немного денег?{/color}":


                scene d_ml_and_f_bedroom_mornig_scene_v1_p2
                MC "Могу ли я одолжить еще немного денег?"
                scene d_ml_and_f_bedroom_mornig_scene_v1_p3
                Dad "Гм? Снова?"
                Dad "Ты должен научиться зарабатывать. Плохо постоянно просить."
                scene d_ml_and_f_bedroom_mornig_scene_v1_p6
                if renpy.loadable("patch.rpy"):
                    Dad "Я думаю, твоя мать всегда ищет дополнительных работников. Я уверен, она будет рада заплатить тебе."
                if not renpy.loadable("patch.rpy"):
                    Dad "Я думаю, Линда всегда ищет дополнительных работников. Я уверен, она будет рада заплатить тебе."
                MC "О, ладно. Спасибо."
                scene d_ml_and_f_bedroom_mornig_scene_v1_p5
                Dad "Не смотри так, дружище! Немного тяжелой работы никогда никого не убивал!"
                MC "(Я не совсем уверен, что это абсолютная правда…)"
                $ d__can_ml_and_f_bedroom_mornig_scene = False
                $ d_ml_and_f_bedroom_mornig_scene_visit = 4
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump parents_bedroom_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
