image intro1 = "/images/intro/1.jpg"
image intro2 = "/images/intro/2.jpg"
image intro3 = "/images/intro/3.jpg"
image intro4 = "/images/intro/4.jpg"
image intro5 = "/images/intro/5.jpg"
image intro6 = "/images/intro/6.jpg"
image intro7 = "/images/intro/7.jpg"
image intro8 = "/images/intro/8.jpg"
image intro9 = "/images/intro/9.jpg"
image intro10 = "/images/intro/10.jpg"
image intro11 = "/images/intro/11.jpg"
image intro12 = "/images/intro/12.jpg"
image intro13 = "/images/intro/13.jpg"
image intro14 = "/images/intro/14.jpg"
image intro15 = "/images/intro/15.jpg"
image intro16 = "/images/intro/16.jpg"
image intro17 = "/images/intro/17.jpg"
image intro18 = "/images/intro/18.jpg"
image intro19 = "/images/intro/19.jpg"
image intro20 = "/images/intro/20.jpg"
image intro21 = "/images/intro/21.jpg"
image intro22 = "/images/intro/22.jpg"
image intro23 = "/images/intro/23.jpg"
image intro24 = "/images/intro/24.jpg"
image intro25 = "/images/intro/25.jpg"
image intro26a = "/images/intro/26a.jpg"
image intro26b = "/images/intro/26b.jpg"
image intro27 = "/images/intro/27.jpg"
image intro28 = "/images/intro/28.jpg"
image intro29 = "/images/intro/29.jpg"
image intro30 = "/images/intro/30.jpg"
image intro31 = "/images/intro/31.jpg"
image intro32 = "/images/intro/32.jpg"
image intro33 = "/images/intro/33.jpg"
image intro34 = "/images/intro/34.jpg"
image intro35 = "/images/intro/35.jpg"
image intro36 = "/images/intro/36.jpg"
image intro37 = "/images/intro/37.jpg"
image intro38 = "/images/intro/38.jpg"
image intro39 = "/images/intro/39.jpg"
image intro40 = "/images/intro/40.jpg"
image intro41 = "/images/intro/41.jpg"
image intro42 = "/images/intro/42.jpg"
image intro43 = "/images/intro/43.jpg"
image intro44 = "/images/intro/44.jpg"
image intro45 = "/images/intro/45.jpg"
image intro46 = "/images/intro/46.jpg"
image intro47 = "/images/intro/47.jpg"
image intro48 = "/images/intro/48.jpg"
image intro49 = "/images/intro/49.jpg"
image intro50 = "/images/intro/50.jpg"
image intro51 = "/images/intro/51.jpg"
image intro52 = "/images/intro/52.jpg"
image intro53 = "/images/intro/53.jpg"
image intro54 = "/images/intro/54.jpg"
image before_intro1 = "/images/intro/before/1.jpg"
image before_intro2 = "/images/intro/before/2.jpg"
image before_intro3a = "/images/intro/before/3a.jpg"
image before_intro3b = "/images/intro/before/3b.jpg"
image before_intro4 = "/images/intro/before/4.jpg"
define flash = Fade(.25, 0.0, .75, color="#fff")
define Judy = Character("[Judy_name]", color="#993333")
define MC = Character("[player_name]", color="#3366FF")
define Sara = Character("[Sara_name]", color="#00FFCC")
define Mom = Character("[Mom_name]", color="#CC00CC")
define Celia = Character("[Celia_name]", color="#FF6EC7")
define Students = Character("[Students_name]")
define Caroline = Character("[Caroline_name]", color="#66CC33")

image intro_movie = Movie(play="/images/intro/before/intro_movie.webm", loop = True,)
transform slightleft:
    xalign 0.96
    yalign 0.4

