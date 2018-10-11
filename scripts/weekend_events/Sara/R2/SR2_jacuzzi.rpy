image SR2_weekend_jacuzzi_background = "images/Weekend_Events/Sara/R2/Map/2.jpg"

image SR2_weekend_jacuzzi_p1 = "images/Weekend_Events/Sara/R2/Jacuzzi/1.jpg"
image SR2_weekend_jacuzzi_p2 = "images/Weekend_Events/Sara/R2/Jacuzzi/2.jpg"
image SR2_weekend_jacuzzi_p3 = "images/Weekend_Events/Sara/R2/Jacuzzi/3.jpg"
image SR2_weekend_jacuzzi_p4 = "images/Weekend_Events/Sara/R2/Jacuzzi/4.jpg"
image SR2_weekend_jacuzzi_p5 = "images/Weekend_Events/Sara/R2/Jacuzzi/5.jpg"
image SR2_weekend_jacuzzi_p6 = "images/Weekend_Events/Sara/R2/Jacuzzi/6.jpg"
image SR2_weekend_jacuzzi_p7a = "images/Weekend_Events/Sara/R2/Jacuzzi/7a.jpg"
image SR2_weekend_jacuzzi_p7b = "images/Weekend_Events/Sara/R2/Jacuzzi/7b.jpg"
image SR2_weekend_jacuzzi_p7c = "images/Weekend_Events/Sara/R2/Jacuzzi/7c.jpg"
image SR2_weekend_jacuzzi_p7d = "images/Weekend_Events/Sara/R2/Jacuzzi/7d.jpg"
image SR2_weekend_jacuzzi_p8a = "images/Weekend_Events/Sara/R2/Jacuzzi/8a.jpg"
image SR2_weekend_jacuzzi_p8b = "images/Weekend_Events/Sara/R2/Jacuzzi/8b.jpg"
image SR2_weekend_jacuzzi_p8c = "images/Weekend_Events/Sara/R2/Jacuzzi/8c.jpg"
image SR2_weekend_jacuzzi_p9 = "images/Weekend_Events/Sara/R2/Jacuzzi/9.jpg"
image SR2_weekend_jacuzzi_p10 = "images/Weekend_Events/Sara/R2/Jacuzzi/10.jpg"
image SR2_weekend_jacuzzi_p11 = "images/Weekend_Events/Sara/R2/Jacuzzi/11.jpg"
image SR2_weekend_jacuzzi_p11anim = Movie(play="videos/02 Sara-Weekend-1.webm", loop = True )
image SR2_weekend_jacuzzi_p12 = "images/Weekend_Events/Sara/R2/Jacuzzi/12.jpg"
image SR2_weekend_jacuzzi_p13 = "images/Weekend_Events/Sara/R2/Jacuzzi/13.jpg"
image SR2_weekend_jacuzzi_p14 = "images/Weekend_Events/Sara/R2/Jacuzzi/14.jpg"
image SR2_weekend_jacuzzi_p15 = "images/Weekend_Events/Sara/R2/Jacuzzi/15.jpg"
image SR2_weekend_jacuzzi_p16 = "images/Weekend_Events/Sara/R2/Jacuzzi/16.jpg"
image SR2_weekend_jacuzzi_p16anim = Movie(play="videos/02 Sara-Weekend-2.webm", loop = True )
image SR2_weekend_jacuzzi_p17 = "images/Weekend_Events/Sara/R2/Jacuzzi/17.jpg"
image SR2_weekend_jacuzzi_p17anim = Movie(play="videos/02 Sara-Weekend-4.webm", loop = True )
image SR2_weekend_jacuzzi_p18 = "images/Weekend_Events/Sara/R2/Jacuzzi/18.jpg"
image SR2_weekend_jacuzzi_p19 = "images/Weekend_Events/Sara/R2/Jacuzzi/19.jpg"
image SR2_weekend_jacuzzi_p20 = "images/Weekend_Events/Sara/R2/Jacuzzi/20.jpg"
image SR2_weekend_jacuzzi_p21 = "images/Weekend_Events/Sara/R2/Jacuzzi/21.jpg"
image SR2_weekend_jacuzzi_p21anim = Movie(play="videos/02 Sara-Weekend-3.webm", loop = True )
image SR2_weekend_jacuzzi_p22 = "images/Weekend_Events/Sara/R2/Jacuzzi/22.jpg"
image SR2_weekend_jacuzzi_p23 = "images/Weekend_Events/Sara/R2/Jacuzzi/23.jpg"
image SR2_weekend_jacuzzi_p24a = "images/Weekend_Events/Sara/R2/Jacuzzi/24a.jpg"
image SR2_weekend_jacuzzi_p24b = "images/Weekend_Events/Sara/R2/Jacuzzi/24b.jpg"
image SR2_weekend_jacuzzi_p24c = "images/Weekend_Events/Sara/R2/Jacuzzi/24c.jpg"
image SR2_weekend_jacuzzi_p25a = "images/Weekend_Events/Sara/R2/Jacuzzi/25a.jpg"
image SR2_weekend_jacuzzi_p25b = "images/Weekend_Events/Sara/R2/Jacuzzi/25b.jpg"

