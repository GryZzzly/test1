image SR2_AS3_vibrator_p1 = "images/sex_shop/scenes/SR2_AS3_v/1.jpg"
image SR2_AS3_vibrator_p2 = "images/sex_shop/scenes/SR2_AS3_v/2.jpg"
image SR2_AS3_vibrator_p3 = "images/sex_shop/scenes/SR2_AS3_v/3.jpg"
image SR2_AS3_vibrator_p4 = "images/sex_shop/scenes/SR2_AS3_v/4.jpg"
image SR2_AS3_vibrator_p5 = "images/sex_shop/scenes/SR2_AS3_v/5.jpg"
image SR2_AS3_vibrator_p6 = "images/sex_shop/scenes/SR2_AS3_v/6.jpg"

label SR2_AS3_vibrator_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    $ can_hide_windows = True

    if SR2_AS3_v_loop == True:
        if inventory.money >= 80:
            S "У тебя есть (80$)?"
            MC "Вот, пожалуйста."
            S "Большое спасибо! Приходи снова!"
            $ inventory.buy(SR2_vibrator)
            $ can_hide_windows = False
            jump sex_shop_evening_label
        else:
            scene SR2_AS3_vibrator_p1 with dissolve
            S "У тебя есть (80$)?"
            MC "Нет."
            $ can_hide_windows = False
            jump sex_shop_evening_label
    else:
        scene SR2_AS3_vibrator_p1 with dissolve

        MC "(Это, наверное, лучшее место, где можно найти вибратор для Сары. Я понятия не имею, какой тип ее.)"
        MC "(Вероятно, я должен спросить девушку за прилавком. Она могла бы дать мне несколько советов.)"
        MC "(Черт, она такая чертовски сексуальная! Просто посмотри, сколько изгибов она демонстрирует!)"
        S "Привет? Я могу помочь? Или ты просто собираешься смотреть на меня?"
        MC "Я ... я ... хотел купить вибратор."

        scene SR2_AS3_vibrator_p2

        S "Ооо, парень, покупающий вибратор ... странно."
        if renpy.loadable("patch.rpy"):
            MC "Нет! Это не для меня! Это для моей сестры!"
            S "Для сестры?!"
        else:
            MC "Нет! Это не для меня! Это для моего друга!"
            S "Для друга?!"
        MC "(FUCK!)"
        MC "Извини! Я имею в виду, моя ... э-э ... моей девушке. Извини, я сейчас просто нервничаю."

        scene SR2_AS3_vibrator_p1
        if renpy.loadable("patch.rpy"):
            S "Хе-хе ... Это нормально. Итак, твоя сестра, я имею в виду, “подруга”, использовала вибратор раньше?"
        else:
            S "Хе-хе ... Это нормально. Итак, твой друг, я имею в виду, “подруга”, использовала вибратор раньше?"
        MC "Нет, моя девушка - нет. Я думал купить ей что-то слабое для новичков?"
        MC "Знаешь, тот, который не слишком силен и может быть меньше среднего?"

        scene SR2_AS3_vibrator_p2

        S "О нет, дорогой. Ты не хочешь этого делать."
        S "Иди большой или иди домой! Это то, что я всегда говорю."

        scene SR2_AS3_vibrator_p3

        MC "Эээ... ты уверена?"
        S "АБ-со-лютно!"
        S "Сиди спокойно, дорогой. Я просто проверю, что у меня еще есть на складе."
        S "Хм ... слишком маленький ... слишком тонкий…"
        S "АГА!"

        scene SR2_AS3_vibrator_p4

        S "Вот малиш Double Deluxe 9000. Сделано в Калифорнии, из материалов самого высокого качества."
        MC "(Господи Иисусе ... эта штука огромная!)"
        MC "Я ... …"
        S "Вот, держи!"


        scene SR2_AS3_vibrator_p5

        MC "Он... очень розовый ... ."
        S "Твоя подруга полюбит его!"
        S "Это также один из самых интенсивных вибраторов на рынке."
        MC "Насколько мощна эта штука?"
        S "Ну, если средний вибратор на рынке-это пять из них; эта вещь-восемь или девять."

        scene SR2_AS3_vibrator_p6

        MC "Ты уверена, что я не должен соглашаться на менее мощный?"
        S "Поверь мне, дорогой. Она по достоинству оценит, свой первый раз."
        MC "(Глоток) Если ты уверена. Сколько я должен?"
        S "Это будет 80$."
        $ SR2_AS3_v_loop = True
        if inventory.money >= 80:
            S "Большое спасибо! Приходи еще!"
            $ inventory.buy(SR2_vibrator)
            $ can_hide_windows = False
            jump sex_shop_evening_label
        else:
            MC "У меня сейчас недостаточно денег.."
            MC "Я вернусь позже."
            $ can_hide_windows = False
            jump sex_shop_evening_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