label intro:
    $ can_hide_windows = True
    scene before_intro1 with dissolve
    "Привет всем! Подождите! Не пропускайте!"
    "Прежде чем мы перейдем к прологу, дайте мне возможность быстро рассказать вам несколько вещей!"
    scene before_intro4
    "Во-первых, и самое главное ... эта игра все еще продолжается!"
    scene before_intro2
    "Черт... Как и почти все другие игры, верно?"
    "Черт ... это было плохое начало."

    scene before_intro4
    "Но - не волнуйся! Там должно быть БОЛЬШЕ, чем достаточно контента, чтобы заставить вас * кхм * повеселиться!"
    scene before_intro3a
    "Второй важной информацией является то, что эта игра полностью интерактивна! Карта, инвентарь, элементы мини-игры, множество символов!"
    "ВЫ решаете, какую историю вы хотите продвигать вперед! Если вам не нравиться кто-то, вы можете даже полностью игнорировать их!"

    scene before_intro4
    "Третья и последняя информация состоит в том, что в игре есть анимированные сексуальные сцены!!"
    "Да! Ну вот! Анимированные!! Вы услышали меня хорошо!"


    scene before_intro3b
    "Просто ознакомьтесь с этим дерьмом!"
    show intro_movie at slightleft
    window hide
    $ renpy.pause()
    scene before_intro1
    "Ладно, я думаю, этого достаточно! Повеселись!"
    $ renpy.music.stop(channel="music", fadeout=2)
    scene black
    show intro21 with flash
    hide intro21
    show intro28 with flash
    hide intro28
    show intro46 with flash
    scene black
    $ Judy_name="???"
    $ player_name="???"
    Judy "С тобой все в порядке?"
    Judy "Эй, тебе нужно проснуться."
    $ renpy.music.play('/sfx/RetroFuture_Clean.mp3',channel="music1", loop=True, fadein=2)
    scene intro1 with dissolve
    MC "Да ?! Где я?!"
    Judy "Это я, Джуди - школьный терапевт."
    $ Judy_name="Джуди"
    Judy "Я попросила тебя закрыть глаза и попытаться вспомнить вчерашние события, но ты уснул."
    MC "О, о да. Извини, я плохо спал в последнее время."
    Judy "Хм ... попробуй откинуться на спинку стула и расслабиться. Устраивайся поудобнее."

    scene intro2
    MC "Хорошо, без проблем."
    Judy "На самом деле, прежде чем мы начнем, мне нужно проверить правильность твоих данных."
    Judy "Ты в классе 7C, правильно?"
    MC "Да, 7C."
    Judy "Хорошо, твое имя?"
    $ player_name = renpy.input("Как вас зовут?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="MC"
    if not renpy.loadable("patch.rpy"):
        Judy "И человек, живущий с тобой, - это ... Линда?"
    if renpy.loadable("patch.rpy"):
        Judy "А твоя мать ... Линда?"
    MC "Да, это так."

    scene intro7
    Judy "Хорошо, все в порядке."
    Judy "Я собираюсь взять пару минут опять."
    Judy "Меня зовут Джуди Ханниган. Я психолог в школе ."
    Judy "Что вчера случилось"

    scene intro3
    MC "Расслабься! Все отлично! Действительно."
    Judy "[player_name], то, что произошло, было очень серьезным."
    MC "Все круто - я могу справиться сам."
    Judy "Я не уверена в то, что все “хорошо”. Эта консультационная служба предназначена для твоего собственного благополучия."
    MC "Я ... я больше не хочу думать о вчерашнем. Я собираюсь уйти и притвориться, что этого никогда не было."
    MC "Хаха! Честно говоря, это шутка, что я вообще здесь."

    scene intro4
    Judy "Но это случилось, [player_name]. Тот факт, что вы просто решили не обращаться к нему, не является здоровым."
    Judy "Избегающее поведение широко распространено в людей, выздоравливающих от травмы."
    Judy "Кроме того, если я выйду из этой комнаты прямо сейчас, у меня не будет выбора, кроме как подписать это письмо о исключении."

    scene intro5
    Judy "Вижу, ты перестал идти к двери. Ты не знал, что я подчиняюсь непосредственно директору?"
    Judy "Он попросил меня следить за твоим прогрессом и поведением., [player_name]."
    Judy "Я знаю, что ты сейчас не чувствуешь этого , но я обещаю, это для твоего же блага."
    $ renpy.music.stop(channel="music1", fadeout=2)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)

    scene intro6
    Judy "То что случилось с тобой, было неловко. Чрезвычайно. Я даже представить не могу, что ты сейчас чувствуешь.."
    Judy "Но бегство ничего не исправит. Пожалуйста, позволь помочь тебе. Садись. Давай поговорим об этом."
    Judy "Ты можешь доверять мне."
    MC "(Вздох)"
    if renpy.loadable("patch.rpy"):
        MC "Отлично ... Не посылай это письмо директору, мама убьет меня."
    if not renpy.loadable("patch.rpy"):
        MC "Отлично ... Не посылай это письмо директору, Линда убьет меня."
    Judy "(Я знаю, что Линда будет бушевать, если его вышвырнут из школы.)"
    Judy "Я рада, что ты передумал. Садись. Начнем с самого начала.."
    scene intro7
    $ a1 = True
    $ a2 = True
label q1_intro:
    Judy "Прежде чем мы начнем, есть ли что-нибудь, что ты хотел бы спросить меня?"
    menu:
        "Не мог бы ты рассказать мне немного больше о себе?" if a1 == True:
            $ a1 = False
            jump q1_a1_intro

        "Сколько времени займет эта терапия?" if a2 == True:
            $ a2 = False
            jump q1_a2_intro
        "Больше вопросов нет.":
            jump after_q1_intro

label q1_a1_intro:
    Judy "Конечно, [player_name]. Лучше всего, когда пациенты чувствуют себя комфортно со своим терапевтом."
    Judy "Мое полное имя Джуди Ханниган. Я квалифицированный терапевт. Я окончила Университет Висконсина четыре года назад. С тех пор я работаю в этой школе."
    jump q1_intro
