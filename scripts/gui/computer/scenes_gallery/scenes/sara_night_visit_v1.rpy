label sara_night_visit_v1:
    hide screen scenes_gallery
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
        Sara "Я сделаю что угодно! Только не говори Папе!"

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
            jump after_mc_sara_night_scene1_v1_choice1r
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
            jump after_mc_sara_night_scene1_v1_choice1r

label after_mc_sara_night_scene1_v1_choice1r:

    scene mc_sara_night_scene1_v1_p19
    MC "(ЗЕВОК!)"
    MC "(Похоже, Сара ушла ночью. Интересно, когда она сбежала. Я, наверное, увижу ее сегодня в школе.)"
    MC "(Я никогда не видел ее такой эмоциональной.)"
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
