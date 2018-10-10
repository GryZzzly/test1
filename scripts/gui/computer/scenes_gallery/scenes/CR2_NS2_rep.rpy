


label CR2_NS2_rep:
    $ renpy.music.stop(channel="music2", fadeout=1)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR2_NS2_p1 with dissolve
    $ can_hide_windows = True
    MC "Привет, Кэролайн."
    if renpy.loadable("patch.rpy"):
        Caroline "Тише... Не говори громко. Мы можем быть снаружи, но остальные члены семьи спят."
    else:
        Caroline "Тише... Попытайся не кричать. Мы можем быть снаружи, но Линда и Боб и Сара спят."
    MC "Нет проблем. Я попытаюсь быть тихим."

    scene black
    $ renpy.pause(3,hard = True)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)
    scene CR2_NS2_p2

    MC "Что это было, Ты хотела поговорить, Кэролайн?"
    Caroline "Я хотела провести серьезную беседу."
    Caroline "Приходи ко мне на скамейку."

    scene CR2_NS2_p3

    MC "(Серьезный разговор? Я надеюсь, что все в порядке.)"
    MC "(Интересно, связано ли это с ограблением ее магазина? - После этого события она выглядела очень напряженной.)"
    MC "(Есть ли что-нибудь еще, о чем она хотела бы поговорить серьезно?)"

    scene CR2_NS2_p4

    Caroline "Не стоит так волноваться. Ничего плохого не произошло."
    MC "О, слава Богу."
    MC "Ты меня испугала!"


    scene CR2_NS2_p5

    Caroline "Ха-ха! Прости, [player_name]. Это серьезная тема, но ты не волнуйся."
    Caroline "Садись рядом."

    scene CR2_NS2_p6

    Caroline "…"
    MC "(Сейчас она очень спокойна. Может быть, я должен начать разговор?)"
    MC "Итак, о чем ты хотела поговорить?"

    scene CR2_NS2_p7

    Caroline "…"
    MC "Кэролайн?"
    MC "(Дерьмо, я чувствую боль в животе.)"
    MC "(Она хочет закончить сделку, которую мы заключили!)"
    MC "Кэролайн? Это о сделке, которую мы заключили?"
    Caroline "Да…"
    MC "(Я так и не понял! Все кончено…)"

    scene CR2_NS2_p8

    MC "(Глоток) Ты хочешь покончить с этим, не так ли?"
    Caroline "Что?! Нет! Нет.. "

    scene CR2_NS2_p9

    Caroline "Конечно, если ты не хочешь."
    MC "Я не хочу!"
    MC "(О, слава Богу!)"
    MC "Фу... Я зря волновался."
    Caroline "Ха-ха! Попытатайся расслабиться. Я здесь не для того, чтобы что-то закончить."

    scene CR2_NS2_p10

    Caroline "Я действительно хотела поговорить с тобой, о том, что ты сделал для меня в последнее время."
    MC "Ты не должна благодарить меня за это."
    Caroline "Нет. Должна. Я не была бы там, где я сейчас, если бы ты не одолжил мне денег."

    scene CR2_NS2_p11

    Caroline "Или помог мне снять эти фотографии."
    Caroline "Или поддержал меня, когда мой магазин был ограблен."
    MC "Ничего. Честно."

    scene CR2_NS2_p12

    Caroline "Не продолжай, я не идиотка!"
    Caroline "Ты единственный человек в моей жизни, который на самом деле поддерживал меня!"
    if renpy.loadable("patch.rpy"):
        Caroline "Не мама. Не папа. Даже мои друзья. Вся помощь, была от тебя, [player_name]. Ты понимаешь?"
    else:
        Caroline "Не Линда. Не Боб. Даже мои друзья. Вся помощь, была от тебя, [player_name]. Ты понимаешь?"
    MC "Я ... я так думаю."

    scene CR2_NS2_p13
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)
    Caroline "(Поцелуй!)"
    MC "Mмм!"
    MC "(Вау! Это произошло из ниоткуда!)"

    scene CR2_NS2_p14

    Caroline "(Это неправильно... Это должна быть романтическая атмосфера ночного воздуха и полнолуния.)"
    if renpy.loadable("patch.rpy"):
        Caroline "(Я не должна чувствовать что-то [player_name]. Он мой брат, Боже!)"
    else:
        Caroline "(Я не могу на самом деле чувствовать что-нибудь к [player_name]. Он мой самый близкий друг, ради Бога!)"
    MC "Mмм..."

    scene CR2_NS2_p15

    Caroline "Не поймите меня неправильно, [player_name].. Это только вознаграждение за помощь ... Больше ничего."
    MC "Кэролайн, я…"
    Caroline "Тише... Просто ... позвольте мне спросить одну вещь."
    MC "Что угодно..."

    scene CR2_NS2_p16

    Caroline "Эти деньги, которые ты мне давал, все время, что ты тратил мне на помощь, то, как ты всегда там, когда ты мне нужен..."
    Caroline "Ты делал эти вещи, для сексуальных удовлетворений как часть нашей сделки?"
    Caroline "Или ты чувствуешь что-то еще?"

    scene CR2_NS2_p17
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    window hide
    menu:
        "Я ... думаю, я влюбляюсь в тебя, Кэролайн.":
            scene CR2_NS2_p8

            MC "Я ... я думаю, что влюбляюсь в тебя, Кэролайн."
            Caroline "Действительно?"
            MC "Да."

            scene CR2_NS2_p9

            Caroline "Спасибо что сказал мне."
            Caroline "Я... "
            if renpy.loadable("patch.rpy"):
                Caroline "Я не чувствую то же самое. Я имею в виду, я люблю тебя, но как брата."
            else:
                Caroline "Я не чувствую то же самое. Я имею в виду, я люблю тебя, но как друга."
            MC "Ой…"

            scene CR2_NS2_p8

            Caroline "Пожалуйста, не грусти!"
            MC "Все нормально. Я все еще трачу, почти каждый день с тобой. Договор нас достаточно хороший."
            Caroline "Ты уверен?"
            MC "Если что-то изменится, мы можем поговорить об этом в будущем, ладно?"
            Caroline "Хорошо."
            jump CR2_NS2_continue1_rep

        "Я делаю так, потому что ты моя сестра. Все остальное - бонус." if renpy.loadable("patch.rpy"):
            jump CR2_NS2_q1_rep

        "Я делаю это, потому что ты мой друг. Все остальное - бонус." if not renpy.loadable("patch.rpy"):
            jump CR2_NS2_q1_rep
        "Я не буду врать тебе - Я делаю все как договорились.":
            scene CR2_NS2_p8

            MC "Я не буду врать тебе - Я делаю все как договорились."
            MC "Я помогаю тебе, и в замен ты помогаешь мне."
            Caroline "Хаха! Ой! Я знала, что парни интересуются только сексом, но ты первый, кто на самом деле был честен со мной."

            scene CR2_NS2_p17

            MC "Прости."
            Caroline "Нет, не извиняйся. Я точно знаю, что я сделаю с тобой. Это хорошая вещь."
            MC "Ты уверена?"
            Caroline "Абсолютно, [player_name]."
            jump CR2_NS2_continue1_rep

