image ml_work_day_scene1_v1_p1 = "/images/ml_work/room1/scenes/1.jpg"
image ml_work_day_scene1_v1_p2 = "/images/ml_work/room1/scenes/2.jpg"
image ml_work_day_scene1_v1_p3 = "/images/ml_work/room1/scenes/3.jpg"
image ml_work_day_scene1_v1_p4 = "/images/ml_work/room1/scenes/4.jpg"
image ml_work_day_scene1_v1_p5 = "/images/ml_work/room1/scenes/5.jpg"
image ml_work_day_scene1_v1_p6 = "/images/ml_work/room1/scenes/6.jpg"
image ml_work_day_scene1_v1_p7 = "/images/ml_work/room1/scenes/7.jpg"
image ml_work_day_scene1_v1_p8 = "/images/ml_work/room1/scenes/8.jpg"
image ml_work_day_scene1_v1_p9 = "/images/ml_work/room1/scenes/9.jpg"
image ml_work_day_scene1_v1_p10 = "/images/ml_work/room1/scenes/10.jpg"
image ml_work_day_scene1_v1_p11 = "/images/ml_work/room1/scenes/11.jpg"
image ml_work_day_scene1_v1_p12 = "/images/ml_work/room1/scenes/12.jpg"
image ml_work_day_scene1_v1_p13 = "/images/ml_work/room1/scenes/13.jpg"
image ml_work_day_scene1_v1_p14 = "/images/ml_work/room1/scenes/14.jpg"
image ml_work_day_scene1_v1_p15 = "/images/ml_work/room1/scenes/15.jpg"

label ml_work_day_scene1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_work_day_scene1_v1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Эй, мам! Я свободен."
    if not renpy.loadable("patch.rpy"):
        MC "Эй, Линда! Я сейчас не занят."
    Mom "Добрый день, милый! Позвольте мне посмотреть, нужно сделать."
    Mom "Хмм…"

    scene ml_work_day_scene1_v1_p2
    Mom "Сейчас мы работаем над документами и базами данных."
    Mom "Однако на прошлой неделе у нас заболела уборщица. Она вывихнула лодыжку и не сможет работать пару месяцев."
    Mom "Если ты уберешь в офисе, я дам тебе 25 долларов."
    MC "Что мне нужно делать?"
    Mom "Собрать и вывезти весь мусор, убрать бумагу."
    Mom "Просто убедись, что не выбросил ничего нужного!"
    if renpy.loadable("patch.rpy"):
        MC "Ладно, мам. Я буду осторожен!"
    if not renpy.loadable("patch.rpy"):
        MC "Хорошо, Линда. Я буду осторожен!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump work_minigame_room1_label

label ml_work_day_scene1_v1_label_after_minigame:
    $ renpy.music.stop(channel="music2", fadeout=1)
    scene black
    $ can_hide_windows = True
    MC "Фу! (это выглядит как последний пиздец.)"
    if renpy.loadable("patch.rpy"):
        MC "(Офис мамы выглядит неплохо!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Офис Линды выглядит неплохо!)"
    MC "(Я пойду и скажу, что я закончил.)"
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene ml_work_day_scene1_v1_p3 with dissolve
    MC "Привет снова! Я поубирал."
    Mom "Отличная работа! Вот $25, как и было обещано."
    $ inventory.earn(25)
    if renpy.loadable("patch.rpy"):
        MC "(Это не много, но это лучше, чем постоянно просить папу!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Это не много, но это лучше, чем постоянно умолять Боба!)"

    scene ml_work_day_scene1_v1_p4
    Mom "(Уборщица получала 40 долларов за работу [player_name], но теперь, когда я привлекла его внимание, можно давать ему болше денег!)"
    Mom "Скажите - ты хотел бы заработать еще 50 долларов??"
    MC "(Еще 50 долларов? Это принесет мне до 75 долларов. Я мог бы реально использовать наличные деньги.)"
    MC "Да, что ты хочешь, чтобы я сделал?"
    Mom "Я хочу ... снова сыграть в игру."
    MC "Игру?"
    Mom "В ту, которую мы играли в машине."
    MC "(Глоток.)"

    scene ml_work_day_scene1_v1_p1
    $ ml_work_day_scene1_v1_q1 = True
    $ ml_work_day_scene1_v1_q2 = True
    $ ml_work_day_scene1_v1_q3 = True
    jump ml_work_day_scene1_v1_menu

