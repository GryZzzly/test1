image SR2_weekend_waterslide_p1 = "images/Weekend_Events/Sara/R2/WaterSlide/1.jpg"
image SR2_weekend_waterslide_p2 = "images/Weekend_Events/Sara/R2/WaterSlide/2.jpg"
image SR2_weekend_waterslide_p3a = "images/Weekend_Events/Sara/R2/WaterSlide/3a.jpg"
image SR2_weekend_waterslide_p3aa = "images/Weekend_Events/Sara/R2/WaterSlide/3aa.jpg"
image SR2_weekend_waterslide_p3b = "images/Weekend_Events/Sara/R2/WaterSlide/3b.jpg"
image SR2_weekend_waterslide_p3bb = "images/Weekend_Events/Sara/R2/WaterSlide/3bb.jpg"
image SR2_weekend_waterslide_p4 = "images/Weekend_Events/Sara/R2/WaterSlide/4.jpg"
image SR2_weekend_waterslide_p5 = "images/Weekend_Events/Sara/R2/WaterSlide/5.jpg"
image SR2_weekend_waterslide_p6 = "images/Weekend_Events/Sara/R2/WaterSlide/6.jpg"
image SR2_weekend_waterslide_p7 = "images/Weekend_Events/Sara/R2/WaterSlide/7.jpg"
image SR2_weekend_waterslide_p8 = "images/Weekend_Events/Sara/R2/WaterSlide/8.jpg"
image SR2_weekend_waterslide_p9 = "images/Weekend_Events/Sara/R2/WaterSlide/9.jpg"
image SR2_weekend_waterslide_p10 = "images/Weekend_Events/Sara/R2/WaterSlide/10.jpg"
image SR2_weekend_waterslide_p11 = "images/Weekend_Events/Sara/R2/WaterSlide/11.jpg"
image SR2_weekend_waterslide_p12 = "images/Weekend_Events/Sara/R2/WaterSlide/12.jpg"
image SR2_weekend_waterslide_p13 = "images/Weekend_Events/Sara/R2/WaterSlide/13.jpg"
image SR2_weekend_waterslide_p14 = "images/Weekend_Events/Sara/R2/WaterSlide/14.jpg"

label SR2_waterslide_label:
    if SR2_after_waterslide == True:
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
        MC "Как насчет того, чтобы попробовать водные горки?"
        Sara "Эх ... Не знаю ... Я не умею хорошо плавать."
        MC "Расслабься. Мы спустимся вместе, и я буду держать тебя, когда мы попадем в бассейн, хорошо?"
        Sara "Обещаешь?"
        MC "Обещаю."
        Sara "(Глоток) Я... Я думаю, так, то…"

        scene SR2_weekend_waterslide_p1

        MC "Вот так. Вы хотите подняться первой?"
        Sara "Это действительно высоко…"
        MC "Я буду рядом с тобой."
        Sara "И ты непременно будешь держишься за меня, когда мы попадаем в воду?"
        window hide
        scene SR2_weekend_waterslide_p2
        menu:
            "Предложение подняться первой.":


                MC "Ты предпочла бы, если бы я поднялся первым?"
                Sara "Честно? Да."
                MC "Нет проблем. Я сейчас начну подниматься по лестнице."

                scene SR2_weekend_waterslide_p3b

                MC "Видишь? Это совершенно безопасно."
                MC "Не боишся высоты, как я?"
                Sara "Только когда высоко над водой."

                scene SR2_weekend_waterslide_p3bb

                MC "Как я и сказал-я буду здесь, и я буду держаться за тебя, как только мы попадем в бассейн."
                Sara "(Вау... эти шорты так плотноприлягают. Я почти вижу контуры его хозяйства.)"
                MC "Все в порядке, Сара?"
                Sara "Ну?"
                MC "Я сказал, я буду держаться за тебя, когда мы войдем в бассейн.."
                Sara "О, да! Все в порядке.."
                jump SR2_after_waterslide_menu
            "Скажи Саре начать подниматься, и что ты будешь прямо за ней.":


                MC "Идем дальше - начинаем восхождение. Я буду прямо за тобой, чтобы поймать тебя, если ты упадешь."

                scene SR2_weekend_waterslide_p3a


                Sara "Благодарю, [player_name]."
                Sara "Я была здесь так много раз с друзьями, но я никогда не была в глубокой части бассейна."
                Sara "И я определенно никогда не каталась прежде."
                MC "Все происходит в первый раз."

                scene SR2_weekend_waterslide_p3aa

                MC "(Черт, у нее симпатичная маленькая задница.)"
                MC "(Я хотел бы сжать и щупать эти булочки!)"
                Sara "Надеюсь, ты не пялишься на мою задницу! Хаха!"
                MC "Эээ... неа!"
                jump SR2_after_waterslide_menu

