image mc_sara_night_scene1_v1_p1 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/1.jpg"
image mc_sara_night_scene1_v1_p2 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/2.jpg"
image mc_sara_night_scene1_v1_p3 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/3.jpg"
image mc_sara_night_scene1_v1_p4 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/4.jpg"
image mc_sara_night_scene1_v1_p5 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/5.jpg"
image mc_sara_night_scene1_v1_p6 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/6.jpg"
image mc_sara_night_scene1_v1_p7 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/7.jpg"
image mc_sara_night_scene1_v1_p8 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/8.jpg"
image mc_sara_night_scene1_v1_p9 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/9.jpg"
image mc_sara_night_scene1_v1_p10 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/10.jpg"
image mc_sara_night_scene1_v1_p11 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/11.jpg"
image mc_sara_night_scene1_v1_p12 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/12.jpg"
image mc_sara_night_scene1_v1_p13 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/13.jpg"
image mc_sara_night_scene1_v1_p14 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/14.jpg"
image mc_sara_night_scene1_v1_p15 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/15.jpg"
image mc_sara_night_scene1_v1_p16a = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/16a.jpg"
image mc_sara_night_scene1_v1_p17 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/17.jpg"
image mc_sara_night_scene1_v1_p18 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/18.jpg"
image mc_sara_night_scene1_v1_p19 = "images/home/mc_room/night/scenes/scene1_mc_sara_v1/19.jpg"

