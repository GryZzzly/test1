image sara_room_evening_scene1_v1_p1 = "images/home/sara_room/evening/scene1_v1/1.jpg"
image sara_room_evening_scene1_v1_after = "images/home/sara_room/evening/scene1_v1/after_sara_scene1.png"

image sara_room_evening_scene2_v1_p1 = "images/home/sara_room/evening/scene2_v1/1.jpg"
image sara_room_evening_scene2_v1_p2 = "images/home/sara_room/evening/scene2_v1/2.jpg"
image sara_room_evening_scene2_v1_p3 = "images/home/sara_room/evening/scene2_v1/3.jpg"
image sara_room_evening_scene2_v1_p4 = "images/home/sara_room/evening/scene2_v1/4.jpg"
image sara_room_evening_scene2_v1_p5 = "images/home/sara_room/evening/scene2_v1/5.jpg"
image sara_room_evening_scene2_v1_p6 = "images/home/sara_room/evening/scene2_v1/6.jpg"
image sara_room_evening_scene2_v1_p7 = "images/home/sara_room/evening/scene2_v1/7.jpg"
image sara_room_evening_scene2_v1_p8 = "images/home/sara_room/evening/scene2_v1/8.jpg"
image sara_room_evening_scene2_v1_p9 = "images/home/sara_room/evening/scene2_v1/9.jpg"
image sara_room_evening_scene2_v1_p10 = "images/home/sara_room/evening/scene2_v1/10.jpg"
image sara_room_evening_scene2_v1_p11 = "images/home/sara_room/evening/scene2_v1/11.jpg"
image sara_room_evening_scene2_v1_p12 = "images/home/sara_room/evening/scene2_v1/12.jpg"
image sara_room_evening_scene2_v1_p13 = "images/home/sara_room/evening/scene2_v1/13.jpg"
image sara_room_evening_scene2_v1_p14 = "images/home/sara_room/evening/scene2_v1/14.jpg"
image sara_room_evening_scene2_v1_p15 = "images/home/sara_room/evening/scene2_v1/15.jpg"
image sara_room_evening_scene2_v1_p16 = "images/home/sara_room/evening/scene2_v1/16.jpg"
image sara_room_evening_scene2_v1_p17 = "images/home/sara_room/evening/scene2_v1/17.jpg"
image sara_room_evening_scene2_v1_p18 = "images/home/sara_room/evening/scene2_v1/18.jpg"
image sara_room_evening_scene2_v1_p19 = "images/home/sara_room/evening/scene2_v1/19.jpg"
image sara_room_evening_scene2_v1_p20 = "images/home/sara_room/evening/scene2_v1/20.jpg"
define Console = Character("Console")