label SR2_jacuzzi_label:
    if SR2_after_swimming == True and SR2_after_lemonade == True and SR2_after_sunbed == True and SR2_after_waterslide == True:
        scene SR2_weekend_jacuzzi_background
        $ can_hide_windows = False
        call screen SR2_jacuzzi_scr
    else:
        show screen swimming_poll_scr
        $ can_hide_windows = False
        $ clickable = False
        Sara "[player_name]... Слишком рано для джакузи! Расслабление должно быть последним."
        $ music_continue = False
        $ clickable = True
        jump swimming_poll_label

screen SR2_jacuzzi_scr:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 810
        ypos 422
        focus_mask True
        idle "images/Weekend_Events/Sara/R2/Map/b6.png"
        hover "images/Weekend_Events/Sara/R2/Map/b6_hover.png"
        hovered Show("displayTextScreen", displayText = "Джакузи")
        action [Hide("displayTextScreen"),SetVariable("music_continue", False),Jump("SR2_jacuzzi_scene_label")]
        unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Jump("swimming_poll_label")]
        unhovered Hide("displayTextScreen")

label SR2_jacuzzi_scene_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)

    scene SR2_weekend_swimming_pool_p2
    $ can_hide_windows = True
    MC "Когда я пришел, я увидел знак, в котором упоминалось что-то о джакузи."
    MC "У них действительно есть джакузи??"
    Sara "О, да! Они потрясающие!"
    Sara "Кроме того, мы получаем частный доступ по 30 минут каждый день с нашими VIP-карточками!"
    MC "Что же мы ждем? Поехали!"

    scene SR2_weekend_jacuzzi_p1

    MC "Это даже лучше, чем я думал."
    MC "Теплое джакузи, красивая женщина и отдельная комната. Это гениально!."
    Sara "Оуу... Я рада, что тебе нравится."

    scene SR2_weekend_jacuzzi_p2

    Sara "(Вздох…)"
    MC "(ГМ? Что на нее нашло?)"
    MC "Ты в порядке, Сара?"
    Sara "Наверное, да…"
    MC "Что случилось?"
    Sara "Наше свидание сегодня... Я имею в виду.. Это вообще свидание? ... Мы на самом деле ничего не сделали."

    if renpy.loadable("patch.rpy"):
        Sara "Такое чувство, что мы вернулись к брату и сестре, когда мы вышли."

    MC "Ну, если честно-было бы очень рискованно вести себя так, будто мы встречаемся."

    scene SR2_weekend_jacuzzi_p3

    Sara "Достань его!"
    MC "Хм?!"
    Sara "Остались только мы с тобой. Никто больше не может войти в течение двадцати пяти минут."
    Sara "Достаточно времени, верно?"
    MC "Достаточно времени для чего?!"

    scene SR2_weekend_jacuzzi_p4

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

    Sara "Я хочу сделать тебе минет как в первый раз."
    MC "Сара, я.."
    Sara "Поцелуй меня."

    scene SR2_weekend_jacuzzi_p5

    MC "(Я думал, Сара была счастлива, принимая вещи медленно-особенно, когда мы были на публике.)"
    MC "(Похоже, она подавляет свое сексуальное влечение!)"
    Sara "Ты можешь коснуться везде, где хочешь."

    scene SR2_weekend_jacuzzi_p6

    MC "(Я думаю, что это открытое приглашение держать ее задницу, пока я целуюсь с ней.)"
    MC "(Интересно, как далеко Сара готова зайти сегодня. Может быть, я смогу ее потрогать?)"
    MC "(Я слишком много об этом думаю. Я должен просто лежать и наслаждаться тем, что происходит.)"
    window hide
    menu:
        "Трогать ее задницу.":
            scene SR2_weekend_jacuzzi_p7a

            Sara "Mмм!"
            MC "Mмм…"
            MC "(Похоже, ей нравится, когда ее задницу лапают!)"

            scene SR2_weekend_jacuzzi_p7b

            MC "(Нужно сжать ее покрепче и посмотреть, как она реагирует!)"

            scene SR2_weekend_jacuzzi_p7c

            Sara "MMMMM!!!!"

            scene SR2_weekend_jacuzzi_p7d

            Sara "(Черт возьми, это было здорово!)"
            MC "(Ага! Похоже, я нашел правильное место.!)"
            jump after_menu_SR2_jacuzzi_scene_label
        "Ждать ее хода.":

            scene SR2_weekend_jacuzzi_p4

            Sara "[player_name], Я хочу, чтобы ты... это было неловко... неважно."
            MC "Говори. Я обещаю, что не буду смеяться."
            Sara "Можешь ... ущипнуть мои соски?"
            MC "Конечно! Сядь передомной.."

            scene SR2_weekend_jacuzzi_p8a

            MC "Как это?"
            Sara "Ах... это хорошо…"
            Sara "Ooх…"

            scene SR2_weekend_jacuzzi_p8b

            MC "Продолжать?"
            Sara "Да, не останавливайся.."
            MC "Посильнее?"
            Sara "Ты можешь ... использовать всю свою руку?"

            scene SR2_weekend_jacuzzi_p8c

            MC "Вроде этого?"
            Sara "О, да ... это потрясающе.…"
            MC "Видишь ли, меньшая грудь, как твоя, гораздо более чувствительна."
            Sara "Mмм… Я рада, что они стали меньше.."
            jump after_menu_SR2_jacuzzi_scene_label