label q1_a2_intro:
    Judy "Столько, сколько потребуется. Ты не можешь торопить эти вещи, [player_name]."
    Judy "Некоторые люди могут быть дома в течение трех или четырех сеансов. Другие люди... намного дольше. Важно добиваться прогресса. Не рассматривай свое лечение как гонку - подумайте об этом как о путешествии."
    MC "Да ... наверное, да. Мне не нравится идея, что это происходит так долго."
    Judy "Мы пересечем этот мост, когда придем к нему."
    jump q1_intro
label after_q1_intro:
    Judy "Теперь скажи мне, [player_name], что случилось вчера?"
    $ renpy.music.stop(channel="music2", fadeout=2)
    scene black
    $ renpy.pause(2.0)
    scene intro8 with dissolve
    $ renpy.music.play('/sfx/Vivacity.mp3', channel="music1", loop=True, fadein = 2)
    $ Sara_name="???"
    Sara "Эй, [player_name]! Проснись! Ты опоздаешь в школу!"
    MC "(Зевок) Еще пять минут, Сара…"
    $ Sara_name="Сара"
    Sara "Ты опоздаешь!"

    scene intro9
    MC "(Вздох) Отлично! Я проснулся.…"
    Sara "Итак, ты действительно собираешься сделать это?"
    MC "Хмм?"
    Sara "Ты действительно собираешься пригласить миссис Селию на свидание?"
    MC "Да, конечно."

    scene intro10
    Sara "Я не думаю, что это такая хорошая идея, [player_name]. Она точно отвергнет тебя.."
    MC "Просто расслабься - все будет хорошо, и я наконец-то трахну ее!"
    Sara "Трахаться-это единственное, о чем ты думаешь?!"
    Sara "Кроме того, почему ты думаешь, что она вообще заинтересована тобой!"

    scene intro11
    MC "Мы работаем по принципу имени. Она позволяет мне называть ее Селия."
    Sara "И что? Я называю некоторых своих учителей по имени."
    MC "Дело не только в этом! Она всегда смотрит на меня и улыбается."
    Sara "Может быть, она просто счастливый человек?"
    MC "Кроме того, она коснулась моей задницы, когда я шел в коридоре!"

    scene intro12
    Sara "Ты уверен, что ее рука не просто скользнула?"
    MC "Что?! Нет, она определенно прикоснулась ко мне, специально!"
    MC "(По крайней мере... я так думаю…)"
    Sara "Эй! Что ты делаешь?! Я все еще здесь!"

    scene intro13
    MC "Да?"
    Sara "Ты изменился! По крайней мере, предупреждай, чтобы я не смотрела на твою мерзкую задницу!"
    MC "О, пожалуйста, у тебя тоже есть. Если ты так беспокоишься, то убирайся из моей комнаты!"
    Sara "Запросто."

    scene intro14
    Sara "Эй! [player_name]! Положи одежду!"
    MC "Я сказал тебе выбраться из комнаты!"
    Sara "Фу! Отлично! Но, пожалуйста, прислушайся к моему совету-не приглашай миссис Селию! Это плохо закончится."
    MC "Расслабься, Сара. Что плохого может случиться?"
    $ renpy.music.stop(channel="music1", fadeout=2)
    scene black
    $ renpy.pause(2.0)
    scene intro15 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    Judy "Хм... интересно... Ты не возражаешь, если я задам вам несколько вопросов о Саре?"
    MC "Наверное, да."
    $ a1 = True
    $ a2 = True
    $ a3 = True
label q2_intro:
    Judy "Кто такая Сара?"
    menu:
        "Расскажите о увлечениях Сары." if a1 == True:
            MC "Сара-зануда. Она проводит свободное время, играя в видеоигры, читает комиксы и смотрит на показательные британские телешоу."
            Judy "Тебе нравятся такие занятия?"
            MC "Я имею в виду, видеоигры-это весело, но я действительно не понимаю привлекательности комических комиксах или шоу, которые она смотрит."
            $ a1 = False
            if a2 == False and a3 == False:
                jump after_q2_intro
            else:
                jump q2_intro
        "Расскажите школьной жизни Сары." if a2 ==True:
            MC "Она лучшая в классе по математике, биологии и химии. Я думаю, что она на самом деле хочет стать компьютерным ученым когда-нибудь."
            if renpy.loadable("patch.rpy"):
                Judy "Она безусловно умная. Ты, должно быть, очень гордишься тем, что у тебя есть сестра."
            if not renpy.loadable("patch.rpy"):
                Judy "Она умная. Ты должно быть очень гордишься ей."
            MC "Наверное, да. Я никогда об этом не думал. "
            $ a2 = False
            if a1 == False and a3 == False:
                jump after_q2_intro
            else:
                jump q2_intro
        "Расскажите о социальной жизни Сары." if a3 == True:
            MC "Сара держит себя в руках, в основном. У нее есть пара близких друзей, но я думаю, что она наслаждается, общаясь с небольшими группами людей."
            Judy "Хммм... В моей профессии мы бы назвали это интровертом. В основном, она находит время в небольших группах более полезным."
            Judy "Следовательно, большие социальные ситуации могут быть особенно утомительными для интровертов."
            $ a3 = False
            if a1 == False and a2 == False:
                jump after_q2_intro
            else:
                jump q2_intro