label CR2_NS2_q1_rep:
    scene CR2_NS2_p17

    if renpy.loadable("patch.rpy"):
        MC "Я делаю это, потому что ты моя сестра. Все остальное - бонус."
    else:
        MC "Я делаю это, потому что ты мой самый близкий друг. Все остальное - бонус."
    MC "Исключительно договор."
    Caroline "В самом деле?"
    MC "Да."
    if renpy.loadable("patch.rpy"):
        Caroline "Мне стало легче. Честно говоря, я люблю тебя только как брата, и если бы все стало романтично, я бы чувствовала себя немного странно."
    else:
        Caroline "Мне стало легче. Честно говоря, я люблю тебя только как друга, и если бы все стало романтично, я бы чувствовала себя немного странно."
    MC "Ну, не беспокойся об эом."
    jump CR2_NS2_continue1_rep

label CR2_NS2_continue1_rep:
    scene CR2_NS2_p18

    Caroline "Давай. Следуй за мной."
    MC "Куда мы идём?"
    Caroline "Назад в мою спальню. Развлечемся."

    scene CR2_NS2_p19
    if renpy.loadable("patch.rpy"):
        MC "Но ты сказала, что мама и папа спят!"
    else:
        MC "Но ты сказала, что Линда и Боб спят!"
    Caroline "Все ... ты трус?"
    MC "Эй! Я не трус!"
    Caroline "Тогда, давай со мной в комнату."

    scene black

    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.pause(3,hard=True)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music2", loop=True, fadein = 2)
    scene CR2_NS2_p20
    $ renpy.sound.play("sfx/door_squeak.mp3")

    "*Скрип*"

    "*Стук*"

    MC "Черт, Кэролайн? Тебе действительно нужно смазать эту дверь!"

    scene CR2_NS2_p21

    Caroline "Мне никогда не приходилось это делать, так как я не пробиралась к  мальчикам в спальню."
    MC "В самом деле?"
    Caroline "Почему ты так удивляешься?"

    scene CR2_NS2_p22

    MC "Я думал, ты приводила мальчиков раньше."
    if renpy.loadable("patch.rpy"):
        Caroline "С таким любопытным братом, как ты, и еще с такой же сестрой, как Сара? Это не стоит риска!"
    else:
        Caroline "С любопытным человеком, как ты, и еще более безлюдным человеком, как Сара? Это не стоило риска!"
    MC "Ха-ха! Я думаю, ты права."
    Caroline "Я ходила к ним чтобы трахаться."

    scene CR2_NS2_p23

    MC "Итак, что именно мы сейчас сделаем?"
    Caroline "Не надейся - мы не будем заниматься сексом."
    Caroline "Я не совсем решила, как далеко я готова пойти - но мы оба узнаем достаточно скоро."

    scene CR2_NS2_p24

    MC "(Ее тело выглядит так сексуально! Интересно, что я смогу делать с ней.)"
    Caroline "Знаешь, это, наверное, хорошо, что у меня нет парня."
    Caroline "Это сделало бы наши отношения немножко неудобными."

    scene CR2_NS2_p25

    Caroline "И я не думаю, что найду парня, который будет относиться ко мне так же хорошо, как ты."
    Caroline "Ты помог развить мне бизнес, а затем, когда меня ограбили - ты его спас."
    MC "Кэролайн, тебе не нужно благодарить меня."

    scene CR2_NS2_p26

    Caroline "Я знаю. Я знаю. Это моя первая независимость. Я хочу так и продолжить."
    MC "Да, я понимаю."
    Caroline "Хорошо, я думаю, что готова."

    scene CR2_NS2_p27

    Caroline "Как насчет потереть свой член между моих бедер, об мои трусики?"
    MC "Звучит неплохо!"
    Caroline "Круто. Итак, ты хочешь сделать это, сзади или спереди?"

    window hide
    menu:
        "Давай сделаем это лицом назад.":
            scene CR2_NS2_p27

            MC "Давай сделаем это лицом назад."
            Caroline "Ммм... Звучит хорошо. Раздевайся и ложись на спину."

            scene CR2_NS2_back_p1

            Caroline "Что ж? Как ты? Тебе удобно?"
            MC "Да, это хорошо."
            Caroline "Прекрасно! Я начинаю двигать бедрами."
            scene CR2_NS2_back_p8anim
            MC "Ахх..."

            scene CR2_NS2_back_p2

            MC "Ммм... Твои холмики такие теплые!"
            Caroline "Тебе хорошо?"
            MC "Ах ... так хорошо."

            scene CR2_NS2_back_p3

            MC "Ооохх…"
            Caroline "(Я чувствую его твердый член, он трется вверх и вниз по киске, через мои трусики!)"
            Caroline "(Это лучше, чем я думала!)"

            scene CR2_NS2_back_p4

            MC "Ах! Да! Это потрясающе, Кэролайн!"
            scene CR2_NS2_back_p4anim
            Caroline "Охх ... Ммм…"
            Caroline "(Я должна сдерживать свой стон. Я не должна показывать что мне очень нравится…)"

            scene CR2_NS2_back_p5

            MC "(Я попытаюсь подвинуть бедра!)"
            Caroline "Ммм! охх…"
            Caroline "(Его член трогает мой клитор!)"

            scene CR2_NS2_back_p6

            Caroline "(И теперь его руки держат мою задницу!)"
            Caroline "(Если он продолжит, я, вероятно, кончу!)"
            MC "(Ее задница настолько мягкая! Я мог бы держать ее весь день!)"

            scene CR2_NS2_back_p7

            Caroline "Тебе нравится, [player_name]?"
            scene CR2_NS2_back_p9anim
            MC "MМM! Охх…"


            scene CR2_NS2_back_p8

            MC "Я в порядке, Кэролайн. Твоя задница выглядит потрясающе!"
            scene CR2_NS2_back_p8aanim
            MC "Я бы хотел трахнуть тебя, когда-нибудь."
            Caroline "Оох ... М-Может быть."

            scene CR2_NS2_back_p9

            Caroline "(Я не могу поверить, что он так просто сказал это!)"
            Caroline "(Я сделаю вид что ничего не слышала.)"

            Caroline "Mmm..."

            scene CR2_NS2_back_p10

            MC "Aхх…"
            MC "Ooхх…"
            Caroline "Aхх…"

            scene CR2_NS2_back_p11

            Caroline "(Я должна быть осторожной,  я не могу позволить себе возбуждаться постоянно от [player_name].)"
            Caroline "(Если он сделает это, я, возможно, не смогу сопротивляться, и в конечном итоге позволяю ему трахнуть меня когда-нибудь!)"
            jump CR2_NS2_continue2_rep
        "Давай сделаем это лицом вперед.":

            scene CR2_NS2_p27

            MC "Давай сделаем это передом."
            Caroline "Ладно, снимай одежду и ложись на кровать."
            scene CR2_NS2_front_p1
            Caroline "Mмм…"

            MC "Вау…"
            Caroline "Наслаждаясь видом?"
            MC "Это невероятно..."

            scene CR2_NS2_front_p2

            Caroline "Как насчет того, если я сожму бедра?"
            MC "Mмм!"
            Caroline "Так нормально?"

            scene CR2_NS2_front_p3

            MC "Очень хорошо!"
            scene CR2_NS2_front_p3anim
            Caroline "(Мне нравится ощущение его члена, трущего мои трусики.)"
            Caroline "(Он трется прям об мой клитор!)"


            scene CR2_NS2_front_p4

            MC "Ooхх…"
            Caroline "Aхх… Aх…"
            MC "Ты тоже наслаждаешся этим, Кэролайн?"

            scene CR2_NS2_front_p5

            Caroline "Я - … ах … просто дышу…"
            MC "Конечно-если это то, что называеться дыханием, Кэролайн."

            scene CR2_NS2_front_p6

            Caroline "(О, Боже, его член чувствует себя так хорошо! Это делает меня такой возбужденной!)"
            Caroline "(Это опасно… Или я действительно возбужусь и позволю ему войти внутрь меня…)"
            Caroline "(Черт, это было бы так неправильно…)"

            scene CR2_NS2_front_p7

            Caroline "Уххх…"
            Caroline "(Это так неправильно, но он чувствует себя так хорошо!)"
            MC "(Она становится все быстрее с каждой минутой!)"

            scene CR2_NS2_front_p8

            MC "Я собираюсь кончить, Кэролайн!"
            MC "Твои бедра чертовски невероятны!"
            scene CR2_NS2_front_p7anim
            Caroline "Aх! Aх! Aхх..."

            scene CR2_NS2_front_p9

            Caroline "(Он собирается кончить на киску!)"
            Caroline "(Черт побери, … мое сердце сейчас выскочит!)"
            Caroline "Aхх… Оххх…"

            scene CR2_NS2_front_p10

            MC "(Я получу намного лучший оргазм, если я возьму под свой контроль ситуацию.)"
            MC "(Надеюсь, Кэролайн не против, если я возьму инициативу на себя, чтобы изменить ситуацию!)"
            Caroline "Mмм! Oхх!"

            scene CR2_NS2_front_p11

            MC "Aхх…"
            MC "(Ну, так ничего не выйдет!)"
            jump CR2_NS2_continue2_rep

