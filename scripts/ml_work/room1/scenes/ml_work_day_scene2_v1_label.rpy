image ml_work_day_scene2_v1_p1 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/1.jpg"
image ml_work_day_scene2_v1_p2 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/2.jpg"
image ml_work_day_scene2_v1_p3 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/3.jpg"
image ml_work_day_scene2_v1_p4 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/4.jpg"
image ml_work_day_scene2_v1_p5 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/5.jpg"
image ml_work_day_scene2_v1_p6 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/6.jpg"
image ml_work_day_scene2_v1_p7 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/7.jpg"
image ml_work_day_scene2_v1_p8 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/8.jpg"
image ml_work_day_scene2_v1_p9 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/9.jpg"
image ml_work_day_scene2_v1_p10 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/10.jpg"
image ml_work_day_scene2_v1_p11 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/11.jpg"
image ml_work_day_scene2_v1_p12 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/12.jpg"
image ml_work_day_scene2_v1_p13 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/13.jpg"
image ml_work_day_scene2_v1_p14 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/14.jpg"
image ml_work_day_scene2_v1_p15 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/15.jpg"
image ml_work_day_scene2_v1_p16 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/16.jpg"
image ml_work_day_scene2_v1_p17 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/17.jpg"
image ml_work_day_scene2_v1_p18 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/18.jpg"
image ml_work_day_scene2_v1_p19 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/19.jpg"
image ml_work_day_scene2_v1_p19a = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/19a.jpg"
image ml_work_day_scene2_v1_p20 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/20.jpg"
image ml_work_day_scene2_v1_p21 = "/images/ml_work/room1/scenes/ml_work_day_scene2_V1/21.jpg"

image ml_work_day_scene2_v1_p6anim = Movie(play="videos/Linda-AfternoonS2-1.webm", loop = True )
image ml_work_day_scene2_v1_p6anim2 = Movie(play="videos/Linda-AfternoonS2-2.webm", loop = True )
image ml_work_day_scene2_v1_p15anim = Movie(play="videos/Linda-AfternoonS2-4.webm", loop = True )
image ml_work_day_scene2_v1_p17anim = Movie(play="videos/Linda-AfternoonS2-3.webm", loop = True )
image ml_work_day_scene2_v1_p18anim = Movie(play="videos/Linda-AfternoonS2-5.webm", loop = True )
label ml_work_day_scene2_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene ml_work_day_scene2_v1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Привет мама! Это опять я."
    if not renpy.loadable("patch.rpy"):
        MC "Привет, Линда! Это снова я."
    Mom "Прекрасно! Будешь делать то же, что и в прошлый раз."
    Mom "25 долларов нормальная цена??"
    MC "Конечно. Нет проблем."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump work_minigame_room2_label

