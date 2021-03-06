image SR2_NS1_p1 = "images/home/mc_room/night/scenes/SR2_NS1/1.jpg"
image SR2_NS1_p2 = "images/home/mc_room/night/scenes/SR2_NS1/2.jpg"
image SR2_NS1_p3 = "images/home/mc_room/night/scenes/SR2_NS1/3.jpg"
image SR2_NS1_p4 = "images/home/mc_room/night/scenes/SR2_NS1/4.jpg"
image SR2_NS1_p5 = "images/home/mc_room/night/scenes/SR2_NS1/5.jpg"
image SR2_NS1_p6 = "images/home/mc_room/night/scenes/SR2_NS1/6.jpg"
image SR2_NS1_p7a = "images/home/mc_room/night/scenes/SR2_NS1/7a.jpg"
image SR2_NS1_p7b = "images/home/mc_room/night/scenes/SR2_NS1/7b.jpg"
image SR2_NS1_p8 = "images/home/mc_room/night/scenes/SR2_NS1/8.jpg"
image SR2_NS1_p9a = "images/home/mc_room/night/scenes/SR2_NS1/9a.jpg"
image SR2_NS1_p9b = "images/home/mc_room/night/scenes/SR2_NS1/9b.jpg"
image SR2_NS1_p10 = "images/home/mc_room/night/scenes/SR2_NS1/10.jpg"

label SR2_NS1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    $ can_hide_windows = True

    scene SR2_NS1_p1 with dissolve

    Sara "Надеюсь, ты не забыл, про мой визит."
    MC "Конечно, Сара!"
    Sara "Хехе... Я просто дразню тебя."
    MC "Что случилось?"

    scene SR2_NS1_p2

    Sara "Вообще-то... об этом немного ... трудно говорить."
    MC "Что-то не так?"
    Sara "Нет! По крайней мере... я так не думаю. Надеюсь, что нет."
    if renpy.loadable("patch.rpy"):
        Sara "Можешь залезть со мной под одеяло? Я действительно не хочу, чтобы мама или папа подслушали нас."
    else:
        Sara "Можешь залезть со мной под подеяло? Я действительно не хочу, чтобы Линда или Боб подслушали нас."
    MC "Конечно, без проблем."

    scene SR2_NS1_p3

    MC "Что ты хотела сказать?"
    Sara "Это ... Я не знаю, почему так сложно. Я ЗНАЮ, что хочу сказать, но я не могу заставить себя сказать ни слова."
    Sara "Ты понимаешь, о чем я?"

    scene SR2_NS1_p4

    MC "Я... Думаю, да?"
    Sara "[player_name], мы делали ... вещи вместе. Как в тот раз, когда я сделала тебе минет."
    MC "Или когда мы играли в видео игры?"
    Sara "Это тоже..."

    scene SR2_NS1_p5

    Sara "А потом ты сказал, что любишь меня…"
    Sara "Мне нужно знать... я теперь твоя девушка ?"
    MC "(Похоже, она хочет, чтобы я посвятил себя ей. Если я дурачусь с другими женщинами, это может сделать вещи неудобными…)"


    menu:
        "Ты станешь моей девушкой после секса.":
            scene SR2_NS1_p6

            MC "Вот что я тебе скажу, Сара. Как насчет того, чтобы отметить день, когда ты станешь моей девушкой с чем-то особенным?"
            Sara "Что ты имеешь в виду?"
            MC "Я думала, что ты станешь моей девушкой, когда мы впервые займемся сексом."

            scene SR2_NS1_p9a

            Sara "Сексом?!"
            MC "(Она выглядит довольно потрясенной моим предложением.)"
            MC "Ты в порядке, Сара?"

            scene SR2_NS1_p9b

            Sara "Да, со мной все в порядке. Ты просто застал меня врасплох."
            MC "Прости, плохой ход."
            Sara "Нет, это не твоя вина. Я просто ... я не думаю, что готова заняться сексом."
            MC "Честно говоря, не беспокойся об этом, Сара. Мы можем не торопиться."

            scene SR2_NS1_p10

            Sara "Серьезно?! Большое спасибо, [player_name]."
            Sara "Я хочу сделать это с тобой... когда-нибудь. Мне просто нужно немного больше времени."
            Sara "Может быть, мы могли бы заняться другими вещами вместе?"
            MC "Конечно. Как тебе угодно, Сара."
            Sara "Спасибо, [player_name]. Ты самый лучший."
            jump SR2_NS1_continue
        "Могу я ответить позже? Все происходит очень быстро.":

            scene SR2_NS1_p6

            MC "Могу я дать тебе ответ позже? Кажется, что все происходит очень быстро."
            Sara "Oх…"
            MC "Я не говорю 'нет'. Мне просто нужно время, чтобы все обдумать."

            scene SR2_NS1_p8

            Sara "Я надеялась, что ты скажешь ‘да’."
            MC "Когда-Нибудь, Сара. Просто... не сейчас. Мне нужно больше времени."
            Sara "Хммм…."

            scene SR2_NS1_p7a

            MC "Да ладно тебе, Сара. Не будь такой!"
            MC "Как бы ты себя чувствовала, если бы я начал давить на тебя, чтобы ты занялась сексом до того, как ты была готова? Ты почувствуешь стресс, верно?"

            scene SR2_NS1_p9b

            Sara "Хм ... я так думаю."
            MC "Ну, называть тебя своей девушкой до того, как я буду готов, это тоже самое. Я бы с удовольствием назвал тебя своей второй половинкой, но я сделаю это только тогда, когда буду действительно готов."
            MC "Ты понимаешь?"
            Sara "Да, наверное, да. Извини, [player_name]."

            scene SR2_NS1_p6

            MC "Тебе не нужно извиняться, Сара. Я действительно люблю тебя."
            Sara "Хехе... Я знаю."

            scene SR2_NS1_p7b

            MC "*Mwah*"
            Sara "(О, Боже мой! Я просто таю, каждый раз, когда он целует меня.)"
            jump SR2_NS1_continue
        "Да, но ... мы все еще не делаем то, что делают пары.":

            scene SR2_NS1_p10

            MC "Конечно, Сара. Я бы с удовольствием назвал тебя своей девушкой."
            Sara "Действительно?!"
            MC "Там только одна маленькая проблема... Мы на самом деле не делаем то, что пары делают."

            scene SR2_NS1_p9a

            Sara "Что случилось? Я не понимаю."
            MC "Сара, мы все еще не занимались сексом вместе. Конечно, мы сделали некоторые мелочи здесь и там, но мы еще не настоль близки чтобы переспать."

            scene SR2_NS1_p9b

            Sara "Oх..."
            Sara "Я не... я не думаю, что я готова делать ... такие вещи."

            scene SR2_NS1_p7a

            MC "Не беспокойся, Сара. Не торопись."
            MC "Мы можем обсудить это снова, когда пройдет еще немного времени. Я не хочу, чтобы на тебя давило что-то, с чем тебе не совсем комфортно."
            MC "Не забывай, что я действительно люблю тебя."

            scene SR2_NS1_p7b

            MC "*Mwah*"
            jump SR2_NS1_continue


