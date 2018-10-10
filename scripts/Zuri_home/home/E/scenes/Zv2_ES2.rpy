image Z_ES2_p1 = "images/Zuri_home/home/E/scenes/Zv2_ES2/1.jpg"
image Z_ES2_p2 = "images/Zuri_home/home/E/scenes/Zv2_ES2/2.jpg"
image Z_ES2_p3 = "images/Zuri_home/home/E/scenes/Zv2_ES2/3.jpg"
image Z_ES2_p4 = "images/Zuri_home/home/E/scenes/Zv2_ES2/4.jpg"
image Z_ES2_p5 = "images/Zuri_home/home/E/scenes/Zv2_ES2/5.jpg"
image Z_ES2_p6 = "images/Zuri_home/home/E/scenes/Zv2_ES2/6.jpg"
image Z_ES2_p7 = "images/Zuri_home/home/E/scenes/Zv2_ES2/7.jpg"
image Z_ES2_p8a = "images/Zuri_home/home/E/scenes/Zv2_ES2/8a.jpg"
image Z_ES2_p8aa = "images/Zuri_home/home/E/scenes/Zv2_ES2/8aa.jpg"
image Z_ES2_p8b = "images/Zuri_home/home/E/scenes/Zv2_ES2/8b.jpg"
image Z_ES2_p8bb = "images/Zuri_home/home/E/scenes/Zv2_ES2/8bb.jpg"
image Z_ES2_p8c = "images/Zuri_home/home/E/scenes/Zv2_ES2/8c.jpg"
image Z_ES2_p8cc = "images/Zuri_home/home/E/scenes/Zv2_ES2/8cc.jpg"
image Z_ES2_p9 = "images/Zuri_home/home/E/scenes/Zv2_ES2/9.jpg"
image Z_ES2_p10 = "images/Zuri_home/home/E/scenes/Zv2_ES2/10.jpg"
image Z_ES2_p11 = "images/Zuri_home/home/E/scenes/Zv2_ES2/11.jpg"
image Z_ES2_p12 = "images/Zuri_home/home/E/scenes/Zv2_ES2/12.jpg"
image Z_ES2_p13 = "images/Zuri_home/home/E/scenes/Zv2_ES2/13.jpg"
image Z_ES2_p14 = "images/Zuri_home/home/E/scenes/Zv2_ES2/14.jpg"
default Zv2_ES2 = False

