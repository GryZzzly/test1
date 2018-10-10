image celia_webcam_evening_scene1_v1_p1 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/1.jpg"
image celia_webcam_evening_scene1_v1_p2 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/2.jpg"
image celia_webcam_evening_scene1_v1_p3 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/3.jpg"
image celia_webcam_evening_scene1_v1_p4 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/4.jpg"
image celia_webcam_evening_scene1_v1_p5 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/5.jpg"
image celia_webcam_evening_scene1_v1_p6 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/6.jpg"
image celia_webcam_evening_scene1_v1_p7 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/7.jpg"
image celia_webcam_evening_scene1_v1_p8 = "images/web_cam_scenes/celia_webcam_evening_scene1_v1/8.jpg"

screen celia_webcam_evening_screen_v1:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("celia_webcam_evening_screen_v1"),Jump("celia_webcam_evening_scene1_v1_label")]
screen celia_webcam_evening_screen1_v1:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        clicked [Jump("celia_webcam_evening_scene1_v1_label2")]
    timer 4.00 action [Hide ("celia_webcam_evening_screen1_v1"),Jump("celia_webcam_evening_scene1_v1_label2")]









label celia_webcam_scenes:
    if celia_webcam_introdution_v1 == 1:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Rhinoceros.mp3', channel="music1", loop=True, fadein = 2)
        show screen live_camera_screen
        show screen celia_webcam_evening_screen1_v1
        show screen celia_webcam_evening_screen_v1
        MC "(О Боже... она онлайн! Мое сердце колотится!)"
    if celia_webcam_menuv1 == True:
        hide screen main_deskop_pcv1
        hide screen live_camera_screen
        jump celia_webcam_scenes_menu1










label celia_webcam_evening_scene1_v1_label:
    $ renpy.sound.play('/sfx/phone_call.mp3', loop=False)
    MC "(Хорошо, я лучше удостоверюсь, что моя веб-камера закрыта.)"



label celia_webcam_evening_scene1_v1_label2:
    $ renpy.sound.stop(channel="sound")
    hide screen main_deskop_pcv1
    hide screen live_camera_screen
    hide screen celia_webcam_evening_screen1_v1
    hide screen celia_webcam_evening_screen_v1
    scene celia_webcam_evening_scene1_v1_p1 with dissolve
    Celia "Привет?! Кто это?"
    MC "(Лучше использовать более глубокий голос, чем обычно.)"
    MC "Я вижу, ты получила мое письмо, миссис Селия."
    Celia "Я не знаю, кто ты, черт возьми, но когда я найду тебя, я выбью из тебя всю дурь!"

    scene celia_webcam_evening_scene1_v1_p2
    Celia "И где ты, чёрт возьми?! Включи веб-камеру, трус!"
    Celia "Если ты собираешься угрожать мне, то по крайней мере, покажи лицо!"
    MC "Я не буду этого делать, миссис Селия."
    Celia "Прекрасно! Тогда я иду."

    scene celia_webcam_evening_scene1_v1_p3
    MC "Ты можешь уйти, а я , тем временем, выложу в интернет фото где ты торгуешь оценками."
    MC "И я не буду останавливаться на достигнутом. Я прослежу, чтобы директор получил копию, как и полиция."
    MC "Ты коррумпированная женщина, миссис Селия. И теперь придется заплатить."

    scene celia_webcam_evening_scene1_v1_p4
    Celia "Черт возьми... чего ты от меня хочешь??"
    MC "Не слишком много. У меня есть только несколько требований."
    MC "Во-первых, я хочу общаться с тобой каждый вечер. Давай сделаем это обычным делом."
    Celia "…"
    Celia "Тьфу! Отлично! (Не похоже что у меня есть выбор..)"
    Celia "И твое второе требование?"
    MC "Я хочу, чтобы ты раздевалась до нижнего белья."

    scene celia_webcam_evening_scene1_v1_p5
    Celia "Что?! Клянусь Богом, я узнаю, кто ты, чертов извращенец.!"
    MC "Вряд ли это правильный способ поговорить с парнем, у которого достаточно доказательств, чтобы тебя уволили с работы."
    MC "А теперь сними это платье, пока я не связался с директором!"
    Celia "…"

    scene celia_webcam_evening_scene1_v1_p6
    MC "МММ... Классная задница, миссис Селия."
    Celia "Да пошёл ты…"
    MC "(Черт, у миссис Селии очень милая попка! Может быть, я трахну ее когда-нибудь?)"

    scene celia_webcam_evening_scene1_v1_p7
    MC "(Ммм! И хорошие сиськи тоже! Я не могу дождаться, чтобы увидеть ее без лифчика.)"
    MC "(Но, вероятно, следует подождать, я должен следовать советам Джуди, и действовать постепенно.)"

    scene celia_webcam_evening_scene1_v1_p8
    Celia "Хорошо? Это моё платье. Что ты хочешь сейчас, извращенец?"
    MC "Этого хватит на сегодня. Я просто хотел, чтобы ты знала, кто держит власть."
    MC "Мы собираемся поболтать снова, завтра вечером. Я хотел бы видеть тебя в нижнем белье, когда мы начинаем болтать."
    Celia "(Ебать... Мне нужно выяснить, кто этот урод, или я в серьезном дерьме.)"
    MC "Увидимся завтра, красивая."
    $ day_time = 4
    $ celia_webcam_introdution_v1 = 3
    $ celia_webcam_menuv1 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    jump mc_room_night1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
