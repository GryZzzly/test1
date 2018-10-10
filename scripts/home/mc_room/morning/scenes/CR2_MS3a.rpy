


label CR2_MS3a_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene CR2_MS3_p1 with dissolve
    $ can_hide_windows = True
    MC "Что случилось? Ты снова мрачная."
    Caroline "Все не так ... прости, мне пора идти."
    MC "Подожди, что случилось?"

    scene CR2_MS3_p2

    Caroline "Вещи не продаються в магазине так быстро, как я первоначально думала."
    MC "О нет... Все в порядке?"
    Caroline "Не совсем ... я должен сто пятьдесят за аренду, за магазин."
    Caroline "Мне было интересно…"

    scene CR2_MS3_p1

    MC "Ты хотела спросить, могу ли я одолжить??"
    Caroline "Мне очень жаль, [player_name]. Я не хочу быть обузой."
    window hide
    menu:
        "Да, у меня тут 150 долларов. Держи. (недоступно)" if inventory.money < 150:
            $ can_hide_windows = False
            jump mc_room_morning1

        "{color=#00ff00}Да, у меня тут 150 долларов. Держи.{/color}" if inventory.money >= 150:
            scene CR2_MS3_p3

            MC "Это было сто пятьдесят долларов, правда?"
            Caroline "Да."
            MC "К счастью для тебя, у меня есть."
            Caroline "Действительно?"

            scene CR2_MS3_p4

            Caroline "Ты уверен, что я могу просто взять их?"
            MC "Абсолютно! Я сказал это в прошлый раз, и скажу еще раз - ты моя сестра. Мы должны заботиться друг о друге."
            Caroline "Огромное спасибо!"

            scene CR2_MS3_p5

            Caroline "Никогда не знал, что ты так обо мне заботишься. Очень мило с твоей стороны сделать такое."
            MC "Пожалуйста, не думайте ничего об этом."

            scene CR2_MS3_p6

            Caroline "Я действительно счастливая девушка. Ты знаешь?"
            Caroline "*Mwah!*"
            MC "(Она действительно поцеловала меня! Кэролайн не делала этого... годами.!)"

            scene CR2_MS3_p7

            Caroline "Вообще-то, прежде чем я уйду ... всего один короткий вопрос."
            MC "Да, Кэролайн?"
            Caroline "Ты даешь мне эти деньги, потому что…"
            Caroline "..."

            scene CR2_MS3_p8

            MC "Потому что, Кэролайн?"
            Caroline "Неважно. Встретимся у входа в наш дом сегодня вечером, и мы поговорим об этом."
            MC "Ладно, увидимся там."
            Caroline "Спасибо снова, [player_name]."
            $ CR2_MS3a = False
            $ CR2_NS2 = True
            $ inventory.drop_money(150)
            $ sms3_fromC = True
            $ CR2_ES2 = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1
        "Извини, у меня сейчас нет 150 долларов.":

            scene CR2_MS3_p2

            MC "Мне очень жаль, Кэролайн. У меня сейчас нет таких денег.."
            Caroline "Все в порядке, я могу отложить все на несколько дней.."
            MC "Мне очень жаль."
            Caroline "Не извиняйся. Это не твоя вина."
            $ can_CR2_MS3a = True
            $ CR2_MS3a = False
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