label mc_sara_night_scene1_v1_label:
    $ renpy.hide("mc_sleep_morning", layer="screens")
    $ renpy.hide("mc_sleep_day", layer="screens")
    $ renpy.hide("mc_sleep_evening", layer="screens")
    $ renpy.hide("mc_sleep_night", layer="screens")
    hide screen mc_room_morning_notclickable
    hide screen mc_room_day_notclickable
    hide screen mc_room_night_notclickable
    hide screen mc_room_evening_notclickable
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene black
    $ renpy.pause(2, hard = True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)

    scene mc_sara_night_scene1_v1_p1 with dissolve
    $ can_hide_windows = True
    Sara "…"
    Sara "(Интересно, он спит?)"
    Sara "[player_name]? Ты спишь?"
    MC "…"

    scene mc_sara_night_scene1_v1_p2
    Sara "(Ладно, ты сможешь, Сара. Буть храброй!)"
    Sara "(Ты должна сделать фотографию для Лили.)"
    Sara "(Тогда ты докажешь, что ты современная девушка, а не просто девственница!)"

    scene mc_sara_night_scene1_v1_p3
    Sara "(Эй, это легче, чем я думала! Он только в трусах!)"
    Sara "(Мне просто нужно снять их, а затем начать теребить его член, пока он не станет, твердый…)"
    Sara "(...как в прошлый раз, когда он прижался ним к моему животу.)"

    scene mc_sara_night_scene1_v1_p4
    Sara "(Вау ... У меня захватывает дух, каждый раз, когда я это вижу!)"
    Sara "(Кажется, в моем животе сейчас сто крошечных бабочек!)"
    Sara "(Я не думаю, что нужно продолжать... он уже довольно твердый!)"

    scene mc_sara_night_scene1_v1_p5
    Sara "(Нужно сделать несколько фотографий, и тихонько выскользнуть из комнаты.)"
    Sara "([player_name] даже не догадываеться, что я здесь! Ха-ха! Перефект!)"
    Sara "(С другой стороны ... я могла бы поиграть с его членом немного…)"

    scene mc_sara_night_scene1_v1_p6
    Sara "(Да, я должна немного потрудиться - чтобы увидеть лучшую картину.)"
    Sara "(Ничего себе ... это становится намного сложнее!)"
    Sara "(Интересно, как долго это продлиться?)"

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

    scene mc_sara_night_scene1_v1_p7
    MC "Бу!"
    Sara "Иеккк!"
    Sara "(Aххх! Он проснулся!)"

    scene mc_sara_night_scene1_v1_p8
    Sara "Я.. Я.. *сопит* Мне так жаль!"
    MC "Что ты делаешь?"
    Sara "Я был ... я пыт ... *всхлипывает* пытаюсь.. сфотографировать…"
    MC "Где делось предыдущее фото?"

    scene mc_sara_night_scene1_v1_p9
    Sara "Я ... хотела еще…"
    Sara "Пожалуйста, прости меня. Я очень сожалею! *всхлипывает*"
    if renpy.loadable("patch.rpy"):
        Sara "Я сделаю что угодно! Только не говори папе!"

        scene mc_sara_night_scene1_v1_p10
        MC "Эй, - расслабься. Я не расскажу папе."
    if not renpy.loadable("patch.rpy"):
        Sara "Я ... я сделаю все! Просто не говорите никому!"

        scene mc_sara_night_scene1_v1_p10
        MC "Эй, - расслабься. Я не расскажу Бобу."
    Sara "Благодарю. * сопит * Я сделаю все для тебя."
    Sara "Или я тебе!"

    scene mc_sara_night_scene1_v1_p11
    MC "Сегодня ты будешь спать сомной."
    Sara "... это - все?"
    MC "Ложись возле меня под теплое одеяло."

    scene mc_sara_night_scene1_v1_p12
    Sara "... спасибо ... Мне очень жаль. *сопит*"
    MC "Эй, все в порядке. Вытри слезы. Попытайся дышать."
    MC "Если тебе так сильно нужна фотка моего члена. могла бы просто попросить."

    scene mc_sara_night_scene1_v1_p13
    Sara "Хе-хе ... Ты всегда заставляешь меня смеяться…"
    MC "Так-то лучше. Давай избавимся от этих слез."
    MC "Я подвиеусь, так что есть место и для тебя."

    scene mc_sara_night_scene1_v1_p14
    Sara "Спасибо, [player_name]..."
    MC "Ты все еще немного напряжена. Все в порядке?"
    Sara "Фактически... Я хотела спросить кое о чем..."

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)
    scene mc_sara_night_scene1_v1_p15
    Sara "Я.. Я тебе нравлюсь?"
    Sara "Потому что после всего, что случилось - с видеоиграми, Лили, тобой .. и мной..."
    Sara "Ты сказал .. Я милая .. сексуальная..."
    Sara "Я ... Мне просто нужно знать…"

    menu:
        "Да, Сара. Ты мне очень нравишься.":

            Sara "(Пожалуйста, скажи да…)"
            MC "Да, Сара. Ты мне очень нравишься."
            scene mc_sara_night_scene1_v1_p16a
            MC "Честно говоря, я думал, это было довольно очевидно."
            Sara "(О мой Бог!)"

            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)
            scene mc_sara_night_scene1_v1_p18
            Sara "Я ... я не могу поверить, что я просто спросила тебя об этом. Спи."
            Sara "Забудь, что я сказала!"
            if renpy.loadable("patch.rpy"):
                Sara "(Глупая Сара! Как он мог полюбить девственницу-ботаничку, как ты?! Он твой брат!)"
            if not renpy.loadable("patch.rpy"):
                Sara "(Глупая Сара! Как он мог полюбить девственницу-ботаничку, как ты?! )"
            MC "(Даа?! Женщины странные…)"
            scene black
            $ renpy.pause(3.0, hard=True)
            jump after_mc_sara_night_scene1_v1_choice
        "Промолчать.":


            scene mc_sara_night_scene1_v1_p17
            if renpy.loadable("patch.rpy"):
                Sara "Я думаю, что люблю тебя...больше чем брата..."
            if not renpy.loadable("patch.rpy"):
                Sara "Потому что я думаю, что люблю тебя... больше чем друга..."
            MC "…"
            Sara "(Пожалуйста, скажи да…)"
            MC "…"
            Sara "(Пожалуйста, [player_name]… скажи что-нибудь...)"
            MC "…"
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)
            scene mc_sara_night_scene1_v1_p18
            Sara "Неважно! Я ... Я тебя спрашиваю!"
            if renpy.loadable("patch.rpy"):
                Sara "(Глупая Сара! Как он мог полюбить такую тупую девственницу, как ты?! Он твой брат!)"
            if not renpy.loadable("patch.rpy"):
                Sara "(Глупая Сара! Как он мог полюбить такую тупую девственницу, как ты?! Он твой друг!)"
            Sara "(Ты не должна были ставить его в такое положение! Это может разрушить ваши отношения!)"
            MC "Ты в порядке, Сара?"
            Sara "Просто ложись спать, большой Дамбо!"
            scene black
            $ renpy.pause(3.0, hard=True)
            jump after_mc_sara_night_scene1_v1_choice