label ml_work_day_scene1_v1_menu:
    scene ml_work_day_scene1_v1_p1
    Mom "Well? What do you say?"
    menu:

        "Ты ... любишь меня больше, чем сына?" if ml_work_day_scene1_v1_q1 == True and renpy.loadable("patch.rpy"):
            MC "Прежде чем я скажу «да», я хочу знать ... ты любишь меня больше, чем сына?"
            Mom "Я не поняла, что ты имеешь в виду."
            scene ml_work_day_scene1_v1_p2
            MC "Я имею в виду, я тебе нравлюсь?"
            Mom "Ой, да ладно. Не глупи, [player_name]."
            $ ml_work_day_scene1_v1_q1 = False
            jump ml_work_day_scene1_v1_menu

        "Ты любишь меня?" if ml_work_day_scene1_v1_q1 == True and not renpy.loadable("patch.rpy"):
            MC "Прежде чем я скажу «да», я хочу знать ... ты  меня любишь?"
            Mom "Я не понимаю, что ты имеешь в виду."
            scene ml_work_day_scene1_v1_p2
            MC "Я имею в виду, я тебя привлекаю??"
            Mom "О, да ладно.Глупый, [player_name]."
            $ ml_work_day_scene1_v1_q1 = False
            jump ml_work_day_scene1_v1_menu

        "Почему ты хочешь снова сыграть в эту игру?" if ml_work_day_scene1_v1_q2 == True:
            MC "Почему ты хочешь снова сыграть в эту странную игру?"
            Mom "Что это значит для тебя? Это легко если ты согласен на 50$."
            MC "(Хм ... Она уклоняеться от ответа.)"
            $ ml_work_day_scene1_v1_q2 = False
            jump ml_work_day_scene1_v1_menu

        "Ты собираешься поцеловать меня снова?" if ml_work_day_scene1_v1_q3 == True:
            MC "Ты хочешь попробовать поцеловать меня снова?"
            scene ml_work_day_scene1_v1_p4
            Mom "Кто знает, что произойдет?"
            Mom "И почему тебя это волнует? Это не то, как я поцеловала тебя раньше."
            $ ml_work_day_scene1_v1_q3 = False
            jump ml_work_day_scene1_v1_menu
        "{color=#00ff00}Хорошо, я готов.{/color}":
            jump ml_work_day_scene1_v1_menu_after

