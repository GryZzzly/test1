image Zv2_ES3_p1 = "images/Zuri_home/home/E/scenes/Zv2_ES3/1.jpg"
image Zv2_ES3_p2 = "images/Zuri_home/home/E/scenes/Zv2_ES3/2.jpg"

image Zv2_ES3foot_p1 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/1.jpg"
image Zv2_ES3foot_p2 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/2.jpg"
image Zv2_ES3foot_p2anim = Movie(play="videos/02 Zuri-6.webm", loop = True )
image Zv2_ES3foot_p3 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/3.jpg"
image Zv2_ES3foot_p4 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/4.jpg"
image Zv2_ES3foot_p4anim = Movie(play="videos/02 Zuri-7.webm", loop = True )
image Zv2_ES3foot_p5 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/5.jpg"
image Zv2_ES3foot_p6 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/6.jpg"
image Zv2_ES3foot_p6anim = Movie(play="videos/02 Zuri-8.webm", loop = True )
image Zv2_ES3foot_p7 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/7.jpg"
image Zv2_ES3foot_p8 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/8.jpg"
image Zv2_ES3foot_p9 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/9.jpg"
image Zv2_ES3foot_p10 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/10.jpg"
image Zv2_ES3foot_p11 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/11.jpg"
image Zv2_ES3foot_p11a = "images/Zuri_home/home/E/scenes/Zv2_ES3/Footjob/11a.jpg"

image Zv2_ES3lick_p1 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/1.jpg"
image Zv2_ES3lick_p2 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/2.jpg"
image Zv2_ES3lick_p3 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/3.jpg"
image Zv2_ES3lick_p4 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/4.jpg"
image Zv2_ES3lick_p5 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/5.jpg"
image Zv2_ES3lick_p6 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/6.jpg"
image Zv2_ES3lick_p7 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/7.jpg"
image Zv2_ES3lick_p8 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/8.jpg"
image Zv2_ES3lick_p8anim = Movie(play="videos/02 Zuri-4.webm", loop = True )
image Zv2_ES3lick_p9 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/9.jpg"
image Zv2_ES3lick_p10 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/10.jpg"
image Zv2_ES3lick_p10anim = Movie(play="videos/02 Zuri-5.webm", loop = True )
image Zv2_ES3lick_p11 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/11.jpg"
image Zv2_ES3lick_p12 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/12.jpg"
image Zv2_ES3lick_p12a = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/12a.jpg"
image Zv2_ES3lick_p13 = "images/Zuri_home/home/E/scenes/Zv2_ES3/Licking/13.jpg"

default Zv2_ES3 = False


