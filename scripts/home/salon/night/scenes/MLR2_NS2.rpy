image MLR2_NS2_p1 = "images/home/salon/night/scenes/MLR2_NS2/1.jpg"
image MLR2_NS2_p2 = "images/home/salon/night/scenes/MLR2_NS2/2.jpg"
image MLR2_NS2_p3 = "images/home/salon/night/scenes/MLR2_NS2/3.jpg"
image MLR2_NS2_p4 = "images/home/salon/night/scenes/MLR2_NS2/4.jpg"
image MLR2_NS2_p5 = "images/home/salon/night/scenes/MLR2_NS2/5.jpg"
image MLR2_NS2_p6 = "images/home/salon/night/scenes/MLR2_NS2/6.jpg"
image MLR2_NS2_p8 = "images/home/salon/night/scenes/MLR2_NS2/8.jpg"
image MLR2_NS2_p9 = "images/home/salon/night/scenes/MLR2_NS2/9.jpg"
image MLR2_NS2_p10 = "images/home/salon/night/scenes/MLR2_NS2/10.jpg"
image MLR2_NS2_p11 = "images/home/salon/night/scenes/MLR2_NS2/11.jpg"
image MLR2_NS2_p11anim = Movie(play="videos/02 Linda-NS2-2.webm", loop = True )
image MLR2_NS2_p12 = "images/home/salon/night/scenes/MLR2_NS2/12.jpg"
image MLR2_NS2_p12anim = Movie(play="videos/02 Linda-NS2-1.webm", loop = True )
image MLR2_NS2_p13 = "images/home/salon/night/scenes/MLR2_NS2/13.jpg"
image MLR2_NS2_p14 = "images/home/salon/night/scenes/MLR2_NS2/14.jpg"
image MLR2_NS2_p15 = "images/home/salon/night/scenes/MLR2_NS2/15.jpg"
image MLR2_NS2_p16 = "images/home/salon/night/scenes/MLR2_NS2/16.jpg"
image MLR2_NS2_p17 = "images/home/salon/night/scenes/MLR2_NS2/17.jpg"
image MLR2_NS2_p17anim = Movie(play="videos/02 Linda-NS2-3.webm", loop = True )
image MLR2_NS2_p18 = "images/home/salon/night/scenes/MLR2_NS2/18.jpg"
image MLR2_NS2_p18anim = Movie(play="videos/02 Linda-NS2-4.webm", loop = True )
image MLR2_NS2_p19 = "images/home/salon/night/scenes/MLR2_NS2/19.jpg"
image MLR2_NS2_p20 = "images/home/salon/night/scenes/MLR2_NS2/20.jpg"
image MLR2_NS2_p21 = "images/home/salon/night/scenes/MLR2_NS2/21.jpg"
image MLR2_NS2_p22 = "images/home/salon/night/scenes/MLR2_NS2/22.jpg"
image MLR2_NS2_p23 = "images/home/salon/night/scenes/MLR2_NS2/23.jpg"
image MLR2_NS2_p24 = "images/home/salon/night/scenes/MLR2_NS2/24.jpg"
image MLR2_NS2_p24anim = Movie(play="videos/02 Linda-NS2-5.webm", loop = True )
image MLR2_NS2_p25 = "images/home/salon/night/scenes/MLR2_NS2/25.jpg"
image MLR2_NS2_p26 = "images/home/salon/night/scenes/MLR2_NS2/26.jpg"
image MLR2_NS2_p26anim = Movie(play="videos/02 Linda-NS2-6.webm", loop = True )
image MLR2_NS2_p26a = "images/home/salon/night/scenes/MLR2_NS2/26a.jpg"
image MLR2_NS2_p27 = "images/home/salon/night/scenes/MLR2_NS2/27.jpg"
image MLR2_NS2_p28 = "images/home/salon/night/scenes/MLR2_NS2/28.jpg"
image MLR2_NS2_p29 = "images/home/salon/night/scenes/MLR2_NS2/29.jpg"
image MLR2_NS2_p29anim = Movie(play="videos/02 Linda-NS2-7.webm", loop = True )
image MLR2_NS2_p30 = "images/home/salon/night/scenes/MLR2_NS2/30.jpg"
image MLR2_NS2_p30anim = Movie(play="videos/02 Linda-NS2-8r.webm", loop = True )
image MLR2_NS2_p30a = "images/home/salon/night/scenes/MLR2_NS2/30a.jpg"
image MLR2_NS2_p31 = "images/home/salon/night/scenes/MLR2_NS2/31.jpg"
image MLR2_NS2_p32 = "images/home/salon/night/scenes/MLR2_NS2/32.jpg"
image MLR2_NS2_p33 = "images/home/salon/night/scenes/MLR2_NS2/33.jpg"
image MLR2_NS2_p34 = "images/home/salon/night/scenes/MLR2_NS2/34.jpg"
default can_MLR2_MS1_ES3 = False
label MLR2_NS2_label:
    $ can_hide_windows = True
    scene MLR2_NS2_p1

    MC "(Глоток…)"
    if renpy.loadable("patch.rpy"):
        MC "(Что ж, папа есть. Интересно, где мама.)"
    else:
        MC "(Что ж, Боб есть. Интересно, где Линда.)"
    MC "(Господи, мое сердце сейчас выскочит. Если он проснется и поймает меня - я ооочень пострадаю.)"

    scene MLR2_NS2_p2

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music2", loop=True, fadein = 2)

    Mom "Привет, милый!"
    MC "Ах-"
    Mom "Тише! Спокойно! "

    scene MLR2_NS2_p3

    Mom "Ты должен молчать, или мы разбудим старика."
    MC "Ладно. Ты напугала меня до усрачки!"
    MC "Не могла бы ты просто лежать на кровати, ожидая меня? "

    scene MLR2_NS2_p4

    Mom "Я не хотела уснуть и пропустить твой визит."
    if renpy.loadable("patch.rpy"):
        Mom "Кроме того, если бы я легла в постель, твой отец хотел бы снова заняться со мной сексом."
    else:
        Mom "Кроме того, если бы я легла в постель, Боб хотел бы снова заняться со мной сексом."
    Mom "Я просто потратила время, разбираясь с одеждой, пока он не ушел спать."

    scene MLR2_NS2_p5

    MC "А, понятно. Только в следующий раз ты могла бы нажать на мое плечо или шепнуть мое имя?"
    Mom "Ой, где тут веселье?"
    MC "(Вздох)"
    Mom "Теперь ... о том обещании, которое я дала…"

    scene MLR2_NS2_p6
    if renpy.loadable("patch.rpy"):
        Mom "Я говорила тебе, что буду держать своего скучного мужа подальше от тебя и не причиню тебе вреда."
    else:
        Mom "Я говорила тебе, что буду держать Боба подальше от тебя и не причиню тебе вреда."
    Mom "Однако-я хочу что-то взамен."
    if renpy.loadable("patch.rpy"):
        MC "Конечно, Мама. О чем ты думаешь?"
    else:

        MC "Конечно, Линда. О чем ты думаешь?"

    scene MLR2_NS2_p8

    Mom "Я хочу, чтобы ты доставил мне удовольствие, которое не может старик."
    Mom "Ты можешь делать все, что хочешь - но сосредоточься на моем удовольствии, а не своем."
    Mom "Ты понял?"
    if renpy.loadable("patch.rpy"):
        MC "Да, без проблем, мама."
    else:
        MC "Да, нет проблем, Линда."
    Mom "Прекрасно! Позвольте мне просто раздеться здесь."
    scene black
    $ renpy.pause(2, hard = True)
    scene MLR2_NS2_p9

    MC "(Ой! Она такая рячая!)"
    Mom "Продолжим."
    MC "Проберемся тайком в мою комнату?"
    Mom "Зачем нам это делать?"
    if renpy.loadable("patch.rpy"):
        MC "Потому что папа буквально спит, прямо рядом с тобой."
    else:
        MC "Потому что Боб буквально спит, прямо рядом с тобой."
    Dad "(Snooooreeee)"
    Mom "Но это половина веселья, милый!"

    scene MLR2_NS2_p10

    Mom "А теперь, как насчет того, чтобы ты пришел сюда и начал играть с моими сиськами, пока я тоже не уснула."
    if renpy.loadable("patch.rpy"):
        MC "(Я думаю, мама немного эксгибиционистка!)"
        MC "Конечно, Мама!"
    else:
        MC "(Я думаю, Линда немного эксгибиционистка!)"
        MC "Конечно, Линда!"

    scene MLR2_NS2_p11

    MC "(Mwah!)"
    Mom "Ooooхх…."
    scene MLR2_NS2_p11anim
    MC "(Сосет Сосет)"
    Mom "Aхх…"

    scene MLR2_NS2_p12

    Mom "Mмм… Сильнее… Да!"
    MC "(Сосет Сосет!)"
    scene MLR2_NS2_p12anim
    Mom "MMMM!!!"
    Dad "(Snooorrreeee)"

    scene MLR2_NS2_p13

    Mom "Eeek…."
    Mom "Aх… Aх… Aх.."
    Mom "Не останавливайся. Не останавливайся..."
    Mom "Черт, это хорошо."

    scene MLR2_NS2_p11

    Mom "Фу... Хорошо... Все, довольно."

    scene MLR2_NS2_p14

    Mom "Планы поменялись..."
    Mom "Мне нужно, чтобы ты спустился к моей киске, прямо сейчас."

    scene MLR2_NS2_p15

    Mom "Mмм… вот так. Поторопись!"
    Mom "Я сейчас мокрая. Мне нужно почувствовать твой язык внутри меня!"
    if renpy.loadable("patch.rpy"):
        MC "Тише - осторожно, не разбуди папу!"
    else:
        MC "Тихо - осторожны не разбуди Боба!"
    Mom "Mмм... Да пошёл он!"

    scene MLR2_NS2_p16

    Mom "Боже, мне так жарко. Пожалуйста, начинай сосать мой клитор. Мне нужно почувствовать, твой горячий мокрый рот!"
    MC "(Вау, она действительно не может держаться!)"
    MC "Ладно, держись! Просто старайся молчать."

    scene MLR2_NS2_p17

    MC "(Давай	начнем...)"
    scene MLR2_NS2_p17anim
    MC "(Там наверху ее клитор. Я могу либо сосредоточиться на этом, либо вставить палец внутрь и найти ее точку g.)"
    MC "(Начнем с точки g.)"

    scene MLR2_NS2_p18

    Mom "Oooх….. Mмм!"
    scene MLR2_NS2_p18anim
    Mom "Да... Да, [player_name]. я люблю тебя!"
    MC "(Похоже, я сделал хороший выбор-она действительно наслаждается этим!)"
    Mom "Глубже!"

    scene MLR2_NS2_p19

    Mom "OOOхххх!"
    MC "Тише! Не разбуди."
    Mom "Возбуди мою распутную киску! ААА! АХХХХ!"
    MC "(Черт, она сейчас такая громкая!)"

    scene MLR2_NS2_p20

    Mom "О, да! Заставь меня кончить!"
    Dad "(Храп…)"
    if renpy.loadable("patch.rpy"):
        MC "(Слава Богу, папа крепко спит!)"
    else:
        MC "(Слава Богу, Боб крепко спит!)"
    Dad "ЗЕВОК!"

    scene MLR2_NS2_p21

    MC "Вот дерьмо..."
    Mom "(Блядь…)"
    Dad "(Snoooree…)"
    MC "Хух…"
    Mom "(Я думала, он проснется!)"

    scene MLR2_NS2_p22

    Mom "Разве я не говорила тебе работать языком??"
    MC "Да, но..."
    Mom "Тащи свое лицо, прижимайся к моим бедрам, прямо сейчас!"

    scene MLR2_NS2_p23

    Mom "Быстрее! Я скоро кончу!"
    if renpy.loadable("patch.rpy"):
        Mom "Мне нужно чувствовать, что язык моего сына извивается и щелкает глубоко внутри моей киски!"
        MC "(Вот так ... давайте дадим маме лучший Кунилингус, который у нее когда-либо был!)"
    else:
        Mom "Мне нужно чувствовать, что [player_name] корчится языком и щелкает-глубоко внутри моей киски!"
        MC "(Вот так ... давайте дадим Линде лучший Куннилингус, который у нее когда-либо был!)"

    scene MLR2_NS2_p24

    Mom "Ааа! да!"
    scene MLR2_NS2_p24anim
    MC "(Лижет! Slurp!)"
    scene MLR2_NS2_p26anim
    om "Прямо там! Не останавливайся! Ах!"

    scene MLR2_NS2_p25

    MC "(Suck! Lick! Shlurp!)"
    Mom "AHHH! Святой трах! Ааа! Мммм!"
    Mom "О Боже! О Боже! Да! Не останавливайся!"

    scene MLR2_NS2_p26

    Mom "Глубже! Сильнее!"
    Dad "(Snoooore…)"
    MC "(Она прижимает мою голову!)"


    scene MLR2_NS2_p26a

    Mom "Ой! Ой! ой!"
    MC "(Ее дыхание стало ДЕЙСТВИТЕЛЬНО быстрым! Похоже, она на подходе!)"
    MC "(Лижет! Лижет! Лижет!)"

    scene MLR2_NS2_p27

    Mom "Oххххх дааааааааа! Кончааааююю! Eek!"
    Mom "Aххххххх! Oooххххх!"
    if renpy.loadable("patch.rpy"):
        Mom "(Горячий влажный язык моего сына заставляет меня кончить!)"
    else:
        Mom "([player_name] с горячим влажным языком заставил меня кончить!)"
    Mom "Хмммммм!!! Aaaххххххх!"

    scene MLR2_NS2_p28

    Mom "(Пыхтит…)"
    Mom "(Задышка…)"
    Dad "(Snooorreeee…)"
    MC "(Лижет!)"
    Mom "Подожди... я - аааа - кончаю!"
    MC "(Лижет Лижет Лижет!)"

    scene MLR2_NS2_p29

    Mom "(О Боже! Это ооочень чувствительно! Почему он не останавливается?!)"
    scene MLR2_NS2_p29anim
    Mom "MMMMMM!!!!!"
    Mom "(Он чувствует себя так хорошо!)"

    scene MLR2_NS2_p30

    Mom "MMMM! MMMMMPPFFFFFF!!!"
    MC "(Лижет Лижет Лижет!)"
    window hide
    scene MLR2_NS2_p30anim
    $ renpy.pause(7,hard = True)
    scene MLR2_NS2_p30a
    MC "(Я думаю, что я заставлю ее кончить, во второй раз!)"
    if renpy.loadable("patch.rpy"):
        MC "(Черт, она извивается и трепещет по всей кровати! Я удивлен, что папа не проснулся!)"
    else:
        MC "(Черт, она извивается и трепещет по всей кровати! Я удивлен, что Боб не проснулся!)"


    scene MLR2_NS2_p31

    Mom "Черт возьми ... это было потрясающе."
    Mom "Где ты научился так делать?"
    MC "Честно? Это первый раз, когда я когда-либо делал куни."

    scene MLR2_NS2_p32

    Mom "Mмм... You’re a natural, then."
    MC "Хех! Я так полагаю."
    Mom "Этот второй был лучшим оргазмом, который я когда-либо чувствовала в своей жизни."
    Mom "Я тебя люблю."

    scene MLR2_NS2_p33

    Mom "Mмм…"
    MC "Mмм!"

    scene MLR2_NS2_p34

    MC "(Был ли я действительно настолько хорош в оральном сексе? Я не понял!)"
    MC "(Мне придется запомнить это, в будущем, для других девушек.)"
    Mom "Mмм…"
    if renpy.loadable("patch.rpy"):
        MC "(Надеюсь, когда-нибудь я смогу трахнуть маму. Не могу дождаться этого.)"
    else:
        MC "(Надеюсь, когда-нибудь я смогу трахнуть Линду. Не могу дождаться этого.)"
    $ can_MLR2_MS1_ES3 = True
    $ MLR2_NS2 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump salon_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
