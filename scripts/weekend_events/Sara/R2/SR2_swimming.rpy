image SR2_weekend_swimming_p1 = "images/Weekend_Events/Sara/R2/Swimming/1.jpg"
image SR2_weekend_swimming_p2 = "images/Weekend_Events/Sara/R2/Swimming/2.jpg"
image SR2_weekend_swimming_p3 = "images/Weekend_Events/Sara/R2/Swimming/3.jpg"
image SR2_weekend_swimming_p4 = "images/Weekend_Events/Sara/R2/Swimming/4.jpg"
image SR2_weekend_swimming_p5 = "images/Weekend_Events/Sara/R2/Swimming/5.jpg"
image SR2_weekend_swimming_p6 = "images/Weekend_Events/Sara/R2/Swimming/6.jpg"
image SR2_weekend_swimming_p7 = "images/Weekend_Events/Sara/R2/Swimming/7.jpg"

label SR2_swimming_label:
    if SR2_after_swimming == True:
        show screen swimming_poll_scr
        $ can_hide_windows = False
        $ clickable = False
        MC "Мы уже были там."
        $ music_continue = False
        $ clickable = True
        jump swimming_poll_label
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)

        scene SR2_weekend_swimming_pool_p2
        $ can_hide_windows = True
        MC "Как насчет того, что я пойду купаться, а ты можешь спокойно посидеть в розовой игрушке фламинго?"
        Sara "Hмм… я не знаю. Это довольно страшно."
        MC "Расслабьтесь-я буду рядом с тобой, чтобы убедиться, что ты не упала."
        Sara "Тогда хорошо."

        scene SR2_weekend_swimming_p1

        MC "Видишь? Не о чем беспокоиться."
        Sara "Я... Я так думаю..."
        MC "Ты все еще выглядишь немного нервной."
        Sara "Да, я немного боюсь воды."

        scene SR2_weekend_swimming_p2

        MC "О, так было бы очень страшно, если бы поплавок начал опрокидываться?"
        Sara "НЕТ! Не смей!"
        MC "Ой-ой! Сигнал бедствия! Сигнал бедствия! Мы спускаемся вниз.!"
        Sara "ОСТАНОВИ ЭТО, [player_name]!"


        scene SR2_weekend_swimming_p3

        Sara "AAAХХХХ!"
        MC "Это американский розовый Фламинго. У нас пробоина. Мы тонем!"
        Sara "СТОП! СТОП! НЕЕЕТТТ!"
        MC "Хахахахаха!"

        scene SR2_weekend_swimming_p4

        Sara "Хмм! Это не смешно, [player_name]!"
        Sara "Я могла утонуть!"
        MC "Бассейн всего шесть футов!"
        Sara "А я всего лишь пять футов!"
        MC "Хорошо. Извини, Сара. Я не буду делать это снова."
        Sara "Хорошо бы."
        MC "Да?"
        Sara "Я сказала, тебе лучше не делать этого снова!"
        MC "Я не могу тебя слышать. Здесь сейчас слишком громко. Ты можешь наклониться?"

        scene SR2_weekend_swimming_p5

        MC "(Хехе. Она влюбилась в него!)"
        Sara "Я сказала, лучше не пытайся опрокинуть поплавок сно.."

        scene SR2_weekend_swimming_p6

        Sara "Mmpff!"
        MC "Mwah…"
        Sara "(Сволочь! Он обманул меня!)"
        MC "Хехе. Попалась!"

        scene SR2_weekend_swimming_p7
        if renpy.loadable("patch.rpy"):
            Sara "Брат…"
            MC "Может быть, не называй меня «Братом» слишком громко. Мы в общественном месте, в конце концов."
        else:
            Sara "[player_name]…"
        Sara "Хе-хе ... О да."
        MC "Все еще сердишься на меня?"
        Sara "Нет. Извинение принято. Просто … не делай этого снова, хорошо?"
        MC "Хорошо."

        scene SR2_weekend_swimming_p6

        MC "Mwah!"
        Sara "(О МОЙ БОГ! ЕЩЕ РАЗ?!)"

        scene SR2_weekend_swimming_p7

        MC "Хаха! Простите! Я не могл устоять. Я люблю это милое, потрясенное выражение, которое ты делаешь, каждый раз, когда я тебя целую."
        Sara "Хе-хе ... ты плохой, ты знаешь?"
        MC "Я знаю."
        Sara "Ха-ха! Ладно, давай назовем этот день.."
        $ SR2_after_swimming = True
        $ can_hide_windows = False
        jump swimming_poll_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