label after_q2_intro:

    scene intro17
    Judy "Спасибо, что ответил на мои вопросы. Мой следующий может быть ... немного неловким, но нам придется углубиться в некоторые методы Фрейдистского психоанализа."
    MC "Психо-что?"
    if renpy.loadable("patch.rpy"):
        Judy "Фрейдистский Психоанализ. Скажи мне, [player_name], ты находишь свою сестру, Сару, сексуально привлекательной?"
    if not renpy.loadable("patch.rpy"):
        Judy "Фрейдистский Психоанализ. Скажи мне, [player_name], ты находишь Сару сексуально привлекательной?"
    scene intro16
    MC "Что?!"
    if renpy.loadable("patch.rpy"):
        Judy "Как ты думаешь, твоя сестра сексуальна?"
    if not renpy.loadable("patch.rpy"):
        Judy "Как ты думаешь, Сара сексуальна?"
    MC "Я-как - это не подходящий вопрос!"

    scene intro17
    Judy "Уверяю тебя, так оно и есть. Фрейдистская Психология вникает в природу человеческой сексуальности. "
    Judy "Учитывая характер этого инцидента, который привел тебя ко мне, сексуализированный элемент психологии наиболее определенно актуален."
    if renpy.loadable("patch.rpy"):
        MC "Но... она моя сестра…"
    if not renpy.loadable("patch.rpy"):
        MC "Но... она моя очень близкая подруга…"
    Judy "Как часто ты фантазируешь о сексе с Сарой?"

    scene intro16
    MC "(Честно? Я думал трахнуть ее не раз. Я помню, как столкнулся с ней, когда она вышла из душа, в прошлом году. Ее полотенце упало, и я увидел ее милые сиськи.)"
    MC "(Я, должно быть, дрочил на этот мысленный образ в течение недели!)"
    MC "Эти вопросы действительно странные. Я не ... мне неудобно говорить об этом.."

    scene intro18
    Judy "Понятно. Ты все еще находишься на ранних стадиях лечения. Это может занять некоторое время, чтобы полностью раскрыться. "
    Judy "Очень важно, чтобы ты были честе со мной, если хотишь полностью вылечиться."
    if renpy.loadable("patch.rpy"):
        MC "(Вздох) Хорошо. Наверное, я ... может быть ... фантазировал о своей сестре, пару раз."
    if not renpy.loadable("patch.rpy"):
        MC "(Вздох) Хорошо. Наверное, я ... может быть ... фантазировал о Саре пару раз."
    Judy "Интересно..."
    Judy "Мы можем вернуться к этому вопросу в другой раз. Пока, пожалуйста, скажите мне, что произошло дальше, в день происшествия."
    MC "Позволь мне подумать ... Я как раз собирался уехать в школу."

    $ renpy.music.stop(channel="music2", fadeout=2)
    scene black
    $ renpy.pause(2.0)
    scene intro19 with dissolve
    $ renpy.music.play('/sfx/Why_Did_You_Do_It_-_Everet_Almond.mp3', channel="music1", loop=True, fadein = 2)
    MC "(Дерьмо! Сара была права! Я опоздаю, если не потороплюсь!)"
    MC "(Думаю, она ушла десять минут назад. Я не должен был так долго сидеть в душе!)"

    scene intro20
    if not renpy.loadable("patch.rpy"):
        $ Mom_name = "Линда"
    Mom "Куда ты торопишься?"
    MC "Я опаздываю в школу.!"
    Mom "ты не забыл сказать доброе утро кому-то?"
    if renpy.loadable("patch.rpy"):
        MC "Доброе Утро, Мама! Увидимся позже."
    if not renpy.loadable("patch.rpy"):
        MC "Доброе Утро, Линда! Увидимся позже."
    scene intro21
    Mom "Да ладно. У тебя есть время поприветствовать меня как следует.."
    Mom "Ты будешь стесняться."
    MC "Я действительно тороплюсь."
    Mom "Почему? Сегодня происходит что-то особенное?"
    MC "Ух... Н-Нет!"

    scene intro22
    Mom "Тогда подойди и поцелуй меня."
    MC "Хорошо, без проблем."
    Mom "В губы."
    if renpy.loadable("patch.rpy"):
        MC "Серьезно, Мам? Никто моего возраста больше не целует маму в губы! Если кто-нибудь узнает, они будут смеяться надо мной!"
    if renpy.loadable("patch.rpy"):
        MC "Серьезно, Мама?"
    Mom "Тогда убедись, что никто не узнает.."

