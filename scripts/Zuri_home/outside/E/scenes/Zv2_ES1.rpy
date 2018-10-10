image Z_ES1_p1 = "images/Zuri_home/outside/E/scenes/Z_ES1/1.jpg"
image Z_ES1_p2 = "images/Zuri_home/outside/E/scenes/Z_ES1/2.jpg"
image Z_ES1_p3 = "images/Zuri_home/outside/E/scenes/Z_ES1/3.jpg"
image Z_ES1_p4 = "images/Zuri_home/outside/E/scenes/Z_ES1/4.jpg"
image Z_ES1_p5 = "images/Zuri_home/outside/E/scenes/Z_ES1/5.jpg"
image Z_ES1_p6 = "images/Zuri_home/outside/E/scenes/Z_ES1/6.jpg"
image Z_ES1_p7 = "images/Zuri_home/outside/E/scenes/Z_ES1/7.jpg"
image Z_ES1_p8 = "images/Zuri_home/outside/E/scenes/Z_ES1/8.jpg"
image Z_ES1_p9 = "images/Zuri_home/outside/E/scenes/Z_ES1/9.jpg"
image Z_ES1_p10 = "images/Zuri_home/outside/E/scenes/Z_ES1/10.jpg"
image Z_ES1_p11 = "images/Zuri_home/outside/E/scenes/Z_ES1/11.jpg"
image Z_ES1_p12 = "images/Zuri_home/outside/E/scenes/Z_ES1/12.jpg"
image Z_ES1_p13 = "images/Zuri_home/outside/E/scenes/Z_ES1/13.jpg"
image Z_ES1_p14 = "images/Zuri_home/outside/E/scenes/Z_ES1/14.jpg"
image Z_ES1_p15 = "images/Zuri_home/outside/E/scenes/Z_ES1/15.jpg"
image Z_ES1_p16 = "images/Zuri_home/outside/E/scenes/Z_ES1/16.jpg"
image Z_ES1_p17 = "images/Zuri_home/outside/E/scenes/Z_ES1/17.jpg"
image Z_ES1_p18 = "images/Zuri_home/outside/E/scenes/Z_ES1/18.jpg"
image Z_ES1_p19 = "images/Zuri_home/outside/E/scenes/Z_ES1/19.jpg"
image Z_ES1_p20 = "images/Zuri_home/outside/E/scenes/Z_ES1/20.jpg"




default Suri_name = "Сури"
default can_Zv2_ES1 = True
label Z_ES1_label:
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene Z_ES1_p1 with dissolve
    $ can_hide_windows = True
    MC "(Ну, это похоже на то место. Хороший дом!)"
    if renpy.loadable("patch.rpy"):
        MC "(Интересно, это будет свидание? Зури кажется кокетливой со мной каждый раз, когда я навещаю папу.)"
    else:
        MC "(Интересно, это будет свидание? Зури кажется кокетливой со мной каждый раз, когда я навещаю Боба.)"
    MC "(Может быть, я просто переоцениваю себя.)"

    $ renpy.sound.play("sfx/knock_knock.wav")
    "*ТУК ТУК ТУК*"
    $ renpy.music.stop(channel="sound", fadeout=1)
    $ Zuri_name = "???"
    Zuri "Входите!"
    $ Zuri_name = "Зури"



    scene Z_ES1_p2

    Zuri "Ой! Привет! Это ты!?"
    MC "(Ебена мать! Она почти голая!)"
    MC "И-э-Привет-"
    Zuri "Ну, чтоты ждешь? Заходи! Не стой как дурак!"

    scene Z_ES1_p3

    Zuri "Что случилось? Ты выглядишь потрясенным, парень."
    MC "Т-ты... низ... ты.."
    Zuri "Что случилось, малыш? Ты заикаешься смотря на меня."
    MC "У тебя есть…"

    scene Z_ES1_p4

    Zuri "Есть ли что-то на меня?"
    MC "Ты носишь только трусики!"
    Zuri "Что ты имеешь в виду?"

    scene Z_ES1_p5

    MC "Я ... эээ (Боже! Почему я так нервничаю сейчас!)"
    MC "(Почему Зури ведет себя так странно! Она никогда не бывает такой в офисе.!)"
    Zuri "Я ничего не вижу на себе."

    scene Z_ES1_p6

    Zuri "Оооо! Ты просто шокирован, что я ношу только трусики?"
    MC "Н-Да!"
    Zuri "Хаха! Как мило! Ты девственник или что-то вроде того?"
    MC "Что?"
    Zuri "Идите и садитесь на диван."

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_Zv2_ES1 = False
    $ can_hide_windows = False
    jump zuri_home_E_label2




