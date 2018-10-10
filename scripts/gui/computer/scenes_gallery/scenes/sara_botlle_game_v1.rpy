label sara_botlle_game_v1:
    hide screen scenes_gallery
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene sis_nerdy_school_scene3_v1_p1 with dissolve
    $ can_hide_windows = True
    Sara "Я честно не знаю, что делать."
    Lily "Ну ... тебе он нравится?"
    Sara "Конечно, он мне нравится."
    Lily "Да ладно, Сара. Ты знаешь, что я имею в виду - нравится??"
    Sara " ... Да ... Я думаю, что да."

    scene sis_nerdy_school_scene3_v1_p2
    Lily "Лёгок на помине!"
    Sara "Хм?!"
    Lily "Привет, [player_name]. Мы говорили о тебе."

    scene sis_nerdy_school_scene3_v1_p3
    MC "Только хорошие вещи, надеюсь."
    Lily "Хехе! Конечно!"
    MC "Что случилось, Сара? Ты немного нервничаешь."
    Lily "Она в порядке! Ей просто нужно отдохнуть. Как насчет того, чтобы мы собрались вместе и свграли в веселую игру? Немного расслабимся!"

    scene sis_nerdy_school_scene3_v1_p4
    MC "Конечно-звучит хорошо."
    Sara "Э... Я так полагаю…"
    Sara "(Бог... Я надеюсь, что он не слышал, как я говорю эти вещи Лили…)"
    Lily "Твои родители сейчас дома, Сара?"
    Sara "Я так не думаю."
    Lily "Прекрасно! Мы можем использовать твою спальню!"
    Sara "Моя спальня? Что это за игра??"

    menu:
        "Поехали! Это звучит весело!":

            MC "Это звучит интересно. Давайте!"
            Lily "Это дух!"
            jump after_sis_nerdy_school_scene3_v1_choice1r
        "Это твоя спальня, Сара. Ты не против?":


            MC "Это твоя спальня, Сара. Ты не против?"
            Sara "Умм ... Может быть? я думаю…"
            Lily "Да, да. Поехали!"
            jump after_sis_nerdy_school_scene3_v1_choice1r