label choice1_intro:
    $ kiss_mom_cheek=False
    $ kiss_mom_lips=False
    menu:
        "Поцеловать маму в щеку." if renpy.loadable("patch.rpy"):

            $ kiss_mom_cheek=True
            scene intro23
            MC "*Поцелуй*"
            MC "Прости, Мам, я вырос. Увидимся позже, когда я вернусь из школы.."

            scene intro26b
            Mom "Хмм!"
            Mom "(Почему он не поцелует меня?! Не похоже, чтобы кто-то из его одноклассников видел, как он это делает…)"
            jump after_choice1_intro
        "Поцеловать маму в губы." if renpy.loadable("patch.rpy"):

            $ kiss_mom_lips=True
            scene intro24
            MC "Хаха! Хорошо, Мам. Если это сделает тебя счастливой."
            Mom "Это будет...."

            scene intro25
            Mom "(Шепот) Это действительно будет..."
            MC "(А? Мама сегодня ведет себя немного странно. Она хорошо себя чувствует?)"

            scene intro26a
            MC "(Поцелуй)"
            Mom "Mмм…"
            Mom "(Боже ... Хотела бы я просто прижать его к кровати и разобраться с ним.)"
            jump after_choice1_intro
        "Поцеловать Линду в щеку." if not renpy.loadable("patch.rpy"):

            $ kiss_mom_cheek=True
            scene intro23
            MC "*Поцелуй*"
            MC "Прости, Линда, я уже вырос. Увидимся позже, когда я вернусь из школы.."

            scene intro26b
            Mom "Хммм!"
            Mom "(Почему он не поцелует меня?! Не похоже, чтобы кто-то из его одноклассников видел, как он это делает…)"
            jump after_choice1_intro
        "Поцеловать Линду в губы." if not renpy.loadable("patch.rpy"):

            $ kiss_mom_lips=True
            scene intro24
            MC "Хаха! Хорошо, Линда. Если это сделает тебя счастливой."
            Mom "Это будет...."

            scene intro25
            Mom "(Шепот) Это действительно..."
            MC "(А? Сегодня Линда немного странная. Интересно, она чувствует себя хорошо?.)"

            scene intro26a
            MC "(Поцелуй)"
            Mom "Mмм…"
            Mom "(Боже ... Хотела бы я просто прижать его к кровати и разобраться с ним.)"
            jump after_choice1_intro

