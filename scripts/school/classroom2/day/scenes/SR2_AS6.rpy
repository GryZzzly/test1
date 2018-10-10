


label SR2_AS6_label:
    if can_SR2_AS6 == False:
        $ clickable = False
        show screen classroom2_day
        MC "Я уже говорил с ней.."
        $ clickable = True
        jump classroom2_morning1

    if not lube in inventory.items:
        $ clickable = False
        show screen classroom2_day
        MC "Я до сих пор не купил смазку."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)


        scene SR2_AS3_p1 with dissolve

        MC "Я наконец-то понял, Сара. Я оставлю ее в доме до позднего вечера."
        Sara "А? Что ты получил? Я не понимаю, о чем ты говоришь."
        MC "Смазка, Сара! Помнишь?"

        scene SR2_AS3_p2

        Sara "Вы действительно купили смазку?!"
        MC "(Черт! Это как вибратор, снова и снова!)"
        MC "Тише! Говори тише.!"

        scene SR2_AS3_p3

        MC "Помнишь, мы говорили об этом на крыше? Это все упростит, когда мы наконец это сделаем."
        MC "Я уберу руку с твоего рта сейчас?"
        Sara "Mмм хмм."

        scene SR2_AS3_p4

        Sara "Что происходит сейчас?"
        MC "Приходи ко мне сегодня вечером, и мы попробуем."
        Sara "Мне страшно... в прошлый раз было так больно.."

        scene SR2_AS3_p5

        MC "На этот раз будет лучше, обещаю. Мы не были должным образом подготовлены в прошлый раз."
        MC "И если тебе будет больно - мы просто остановимся. Окей?"
        Sara "Ладно ... наверное, да. Увидимся вечером в твоей спальне.."
        MC "Я с нетерпением жду этого. Увидимся позже, Сара."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False

        $ can_SR2_AS6 = False
        $ SR2_NS4 = True
        $ S_N_inbed = False
        jump classroom2_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