label after_sis_nerdy_school_scene3_v1_choice1r:

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Doobly Doo.mp3', channel="music2", loop=True, fadein = 2)

    scene sis_nerdy_school_scene3_v1_p5 with fadehold
    MC "Хорошо? Что теперь?"
    Lily "Нада найти бутылку."
    MC "Бутылку?"
    Lily "Да - стеклянную. Они вращаются лучше."
    MC "О! Мы будем играть в бутылочку."

    scene sis_nerdy_school_scene3_v1_p6
    MC "Я вернусь через несколько минут."
    Lily "Классно! Скоро увидимся!"
    Sara "(Шепчет) Ты не можешь быть серьёзной, Лили.!Он не будет меня целовать, если бутылка укажет на меня?!"
    Lily "Давай подождем и посмотрим…"

    scene sis_nerdy_school_scene3_v1_p7
    Lily "Оуу... Не смотри так мрачно, Сара! В чем дело?"
    Sara "Что, если он не схочет меня целовать?"
    Lily "Ну, это не имеет значения…"

    scene sis_nerdy_school_scene3_v1_p8
    Lily "...потому что он собирается целовать эти сочные губы сначала!"
    Lily "Я думаю, он действительно захочет разобраться со мной. Я обязательно поцелую его РЕАЛЬНО хорошо и за тебя."

    scene sis_nerdy_school_scene3_v1_p9
    if renpy.loadable("patch.rpy"):
        Sara "Эй! Ты говоришь о моем брате!"
    if not renpy.loadable("patch.rpy"):
        Sara "Эй! Ты говоришь о моем друге!"
    Lily "Легко, Сара. Расслабься!"
    Sara "Не говори мне, расслабся!"

    scene sis_nerdy_school_scene3_v1_p10
    Sara "Не смей думать, что можешь просто поцело..."
    MC "Эй, я нашел бут.."
    MC "*гм* Все в порядке? Вы боретесь?"

    scene sis_nerdy_school_scene3_v1_p11
    Lily "Борьба? Ха-ха! Нет, мы просто сражаемся!"
    Sara "Да…"
    MC "Прекрасно! Тогда давайте начнем. Как вы хотите сделать это?"

    scene sis_nerdy_school_scene3_v1_p12
    Lily "Ладно, ты первый, [player_name]. Тот, на кого указывает бутылка, - целуеться."
    MC "Подождите - даже Сара?"
    Lily "Ага! Сара тоже!"
    MC "(Вау ... Сара выглядит такой нервной…)"

    scene sis_nerdy_school_scene3_v1_p13
    Lily "Давайте раскрутим бутылку!"

    scene bottle_spin1
    $ renpy.pause (2.26, hard=True)

    Lily "Вау! Это я!"

    scene sis_nerdy_school_scene3_v1_p14
    Lily "Иди сюда, большой мальчик, и дай мне поцелуй!"
    MC "Э... хорошо…"
    MC "(Она, кажется, действительно разбираеться! Я никогда не думал, что могу так нравиться девушкам!)"
    if renpy.loadable("patch.rpy"):
        Sara "(Нееет! Боже ... видя, что она склоняется к моему брату, заставляет меня чувствовать себя больной.)"
    if not renpy.loadable("patch.rpy"):
        Sara "(Нееет! Боже ... видя, что она склоняется к моему другу, заставляет меня чувствовать себя больной.)"

    scene sis_nerdy_school_scene3_v1_p15
    Sara "(Я знаю, что она мой другом ... но я чувствую себя так ... грустно и сердито, что она флиртует с ним.)"
    if renpy.loadable("patch.rpy"):
        Sara "(И он мой брат - я не должна даже испытывать к нему чувства!)"
    if not renpy.loadable("patch.rpy"):
        Sara "(И он мой друг - я не должна даже испытывать к нему чувства!)"

    scene sis_nerdy_school_scene3_v1_p16
    Lily "Mмм…"
    MC "(Ой! Она хорошо целуется!)"
    Sara "(Успокойся, Сара... это всего лишь один поцелуй. Скоро твоя очередь.)"

    scene sis_nerdy_school_scene3_v1_p17
    Lily "(Хе-хе ... Я чувствую, как Сара смотрит на меня. Почему мужчины всегда, гораздо более привлекательны, когда с другими женщинами?)"
    MC "(Ее губы настолько мягкие! Я могу целовать ее часами!)"

    scene sis_nerdy_school_scene3_v1_p18

    Lily "Ммм, это было весело. благодарю, [player_name]."
    Lily "Надеюсь, это будет не последний раз, когда наши губы коснутся сегодня."
    Sara "(Эта сука…)"
    MC "Да, я тоже так надеюсь!"

    scene sis_nerdy_school_scene3_v1_p19
    Lily "Твоя очередь, Сара! На кого попадет?"
    Sara "…"
    Lily "Да ладно! Меня сжигает интерес!"
    Sara "Я не буду."
    Lily "А? Твоя потеря!"

    scene sis_nerdy_school_scene3_v1_p20
    Lily "Думаю, снова твоя очередь, [player_name]! Крути?"
    MC "Могу ли я выбрать себя?"
    Lily "Хехе! Конечно!"

    scene bottle_spin1
    $ renpy.pause (2.26, hard=True)


    scene sis_nerdy_school_scene3_v1_p21
    Lily "Ура! Меня еще раз!"
    Lily "Надеюсь, ты готов ко второму раунду!"

    scene sis_nerdy_school_scene3_v1_p22
    MC "(Черт! Я никогда не думал, что это будет такой замечательный день!)"
    MC "(Я должен чаще болтаться с Лили!)"

    scene sis_nerdy_school_scene3_v1_p23
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music1", loop=True, fadein = 2)
    if renpy.loadable("patch.rpy"):
        Sara "(Чертова сука! Это мой брат!)"
    if not renpy.loadable("patch.rpy"):
        Sara "(Чертова сука! Это мой друг!)"
    Sara "(Как ей кажется, она может просто прийти в мою спальню и сделать с ним что угодно!)"

    scene sis_nerdy_school_scene3_v1_p24
    Sara "(Я покажу ей. Я покажу этой распутной маленькой шлюхе!)"
    if renpy.loadable("patch.rpy"):
        Sara "Отвали от моего брата!"
    if not renpy.loadable("patch.rpy"):
        Sara "Отвали от моего друга!"

    scene sis_nerdy_school_scene3_v1_p25
    $ renpy.pause(0.7)

    scene sis_nerdy_school_scene3_v1_p26 with flash2

    $ renpy.sound.play('/sfx/glass-smash.mp3', loop=False)
    $ renpy.pause(1, hard = True)
    scene sis_nerdy_school_scene3_v1_p27
    MC "Что?!"
    Sara "Гмм!"
    Sara "Лили! Убирайся из моего дома!"
    Lily "Боже! Хорошо, я пойду! Увидимся, [player_name]."

    scene sis_nerdy_school_scene3_v1_p28
    Sara "Я не хочу играть в эту... глупую игру больше."
    MC "Сара, я..."
    Sara "Оставь меня в покое!"
    MC "Но..."
    Sara "Я сказала, что хочу побыть одна!"

    scene sis_nerdy_school_scene3_v1_p29
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/OctoBlues.mp3', channel="music2", loop=True, fadein = 2)

    MC "Эй, Сара... Всё в порядке. Что не так?"
    Sara "(сопит)"
    MC "Ты плачешь?"

    scene sis_nerdy_school_scene3_v1_p30
    Sara "Я (сопит) Я-я.. извини, [player_name]. Когда я увидела, как ты целовал ее, я…"
    MC "Эй, все в порядке. Тише-все в порядке."

    menu:
        "Поцеловать ее.":

            scene sis_nerdy_school_scene3_v1_p31b
            MC "Mwah."
            Sara "(О, вау ... Он на самом деле целует меня... )"
            Sara "(Это одн из моих желаний…)"
            jump after_sis_nerdy_school_scene3_v1_choice21r
        "Обнять ее.":


            scene sis_nerdy_school_scene3_v1_p31a
            MC "Все в порядке, Сара. я думаю, что понял."
            Sara "(сопит)"
            MC "У меня есть ты. Мы больше не будем играть в эту игру."
            jump after_sis_nerdy_school_scene3_v1_choice21r