label after_choice1_intro:

    scene intro22
    if renpy.loadable("patch.rpy"):
        MC "Увидимся позже, мама."
    if not renpy.loadable("patch.rpy"):
        MC "Увидимся позже, Линда."
    Mom "Увидимся вечером, милый!"
    Mom "(Я начинаю промокать, просто думая о том, что поцеловалась с ним..)"
    $ renpy.music.stop(channel="music1", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro27 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    if renpy.loadable("patch.rpy"):
        Judy "Твоя мать очень интересный человек. Она явно заботится о тебе."
    if not renpy.loadable("patch.rpy"):
        Judy "Линда очень интересный человек. Она явно заботится о тебе."
    MC "Да, я думаю, да."
    Judy "Мы вернемся, чтобы поговорить о ней позже. Пока же, пожалуйста, расскажи мне об инциденте."
    MC "(Глоток)"
    Judy "Я знаю, что это трудно. Пожалуйста, не торопись. Если тебе нужно сделать перерыв, просто дай мне знать."

    $ renpy.music.stop(channel="music2", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro28 with dissolve
    $ renpy.music.play('/sfx/Fork_and_Spoon.mp3', channel="music1", loop=True, fadein = 2)
    MC "Миссис Селия?"
    Celia "Пожалуйста, я сказал тебе называть меня Селия. Как я могу тебе помочь, [player_name]?"
    MC "Миссис Сели-Селия, я хотел спросить, не хочешь ли ты пойти со мной ... в пиццерию Бенизы, и ... (залпом) посмотреть фильм после этого?"
    Celia "Ты приглашаешь меня на свидание, [player_name]?"

    scene intro29
    MC "Д-Да."
    Celia "…"
    MC "Что ж?"
    Celia "…"
    Celia "Хахахахаха! Ты серьезно приглашаешь учителя на свидание.?!"
    MC "Я - Э - Эх…"

    scene intro30
    Celia "О, Боже мой! Это слишком смешно!"
    MC "Я думал..."
    Celia "Хахахах!"

    show intro31 with hpunch
    Students "Он просто спросил ее?!"
    Students "О мой Бог! Он сделал!"
    Students "Я был бы огорчен, если бы это случилось со мной!"
    Students "Aхахахаха!"
    Students "Какой неудачник! Хахаха!"
    $ renpy.music.stop(channel="music1", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro32 with dissolve
    $ renpy.music.play('/sfx/Secrets_of_the_Schoolyard.mp3', channel="music2", loop=True, fadein = 2)
    MC "Я был таким... чертовски злым."
    Judy "Я вижу. Ты показываешь чрезвычайно агрессивный язык тела - сжатые кулаки, сгорбленная поза."
    Judy "Ты все еще злишься, не так ли?"
    MC "Конечно, черт возьми! Она опозорила меня перед всей школой.!"

    scene intro33
    Judy "Я думаю, это хорошо, что ты пришел на терапию."
    Judy "Скажи мне, [player_name], ты хочешь отомстить миссис Селии?"

    scene intro32
    MC "…"
    Judy "Ты можешь сказать мне правду. Пожалуйста, будь честен."
    MC "Да... я ненавижу ее."

    scene intro33
    Judy "Спасибо за честность. Поговорим позже о миссис Селии. А пока, не мог бы ты рассказать мне, что произошло после?"
    if renpy.loadable("patch.rpy"):
        MC "Дай подумать ... я ... я пошел и украл виски моей сестры из ее комнаты."
    if not renpy.loadable("patch.rpy"):
        MC "Дай подумать ... я ... я пошел и украл виски моей подруги из ее комнаты."
    Judy "У Сары есть виски в спальне? (Это похоже на то, что я должна сообщить директору.)"
    if renpy.loadable("patch.rpy"):
        MC "Нет, это была моя старшая сестра, Кэролайн."
    if not renpy.loadable("patch.rpy"):
        MC "Нет, это была моя старшая подруга, Кэролайн.."
    Judy "(О, слава Богу)"
    $ renpy.music.stop(channel="music2", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro34 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    Caroline "Хм? О, эй, [player_name]! Разве ты не знаешь, что вежливо сначала постучать?"
    MC "…"

    scene intro35
    Caroline "Э ... что-то не так, [player_name]?"
    MC "..."
    Caroline "(Что с ним? Он обычно не тихий.)"

    scene intro36
    Caroline "Если ты ищешь зарядное устройство для телефона, я уже вернула ее. Она рядом с твоей кроватью."
    MC "Я ... мне нужен твой виски."
    Caroline "А? Зачем?"
    MC "Я ... мне нужно выпить."
    Caroline "Все в порядке? Тебе нужно немного денег, чтобы купить свой собственный?"
    MC "Я не могу беспокоиться о выходе из дома…"

    scene intro37
    Caroline "Я немного беспокоюсь о тебе..."
    MC "Да, неважно.…"
    Caroline "(Что с ним случилось? Я никогда не видела, чтобы он вел себя так странно..)"
    Caroline "(Может он страдает от депрессии?)"

    scene intro38
    Caroline "В любом случае, я должна закончить еще три главы этой книги к завтрашнему утру."
    Caroline "Иди и возьми бутылку. Будешь должен."
    MC "Конечно…"
    Caroline "(Интересно, что случилось сегодня в школе? Я должна поговорить с Сарой, когда у меня будет шанс..)"
    $ renpy.music.stop(channel="music1", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro7 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    Judy "Что случилось после того, как ты взял виски, [player_name]?"

    scene intro27
    MC "Я много выпил... следующие пару часов были немного размыты. Я помню, как лежал на кровати, думая... …"
    Judy "Что мир поглотит тебя целиком?"
    MC "Да…"
    Judy "Многие пациенты говорили похожие вещи."
    Judy "Скажи мне-что случилось?"
    if renpy.loadable("patch.rpy"):
        MC "Моя мама. Она вошла в мою комнату тем вечером - я не пришел на семейный ужин."
    if not renpy.loadable("patch.rpy"):
        MC "Линда. Она пришла в мою комнату, в тот вечер я не пришел на ужин."

    $ renpy.music.stop(channel="music2", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro39 with dissolve
    $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
    MC "(О Боже ... что я натворил? Я больше не могу показываться в школе.)"
    MC "(Миссис Селия считает меня смешным. Мои одноклассники считают меня неудачником..)"
    MC "(Моя жизнь разрушена…)"

    scene intro40
    "(Стук Стук)"
    Mom "Приветик, сладкий. Что случилось? Ты выглядишь мрачным.."
    if renpy.loadable("patch.rpy"):
        MC "Ничего страшного, мам. Я в порядке."
    if not renpy.loadable("patch.rpy"):
        MC "Ничего страшного, Линда. Я в порядке."
    Mom "Ты выглядишь не очень хорошо. И здесь воняет алкоголем. Ты пил?"
    MC "Чуточку…"
    Mom "(Вздох)"

    scene intro41
    Mom "Кэролайн рассказала мне все, что случилось сегодня в школе. Она беспокоилась о тебе и пошла поговорить с Сарой.. "
    if renpy.loadable("patch.rpy"):
        Mom "Кажется, все в этой семье, кроме меня, знают что случилось. Я надеялася, что ты расскажешь мне."
    if not renpy.loadable("patch.rpy"):
        Mom "Кажется, все здесь знают, что произошло. Я надеялася, что ты расскажешь мне."
    if renpy.loadable("patch.rpy"):
        MC "Мама?"
    if not renpy.loadable("patch.rpy"):
        MC "Линда?"
    Mom "Да, Сладкий?"
    MC "Я ... Я урод?"

    scene intro42
    Mom "Что?! Кто тебе сказал?"
    MC "Никто... Но я чувствую."
    Mom "Ты очень красивый молодой человек."
    if renpy.loadable("patch.rpy"):
        MC "(Вздох) Ты должна сказать это - ты моя мама."
    if not renpy.loadable("patch.rpy"):
        MC "(Вздох) Ты должна сказать..."
    Mom "Посмотри на меня, [player_name]."

    scene intro43
    if renpy.loadable("patch.rpy"):
        Mom "Ты совсем не урод. И я говорю это не потому, что я твоя мама. Во всяком случае, это означает - даже больше - когда это звучит от меня. Я думаю, ты невероятно красив."
        MC "...спасибо, мам. Я все еще не верю, что это правда."
    if not renpy.loadable("patch.rpy"):
        Mom "Ты совсем не урод. Ты невероятно красив.."
        MC "...спасибо, Линда. Я все еще не верю, что это правда."
    scene intro44
    MC "Пфф!"
    if renpy.loadable("patch.rpy"):
        MC "(Какого черта, мама?!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Какого черта, Линда?!)"
    Mom "Mмм!"

    scene intro45
    Mom "(Черт возьми! Не могу поверить, что я это сделала.!)"
    Mom "(Я полностью потерял контроль, Моя похоть взяла верх!)"
    if renpy.loadable("patch.rpy"):
        MC "(Что мама делает?!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Что Линда делает?!)"
    scene intro46
    MC "Для чего это было?!"
    if renpy.loadable("patch.rpy"):
        MC "М-Мама! Ты только что поцеловала меня!?"
    if not renpy.loadable("patch.rpy"):
        MC "Л-Линда! Ты только что поцеловала меня!?"
    if kiss_mom_cheek == True:
        Mom "Ну, ты задолжал мне настоящий поцелуй, за сегоднешнее утро."
        MC "..."
        Mom "…"

        jump after_conditional_mom_kiss_cheek_lips_intro
    if kiss_mom_lips == True:
        Mom "Что? Как это отличается от того, что ты целовал меня сегодня утром?"
        MC "..."
        Mom "…"

        jump after_conditional_mom_kiss_cheek_lips_intro

label after_conditional_mom_kiss_cheek_lips_intro:

    scene intro47
    Mom "Извини. Я немного увлеклась и не могла сдержаться."
    MC "Чт.."
    Mom "Я должна идти. Твой ужин будет в духовке, чтобы не остыл."

    scene intro48
    MC "(Что она имела в виду “не могла сдержаться”?)"
    $ renpy.music.stop(channel="music1", fadeout=2)

    scene black
    $ renpy.pause(2.0)

    scene intro49 with dissolve
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
    MC "Так что да, это было примерно так."
    Judy "Хм ... Когда директор узнал об этом инциденте с миссис Селией?"
    MC "Около четырех часов назад - рано утром."

    scene intro50
    Judy "Мне действительно жаль слышать о том, что с тобой случилось. Звучит ужасно неловко. Я даже не могу себе представить, как он должен чувствовать себя."
    Judy "Поверь мне, - с регулярными сеансами терапии, мы пройдем через все это."
    Judy "Тебе явно - (кхм) - нравиться миссис Селия. Мне интересно-относится ли это притяжение к другим женщинам аналогичного возраста?"
    MC "Ну ... например, кто?"
    if renpy.loadable("patch.rpy"):
        Judy "- О, я не знаю... Как насчет ... твоей матери?"
    if not renpy.loadable("patch.rpy"):
        Judy "- О, я не знаю... Как насчет Линды... ?"
    scene intro51
    if renpy.loadable("patch.rpy"):
        MC "Что?! Ты спрашиваешь меня, нравится ли мне моя мать??"
    if not renpy.loadable("patch.rpy"):
        MC "Что?! Ты спрашиваешь меня, нравится ли мне Линда??"
    Judy "Ты только что сказал мне, что целовал ее, лежа на кровати.."
    MC "Это она меня поцеловала.!"
    if renpy.loadable("patch.rpy"):
        Judy "Так ты оттолкнул свою маму, когда она пыталась поцеловать тебя?"
    if not renpy.loadable("patch.rpy"):
        Judy "Так ты оттолкнул ее, когда она пыталась поцеловать тебя?"
    MC "Н-не совсем - но..."

    scene intro1
    if renpy.loadable("patch.rpy"):
        Judy "Итак, позволь мне задать вопрос еще раз. У тебя есть сексуальные фантазии о своей матери?"
    if not renpy.loadable("patch.rpy"):
        Judy "Итак, позвольте мне задать вопрос еще раз. У тебя есть сексуальные фантазии о Линде?"
    MC "Нет!"
    if renpy.loadable("patch.rpy"):
        Judy "Почему нет? Ты сказала, что тебя привлекает твоя сестра, Сара.."
    if not renpy.loadable("patch.rpy"):
        Judy "Почему нет? Ты сказал, что тебя привлекает Сара."
    if renpy.loadable("patch.rpy"):
        MC "Это не имеет значения-даже если бы она мне понравилась, я бы ничего не сделал! Она моя мать! Это просто... странно. Знаешь?"
    if not renpy.loadable("patch.rpy"):
        MC "Это не имеет значения-даже если бы она мне понравилась, я бы ничего не сделал! Она моя подруга! Это просто... странно. Знаешь?"
    scene intro15
    if renpy.loadable("patch.rpy"):
        Judy "Ты кажешься добродушным мальчиком. Очевидно, ты хочешь лучшего для своей семьи, верно? Ты хочешь, чтобы они были счастливы?"
    if not renpy.loadable("patch.rpy"):
        Judy "You seem like a good-natured boy. Obviously, you want what’s best for your friends, right? You want them to be happy?"
    MC "Конечно!"
    if renpy.loadable("patch.rpy"):
        Judy "Что если это значит, принять мать как романтического партнера? Что, если это то, что требовалось, чтобы действительно сделать маму счастливой?"
    if not renpy.loadable("patch.rpy"):
        Judy "Что если это означало, принять Линду как романтического партнера? Что, если это то, что требовалось, чтобы действительно сделать ее счастливой?"
    MC "Что это за вопросы??!"
    Judy "Я уже говорила тебе, это Фрейдистская Психология. Почитай об этом в школьной библиотеке, если мне не веришь."
    if renpy.loadable("patch.rpy"):
        Judy "Итак, позволь мне перефразировать. Если бы у тебя была возможность трахнуть свою мать, бы бы это сделал? "
    if not renpy.loadable("patch.rpy"):
        Judy "Итак, позволь мне перефразировать. Если бы у тебя была возможность трахнуть Линду, ты бы это сделал? "
    if renpy.loadable("patch.rpy"):
        Judy "Мы уже выяснили, что ты хочешь сделать свою маму счастливой. И это довольно очевидно, ты хочешь перепихнуться. Это не беспроигрышная ситуация?"
    if not renpy.loadable("patch.rpy"):
        Judy "Мы уже установили, что ты хочешь сделать Линду счастливой. И это довольно очевидно, ты хочешь перепихнуться. Это не беспроигрышная ситуация?"
    scene intro16
    MC "Я ... Нет! Я никогда о ней так не думал.!"
    if renpy.loadable("patch.rpy"):
        MC "Она моя мать! Я уже сказал, что ничего не буду с ней делать.!"
    if not renpy.loadable("patch.rpy"):
        MC "Она моя подруга! Я уже сказал, что ничего не буду с ней делать.!"

    scene intro52
    if renpy.loadable("patch.rpy"):
        Judy "Интересно... Я попрошу прийти ко мне еще раз, если между тобой матерью произойдет что-то примечательное. Или даже, возможно, с твоими сестрами."
    if not renpy.loadable("patch.rpy"):
        Judy "Интересно... Я попрошу тебя навестить меня еще раз, если между тобой и Линдой случится что-нибудь примечательное. Или даже, возможно, с твоими друзьями."
    MC "Примечательно?"
    Judy "Я уверена, что ты поймеш, когда это произойдет."
    Judy "Теперь отдохни, [player_name]. Отдых очень важен."
    $ renpy.music.stop(channel="music2", fadeout=2)

    scene black
    $ renpy.pause(5.0)

    scene intro53 with dissolve
    $ renpy.music.play('/sfx/Why_Did_You_Do_It_-_Everet_Almond.mp3', channel="music1", loop=True, fadein = 2)
    MC "(Зевок!)"
    MC "(Это начало совершенно нового дня. Давай сделаем все возможное!)"
    MC "(Мне нужно сосредоточиться на том, чтобы вернуть мою жизнь в нужное русло после этой ... вчерашней неудачи.)"

    scene intro54

    MC "(Давай вернем мою уверенность, найдем горячую девушку и трахнемся!)"
    MC "(Собирание цыплят было бы намного проще, если бы я был в одной из тех сексуальных игр от Patreon.)"
    MC "(Я не могу сдаться !)"
    $ renpy.music.stop(channel="music1", fadeout=2)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