label sis_nerdy_evening_scene1_v1_l:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    $ can_hide_windows = True
    if can_sis_nerdy_evening_scene1_v1 == True and sis_nerdy_evening_scene2_v1 == 0:
        scene sara_room_evening_scene1_v1_p1 with dissolve
        MC "Эй, Сара, ты свободна?"
        Sara "Извини, [player_name]. Я в середине финала Лиги! Я выиграю этот матч до следующего сезона!"
        Sara "Я найду тебя позже!"
        MC "(Сара принимает свою игру слишком серьезно.)"
        MC "Хорошо, увидимся позже, Сара."
        $ can_sis_nerdy_evening_scene1_v1 = False
        $ can_hide_windows = False
        jump sister_nerdy_evening1
    if can_sis_nerdy_evening_scene1_v1 == False:
        show sara_room_evening_scene1_v1_after
        $ can_hide_windows = False
        MC "Я уже говорил с ней."
        jump sister_nerdy_evening1
    if sis_nerdy_evening_scene2_v1 == 1:
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)


        scene sara_room_evening_scene2_v1_p1 with dissolve
        MC "Эй, Сара, ты все еще занята?"
        Sara "Дайте мне две секунды... Этот матч почти закончился."
        Sara "Аааа! Я сделала!"

        scene sara_room_evening_scene2_v1_p2
        Sara "Скажи, ты хочешь поиграть вместе? Я могу загрузиться на кссвитч4!"
        MC "Прекрасно! В какую игру ты хочешь поиграть?"
        Sara "Позвольте мне взглянуть и посмотреть, что многопользовательское у меня есть."

        scene sara_room_evening_scene2_v1_p3
        Sara "Хм... Медаль долга? Призыв чести?"
        Sara "О! У меня уличные бои VII!"
        MC "Все работает для меня."
        Sara "Тогда давайте сделаем уличные бои VII. Один против одного Deathmatch!"
        MC "Звучит весело!"

        scene sara_room_evening_scene2_v1_p4
        Sara "Ладно, Вот твой Контролер. Ты играл раньше, да?"
        MC "Спасибо. Да, и я чертовски хорош в этом-так что тебе лучше следить за собой!"
        Sara "Ну, так как ты уверен, как насчет того, чтобы изменить правила немного?"
        MC "О чем ты думаешь? Игра на деньги?"

        scene sara_room_evening_scene2_v1_p5
        Sara "Проигравший должен...... снимать одежду, каждый раз, когда умирает."
        Sara "(Это моя месть за попытку украсть мои трусики!)"
        MC "(Подожди? Что?!)"
        MC "Прости, я не слышал. Что ты сказала?"
        Sara "Каждый раз, когда твой персонаж умирает в игре, ты должны снять часть одежды. Согласен?"

        scene sara_room_evening_scene2_v1_p6
        MC "(Срань Господня! Я мечтаю! Это не может на самом деле происходит!)"
        MC "Ах да, это сделка."
        MC "Ты понимаешь, что это значит, что ты собираешься раздеться догола? Когда дело доходит до уличных бойцов-я чертовский про."

        scene sara_room_evening_scene2_v1_p7
        Sara "Эм, я уверена, что ты..."
        Sara "ты не увидишь мои сиськи сегодня."
        MC "(Черт, я не могу ждать, чтобы увидеть ее сиськи. Я не могу потерять девушку! Я играю в игру уличные бои с тех пор, как был в садике!)"

        scene sara_room_evening_scene2_v1_p8
        Console "ГОТОВЫЙ! БОРЬБА!"
        MC "(Черт! Она быстро!)"
        Sara "В чем дело, [player_name]? Ты выглядишь немного напряженными!"
        Sara "Хе-хе ... Почему ты еще не ударил меня?"
        MC "Потому что ты не даешь мне возможности"
        Console "Игрок 2 потерпел поражение!"
        MC "Черт побери!"
        $ renpy.music.stop(channel="music2", fadeout=1)
        scene black
        "(Пятнадцать минут спустя…)"
        $ renpy.pause(2.0)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

        scene sara_room_evening_scene2_v1_p9
        Sara "Хехе! Ты уверен, что хочешь продолжить еще один раунд? На тебе остались только боксеры!"
        if renpy.loadable("patch.rpy"):
            MC "Это еще не конец! Я просто поддался тебе, потому что ты моя сестра."
        if not renpy.loadable("patch.rpy"):
            MC "Это еще не конец! Я просто успокоился, потому что ты мой друг."
        Sara "Уверен!"
        $ renpy.music.stop(channel="music2", fadeout=1)
        scene black
        "(Пять Минут Спустя…)"
        $ renpy.pause(2.0)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
        Console "Игрок 2 победил!"
        Console "Игрок 1 побил новый рекорд по смертям!"
        Sara "Юхуу!"

        scene sara_room_evening_scene2_v1_p10
        Sara "Не волнуйся, [player_name]. Тебе не нужно снимать нижнее белье."
        Sara "Я думаю, ты уже достаточно унижен! Хехе!"
        MC "Чесный разговор - мы договорились о правилах, прежде чем мы начали."
        Sara "Подожди - ты серьезно не собираешься..."

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music1", loop=True, fadein = 2)

        scene sara_room_evening_scene2_v1_p11
        Sara "О мой Бог! Какой огромный!"
        Sara "Почему это так сложно?!"
        MC "(Может быть, потому что я хочу, трахнуть тебя?)"
        MC "Это - потому что ты смотришь на него прямо сейчас. Член склонен становиться твердыми, когда на него обращают внимание."

        scene sara_room_evening_scene2_v1_p12
        MC "Право - что происходит теперь?"
        Sara "…"
        MC "Это - еще один раунд, чтобы решить победителя? Или ты победила, так как я гол?"

        scene sara_room_evening_scene2_v1_p13
        MC "(Она не слушает меня больше …, Она просто уставилась на моего член.)"
        MC "(Интересно, является ли это первый раз, когда она когда-либо видела его. Она, кажется, чрезвычайно интересуется им!)"
        Sara "(Ошеломите …, Это - настолько большой и твердый …, который я не знаю, почему, но я действительно хочу коснуться его.)"

        scene sara_room_evening_scene2_v1_p14
        MC "Так … ммм … я собираюсь идти одеваться."
        if renpy.loadable("patch.rpy"):
            MC "Последняя вещь, которую мы хотим, чтобы не вломились мама или папа!"
        if not renpy.loadable("patch.rpy"):
            MC "Последняя вещь, которую мы хотим, чтобы не вломились Линда или Боб!"
        $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
        "(Щелчек) (Вспышка света заполняет комнату)"
        $ renpy.sound.stop(channel="sound")
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture_Clean.mp3', channel="music2", loop=True, fadein = 2)

        scene sara_room_evening_scene2_v1_p15
        Sara "(Получила его! Я не могла позволить этому просто быть памятью!)"
        MC "Что, черт возьми, Сара! Ты просто делали снимок моего пениса?"
        Sara "Н-нет?"
        MC "Да! Я вижу, ты делаешь фото прямо сейчас! Удали его!"


        scene sara_room_evening_scene2_v1_p16
        Sara "Ты собираешься поймать меня первым! Хехе!"
        MC "Вернись сюда!"
        MC "Серьезно, Сара! Дай мне свой телефон!"
        if renpy.loadable("patch.rpy"):
            Sara "Если ты не перестанешь преследовать меня, я позвоню маме!"
        if not renpy.loadable("patch.rpy"):
            Sara "Если ты не перестанешь преследовать меня, я позвоню Линде!"
        scene sara_room_evening_scene2_v1_p17
        MC "Попался!"
        Sara "[player_name], стоп! Шутки в сторону!"
        MC "Удали эту картинку с телефона!"
        Sara "Я не говорю об этом с тобой!"
        MC "Ну, может быть, мне просто нужно будет..."
        Sara "Ммм… [player_name]?"

        scene sara_room_evening_scene2_v1_p18
        MC "(Вот дерьмо! Мой член нажал прямо на ее голый живот. Это так тепло на кончике моего члена.)"
        Sara "(О мой Бог! член [player_name] касается меня!)"
        MC "Я ... я ... мне жаль ... Я сейчас уйду!"

        scene sara_room_evening_scene2_v1_p19
        MC "(Дерьмо, что получилось странно, ДЕЙСТВИТЕЛЬНО быстро.)"
        MC "(Надеюсь, она не слишком злится на меня за то, что она подтолкнула мой член к ней. Я не хотел!)"
        Sara "(Это было интенсивно ... Я должен снова проверить эту фотографию, когда он уходит!)"

        scene sara_room_evening_scene2_v1_p20
        Sara "(Ничего себе ... Это очень здорово!)"
        Sara "(Мне нужно показать Лили! Она не поверит в это!)"
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ day_time +=1
        $ sis_nerdy_evening_scene1_v1 = 0
        $ first_sis_nerdy_scene4_v1 = 3
        $ sara_door_open = False
        $ sis_nerdy_school_scene2_v1 = 1
        $ sis_nerdy_evening_scene2a_v1 = 1
        $ fourth_visit_sister_nerdy_scene4_v1 = 1
        $ can_sms2_from_sara = 1
        $ can_lily_scene = False
        $ can_gamepad_sara = True
        $ can_hide_windows = False
        jump corridor_night1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
