image CR2_MS3_p1 = "images/home/mc_room/morning/scenes/CR2_MS3/1.jpg"
image CR2_MS3_p2 = "images/home/mc_room/morning/scenes/CR2_MS3/2.jpg"
image CR2_MS3_p3 = "images/home/mc_room/morning/scenes/CR2_MS3/3.jpg"
image CR2_MS3_p4 = "images/home/mc_room/morning/scenes/CR2_MS3/4.jpg"
image CR2_MS3_p5 = "images/home/mc_room/morning/scenes/CR2_MS3/5.jpg"
image CR2_MS3_p6 = "images/home/mc_room/morning/scenes/CR2_MS3/6.jpg"
image CR2_MS3_p7 = "images/home/mc_room/morning/scenes/CR2_MS3/7.jpg"
image CR2_MS3_p8 = "images/home/mc_room/morning/scenes/CR2_MS3/8.jpg"


label CR2_MS3_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_MS3_p1 with dissolve

    $ can_hide_windows = True
    MC "Что случилось, Кэролайн? Ты выглядишь немного обеспокоенной. Тебя что-то беспокоит?"
    Caroline "Нет, я имею в виду, да."
    MC "Давай присядем и поговорим об этом?"

    scene CR2_MS3_p2

    Caroline "Нет, я ... Ты помнишь то предложение, которое сделал мне? Дать мне деньги для моего бизнеса."
    MC "Да."
    if renpy.loadable("patch.rpy"):
        Caroline "Это предложение все еще... в силе? Мне действительно нужно двести долларов, чтобы заплатить за квартиру маме."
    else:
        Caroline "Это предложение все еще... в силе? Мне действительно нужно двести долларов, чтобы оплатить аренду Линде."

    scene CR2_MS3_p1

    Caroline "Я уверена, что она не будет возражать, если я пропущу месячную арендную плату... но я не хочу, чтобы она знала, что я провалилась в бизнесе."
    window hide
    menu:
        "{color=#00ff00}Конечно! держи.{/color}" if inventory.money >= 200:
            scene CR2_MS3_p3

            if renpy.loadable("patch.rpy"):
                MC "Конечно, Кэролайн! У меня здесь две cотни. И не волнуйся, я не скажу ни слова маме об этом."
            else:
                MC "Конечно, Кэролайн! У меня здесь две cотни. И не волнуйся, я не скажу ни слова Линде об этом."
            Caroline "Серьезно? Ты не должен этого делать, ты знаешь."

            MC "Расслабься. Я рад помочь."

            scene CR2_MS3_p4

            Caroline "Огромное спасибо. Ты понятия не имеешь, насколько это для меня сейчас важно."
            Caroline "Я скоро стану на ноги. Мне просто нужна небольшая помощь, чтобы вернуть мои финансы."
            Caroline "Ты реальный спасатель, [player_name]."

            scene CR2_MS3_p5

            MC "Ничего! Ты бы сделала то же самое для меня."
            Caroline "Еще раз спасибо! Я когда-нибудь верну. Обещаю."
            $ inventory.drop_money(200)
            $ CR2_MS3 = False
            $ can_CR2_MS3a = True
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1

        "Конечно, у меня двести. (недоступно)" if inventory.money < 200:
            $ can_hide_windows = False
            jump mc_room_morning1
        "Прости, Кэролайн. Мне сейчас тоже не хватает денег.":


            scene CR2_MS3_p2

            MC "Мне очень жаль, Кэролайн. У меня сейчас нет."
            Caroline "О! Точно ... мне так жаль, что я заговорила об этом."
            Caroline "Я ... я должна идти."
            $ CR2_MS3 = False
            $ can_CR2_MS2 = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