label after_sis_nerdy_school_scene3_v1_choice21r:

    scene sis_nerdy_school_scene3_v1_p32
    Sara "(сопит) Спасибо, [player_name]. Ты думаешь, что можешь дать мне ... настоящий поцелуй?"
    MC "Настоящий поцелуй?"
    if renpy.loadable("patch.rpy"):
        Sara "Как и мама и папа, когда они смотрят романтический фильм."
    if not renpy.loadable("patch.rpy"):
        Sara "Подобно Линде и Бобу, когда они смотрят романтический фильм."
    MC "Конечно, Сара. Подойти ближе."

    scene sis_nerdy_school_scene3_v1_p33r
    Sara "(О мой Бог! Он сделал это! ... Это рай!)"
    if renpy.loadable("patch.rpy"):
        MC "(Она гораздо лучше целуется, чем Лили! Чувствуется, что в поцелуе сары много страсти.)"
        MC "(Почему я соглашаюсь с этим, так просто? Она моя сестра! Я не должен так ее целовать. Правильно?)"
    if not renpy.loadable("patch.rpy"):
        MC "(Она гораздо лучше целуется, чем Лили! Чувствуется, что в поцелуе сары много страсти.)"
        MC "(Почему я соглашаюсь с этим, так просто? Она моя подруга! Я не должен так ее целовать. Правильно?)"
    scene sis_nerdy_school_scene3_v1_p34
    Sara "Огромное спасибо, [player_name]."
    MC "Что случилось? Ты как-то испугалась."
    Sara "Я ... я не знаю… Когда я увидел, что Лили целует тебя, я просто так ... разозлилась."
    MC "Все нормально. я думаю, что понял."

    scene sis_nerdy_school_scene3_v1_p35
    Sara "Я ... я хочу сделать ... что-то для тебя."
    MC "Что ты имеешь в виду?"
    Sara "Я видела видео... женщины, использующей рот, чтобы сосать парню...."
    MC "What?! Ты говоришь о минете?"

    scene sis_nerdy_school_scene3_v1_p36
    Sara "Пожалуйста, [player_name] - просто останься и позволь мне сделать это. Я хочу, чтобы ты чувствовали себя хорошо."
    if renpy.loadable("patch.rpy"):
        MC "Сара, я ... ты моя младшая сестра."
    if not renpy.loadable("patch.rpy"):
        MC "Сара, я ... ты мой маленький друг."
    Sara "Тсс! Просто позволь мне стянуть брюки."

    scene sis_nerdy_school_scene3_v1_p37
    MC "Сара, подожди. Ты в этом уверена?"
    Sara "Я ... Хм ... да."
    MC "Я не хочу, чтобы ты делала то, о чем позже пожалеешь."

    scene sis_nerdy_school_scene3_v1_p37a
    Sara "Если я это сделаю с тобой, я никогда не пожалею."
    MC "Ты уверены? Ты делала что-нибудь как это прежде?"
    Sara "Нет... это мой первый раз."
    MC "Позвольте мне сесть на кровать, чтобы тебе было легче."
    Sara "Есть ли что-нибудь еще, что я должна делать??"
    MC "Не могла бы ты снять верх, прежде чем начать?"
    Sara "(ААА... Это так неловко... Я чувствую, что я должна сделать это для него, хотя…)"
    Sara "O-Окей…"

    scene sis_nerdy_school_scene3_v1_p38
    MC "Вау ... Ты выглядишь так жарко, Сара."
    Sara "С-спасибо…"
    Sara "Что мне теперь делать?"
    MC "Сними с меня нижнее белье."

    scene sis_nerdy_school_scene3_v1_p39
    $ renpy.pause(1.2)
    scene sis_nerdy_school_scene3_v1_p39anim
    $ renpy.pause(3)
    scene sis_nerdy_school_scene3_v1_p40r
    Sara "Вау!"
    Sara "(Это больше, чем я помню! Как я могу поместить все это во рту?)"
    Sara "Hehe! Он такой упругий…"
    MC "(Она определенно не играла с членом прежде. Я предполагаю, что просто позволю ей позабавиться, в то время как она экспериментирует.)"
    Sara "Ты чувствуешь, когда я это делаю?"
    MC "Да, но лучше, если ты возьмешь руками и начнешь двигать вверх и вниз."

    scene sis_nerdy_school_scene3_v1_p41r
    Sara "Типа так, [player_name]?"
    MC "ААА... Это хорошо, Сара."
    Sara "Хе-хе ... Ты улыбаешься!"
    MC "Это потому, мне действительно хорошо."

    scene sis_nerdy_school_scene3_v1_p41rr
    MC "Mмм!"
    Sara "(Он становится все тверже, чем больше я двигаюсь!)"
    if renpy.loadable("patch.rpy"):
        Sara "(Я только мечтала прикоснуться к члену [player_name]! Сейчас это происходит!)"
    if not renpy.loadable("patch.rpy"):
        Sara "(Я только мечтала прикоснуться к члену [player_name]! Сейчас это происходит!)"
    MC "Хорошо - начинай лизать. Просто используйте свой язык, вращай ним вокруг кончика моего члена."

    scene sis_nerdy_school_scene3_v1_p42r
    Sara "(На вкус немного соленый! Это совсем не то, чего я ожидала!)"
    MC "Ох ... Это хорошо. Продолжай, Сара."

    scene sis_nerdy_school_scene3_v1_p43
    Sara "Я делаю правильно, [player_name]?"
    MC "Да, это так хорошо."
    Sara "Что я должен делать дальше?"

    scene sis_nerdy_school_scene3_v1_p44
    MC "Попробуй взять мой член во рот."
    Sara "Весь?"
    Sara "(Это так много… Я не думаю, что смогу вставить, даже половину в рот!)"

    scene sis_nerdy_school_scene3_v1_p45
    MC "Успокойся. Не весь. Просто заходите как можно больше, не делая себя неудобно."
    Sara "Но я хочу, чтобы ты тоже хорошо себя чувствовал…"
    MC "Мне будет хорошо - ты не должна навредить себе."
    Sara "O-Окей!"

    scene sis_nerdy_school_scene3_v1_p46r
    "(Шлурп)"
    "(Сосет сосет)"
    MC "(Ммм... Это приятно. Она так нежна!)"

    scene sis_nerdy_school_scene3_v1_p47
    "(Shllurrrrrrrpp)"
    Sara "(Я не думаю, что я могу сделать гораздо глубже, чем только что!)"
    MC "Нормально, Сара. Тебе не нужно винить себя-это твой первый раз."
    MC "Это потрясающе."

    scene sis_nerdy_school_scene3_v1_p48
    MC "(Я не могу поверить, что Сара привлекала меня сексуально. Как долго она это чувствовала?)"
    if renpy.loadable("patch.rpy"):
        MC "(Был ли я действительно так одержим моим учителем, что я даже не заметил привязанности моей сестры к себе?)"
    if not renpy.loadable("patch.rpy"):
        MC "(Был ли я действительно так одержим моим учителем, что я даже не заметил привязанности моей подруги к себе?)"
    "(Сосет сосет)"

    scene sis_nerdy_school_scene3_v1_p49r
    "(Шлурп сосет)"
    MC "О! ААА!"
    MC "(Я собираюсь кончить, если она дойдет до этого! Для первого раза у нее отлично получаеться!)"

    scene sis_nerdy_school_scene3_v1_p50
    MC "(Я собираюсь кончить. Я должен сказать ей!)"
    MC "Сара, я собираюсь кончить-это означает, что сперма собирается выйти из моего члена."
    Sara "Mмм хмм!"

    scene sis_nerdy_school_scene3_v1_p51
    MC "Aхх! Ебать! Я кончаю!"
    Sara "(Ой! Я чувствую, как он дрожит! Ему нравиться мой минет!)"
    MC "Ммммм!"
    Sara "(Я должна держать член во рту, пока он кончает!)"

    scene sis_nerdy_school_scene3_v1_p52
    MC "Aхх! Да! Ммм!"
    Sara "(Я чувствую, что оно наполняет мой рот! Это действительно теплое и соленое!)"
    MC "Блядь! Ах! Ты так хороша, Сара!"
    scene sis_nerdy_school_scene3_v1_p52 with fadehold
    $ renpy.pause(0.1)
    scene sis_nerdy_school_scene3_v1_p52 with fadehold
    $ renpy.pause(0.1)
    scene sis_nerdy_school_scene3_v1_p52
    MC "Ах! Ты можешь остановиться - я закончил!"

    scene sis_nerdy_school_scene3_v1_p53
    Sara "Wha duh I duh wuh thus?"
    MC "(Я думаю, она спрашивает, что сделать с моей спермой сейчас.)"

    menu:
        "Я хочу, чтобы ты проглотила ее.":

            MC "Я хочу видеть как ты ее проглотишь."

            scene sis_nerdy_school_scene3_v1_p54
            Sara "(Глоток)"
            Sara "(Да? Это не так уж плохо. Лили рассказывала мне, что она ненавидела вкус спермы, когда делала минет!)"
            scene sis_nerdy_school_scene3_v1_p55
            Sara "Aхх! Все ушла!"
            MC "Спасибо, Сара. Ты очаровательна."
            Sara "Хе-хе ... Я знаю!"
            jump after_sis_nerdy_school_scene3_v1_choice31r
        "Не нужно глотать, если не хочешь.":

            scene sis_nerdy_school_scene3_v1_p53
            MC "Некоторые девушки проглатывают, но тебе не нужно, если не хочешь"
            scene sis_nerdy_school_scene3_v1_p54
            Sara "(Глоток!) Aхх!"
            Sara "(Надеюсь, он мне больше понравится, если я проглочу всю его сперму!)"
            scene sis_nerdy_school_scene3_v1_p55
            Sara "Все ушло!"
            MC "Тебе не нужно было это делать в первый раз!"
            Sara "Я хотела. Я хотела сделать лучше для тебя!"
            jump after_sis_nerdy_school_scene3_v1_choice31r

label after_sis_nerdy_school_scene3_v1_choice31r:
    scene sis_nerdy_school_scene3_v1_p56
    Sara "я действительно тебя люблю, [player_name]."
    Sara "(Я чувствую себя так хорошо возле него.)"
    MC "(Вау ... Она очень любит меня!)"
    scene sis_nerdy_school_scene3_v1_p57
    Sara "Я хочу полежать здесь с тобой…"
    MC "Тебе удобно?"
    Sara "Да."
    MC "Просто расслабься. Большое тебе спасибо за все, Сара."
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
