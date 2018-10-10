image sis_nerdy_school_scene2_v1_p1 = "images/school/school_entrance/day/scenes/sara_scene2_v1/1.jpg"
image sis_nerdy_school_scene2_v1_p2 = "images/school/school_entrance/day/scenes/sara_scene2_v1/2.jpg"
image sis_nerdy_school_scene2_v1_p3 = "images/school/school_entrance/day/scenes/sara_scene2_v1/3.jpg"
image sis_nerdy_school_scene2_v1_p4 = "images/school/school_entrance/day/scenes/sara_scene2_v1/4.jpg"


label sis_nerdy_school_scene2_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    hide screen school_entrance_day_notclickable
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music2", loop=True, fadein = 2)

    scene sis_nerdy_school_scene2_v1_p1 with dissolve
    $ can_hide_windows = True
    MC "(О! Это Лили и Сара. Они ждут свой следующий урок.)"
    Lily "Что ты так хотела показать мне?"
    MC "(А? Сара вытаскивает свой телефон?)"
    Lily "Боже мой! Это Дэн на химии?"

    scene sis_nerdy_school_scene2_v1_p2
    if renpy.loadable("patch.rpy"):
        Sara "Нет! Мой брат…"
    if not renpy.loadable("patch.rpy"):
        Sara "Нет! Это же… [player_name]"
    Lily "Ты шутишь! Покажи еще раз!"
    Sara "Не в школе..."
    Lily "Боже мой!"
    MC "(Она демонстрирует фотографию моего члена!)"

    scene sis_nerdy_school_scene2_v1_p3
    Lily "Как, что, черт возьми, произошло? Почему он показывал тебе свое барахло?"
    Sara "Мы …, Мы играли в игру … Это, вышло из-под контроля немного."
    Lily "Без шуток! Вам НЕОБХОДИМО еще одно фото!"
    Sara "Еще одна фотография?"
    Lily "Да, и убедитесь, что он полностью встал."

    scene sis_nerdy_school_scene2_v1_p4
    MC "(Боже... Я должен был заставить ее удалить его, когда у меня был шанс. Я должен отправиться на следующий урок.)"
    Sara "Как именно я должна это делать?"
    Lily "Легко - подожди, пока он заснет. Потрите руку по его члену немного,потом фотографируй. Легко!"
    Sara "А … я не знаю …, Это кажется немного опасно."
    Lily "Ты же не боишься, Сара!"

    $ sis_nerdy_school_scene2_v1 = 3
    $ can1_mc_sara_night_scene1_v1 = True
    $ mc_sara_night_scene1_v1 = 1
    $ can2_sis_nerdy_school_scene1_v1 = False
    $ can_lily_scene = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump school_entrance_day1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