label Z_ES1_q2_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music1", loop=True, fadein = 2)
    scene Z_ES1_p7
    $ can_hide_windows = True
    MC "Итак, э-э ... Ты хотела, чтобы я пришел сегодня вечером?"
    MC "Что мы, гм ... планируем делать? Ужин? Или фильм?"
    Zuri "Ты много говоришь, малыш."

    scene Z_ES1_p8

    Zuri "Просто пытайся расслабиться. Ты заставляешь меня нервничать."
    Zuri "Ты никогда не видел девушку, одетую как шлюха?"
    MC "Да. Я имею в виду…"

    scene Z_ES1_p9

    Zuri "Тогда тебе не стоит нервничать из-за меня.."
    Zuri "Теперь иди и сядь на диван."

    jump Z_ES1_q1_label

label Z_ES1_q1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    scene Z_ES1_p10
    $ can_hide_windows = True
    MC "(Какого черта происходит?)"
    MC "(Зури совсем не ведет себя как она. И я понятия не имею, зачем она меня сюда пригласила..)"
    MC "(Она одета очень скудно, так что, возможно, она хочет заняться сексом?)"

    scene Z_ES1_p11

    Zuri "Ах, вот ты где."
    MC "Вау! Ты быстро оделась !"
    Zuri "Хмм?"

    scene Z_ES1_p12

    MC "Ты действительно напугала меня, когда открыла входную дверь, почти голой!"
    Zuri "Угу…"
    MC "Серьезно, что если это был не я? Что, если бы это был почтальон или кто-то?"

    scene Z_ES1_p13

    Zuri "Я не открывал тебе дверь.."
    MC "Как?"
    Zuri "И я ношу одежду всю ночь."
    MC "Тогда кто...?"

    scene Z_ES1_p14
    $ Suri_name = "???"
    Suri "Буу!"
    MC "Aаа!"
    if renpy.loadable("patch.rpy"):
        Zuri "[player_name], познакомься с моей сестрой-близнецом, Сури."
    else:
        Zuri "[player_name], знакомься, Сури."
    $ Suri_name = "Сури"
    Suri "Прости, что не сказала тебе раньше."

    scene Z_ES1_p15

    MC "Вас двое?!"
    if renpy.loadable("patch.rpy"):
        Zuri "О, да. Сури не работает в компании твоего отца."
    else:
        Zuri "О, да. Сури не работает в компании Боба."
    MC "Тогда зачем ты хотела, чтобы я пришел сегодня вечером??"

    scene Z_ES1_p16

    Zuri "Это не просто свидание. Я уверена, ты догадался."
    if renpy.loadable("patch.rpy"):
        Zuri "Это деловое предложение. Твой отец в настоящее время строит инвестиционный портфель очень богатых компаний. Если он приобретет большинство своих акций, его компания может заработать миллионы."
    else:
        Zuri "Это деловое предложение. Боб в настоящее время строит инвестиционный портфель очень богатых компаний. Если он приобретет большинство своих акций, его компания может заработать миллионы."
    Zuri "Вот где вы ходите."

    scene Z_ES1_p17

    Suri "Мы хотим, чтобы ты дал нам названия компаний."
    if renpy.loadable("patch.rpy"):
        MC "Зачем мне это делать? Разве это не повредит компании моего отца?"
    else:
        MC "Зачем мне это делать? Не повредит ли это Бобу?"
    Suri "Конечно! Со временем!"
    Suri "Но мы предлагаем тебе что-то действительно интересное в замен."

    scene Z_ES1_p18
    if renpy.loadable("patch.rpy"):
        Zuri "Это может быть единственный раз в твоей жизни, когда ты будешь с близнецами."
    else:
        Zuri "Это может быть единственный раз в твоей жизни, когда ты сможешь позабавиться с нами."
    Zuri "Вот именно. За каждое название компании , с нас сексуальная награда."
    Zuri "Как это звучит?"
    MC "(Черт побери... я сейчас в таком замешательстве..)"

    scene Z_ES1_p19

    Zuri "Я дам тебе время, чтобы принять решение.."
    Zuri "В то же время, я уверен, что Сури может ... помочь убедить тебя в принятии правильного решения."
    if renpy.loadable("patch.rpy"):
        Suri "Конечно могу, сестренка.."
    else:
        Suri "Конечно могу, Зури.."

    scene Z_ES1_p20

    Suri "Вот то, что ты получешь, если поможешь нам."
    Suri "Что скажешь??"
    MC "(Вау! Эти сиськи потрясающие!)"
    MC "Я ..."
    Suri "Подумай об этом. Тогда поговори с Зури, когда будешь готов принять решение."
    $ zuri_bath_event_unlock = True
    $ day_time = 4
    $ Zv2_ES1 = False
    $ Zv2_MS2_q9 = True
    $ zuri_inhome = False
    $ Bobv2_MS1_q4 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