label ml_work_day_scene2_v1_label_after_work:
    scene black
    $ can_hide_windows = True
    $ renpy.music.stop(channel="music2", fadeout=1)
    MC "(Это я сделал.)"
    if renpy.loadable("patch.rpy"):
        MC "(Пора вернуться к маме и получить свои деньги.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Пора вернуться к Линде и получить свои деньги.)"
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_work_day_scene1_v1_p3 with dissolve
    MC "Вот и все."
    Mom "Чудесно!"

    scene ml_work_day_scene1_v1_p4
    Mom "Скажи - мы можем  посидеть на диване некоторое время?"
    MC "Конечно."

    scene ml_work_day_scene2_v1_p2
    MC "(Она просто села на мое колено! Неожиданно!)"
    Mom "У тебя красивые глаза, [player_name]. Ты знаешь?"
    if renpy.loadable("patch.rpy"):
        MC "Спасибо, мама."
    if not renpy.loadable("patch.rpy"):
        MC "Спасибо, Линда."
    Mom "На самом деле. Я могу смотреть в них часами."

    scene ml_work_day_scene2_v1_p3
    MC "(Глоток!)"
    Mom "Ты выглядишь немного нервным."
    Mom "You shouldn’t be. I promise, you’re in very safe hands right now."
    Mom "Попробуйте расслабиться. Положи руку на мое бедро."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)

    scene ml_work_day_scene2_v1_p4
    Mom "Ну вот. Видишь?"
    Mom "Я слышу как стучит твое сердце."
    Mom "Просто успокойся, и закрой глаза."
    Mom "Я обещаю, тебе понравится."

    scene ml_work_day_scene2_v1_p5
    MC "(Боже мой ... Это действительно так. Она больше не пугает меня!)"
    MC "(Как далеко она собирается зайти? Просто поцелуй?)"

    scene ml_work_day_scene2_v1_p6
    Mom "Mмм…"
    scene ml_work_day_scene2_v1_p6anim with dissolve
    MC "Mмм!"
    scene ml_work_day_scene2_v1_p6anim2
    MC "(Ничего себе! Она - удивительно целуется!)"

    scene ml_work_day_scene2_v1_p7
    Mom "(Боже … Это еще лучше, чем я мечтал.)"
    Mom "(Хотел бы я просто заморозить этот момент и остаться в нем навсегда.)"
    if renpy.loadable("patch.rpy"):
        MC "(Мама тоже должно быть нервничает - ее сердце бьется громче моего!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Линда тоже должно быть нервничает - ее сердце бьется громче моего!)"

    scene ml_work_day_scene2_v1_p8
    Mom "Ложись на диван. Я хочу что-то сделать."
    MC "Что-то сделать? Что именно?"
    if renpy.loadable("patch.rpy"):
        Mom "Тише... Просто ляг и расслабься. Мама позаботиться обо всем."
    if not renpy.loadable("patch.rpy"):
        Mom "Тише... Просто ляг и расслабься. Линда будет заботиться обо всем."

    scene ml_work_day_scene2_v1_p9
    MC "Oooхх…."
    MC "(Срань господня... Ее пальци вьються вокруг моего члена.)"
    MC "(Она массирует его.)"

    scene ml_work_day_scene2_v1_p10
    if renpy.loadable("patch.rpy"):
        MC "М-мама! Ты.."
    if not renpy.loadable("patch.rpy"):
        MC "Линда. Т-ты.."
    Mom "Тише... Я вижу, у тебя есть большая проблема."
    if renpy.loadable("patch.rpy"):
        Mom "Пусть мать разберется."
    if not renpy.loadable("patch.rpy"):
        Mom "Позволь мне помочь тебе разобраться."

    scene ml_work_day_scene2_v1_p11
    Mom "(Ммм... Он такой большой!)"
    Mom "(Мне бы очень хотелось почувствовать это чудовище внутри моей киски!)"
    Mom "(Боже, я стаю мокрой от одной мысли об этом!)"

    scene ml_work_day_scene2_v1_p12
    Mom "Тебе нравиться, когда я обнимаю твой член пальцами?"
    MC "О да..."
    Mom "Я скажу тебе, почему это так чувствительно."

    scene ml_work_day_scene2_v1_p13
    Mom "Это называется уздечкой - и это чувствительная небольшая группа нервов."
    Mom "Трюк заключаеться в том, чтобы быстро щелкнуть языком по нему."
    Mom "Ни один парень не мог продержаться тридцать секунд, когда я делала ему минет."

    scene ml_work_day_scene2_v1_p14
    Mom "Но достаточно прелюдии - давайте приступим к делу."
    MC "Aх! Aхх… Ooххх!"
    Mom "Ммм... Похоже, мой мальчик наслаждается этим."

    scene ml_work_day_scene2_v1_p15
    MC "Oooх!"
    scene ml_work_day_scene2_v1_p15anim
    if renpy.loadable("patch.rpy"):
        MC "(Боже мой! Я никогда не думал, что мама такая странная!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Боже мой! Я никогда не думал, что мама такая странная!)"
    Mom "(Ха-ха! Я почувствовала, как он содрогнулся, когда я облизнула его. Он кончит в мгновение ока.)"

    scene ml_work_day_scene2_v1_p16
    Mom "Вверх и вниз…"
    Mom "Вверх... и вниз."
    Mom "Я надеюсь, ты наслаждаешься этим так же, как я."

    scene ml_work_day_scene2_v1_p17
    MC "Aхх…"
    scene ml_work_day_scene2_v1_p17anim
    Mom "Ты близко?"
    Mom "Я хочу, чтобы ты кончил для меня."

    scene ml_work_day_scene2_v1_p18
    C "Mмм! MMMMM!"
    MC "(Ебать! Я собираюсь кончить!)"
    scene ml_work_day_scene2_v1_p18anim
    Mom "Mмм…"
    Mom "(Я чувствую его член, дергающийся и пульсирующий в моей руке. Мой мальчик собирается кончить!)"

    scene ml_work_day_scene2_v1_p19
    if renpy.loadable("patch.rpy"):
        Mom "Это оно! Кончи для мамы! Хороший мальчик!"
    if not renpy.loadable("patch.rpy"):
        Mom "Это оно! Сперма для друга! Хороший мальчик!"
    MC "Aх! Ooooх! Aххх!"
    scene white with dissolve
    $ renpy.pause(1,hard=True)
    scene ml_work_day_scene2_v1_p19
    $ renpy.pause(1,hard=True)
    scene white with dissolve
    $ renpy.pause(1,hard=True)
    scene ml_work_day_scene2_v1_p19a with dissolve
    Mom "Вау ... Это много спермы! Тебе повезло, что разрешил помочь."

    scene ml_work_day_scene2_v1_p20
    Mom "Ты закончил? Или мне продолжить?"
    MC "Нет, я... Я сделал..."
    Mom "Итак, как это было? Тебе понравилось?"

    scene ml_work_day_scene2_v1_p21
    if renpy.loadable("patch.rpy"):
        MC "Это было Потрясающе, мам! Спасибо!"
    if not renpy.loadable("patch.rpy"):
        MC "Это было Потрясающе, Линда! Спасибо!"
    Mom "Я очень рада."
    Mom "Ты делаешь такое милое лицо, когда кончаешь!"
    if renpy.loadable("patch.rpy"):
        MC "Мама!"
        Mom "Ха-ха! Мне лучше вернуться к работе. Увидимся вечером."
        MC "Да, мама. еще раз спасибо."
    if not renpy.loadable("patch.rpy"):
        MC "Линда!"
        Mom "Ха-ха! Мне лучше вернуться к работе. Увидимся вечером."
        MC "Хорошо, Линда. Еще раз спасибо."
    $ inventory.earn(25)
    $ ml_work_day_scene2 = False
    $ ml_mc_room_night_scene3 = True
    $ SR2_ML = True
    $ day_time = 3
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_sms1_from_ml = True
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