label after_menu_SR2_jacuzzi_scene_label:
    scene SR2_weekend_jacuzzi_p9

    Sara "Я так сильно тебя люблю, [player_name]."
    MC "Я тоже тебя люблю, Сара. Еще раз спасибо за покупку VIP-пропуска."
    Sara "Тебе не нужно меня благодарить. Для меня это был удивительный подарок."

    scene SR2_weekend_jacuzzi_p10

    Sara "Oooх! Такое чувство, что кому-то снова тяжело!"
    MC "Упс... Прости! Хаха!"
    Sara "[player_name] я хочу обратить внимание на твоего младшего брата!"
    Sara "Давай снимем с тебя эти плавки.."
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ renpy.pause(3,hard=True)

    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music1", loop=True, fadein = 2)
    scene SR2_weekend_jacuzzi_p11

    Sara "Ух ты ... я и забыла, какой он большой.!"
    Sara "Эй [player_name], каково это, если я дотронусь до твоих яиц?"

    MC "Попробуй. Просто ... будь нежной.!"

    scene SR2_weekend_jacuzzi_p12

    Sara "*Лижет Лижет*"
    MC "Aхх…"
    Sara "(Ага! Так что это действительно хорошо, когда играют с яйцами парня!)"

    scene SR2_weekend_jacuzzi_p13

    MC "О, да, вот и все. Продолжай, Сара..."
    scene SR2_weekend_jacuzzi_p11anim
    Sara "*Лижет Лижет*"
    Sara "(Вау! Он дрочил себе, пока я сосала его яйца.)"

    scene SR2_weekend_jacuzzi_p14

    MC "ММ! Mмм…. Aх…."
    Sara "(Похоже, он действительно наслаждается этим!)"
    Sara "(Я надеюсь, что он не кончит слишком быстро!)"

    scene SR2_weekend_jacuzzi_p15

    Sara "Ты хочеш, чтобы я сделала тебе минет?"
    MC "Определенно!"
    Sara "Хорошо, позволь мне занять позицию."

    scene SR2_weekend_jacuzzi_p16

    Sara "Так подойдет?"
    scene SR2_weekend_jacuzzi_p16anim
    MC "Идеально!"
    MC "Твои глаза изумительны, ты знаешь?"
    Sara "Хехе... Благодарю. Я готова начать."

    scene SR2_weekend_jacuzzi_p17

    Sara "Mwah!"

    MC "(Она такая милая. Мне нравится, как она начинает минет с поцелуя.)"
    Sara "(Ладно, я сделаю все, что смогу, чтобы убедиться, что [player_name] очень любит этот!)"

    scene SR2_weekend_jacuzzi_p18

    Sara "*Лижет Лижет*"
    MC "Mмм… Oх… Это хорошо…"
    Sara "(На вкус немного соленый!)"

    scene SR2_weekend_jacuzzi_p19

    Sara "(Хорошо, пора заглотить его.)"
    MC "Это здорово, Сара.."
    MC "Aхх… Вау…"

    scene SR2_weekend_jacuzzi_p20

    MC "Вау!"
    scene SR2_weekend_jacuzzi_p17anim
    MC "(Ощущение ее горячего рта-плотно обернутого вокруг моей головоки-неописуемо.)"
    MC "(Я должен бороться с желанием кончить сразу!)"

    scene SR2_weekend_jacuzzi_p21

    MC "Oхх… Oхххх… Mмм…."
    scene SR2_weekend_jacuzzi_p21anim
    Sara "*Лижет* *Лижет* *Лижет*"
    Sara "*ЛИЖЕЕЕЕТ*"

    scene SR2_weekend_jacuzzi_p22

    MC "(Черт! Я долго не продержусь! Интересно, если она будет возражать, глотать его глубже!)"
    MC "(Давай толкнем мои бедра вперед и посмотрим.)"
    Sara "*Лижет Лижет*"

    scene SR2_weekend_jacuzzi_p23

    Sara "*Лижет* *давиться*"
    MC "Aхххх! БЛЯ! Да!"
    MC "Ебать! Я собираюсь кончить!"

    window hide
    menu:
        "Удар горячей спермы глубоко внутри рта младшей сестры.":
            scene SR2_weekend_jacuzzi_p24a

            MC "Открой пошире, Сара!"
            Sara "Aхххх…."
            MC "ММММ! ДА!"

            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p24a with dissolve
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p24b with dissolve

            MC "AХХХХХ!"
            MC "МММ!! Aхх…."
            MC "Фух… Это было невероятно!"
            Sara "Mмм…"

            scene SR2_weekend_jacuzzi_p24c

            Sara "(Интересно, почему он всегда такой соленый.)"
            Sara "(Глоток)"
            MC "Спасибо, Сара. Ты великолепна в этом.!"
            jump after_menu2_SR2_jacuzzi_scene_label
        "Распылите свое семя на красивое лицо вашей младшей сестры.":

            scene SR2_weekend_jacuzzi_p25a

            Sara "Ты не хочешь, чтобы я продолжал сосать?"
            MC "Просто оставь так! Ммм!"
            Sara "Ты увер..."
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p25a with dissolve
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene SR2_weekend_jacuzzi_p25b with dissolve

            Sara "Оуу!"
            MC "Aхх! Ммм!"
            MC "Черт! Это хорошо!"
            Sara "Фу! (Я чуть не получила в глаза!)"
            jump after_menu2_SR2_jacuzzi_scene_label


label after_menu2_SR2_jacuzzi_scene_label:
    scene SR2_weekend_jacuzzi_p9

    MC "Ну? Как прошла эта дата?"
    Sara "ЛУЧШЕЕ до сих пор!"
    MC "В самом деле?"
    Sara "Да, [player_name]. Я вроде как надеялся снова сблизиться с тобой."

    scene SR2_weekend_jacuzzi_p10

    Sara "Я действительно люблю тебя."
    Sara "Но я хочу больше, чем просто слова... мне нужны интимные физические отношения с тобой. Как то, что мы только что сделали."
    MC "Позвольте мне подумать об этом, и я посмотрю, смогу ли я думать о том, как мы можем безопасно быть близкими, не замечая других."
    Sara "Спасибо, [player_name]. Ты самый лучший!"
    MC "Я люблю тебя, Сара.."
    $ can_hide_windows = False
    $ SR2_after_swimming = False
    $ R2_after_lemonade = False
    $ SR2_after_sunbed = False
    $ SR2_after_waterslide = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    if can_sms4_sara == True:
        $ sms4_sara = True
        $ can_sms4_sara = False
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