label Zv2_ES3_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene Zv2_ES3_p1 with dissolve
    $ can_hide_windows = True
    Zuri "С возвращением, [player_name]."
    Suri "Рада снова тебя видеть, малыш."
    MC "Я тоже рад тебя видеть."
    Zuri "Еще раз спасибо за помощь с названием компании. Мы оба убедимся, что ты достойно вознагражден"
    Suri "Как насчет того, чтобы мы отправились в заднюю комнату и начали эту вечеринку?"
    $ renpy.music.stop(channel="music1", fadeout=1)
    scene black
    $ renpy.pause(3, hard= True)
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene Zv2_ES3_p2

    Suri "Итак, о чем ты думаешь?"
    Zuri "Мы бы могли поласкать тебя ногами."
    Suri "Или мы могли бы лизать твой член, пока ты не кончишь."
    window hide
    menu:
        "Вы можете лизать мой член?":
            scene Zv2_ES3_p2

            MC "Я хотел бы видеть, как вы двое лижите мой член."

            scene Zv2_ES3lick_p1

            Suri "Это так, малыш?"
            Zuri "Я полагаю, ты должен наслаждаться видом двух красивых девушек, на коленях перед вами."
            Zuri "Давай расстегнем эти джинсы.."

            scene Zv2_ES3lick_p2

            MC "(Это будет потрясающе! У меня никогда не было двойного минета раньше!)"
            Zuri "Так вот, мы будем лизать тебя только сегодня. Но если ты дашь нам больше имен, мы, конечно, можем подумать о том, чтобы отсосать тебе. Сделка?"
            MC "Да, договорились."

            scene Zv2_ES3lick_p3

            Zuri "Он довольно большой, Сури, не так ли!"
            Suri "Парень удивил меня.!"
            if renpy.loadable("patch.rpy"):
                MC "(Боже, почему я просто позволяю им делать это? Они соблазняют меня разрушить компанию отца.!)"
            else:
                MC "(Боже, почему я просто позволяю им делать это? Они соблазняют меня разрушить компанию Боба.!)"
            scene Zv2_ES3lick_p4

            MC "(Я должен встать и сказать “больше нет”.)"
            Zuri "Это ооочень толстый тоже!"
            Suri "Это было бы очень хорошо внутри меня!"

            scene Zv2_ES3lick_p5

            MC "Oooх……."
            Suri "(Лижет лижет)"
            Zuri "(Лижет лижет)"

            scene Zv2_ES3lick_p6
            if renpy.loadable("patch.rpy"):
                MC "(С другой стороны, может быть, папина компания не стоит хорошего минета!)"
            else:
                MC "(С другой стороны, может быть, компания Боба не стоит такого хорошего минета!)"
            Suri "(Лижет Лижет)"
            MC "(Они дразнят каждый дюйм моего члена! Я буду кончать в кратчайшие сроки!)"

            scene Zv2_ES3lick_p7

            Zuri "(Лижет! Чавкает!)"
            MC "Aхх… Oхх…"
            Suri "(Лижет! Лижет!)"

            scene Zv2_ES3lick_p8

            MC "(Боже, ее глаза потрясающие!)"
            scene Zv2_ES3lick_p8anim
            MC "(Как она смотрит на меня, когда она лижет мой член, сердце плавится!)"

            scene Zv2_ES3lick_p9

            Suri "Сосет Сосет!"
            Zuri "Сосет Сосет!"
            MC "Уоххх Бог! MMMMM!"

            scene Zv2_ES3lick_p10

            MC "Aххх!"
            scene Zv2_ES3lick_p10anim
            Zuri "Shluuuurrrrp!"
            Suri "Сосет Сосет!"

            scene Zv2_ES3lick_p11

            MC "Хмммм!"
            MC "Я собираюсь кончить! Это слишком интенсивно! АХХХХ!"
            $ Suri_name = "Обе"
            Suri "SHLURP! Сосет Сосет!"
            $ Suri_name = "Сури"

            scene Zv2_ES3lick_p12

            MC "Я кончаю! Хннннггг!"
            Suri "Лижет Лижет"
            Zuri "Лижет Лижет"
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene Zv2_ES3lick_p12 with dissolve
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene Zv2_ES3lick_p12a with dissolve

            MC "Айаааааххххх!!!"
            MC "Боже мой…"
            Suri "Ммм... Соленый!"

            scene Zv2_ES3lick_p13

            Zuri "Ты видел, что мы можем сделать сейчас. Как насчет третьего имени?"
            Suri "Да. Если ты сделаешь это, мы возьмем весь твой член в рот. Договорились?"
            MC "Абсолютно! Вы, девочки, невероятны!"
            $ day_time = 4
            $ Zv2_ES3 = False
            $ zuri_inhome = False
            $ Zv2_MS2_q10 = True
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump map_label
        "Не могли бы вы поласкать меня ногами?":


            MC "Я согласен."
            Zuri "МММ... Хороший выбор. Давай, снимай штаны, а потом ложись на кровать.."

            scene Zv2_ES3foot_p1

            Suri "Его член настолько велик, Зури! Хехе!"
            Zuri "Это действительно так! Я надеюсь, что он будет наслаждаться нашими потираниями ног."
            MC "(Близнецы трутся ногами о мой член? Это мой счастливый день!)"


            scene Zv2_ES3foot_p2

            Suri "И вот мы идем. Хехе! Я чувствую, как он дергается под моими пальцами!"
            scene Zv2_ES3foot_p2anim
            Suri "Думаю, ему это нравится.!"
            MC "МММ! О да..."


            scene Zv2_ES3foot_p3

            Zuri "Там будет еще много вещей, которые мы можем сделать для тебя. "
            Suri "Мы можем дать тебе ооочень много удовольствия."
            Zuri "И единственное, что тебе нужно сделать, это лечь и наслаждаться этим."

            scene Zv2_ES3foot_p4

            MC "МММ! Ах…"
            scene Zv2_ES3foot_p4anim
            MC "(Это так чертовски хорошо…)"
            Suri "Может быть, мы даже позволим тебе трахнуть наши киски когда-нибудь."

            scene Zv2_ES3foot_p5

            Zuri "И единственное, что вам нужно сделать - продолжать зарабатывать эти награды-это получить нам эти имена."
            Zuri "Просто, правильно?"
            MC "Эх... угу…"

            scene Zv2_ES3foot_p6

            Suri "Что случилось, малыш? Ты хочешь, чтобы мы ускорились?"
            scene Zv2_ES3foot_p6anim
            MC "Боже да!"
            Zuri "Давай ускорим процесс, Сури.."

            scene Zv2_ES3foot_p7

            MC "Ох! Боже... это потрясающе…"
            if renpy.loadable("patch.rpy"):
                MC "(Я не должен был делать это с папиной компанией... но они чертовски сексуальны…)"
            else:
                MC "(Я не должен был делать это с компанией Боба... но они чертовски сексуальны…)"
            MC "(Моему члену так трудно прямо сейчас!)"

            scene Zv2_ES3foot_p8

            MC "Ах! ААА!"
            Suri "Похоже, этот парень не продержится долго.!"
            Zuri "Ой, какой позор."

            scene Zv2_ES3foot_p9

            Suri "Ты собираешься кончить, парень?"
            Zuri "Да, ты кончишь, нам в ноги?"
            MC "Мммм! ААА…"

            scene Zv2_ES3foot_p10

            MC "Черт! Я кончаю!"
            MC "Хннннннгггг!"
            Suri "Вот и все, кончай для меня! Сперма для меня сейчас!"
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene Zv2_ES3foot_p10
            $ renpy.pause(0.7, hard = True)
            scene white with dissolve
            $ renpy.pause(0.7, hard = True)
            scene Zv2_ES3foot_p11

            Suri "Брызги спермы на всей длине моих пальцев ног!"
            MC "ААА! Ах ах!"

            scene Zv2_ES3foot_p11a

            MC "Oooх….. (Пыхтит Пыхтит)"
            Zuri "Вау! Это очень много спермы, Сури."
            Suri "Мы можем сделать это снова, парень. Все, что тебе нужно сделать, это дать нам больше имен. Окей?"
            MC "(Пыхтит) Да, хорошо...."
            $ day_time = 4
            $ Zv2_ES3 = False
            $ zuri_inhome = False
            $ Zv2_MS2_q10 = True
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
