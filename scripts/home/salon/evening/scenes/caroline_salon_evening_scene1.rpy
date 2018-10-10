image caroline_salon_evening_scene1_p1 = "images/home/salon/evening/scenes/caroline_salon_evening_scene1/1.jpg"
image caroline_salon_evening_scene1_p2 = "images/home/salon/evening/scenes/caroline_salon_evening_scene1/2.jpg"
image caroline_salon_evening_scene1_p3 = "images/home/salon/evening/scenes/caroline_salon_evening_scene1/3.jpg"
image caroline_salon_evening_scene1_p4 = "images/home/salon/evening/scenes/caroline_salon_evening_scene1/4.jpg"

label caroline_salon_evening_scene1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_salon_can_evening_scene1 == False:
        show screen salon_evening_notclickable
        MC "Я уже говорил с ней."
        jump salon_morning1
    if caroline_salon_can_evening_scene1 == True:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
        scene caroline_salon_evening_scene1_p1 with dissolve
        $ can_hide_windows = True
        MC "Привет, Кэролайн!"
        Caroline "Привет!"
        MC "Ты не одета?"
        Caroline "Что ты имеешь в виду? Я ношу верх."
        MC "(Да, я думаю, она считает, трусики “повседневной одеждой”.)"
        MC "Неважно. Как дела??"
        Caroline "У меня есть кое что вещей на уме , но оно не стоит того, чтобы жаловаться."
        Caroline "Как насчет тебя? Что ты делаешь дома в такое время? Парень твоего возраста должен быть на вечеринке."
        window hide
        menu:
            "Я пришел домой, чтобы увидеть лучшую сестру в мире." if renpy.loadable("patch.rpy"):
                scene caroline_salon_evening_scene1_p2
                MC "Я просто пришел домой, чтобы увидеть лучшую сестру в мире."
                Caroline "О, действительно? Как приятно."
                MC "Да, я все еще еще не нашел Сару. Ха-ха!"

                scene caroline_salon_evening_scene1_p1
                Caroline "Ahh, you bastard! Haha!"
                MC "Прости, Кэролайн. Не смог устоять."
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ caroline_salon_can_evening_scene1 = False
                $ can_hide_windows = False
                jump salon_morning1
            "Я пришел домой, чтобы увидеть лучшего друга в мире." if not renpy.loadable("patch.rpy"):
                scene caroline_salon_evening_scene1_p2
                MC "Я просто пришел домой, чтобы увидеть лучшего друга в мире."
                Caroline "О, правда? Как приятно."
                MC "Да, но я до сих пор не нашел Сару. Хаха!"

                scene caroline_salon_evening_scene1_p1
                Caroline "Ах, ты ублюдок! Хаха!"
                MC "Прости, Кэролайн. Не смог устоять."
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ caroline_salon_can_evening_scene1 = False
                $ can_hide_windows = False
                jump salon_morning1
            "Нет, никто не приглашает меня на вечеринки после того фиаско с миссис Селией.":
                scene caroline_salon_evening_scene1_p3
                MC "Да... в последнее время меня не приглашают на вечеринки."
                MC "Вероятно, это связано с фиаско с миссис Селией."
                Caroline "Боже... Мне жаль это слышать."

                scene caroline_salon_evening_scene1_p4
                Caroline "Я хотела бы дать тебе несколько советов, которые бы исправили это."
                Caroline "Но... честно говоря, даже не знаю с чего начать."
                MC "Все в порядке, Кэролайн. Спасибо в любом случае."
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ caroline_salon_can_evening_scene1 = False
                $ can_hide_windows = False
                jump salon_morning1
            "Я просто пришел домой, чтобы оттохнуть.":
                scene caroline_salon_evening_scene1_p2
                MC "Я просто пришел домой, чтобы отдохнуть некоторое время."
                Caroline "Классно. Весело провести время."
                MC "Спасибо, Кэролайн. Ты невероятная."

                scene caroline_salon_evening_scene1_p3
                Caroline "Простое изучение маркетинговых идей."
                Caroline "Знаешь [player_name], я должна сказать тебе..."

                scene caroline_salon_evening_scene1_p4
                Caroline "Я никогда не думала, что управлять бизнесом будет так сложно!"
                Caroline "Хотелось, чтобы был простой способ бросить бизнес. Может быть, с ежемесячной подпиской для пользователей? Как веб-сайт!"
                Caroline "Черт - такая система может даже использоваться для финансирования небольших разработчиков игр и художников!"

                scene caroline_salon_evening_scene1_p2
                Caroline "Я сумасшедшая, [player_name], или это звучит как хорошая идея?"

                scene caroline_salon_evening_scene1_p4
                Caroline "Вообще-то, не отвечай! Это было бы просто еще одно плохое финансовое вложение!"
                MC "Не будьте слишком строгая к себе, Кэролайн!"
                MC "Это звучит как хорошая идея , но тебе, вероятно, придется начать принимать сложные решения, например, произвольно запрещать определенных создателей Контента, если тебе не нравится их материал."
                Caroline "Правда - ее наверняка затопят извращенцы, делая грязные секс-игры."
                MC "Тебе лучше просто придерживаться твоего магазина одежды."

                scene caroline_salon_evening_scene1_p1
                Caroline "Да, ты прав, [player_name]. Благодарю!"
                MC "Классно. Увидимся позже, Кэролайн!"
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ caroline_salon_can_evening_scene1 = False
                $ can_hide_windows = False
                jump salon_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