label SR2_after_waterslide_menu:
    scene SR2_weekend_waterslide_p4

    MC "Хорошо, вот мы здесь. Ты крепко держишься за мою руку. Ты хорошо себя чувствуешь?"
    Sara "Просто немного тошнит."
    MC "Постарайся расслабиться. Сделайте глубокий вдох."

    scene SR2_weekend_waterslide_p5

    MC "С тобой все будет хорошо. Это не очень глубокий бассейн, и ты с одним из лучших пловцов в мире."
    Sara "Ты один из лучших пловцов в мире?!"
    MC "Конечно, да! Разве вы не слышали о [player_name] рыбе?"
    Sara "Хахаха!"
    MC "(Она смееться. Надеюсь, это отвлечет ее страх.)"

    scene SR2_weekend_waterslide_p6

    MC "Просто Держи меня за руку, и мы окажемся в положении, в котором ты чувствуешь себя в безопасности."
    Sara "Я слишком тяжелая, чтобы сидеть на твоем колене?"
    MC "Конечно, нет. Ты легкая, как перышко."

    scene SR2_weekend_waterslide_p7

    MC "Видишь? Ты отлично сидишь на моем колене."
    Sara "Хехе…"
    Sara "(Мне нравится ощущение его теплых рук, обернутых вокруг моего живота.)"
    Sara "(Я хотела бы обнимать его так каждую ночь.)"
    MC "Готова?"


    scene SR2_weekend_waterslide_p8

    Sara "Ага!"
    MC "Я буду держать крепко - не волнуйся!"
    Sara "(А? Что это за жесткая штука тыкает в мою задницу?)"

    scene SR2_weekend_waterslide_p9

    MC "Ууу!"
    Sara "Ууууххххуу!"
    Sara "(О Боже мой! У него снова стояк! Он давит на мое влагалище!)"
    MC "(Похоже, она наслаждается этим больше, чем я!)"

    scene SR2_weekend_waterslide_p10

    MC "(Надеюсь, она не заметила мой жесткий стояк.)"
    MC "(Я не смог справиться с ним с тех пор, как впервые увидел ее в ее плотном розовом купальнике.)"
    Sara "Глоток!"
    Sara "Вода! Не отпускай!"

    scene SR2_weekend_waterslide_p11

    "ВСПЛЕСК!"
    Sara "Aхх! Холодно!"
    MC "Вот и все! Это твое первое скольжение в бассейн!"
    Sara "Не отпускай! Не отпускай!"
    MC "Расслабься! Это мелкий бассейн! Ты, вероятно, можешь коснуться дна пальцами ног."
    Sara "Да?"

    scene SR2_weekend_waterslide_p12

    MC "Видишь? Твой нос все еще над водой."
    Sara "(Слава Богу... это было страшно.)"
    Sara "(Я, вероятно, должна помочь [player_name] с его стояком…)"

    scene SR2_weekend_waterslide_p14
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)

    Sara "Хм... спускаясь по горке, я почувствовала что-то твердое."
    MC "(Ой-ой…)"
    Sara "[player_name]… у тебя была эрекция??"

    scene SR2_weekend_waterslide_p13

    MC "Да... и я до сих пор..."
    Sara "Это потому что ... потому что..."
    MC "Потому что я с тобой?"
    Sara "Да?"
    MC "Да, это так."

    scene SR2_weekend_waterslide_p14

    Sara "Но я даже не голая.…"
    MC "Ты все еще великолепна. Всякий раз, когда я вижу что-то действительно сексуальное, мой член решает встать. Я не могу это контролировать.."
    MC "У него свой собственный ум."
    Sara "А?! Так вот как на самом деле работают пенисы? Или ты просто издеваешься надо мной?"
    MC "Нет, это правда. Ребята не могут реально контролировать, когда они получают эрекцию."
    Sara "Да... Это действительно странно."
    MC "Неужели? Можете ли вы контролировать свое возбуждение?"

    scene SR2_weekend_waterslide_p12

    Sara "[player_name]…."
    MC "Хаха! Ты очаровательна, когда стесняешься."
    MC "Хорошо, давай выйдем из бассейна.."
    $ SR2_after_waterslide = True
    $ can_hide_windows = False
    jump swimming_poll_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
