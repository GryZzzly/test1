image caroline_cloth_shop_afternoon_scene2_p1 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/1.jpg"
image caroline_cloth_shop_afternoon_scene2_p2 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/2.jpg"
image caroline_cloth_shop_afternoon_scene2_p3 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/3.jpg"
image caroline_cloth_shop_afternoon_scene2_p4 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/4.jpg"
image caroline_cloth_shop_afternoon_scene2_p5 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/5.jpg"
image caroline_cloth_shop_afternoon_scene2_p6 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/6.jpg"
image caroline_cloth_shop_afternoon_scene2_p7 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/7.jpg"
image caroline_cloth_shop_afternoon_scene2_p8 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/8.jpg"
image caroline_cloth_shop_afternoon_scene2_p9 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/9.jpg"
image caroline_cloth_shop_afternoon_scene2_p10 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/10.jpg"
image caroline_cloth_shop_afternoon_scene2_p11 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/11.jpg"
image caroline_cloth_shop_afternoon_scene2_p12 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/12.jpg"
image caroline_cloth_shop_afternoon_scene2_p13 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/13.jpg"
image caroline_cloth_shop_afternoon_scene2_p14 = "images/cloth_shop/room1/day/scenes/caroline_cloth_shop_afternoon_scene2/14.jpg"


label caroline_cloth_shop_afternoon_scene2_label:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_cloth_shop_afternoon_scene2_p1 with dissolve
    Caroline "Это немного неловко."
    MC "Расслабься! Помни о продажах, которые ты сделаешь!"
    Caroline "Да, я полагаю, так."

    scene caroline_cloth_shop_afternoon_scene2_p2
    MC "Ты отлично выглядишь в этом, кстати."
    Caroline "Все - тебе не нужно это говорить. Это по крайней мере один размер, слишком маленький, на меня, в любом случае!"
    Caroline "Только посмотри насколько меньше!"
    MC "(Это точно!)"

    scene caroline_cloth_shop_afternoon_scene2_p3
    Caroline "Я здесь, чтобы меняться."
    MC "Нет проблем, Кэролайн."
    MC "(Черт, это ДЕЙСТВИТЕЛЬНО узкие стринги на этом костюме!)"

    scene caroline_cloth_shop_afternoon_scene2_p4
    MC "(Хм ... ей обычно требуется время, чтобы переодеться в косплей.)"
    MC "(Может быть, у меня будет достаточно времени, чтобы посмотреть на нее, пока она раздевается!)"
    MC "(Просто немного ближе…)"

    scene caroline_cloth_shop_afternoon_scene2_p5
    MC "(Отсюда хорошо видно.)"
    MC "(Я хорошо спрятался, поэтому она не сможет меня видеть - и я могу уклониться за угол, если она быстро повернется.)"
    MC "(Время отдыхать и наслаждаться шоу!)"

    scene caroline_cloth_shop_afternoon_scene2_p6
    MC "(Да ладно, Кэролайн. Время раздеться…)"
    MC "(Посмотрим на твои большие сиськи!)"

    scene caroline_cloth_shop_afternoon_scene2_p7
    MC "(Хорошо. Она ищет ящик для своей одежды.)"
    MC "(Боже, стук моего сердца прямо сейчас! Еще несколько секунд, и она будет...)"

    scene black
    $ renpy.sound.play("sfx/shelf_fall.mp3")
    MC "ВААУУУ!"

    scene caroline_cloth_shop_afternoon_scene2_p8 with dissolve
    Caroline "Ааааа!"
    Caroline "Ч-что, черт возьми?!"
    MC "Ой…"
    MC "(Блядь! Полка сломалась, когда я опирался на нее!)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Rhinoceros.mp3', channel="music2", loop=True, fadein = 2)
    scene caroline_cloth_shop_afternoon_scene2_p9

    Caroline "[player_name]! Что ты делаешь, блядь?!"
    MC "Я… Ммм…"
    window hide
    menu:
        "Яяя… Я ... напылял полку!":

            scene caroline_cloth_shop_afternoon_scene2_p9
            MC "Я был ... эээ ... пыль на полке!"
            Caroline "Да неужели?"
            MC "Д-да?"

            scene caroline_cloth_shop_afternoon_scene2_p10
            Caroline "С чем?! У тебя явно нет ткани или какой-либо полировки!"
            Caroline "ПЛЮС, я вымыла все это место, как два часа назад!"
            MC "ОЙ! ОЙ!"
            jump caroline_cloth_shop_afternoon_scene2_after_menu
        "Я ... гм ... проверял, нужна ли тебе помощь!":


            scene caroline_cloth_shop_afternoon_scene2_p9
            MC "Я был ... гм ... проверял, нужна ли тебе помощь!"
            Caroline "Ты проверял, нужна ли мне какая-либо помощь?"
            MC "Да, я имею в виду, НЕТ!"

            scene caroline_cloth_shop_afternoon_scene2_p10
            Caroline "Ты отвратительный маленький извращенец!"
            if renpy.loadable("patch.rpy"):
                Caroline "Я твоя сестра!"
            if not renpy.loadable("patch.rpy"):
                Caroline "Я твой друг!"
            MC "Ой! Ааа! Прости!"
            jump caroline_cloth_shop_afternoon_scene2_after_menu
        "Я увидел ... большого ... гм ... паука! И мне пришлось попробовать и поймать его!":


            scene caroline_cloth_shop_afternoon_scene2_p9
            MC "Я увидел ... большого ... паука ... сверху на полке!"

            scene caroline_cloth_shop_afternoon_scene2_p11
            Caroline "Большой паук, да?"
            MC "Д-да! Тарантул или что-то еще…"
            Caroline "Ты ужасный лжец."
            MC "Н-нет! В самом деле! Это было ... э-э…"

            scene caroline_cloth_shop_afternoon_scene2_p10
            Caroline "Плохо, что ты подсматривал за мной, пока я переод…"
            MC "Ой! ПРОСТИ!"
            Caroline "Но тогда ты должен были пойти и сделать все, что угодно!"
            Caroline "Ты думаешь я тупая?!"
            MC "Прости!"
            jump caroline_cloth_shop_afternoon_scene2_after_menu

label caroline_cloth_shop_afternoon_scene2_after_menu:
    scene caroline_cloth_shop_afternoon_scene2_p12
    Caroline "ЧТО ЗА ХУЙНЯ?!"
    MC "Хм?"
    Caroline "У тебя стояк!"
    MC "(Иисус Христос! Не сейчас!)"

    scene caroline_cloth_shop_afternoon_scene2_p13
    MC "Я ... мне жаль! Я не контролирую его!"
    Caroline "Да, да! Ты был тем, кто спас меня!"
    MC "(Черт, у нее на самом деле есть точка там…)"

    scene caroline_cloth_shop_afternoon_scene2_p14
    Caroline "Выйди из моего магазина, сейчас же."
    Caroline "Сегодня вечером, когда я вернусь домой, у нас будет ОЧЕНЬ серьезное обсуждение границ."
    MC "Мне очень жаль, Кэролайн."
    Caroline "Просто оставь."
    $ caroline_after_cosplay_outfit5 = False
    $ day_time = 3
    $ caroline_salon_evening_scene1 = False
    $ caroline_mc_room_evening_scene2 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