label ml_work_day_scene1_v1_menu_after:
    scene ml_work_day_scene1_v1_p4
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)
    MC "Хорошо, я готов."
    Mom "Не двигайся. Две минуты начинаются."

    scene ml_work_day_scene1_v1_p5
    MC "(Один.. два.. три…)"
    MC "(О мой Бог! Она поднимает мою футболку?!)"
    Mom "(Мое сердце гоняется. Интересно, как долго я смогу продержаться.)"
    Mom "(У меня будет достаточно времени, чтобы увидеть его твердый член?)"

    scene ml_work_day_scene1_v1_p6
    Mom "Ах ах - не двигайся! Мы только что начали, милый."
    MC "Я ... ах…"
    Mom "Не разговаривать. Язык тоже считается мышцей, ты знаешь!"

    scene ml_work_day_scene1_v1_p7
    if renpy.loadable("patch.rpy"):
        MC "(Дерьмо! Она моя мать!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Дерьмо! Она мой друг!)"
    MC "(Я имею в виду ... Мне определенно становится трудно сейчас ... но это неправильно. Разве это не так?)"
    MC "Осторожно! Я падаю назад!"

    scene ml_work_day_scene1_v1_p8
    MC "Вууууух!"
    Mom "(Oooх! Захватывающие!)"
    if renpy.loadable("patch.rpy"):
        MC "(Боже! Мама полностью потеряла контроль над собой!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Боже! Линда полностью потеряла контроль над собой!)"

    scene ml_work_day_scene1_v1_p9
    Mom "(Ммм! Мне нравится эта позиция!)"
    if renpy.loadable("patch.rpy"):
        MC "М-мама! Подожди!"
    if not renpy.loadable("patch.rpy"):
        MC "Линда! Подожди!"
    Mom "(Да? Что на него нашло? На этот раз он больше сопротивляеться.)"

    scene ml_work_day_scene1_v1_p10
    Mom "Что случилось, милый?"
    Mom "Ты хочешь, чтобы я продолжала или нет?"
    menu:
        "Да.":
            scene ml_work_day_scene1_v1_p10

            MC "Да... Да."
            MC "Я просто немного ошеломлен"
            jump ml_work_day_scene1_v1_menu_after2
        "Нет.":

            MC "Я не знаю…"
            MC "Это немного слишком…."
            jump ml_work_day_scene1_v1_menu_after2
label ml_work_day_scene1_v1_menu_after2:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene ml_work_day_scene1_v1_p11
    Mom "(Боже мой... Что я делаю?)"
    if renpy.loadable("patch.rpy"):
        Mom "(Не могу поверить, что я так низко пала. Какая мать пытается изнасиловать своего сына?!)"
    if not renpy.loadable("patch.rpy"):
        Mom "(Я не могу поверить, что я пала так низко... Даже пытаться изнасиловать его?!)"
    Mom "Я... Мне так жаль."
    if renpy.loadable("patch.rpy"):
        MC "Мам, я.."
    if not renpy.loadable("patch.rpy"):
        MC "Линда, я.."

    scene ml_work_day_scene1_v1_p12
    Mom "Мне так жаль, [player_name]."
    if renpy.loadable("patch.rpy"):
        MC "Все в порядке, мам."
    if not renpy.loadable("patch.rpy"):
        MC "Все в порядке, Линда."
    Mom "Нет, не в порядке."
    Mom "Я всегда так чувствовала."

    scene ml_work_day_scene1_v1_p13
    Mom "Я слерживала свои эмоции так долго."
    Mom "Я держала все это внутри,-а иногда, я позволил себе фантазировать о тебе."
    Mom "Но я всегда чувствовала себя такой виноватым потом."
    Mom "Это было, тогда, когда ты начинал хотеть встречаться с другими женщинами, что я, наконец, сломалась."
    Mom "Я… (сопит) Я не могу выносить мысль о том, что ты романтически связан с кем-то еще."

    scene ml_work_day_scene1_v1_p14
    if renpy.loadable("patch.rpy"):
        MC "Тшшш - все в порядке, мама. Расслабься."
    if not renpy.loadable("patch.rpy"):
        MC "Тшшш - все в порядке, мама. Расслабься."
    MC "Ты знаешь, что я люблю..."

    scene ml_work_day_scene1_v1_p15
    Mom "Нет. Нет.."
    Mom "Я не хочу слышать об этом."
    Mom "Я чувствую себя куском дерьма, после того, что я сделал с тобой сегодня."
    Mom "Просто ... подумайте обо всем, что я вам сказала, и ... дайте мне знать завтра утром. Хорошо?"
    if renpy.loadable("patch.rpy"):
        MC "Хорошо мам, мама."
    if not renpy.loadable("patch.rpy"):
        MC "Окей, Линда."
    $ inventory.earn(50)
    $ day_time += 1
    $ ml_work_day_scene1 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ ml_bedroom_morning_scene6 = True
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