label after_mc_sara_night_scene1_v1_choice:

    scene mc_sara_night_scene1_v1_p19
    MC "(ЗЕВОК!)"
    MC "(Похоже, Сара ушла ночью. Интересно, когда она сбежала. Я, наверное, увижу ее сегодня в школе.)"
    MC "(Я никогда не видел ее такой эмоциональной.)"
    $ can_hide_windows = False
    $ mc_sara_night_scene1_v1 = 3
    $ can1_mc_sara_night_scene1_v1 = False
    $ can2_mc_sara_night_scene1_v1 = False
    $ can2_sis_nerdy_school_scene3_v1 = True
    $ sis_nerdy_school_scene3_v1 = 1
    $ can_lily_scene = False


    $ can_ml_work_day_scene1 = True
    $ can_school_intercom = True
    $ next_day = True
    $ next_day_sister_nerdy_scene4_v1 = True
    $ can_sis_nerdy_school_scene1_v1 = True
    $ can2_sis_nerdy_school_scene1_v1 = True
    $ can_sis_nerdy_evening_scene1_v1 = True
    $ can_sis_nerdy_night_sleeping1_v1 = True
    $ can_lily_work_in_progress = True
    $ sara_door_open = True
    $ can_celia_school_morning_scene1v1 = True
    $ ml_can_salon_morning_scene = True
    $ ml_can_salon_morning_scene2 = True
    $ ml_can_salon_morning_scene_dish_wash = False
    $ ml_can_kitchen_morning_scene4 = True
    $ ml_can_bedroom_morning_scene5 = True
    $ ml_can_evening_bathroom_scene_v1 = True
    $ ml_can_ml_and_f_bedroom_night_scene_v1 = True
    $ d__can_ml_and_f_bedroom_mornig_scene = True
    $ caroline_can_room_morning_scenes = True
    $ caroline_can_door_locked = True
    $ caroline_room_can_night_scene1 = True
    $ caroline_salon_can_evening_scene1 = True
    $ caroline_mc_room_can_evening_scene3 = True
    $ can_sara_scene3_v1 = True
    $ can_caroline_morning_scene4_after = False
    $ can_toilet_after_sara_scene4_1 = True
    $ can_ml_work_day_scene2 = True
    $ can_celia_morning_school_work_in_pr = True

    if can_CR2_MS1 == False:
        $ CR2_MS1  = False

    if can_CR2_MS2 == False:
        $ CR2_MS2  = False
        $ CR2_MS3 = True
        $ can_CR2_MS2 = True

    if can_CR2_MS3a == True:
        $ CR2_MS3a = True
        $ can_CR2_MS3a = False

    if can_CR2_ES1_day2 == True and CR2_ES1_day2_firsttime == True:
        $ CR2_ES1_day = 2

    if can_CR2_ES1_day3 == True and CR2_ES1_day3_firsttime == True:
        $ CR2_ES1_day = 3

    if can_CR2_ES2_day2 == True and CR2_ES2_day2_firsttime == True:
        $ CR2_ES2_day = 2

    if can_CR2_ES2_day3 == True and CR2_ES2_day3_firsttime == True:
        $ CR2_ES2_day = 3
    if CR2_NS3 == True:
        $ CR2_NS3 = False
    $ can_Bob_work_minigame = True
    $ can_CR2_ES2 = True
    $ can_CR2_ES1 = True
    $ can_MLR2_MS1_talk = True
    $ can_MLR2_MS1_kiss = True
    $ can_ml_workR2 = True
    $ can_MLR2_ES2 = True
    $ MLR2_Sleep = True
    $ can_B2_AS1_day = True
    $ MLR2_can_MS1 = True
    if can_Zv2_MS2_q == True and can2_Zv2_MS2_q == True:

        $ Zv2_MS2_q5 = True
        $ Zv2_MS2_q6 = True
        $ Zv2_MS2_q7 = True
        $ can2_Zv2_MS2_q = False
    if Zv2_ES4 == 1:
        $ Zv2_ES4_counter += 1
        if Zv2_ES4_counter == 3:
            $ Zv2_ES4 = True
            $ Bobv2_MS1_q5 = True
            if Zv2_lie_counter > 1:
                $ sms1_fromZuri = True
                $ company_profit = 2
            if Zv2_true_counter > 1:
                $ sms2_fromZuri = True
                $ company_profit = 1

    $ can_SR2_MS2 = True
    $ SR2_bath = False
    if celia_school_morning_scene2v1 == 1 and can1_celia_school_morning_scene2v1 == True:
        $ can1_celia_school_morning_scene2v1 = False
        $ celia_school_morning_scene1v1 = 1
        $ celia_school_morning_scene2v1 = 0
    if celia_school_morning_scene2v1 == 1:
        $ can1_celia_school_morning_scene2v1 = True
        $ can_school_intercom = False
        $ can_celia_morning_school_work_in_pr = False


    if week_day == 1:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 2:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 3:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 4:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 5:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 6:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 7:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