label SR2_NS1_continue:
    scene SR2_NS1_p4

    Sara "Ну ... может быть, мы могли бы попробовать некоторые другие вещи, чтобы помочь нам приблизиться к сексу?"
    MC "Звучит неплохо. О чем ты думаешь?"
    Sara "Честно говоря, я не знаю. Извини, я вообще не разбираюсь в таких вещах. Как ты думаешь, что бы ты могла мне дать?"

    scene SR2_NS1_p6

    MC "Все нормально. Дай мне подумать…"
    MC "Как я тебя вибратор? Ты можешь использовать его, чтобы практиковать мастурбацию и получать некоторую уверенность в своем собственном теле."
    Sara "Прости, я немного нервничаю.."
    MC "Все нормально. Вот что я тебе скажу - я пойду и куплю тебе один. Ты можешь оставить его в своей комнате и попробовать сама. Я не буду давить на тебя, используй когда захочешь."

    scene SR2_NS1_p10

    Sara "Да... звучит не так уж плохо!"
    Sara "После того, как купишь его, скажи мне в школе. И я прокрадусь к тебе в спальню чтобы забрать его."
    MC "Без проблем, Сара. Я дам тебе знать."
    Sara "Ладно, мне лучше вернуться в постель. Увидимся позже, [player_name]. Спокойной ночи!"
    MC "Сладких снов, Сара."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    $ SR2_AS2 = False
    $ SR2_NS1 = False
    $ SR2_AS3 = True
    $ S_N_inbed = True
    jump sleeping_after_scene
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
