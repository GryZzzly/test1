

image Zv2_ES3a_p6 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/6.jpg"
image Zv2_ES3a_p6anim = Movie(play="videos/02 Zuri-1.webm", loop = True )
image Zv2_ES3a_p7 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/7.jpg"
image Zv2_ES3a_p7anim = Movie(play="videos/02 Zuri-2.webm", loop = True )
image Zv2_ES3a_p8 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/8.jpg"
image Zv2_ES3a_p9 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/9.jpg"
image Zv2_ES3a_p9anim = Movie(play="videos/02 Zuri-3.webm", loop = True )
image Zv2_ES3a_p10 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/10.jpg"
image Zv2_ES3a_p11 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/11.jpg"
image Zv2_ES3a_p12 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/12.jpg"
image Zv2_ES3a_p13 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/13.jpg"
image Zv2_ES3a_p14 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/14.jpg"
image Zv2_ES3a_p15 = "images/Zuri_home/home/E/scenes/Zv2_ES3a/15.jpg"


default Zv2_ES3a = False
default Zv2_ES4 = False
default Zv2_ES4_counter = 0
label Zv2_ES3a_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene Zv2_ES3_p1 with dissolve
    $ can_hide_windows = True
    Zuri "С возвращением, [player_name]."
    Zuri "Еще раз спасибо за помощь! Пойдем в нашу комнату наслаждений."
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(3, hard= True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene Zv2_ES3_p2

    Zuri "Ты сделал еще одну отличную работу для нас."
    Suri "Да, ты действительно пришел, парень. Ты собираешься сделать нас супер богатыми!"
    MC "Теперь я получаю еще одну награду, правда?"
    Suri "Хе-хе ... Да. Думаю, мы пообещали тебе минет."



    scene Zv2_ES3lick_p1
    Suri "Ммм, я не могу дождаться, когда начну сосать его член. Это выглядело очень вкусно, в прошлый раз мы это сделали!"
    Zuri "Что ж? Что мы ждем? Давай снимем с него эти штаны."
    MC "(Это будет здорово!)"

    scene Zv2_ES3lick_p2

    Suri "Итак, кто из нас первый?"
    MC "Я не суетливый!"
    Zuri "Будьте моим гостем, Сури!"

    scene Zv2_ES3lick_p3

    Zuri "Если тебе понравится, что мы это делаем, просто подожди, пока ты не увидишь, что у нас есть для тебя грандиозный финал!"
    Suri "Да, сегодня мы взорвем твой член, но в следующий раз - мы взорвем твой ум!"

    scene Zv2_ES3lick_p4

    Suri "Тебе всегда так тяжело, малыш?"
    Suri "Я не думаю, что когда-либо видела тебя, без массивной эрекции."
    MC "Трудно удержаться, когда я рядом с такой красавицей, как ты."

    scene Zv2_ES3lick_p5

    Suri "Лижет Лижет"
    Zuri "Лижет Лижет"
    MC "МММ... это хорошо. прямо там…"

    scene Zv2_ES3a_p6

    Suri "Всосала"
    MC "Oooх…"
    MC "(Я чувствую рот Сури, обернутый вокруг кончика моего члена. Это так жарко и мокро!)"

    scene Zv2_ES3a_p7

    MC "Боже... Мммм…"
    scene Zv2_ES3a_p6anim
    Zuri "Лижет Лижет"
    scene Zv2_ES3a_p7anim
    Suri "Всосала"

    scene Zv2_ES3a_p8

    MC "(Это слишком много! Их языки так хороши!)"
    MC "(Кто знал, корпоративный шпионаж мог чувствовать себя так правильно?)"
    Zuri "Mмммм…"
    Suri "Лижет Лижет"

    scene Zv2_ES3a_p9

    Zuri "Сосет сосет"
    scene Zv2_ES3a_p9anim
    if renpy.loadable("patch.rpy"):
        MC "(Блин, Зури так же хорошо сосет хуй, как ее сестра-близнец!)"
    else:
        MC "(Черт, Зури так же хорошо сосет хуй, как Сури!)"
    MC "(Они вместе, охуенно!)"

    scene Zv2_ES3a_p10

    Zuri "ГЛОТОК"
    MC "Черт! МММ!"
    MC "(Я чувствую тугое горло Зури вокруг моей головоки!)"

    scene Zv2_ES3a_p11

    MC "(Если она продолжит в том же духе, я кончу! Это слишком интенсивно!)"
    MC "Хннг! ААА!"
    Zuri "Shlurp"

    scene Zv2_ES3a_p12

    Suri "Сопит!!!"
    Zuri "Оппс! Прости, Сури. !"
    MC "Aххх! Да?"

    scene Zv2_ES3a_p13
    if renpy.loadable("patch.rpy"):
        Zuri "Извини, похоже, что голова моей сестры... случайно упала на твой член."
    else:
        Zuri "Извини, похоже, что голова Сури была... случайно упала на твой член."
    Suri "Mmmpfff! SHLURRRRP"
    MC "Oх! Aххххх!"

    scene Zv2_ES3a_p14

    MC "Я кончаю!"
    Zuri "Выпей все это, Сури!"
    Suri "SHLURRRP! КАШЕЛЬ!"
    MC "HNNNNNGGG!!! Тьфу! Да!"
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene Zv2_ES3a_p14 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene Zv2_ES3a_p14 with dissolve
    MC "(Я чувствую, как мой член дергается во рту! Она выпила меня насухо!)"

    scene Zv2_ES3a_p15

    MC "Вау... это было потрясающе..."
    Suri "Зури! Ах ты сука!"
    Zuri "Хехе! Я не могла устоять!"
    Suri "Мне придется отшлепать тебя сегодня вечером, за это!"
    Zuri "Не стесняйтесь идти, [player_name]."
    $ Zv2_ES3a = False
    $ zuri_inhome = False
    $ day_time = 4
    $ Zv2_ES4 = 1
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