label Zv2_ES2_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene Z_ES2_p1 with dissolve
    $ can_hide_windows = True
    MC "Ну, я сделал именно то, что ты просила. Я принес тебе название компании."
    Zuri "И ты отлично справился. Мы уже начали скупать акции, чтобы получить большинство голосов внутри компании."
    Suri "И мы не смогли бы сделать это без твоей помощи."
    MC "Ну ... какую награду ты имеешь в виду?"
    Zuri "Следуй за мной."
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(3, hard= True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene Z_ES2_p2

    Zuri "Это все твое сегодня вечером, [player_name]. Идти вперед и играть с ее грудью."

    Suri "Ты можешь делать все что угодно с моими сиськами, [player_name]."
    MC "(Это будет круто!)"


    scene Z_ES2_p3

    Suri "Итак, что ты думаешь, парень?"
    MC "Они изумительны!"
    Suri "Хехе... Я так и думала."

    scene Z_ES2_p4

    Suri "Ты хочешь играть с ними, не так ли?"
    MC "О да!"
    Suri "Они все твои. И будет намного больше, если ты дашь нам больше имен."

    scene Z_ES2_p5

    Suri "Теперь давайте начнем с твоей награды."
    Suri "Попробуй расслабиться - не стесняйтесь."
    MC "(Боже! Хотел бы я трахнуть их обоих одновременно! Это было бы самой горячей вещью когда-либо случавшейся в моей жизни!)"

    scene Z_ES2_p6

    Suri "Я чувствую твой твердый член сквозь джинсы. Кажется, что кто-то возбуждается от этого!"
    MC "Трудно не волноваться, когда у меня на коленях такая сексуальная девушка, как ты."
    Suri "Хехе! Ладно, так что ты хочешь сделать с моими сиськами?"

    scene Z_ES2_p7

    MC "Я могу сделать что угодно?"
    Suri "Все, что захочешь, парень."
    MC "Хмм…"
    $ menu_q1 = True
    $ menu_q2 = True
    $ menu_q3 = True
    jump Zv2_ES2_menu

label Zv2_ES2_menu:
    scene Z_ES2_p7
    window hide
    menu:
        "Щипать ее соски." if menu_q1 == True:
            scene Z_ES2_p8a

            MC "(Я думаю, что я начну сжимая и розжимая ее соски немного.)"
            Suri "МММ, Шалунишка ."
            Suri "Тебе нравиться дразнить мои соски?"

            scene Z_ES2_p8aa

            Suri "Оооо! Это хорошо…."
            if renpy.loadable("patch.rpy"):
                Zuri "Моя сестра любит, когда с ее сосками играют. Она может превратиться в настоящую шлюшку, если парень достаточно ее возбуждает."
            else:
                Zuri "Сури любит, когда с ее сосками играют. Она может превратиться в настоящую шлюшку, если парень достаточно ее возбуждает."
            Suri "Игнорируй ее, парень. Она просто пытается меня смутить."
            $ menu_q1 = False
            if menu_q1 == True and menu_q2 == True and menu_q3 == True:
                jump Zv2_ES2_continue
            else:
                jump Zv2_ES2_menu

        "Сжимать ее грудь." if menu_q2 == True:
            scene Z_ES2_p8b

            MC "(Нащупаем и зажмем соски Сури!)"
            MC "Они очень мягкие, Сури.!"
            Suri "Хехе. Я знаю. Зури любит использовать их в качестве подушки."
            MC "В самом деле?"

            scene Z_ES2_p8bb

            Zuri "Сури! Это должно быть тайной!"
            Suri "Да ладно тебе. Ты сделала для меня гораздо больше, чем просто использовала мою грудь в качестве подушки.."
            Zuri "(Вздох) Это очень верно."
            MC "(Эти девочки - полные нимфоманки!)"
            $ menu_q2 = False
            if menu_q1 == True and menu_q2 == True and menu_q3 == True:
                jump Zv2_ES2_continue
            else:
                jump Zv2_ES2_menu

        "Сосать ее соски." if menu_q3 == True:
            scene Z_ES2_p8c

            MC "(Хорошо, давайте посмотрим, как она любит, когда я сосу ее соски.)"
            Suri "Оооо! Хехе! Щекотно!"
            Zuri "Не бойтесь немного покусать зубами. Она такая странная.!"
            Suri "Зури! Прекрати! Хехе!"

            scene Z_ES2_p8cc

            Suri "Oooх! Aххх! О, Боже мой! МММ!"
            MC "(Всасывает всасывает!)"
            Suri "Oooххх…."
            $ menu_q3 = False
            if menu_q1 == True and menu_q2 == True and menu_q3 == True:
                jump Zv2_ES2_continue
            else:
                jump Zv2_ES2_menu

label Zv2_ES2_continue:
    scene Z_ES2_p9

    Zuri "(Блядь, что она делает…?)"
    Zuri "Да ладно тебе, Сури. Ты его совсем не соблазняешь.!"
    Suri "Я пытаюсь, Зури.!"
    Zuri "Пожалуйста, ты ведешь себя как мама со своим ребенком! Позвольте мне помочь."

    scene Z_ES2_p10

    Suri "Эй! У меня было это!"
    Zuri "Конечно, ты сделала. Я здесь, чтобы помочь тебе.."
    Suri "Хорошо…"

    scene Z_ES2_p11

    Zuri "Мне удалось найти нам имя. Если мы будем работать вместе, я уверен, что мы сможем убедить [player_name] дать нам еще немного."
    Suri "Ах... да!"

    scene Z_ES2_p12

    Suri "Итак, что ты скажешь, [player_name]?"
    Suri "В следующий раз, когда ты получишь название компании, ты получишь удовольствие от нас обоих одновременно. Как это звучит?"
    MC "Охуенно!"
    Zuri "Я тоже так думаю."

    scene Z_ES2_p13

    Zuri "Я обещаю вам, - ночь с нами ты никогда не забудешь."
    Suri "Все, что тебе нужно сделать, это получить имя."
    Suri "А потом мы будем сосать и ебать твои мозги, парень."

    scene Z_ES2_p14

    Zuri "Мы договорились?"
    MC "(Боже ... они неотразимы.!)"
    MC "Черт возьми, да..."
    Zuri "Это то, что нам нравится слышать!"
    $ day_time = 4
    $ Zv2_ES2 = False
    $ zuri_inhome = False
    $ can_safe_note = True
    $ Zv2_MS2_q10 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
