image celia_school_morning_scene1bv1_p1 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/1.jpg"
image celia_school_morning_scene1bv1_p2 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/2.jpg"
image celia_school_morning_scene1bv1_p3 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/3.jpg"
image celia_school_morning_scene1bv1_p4 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/4.jpg"
image celia_school_morning_scene1bv1_p5 = "images/school/teacher_room1/morning/scenes/celia_school_morning_scene1bv1/5.jpg"

label celia_school_morning_scene1bv1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Marty_Gots_a_Plan.mp3', channel="music1", loop=True, fadein = 2)

    scene celia_school_morning_scene1bv1_p1 with dissolve
    $ can_hide_windows = True
    Celia "[player_name]? О, слава Богу, ты здесь."
    MC "Да? Все в порядке, миссис Селия.?"
    Celia "Всё прекрасно... Вообще-то нет. Нет, это действительно не так. Нам надо поговорить."

    scene celia_school_morning_scene1bv1_p2
    Celia "Ты можешь быть удивлен, почему я действовала так...."
    MC "Вы имеете в виду, как в туалете, когда мы.."
    Celia "Да! Не нужно описывать это мне. Дело в том, что меня шантажировали.."
    MC "Шантажировал?! Кто?"

    scene celia_school_morning_scene1bv1_p3
    Celia "В этом суть проблемы. Я не знаю, кто."
    MC "Да... Вы ничего не можете сделать?"
    Celia "Безусловно, есть. Мне нужна ваша помощь, хотя."
    MC "Что это значит? Отслеживание какого-то жуткого шантажиста, не звучит слишком безопасно."

    scene celia_school_morning_scene1bv1_p4
    Celia "Если ты поможешь мне поймать его, в нем будет вознаграждение для тебя."
    Celia "Если ты поймаешь о чем я?"
    MC "Я буду трахать тебя?"
    Celia "Это зависит от того, насколько хорошо ты справишься."

    scene celia_school_morning_scene1bv1_p5
    MC "Я в деле!"
    Celia "Отлично! Пожалуйста, возьмите это. Это мой адрес. Я хочу, чтобы ты пришел."
    Celia "Я, как правило, дома в вечернее время... Нет, в ночное время."
    Celia "Мой муж уезжает в командировку, так что мы сядем и создадим твердую стратегию для ловли этого ублюдка."
    MC "Классно. Увидимся позже, миссис Селия."
    Celia "До свидания, [player_name]."
    show relationship_plus
    $ renpy.pause(3.0, hard=True)
    $ Celia_points += 1
    $ celia_school_morning_scene1bv1 = 3
    $ celia_work_in_progress_v1 = 1
    $ can_celia_school_morning_scene1bv1 = 3
    $ celia_house_unlocked = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump teacher_room1_morning2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
