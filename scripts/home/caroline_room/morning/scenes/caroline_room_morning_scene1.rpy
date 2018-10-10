image caroline_room_morning_scene1_p1 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/1.jpg"
image caroline_room_morning_scene1_p2 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/2.jpg"
image caroline_room_morning_scene1_p3 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/3.jpg"
image caroline_room_morning_scene1_p4 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/4.jpg"
image caroline_room_morning_scene1_p5 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/5.jpg"
image caroline_room_morning_scene1_p6 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene1/6.jpg"

label caroline_room_morning_scene1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_can_room_morning_scenes == False:
        show screen caroline_room_morning_not_clickable
        MC "Я уже говорил с ней."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_room_morning_scene1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "(Кэролайн всегда была заботливой сестрой.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Кэролайн всегда была заботливым другом.)"
    MC "(На самом деле, одно из моих самых ранних воспоминаний было, когда надомной издевались в школе. Мне было шесть или семь лет.)"
    MC "(Дуэт Том и Самсон решили украсть мои деньги на обед - всего пару долларов; но я отказался им их отдавать.)"
    MC "(Я помню боль ударов по животе и их жестокий смех.)"
    MC "(Кэролайн была на четыре года старше меня, но это не мешало ей избивать хулиганов своими голыми кулаками.)"
    MC "(За свою беду она получила два набора избитых суставов и трехнедельный отдых.)"
    MC "(Том и Самсон тоже получили три недели перерыва. Однако их «перерыв» был проведен в больнице.)"

    scene caroline_room_morning_scene1_p2 at pandown2
    $ renpy.pause(4)
    MC "Кэролайн, я"
    MC "(Ебена мать! Посмотри на эту задницу! Поговорите о пузыре!)"
    MC "Извини! Я не знал, что ты переодеваешся! Я должен был постучать!"

    scene caroline_room_morning_scene1_p3
    Caroline "Привет, [player_name]!"
    Caroline "Не переживай [player_name]. Не похоже, что ты один из тех, жутких парней из колледжа, которые просто пытаются залезть в мои штаны."
    MC "Ух, да…"
    MC "(Я думал, что ее задница хороша, но ее грудь может быть даже лучше!)"
    Caroline "Ну что, как поживаешь?"
    MC "Ничего особенного - просто пришел, чтобы поздороваться."

    scene caroline_room_morning_scene1_p4
    Caroline "Ой! Прежде чем я забуду - что случилось в школе на днях?"
    if renpy.loadable("patch.rpy"):
        Caroline "Я только собрал фрагменты истории от Сары и мамы?"
    if not renpy.loadable("patch.rpy"):
        Caroline "Я только подобрал фрагменты истории из Сары и Линды?"
    menu:
        "Сказать ей всю правду.":
            MC "Эх ... Это было плохо. Я спросил миссис Селию и получил отказ."
            Caroline "Ой, это звучит грубо. Я знаю, как трудно быть с разбитым сердцем."
            MC "Ой! Это не разбитое сердце, это плохая часть - она унизила меня посреди людного коридора."
            Caroline "О Боже… [player_name]... Мне очень жаль."
            jump caroline_room_morning_scene1_after_menu
        "Играть это здорово.":
            MC "Расслабься - ничего."
            Caroline "Ты уверен? Я слышал кое-что о тебе, оскорбляющем общественность?"
            MC "В самом деле! Это было неважно. Я спросил миссис Селию, но ничего из этого не вышло."
            Caroline "Хм ... Многие мужчины склонны обсуждать свои чувства, а не говорить о своих проблемах."
            Caroline "Убедись, что ты заботишься о себе - и если ты когда-нибудь захочеш поговорить, ты знаешь, что моя дверь всегда открыта."
            jump caroline_room_morning_scene1_after_menu
        "Я бы предпочел не говорить об этом.":
            MC "Да ... Я бы предпочел не говорить об этом."
            Caroline "Ой! Прости!"
            MC "Нет, это не твоя вина. Не нужно извиняться."
            Caroline "Ладно, просто обещай позаботиться о себе? Я слышал кое-что о миссис Селии и тебе в коридоре, но я не получил полную информацию."
            MC "Я ... Извини, я бы не подумал об этом."
            Caroline "Это нормально. Если ты когда-нибудь передумаешь, я всегда здесь, чтобы поболтать."
            MC "Спасибо, Кэролайн."
            jump caroline_room_morning_scene1_after_menu

label caroline_room_morning_scene1_after_menu:
    scene caroline_room_morning_scene1_p5
    Caroline "Прежде чем ты уйдешь, я хочу, чтобы ты обещал мне что-то?"
    MC "Что?"
    Caroline "Обещай, что ты придешь ко мне, если ты когда-нибудь почувствуешь стресс или что-то похожее, хорошо?"
    MC "Я буду в порядке."

    scene caroline_room_morning_scene1_p6
    Caroline "Я не спрашивала, будет ли с тобой все будет в порядке."
    Caroline "Я попросила вас пообещать мне, что ты  прийдешь ко мне, если вы почувствуете себя не так."
    MC "Я обещаю."
    Caroline "Спасибо."

    scene caroline_room_morning_scene1_p3
    Caroline "Увидимся, [player_name]. Мне нужно закончить макияж."
    MC "Увидимся, Кэролайн."
    $ caroline_can_room_morning_scenes = False
    $ caroline_morning_scenes_visit = 2
    $ can_hide_windows = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump caroline_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