label CR2_NS2_continue2_rep:
    scene black with dissolve
    $ renpy.pause(0.7,hard= True)
    scene CR2_NS2_p28 with dissolve

    Caroline "Эй!"
    MC "Ты должна молчать, Кэролайн. Помнишь?"
    if renpy.loadable("patch.rpy"):
        MC "Не хочу разбудить маму и папу!"
    else:
        MC "Не хочу, чтобы проснулись Линда и Боб!"

    scene CR2_NS2_p29

    Caroline "Mмм…. Oхх…"
    MC "(Это гораздо лучше!)"
    MC "(И по лице Кэролайн видно, ей нравиться!)"

    scene CR2_NS2_p30

    Caroline "Aх! Aх! Aх!"
    scene CR2_NS2_p30anim
    Caroline "(Боже! Он собирается залить меня спермой!)"
    MC "Черт, это хорошо!"

    scene CR2_NS2_p31
    Caroline "Oooххх!"
    Caroline "(Я чувствую, как моя киска горит! Я скоро кончу!)"
    MC "Я не собираюсь долго ждать!"

    scene CR2_NS2_p32

    Caroline "Давай быстрее! Ах! "
    MC "Ты уверена?"
    scene CR2_NS2_p32anim
    Caroline "О, Господи! Да! Да!"

    scene CR2_NS2_p33

    Caroline "Mмм! Ебать... Это так хорошо…"
    Caroline "Aхх!"
    MC "Оохх! Я собираюсь кончить!"

    scene CR2_NS2_p34

    Caroline "Подожди! Боже мой!"
    Caroline "Осторожный! Только не на.."
    MC "AAХХХХ"
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene CR2_NS2_p34 with dissolve
    $ renpy.pause(0.7, hard = True)
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)
    scene CR2_NS2_p35 with dissolve

    Caroline "...лицо."
    MC "Вот дерьмо! Я сожалею, Кэролайн."
    Caroline "Не беспокойся об этом..."

    scene CR2_NS2_p36

    Caroline "Возвращайся в свою комнату. Мне нужно убрать здесь."
    MC "Ты уверена?"
    Caroline "Да. Увидимся завтра."

    scene CR2_NS2_p37

    Caroline "(Черт ... запах его спермы, меня ОЧЕНЬ возбуждает!)"
    Caroline "(Это помогло ему, но не мне.)"
    Caroline "(Время, взять свою специальную игрушку…)"

    scene CR2_NS2_p38

    Caroline "Хмм… Где я ее оставила?"
    Caroline "Я могла бы поклясться, что она у меня под подушкой…"
    Caroline "Если…"

    scene CR2_NS2_p39
    if renpy.loadable("patch.rpy"):
        Caroline "(Я должна была спрятать ее под кроватью, если бы мама решила убрать мою комнату.)"
    else:
        Caroline "(Я должна была спрятать ее под кроватью, если бы Линда решила убрать мою комнату.)"
    Caroline "(Было бы неловко, если бы она нашла ее.)"
    Caroline "(Ну, давай... Куда ты делась?)"

    scene CR2_NS2_p40


    Caroline "Аха! А вот и ты!"
    Caroline "(Почему она так далеко под кроватью?)"
    Caroline "(Возможно, она закотилась туда после прошлого раза.)"
    Caroline "(Мне нужно ее вымыть, тогда она будет готова к использованию.)"

    scene CR2_NS2_p41

    Caroline "(Ладно, вот и все... Пора веселиться.)"
    Caroline "(Это будет долго, так как у меня много время.)"
    Caroline "(Пора вставить тебя в киску.)"

    scene CR2_NS2_p42

    $ renpy.sound.play("sfx/vibrator_high.mp3")
    Caroline "Ooo…"
    Caroline "Да ... Прямо так…"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    Caroline "Mмм! Это оно…"

    scene CR2_NS2_p43

    Caroline "Да…"
    $ renpy.sound.play("sfx/vibrator_high.mp3")
    Caroline "Mмм… Это хорошо! Aх!"
    Caroline "OХ! OХХХ, [player_name]! Еби меня сильнее!"
    $ renpy.sound.play("sfx/vibrator_high.mp3")

    scene CR2_NS2_p44

    Caroline "Что? Да!? Что я только что сказала!?"
    Caroline "(Я серьезно думаю о [player_name] трахающему меня?)"
    Caroline "(Это неправильно ... не так ли?)"
    Caroline "(Что со мной не так!?)"


    scene CR2_NS2_p45

    Caroline "(Проклятье! Эта глупая сделка затрагивает меня!)"
    Caroline "(Мне не нравится [player_name]! Это должно быть просто весело!)"
    Caroline "(Это ... странно ... и неправильно!)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pc_icon_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
