image ml_bedroom_morning_scene6_v1_p1 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/1.jpg"
image ml_bedroom_morning_scene6_v1_p2 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/2.jpg"
image ml_bedroom_morning_scene6_v1_p3 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/3.jpg"
image ml_bedroom_morning_scene6_v1_p4 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/4.jpg"
image ml_bedroom_morning_scene6_v1_p5 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/5.jpg"
image ml_bedroom_morning_scene6_v1_p6 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/6.jpg"
image ml_bedroom_morning_scene6_v1_p7 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/7.jpg"
image ml_bedroom_morning_scene6_v1_p8 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/8.jpg"
image ml_bedroom_morning_scene6_v1_p9 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/9.jpg"
image ml_bedroom_morning_scene6_v1_p10 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/10.jpg"
image ml_bedroom_morning_scene6_v1_p11 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/11.jpg"
image ml_bedroom_morning_scene6_v1_p12 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/12.jpg"
image ml_bedroom_morning_scene6_v1_p13 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/13.jpg"
image ml_bedroom_morning_scene6_v1_p13a = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/13a.jpg"
image ml_bedroom_morning_scene6_v1_p14 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/14.jpg"
image ml_bedroom_morning_scene6_v1_p15 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/15.jpg"
image ml_bedroom_morning_scene6_v1_p16 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/16.jpg"
image ml_bedroom_morning_scene6_v1_p16a = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/16a.jpg"
image ml_bedroom_morning_scene6_v1_p17 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/17.jpg"
image ml_bedroom_morning_scene6_v1_p18 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/18.jpg"
image ml_bedroom_morning_scene6_v1_p19a = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/19a.jpg"
image ml_bedroom_morning_scene6_v1_p19b = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/19b.jpg"
image ml_bedroom_morning_scene6_v1_p19c = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/19c.jpg"
image ml_bedroom_morning_scene6_v1_p20 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/20.jpg"
image ml_bedroom_morning_scene6_v1_p21 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/21.jpg"
image ml_bedroom_morning_scene6_v1_p22 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/22.jpg"
image ml_bedroom_morning_scene6_v1_p23 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/23.jpg"
image ml_bedroom_morning_scene6_v1_p24 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/24.jpg"
image ml_bedroom_morning_scene6_v1_p25 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/25.jpg"
image ml_bedroom_morning_scene6_v1_p26 = "/images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_morning_scene6_v1/26.jpg"

image ml_bedroom_morning_scene6_v1_p11anim = Movie(play="videos/Linda-MorningS6-1.webm", loop = True )

label ml_bedroom_morning_scene6_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Chill Wave.mp3', channel="music1", loop=True, fadein = 2)

    scene ml_bedroom_morning_scene6_v1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "Привет, Мам. Я здесь, чтобы поговорить с тобой о вчерашнем событии."
    if not renpy.loadable("patch.rpy"):
        MC "Привет, Линда. Я здесь, чтобы поговорить с тобой о вчерашнем событии."
    Mom "(Залпом) Д-Да?"
    MC "Сейчас подходящее время? Или ты хочешь, чтобы я вернулся позже?"
    Mom "Я ... я скоро начну работать, но у меня есть несколько минут."

    scene ml_bedroom_morning_scene6_v1_p2
    menu:
        "Я тоже тебя люблю.":
            if renpy.loadable("patch.rpy"):
                MC "Мам, я ... Я тоже тебя люблю."
                MC "Не так, как сын обычно любит свою маму. Я имею в виду, я действительно люблю тебя."
            if not renpy.loadable("patch.rpy"):
                MC "Линда, я... Я тоже тебя люблю."
                MC "И не просто. Я имею в виду, я действительно люблю тебя."
            jump ml_bedroom_morning_scene6_v1_label_after_ch
        "Я думаю, я хочу ... то же самое.":


            MC "После всего, что ты сказала вчера, и того, как ты действовала…"
            MC "Думаю, я хочу того же, что и ты."
            jump ml_bedroom_morning_scene6_v1_label_after_ch
        "Ты должна была сказать мне раньше.":

            if renpy.loadable("patch.rpy"):
                MC "Мам ... ты должна была сказать мне раньше."
            if not renpy.loadable("patch.rpy"):
                MC "Линда ... ты должна была сказать мне раньше."
            MC "Ты сказала, что всегда так чувствовала. Если бы я знал, то смог бы понять, почему ты так себя ведешь."
            MC "Все имело бы смысл."
            jump ml_bedroom_morning_scene6_v1_label_after_ch

label ml_bedroom_morning_scene6_v1_label_after_ch:

    scene ml_bedroom_morning_scene6_v1_p3
    if renpy.loadable("patch.rpy"):
        MC "В любом случае, мне пора идти. Но... я действительно люблю тебя, мама. "
    if not renpy.loadable("patch.rpy"):
        MC "В любом случае, мне пора идти. Но... я действительно люблю тебя, Линда. "
    MC "И мне, возможно, будет интересно ... заняться кое-чем ... ЭМ... вещи... это..."
    MC "Прости, я начинаю нервничать и спотыкаться о свои слова. Мне нужно идти."

    scene ml_bedroom_morning_scene6_v1_p4
    Mom "Не уходи! Пожалуйста!"
    MC "Ой!"
    Mom "Прости, я не хотела тебя пугать."
    if renpy.loadable("patch.rpy"):
        Mom "Я была...  так увереннна, что ты собираешься сказать мне, что любишь меня, как мать."
    if not renpy.loadable("patch.rpy"):
        Mom "Я была... так уверена, что ты собирался сказать, что любишь меня как друга."
    Mom "Мне было страшно, что я могу оттолкнуть тебя, глупыми играми."
    Mom "Я знаю, что все движется довольно быстро... но если хочешь, мы могли бы раздеться до белья. Как это звучит?"
    MC "Действительно?"
    Mom "Сядь на край постели."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Niles_Blues.mp3', channel="music2", loop=True, fadein = 2)

    scene ml_bedroom_morning_scene6_v1_p5
    Mom "Я хочу, чтобы ты увидел это."
    Mom "Я хочу, чтобы ты наслаждался моим телом."
    Mom "Это только для тебя."

    scene ml_bedroom_morning_scene6_v1_p6
    Mom "Хорошо? Как ты думаешь?"
    Mom "(Я надеюсь, что он любит мое тело... Я знаю, что я не молодая…)"
    if renpy.loadable("patch.rpy"):
        MC "Ой... Ты потрясающая, мам."
    if not renpy.loadable("patch.rpy"):
        MC "Ой... Ты потрясающая, Линда."

    scene ml_bedroom_morning_scene6_v1_p7
    Mom "Ты действительно так думаешь?"
    MC "Да - твое тело невероятно! И это белье, которое ты носишь, идеально тебе подходит!"
    Mom "Я рад, что тебе нравится."

    scene ml_bedroom_morning_scene6_v1_p8
    Mom "Как насчет того, если я разденусь?"
    Mom "Я показала тебе, что у меня есть - справедливо, если и ты покажешь свое."
    MC "Ладно, подожди.…"

    scene ml_bedroom_morning_scene6_v1_p9
    MC "Хорошо? Это так как ты себе представляла?"
    Mom "МММ ... Почти. Часть, о которой я фантазировала, все еще в одежде."

    scene ml_bedroom_morning_scene6_v1_p10
    Mom "Это будет так хорошо, чтобы наконец поцеловать тебя, не чувствуя мурашек."
    MC "Ты заставила меня задаться вопросом, что происходит, несколько дней назад."
    Mom "Хе-хе ... Извини. Я просто не могу сопротивляться тебе."

    scene ml_bedroom_morning_scene6_v1_p11
    MC "Mмм…"
    Mom "(Что может пойти не так?)"
    scene ml_bedroom_morning_scene6_v1_p11anim with dissolve
    Mom "(Это как... мои мечты, наконец, начинают сбываются.)"
    Mom "(Каждый раз, когда я целую [player_name], бабочки в моем животике …, я никогда не чувствовала такого, когда целовала кого-то еще в моей жизни.)"

    scene ml_bedroom_morning_scene6_v1_p12
    Mom "Ляг на кровати. Именно так."
    Mom "(Я вижу, как ему тяжело... но я должна чувствовать это своей рукой.)"

    scene ml_bedroom_morning_scene6_v1_p13
    Mom "Не возражаешь, если я ... дотронусь до тебя рукой?"
    MC "Конечно... я не возражаю."

    scene ml_bedroom_morning_scene6_v1_p13a
    Mom "(Вау ... он огромный…)"
    Mom "(Если бы только он не носил эти боксерские шорты…)"
    Mom "(Я хотела бы взять его член в рот прямо сейчас, и сосать его, пока он не кончит.)"

    scene ml_bedroom_morning_scene6_v1_p14
    if renpy.loadable("patch.rpy"):
        MC "Ах... М-Мама..."
    if not renpy.loadable("patch.rpy"):
        MC "Aхх… Л-Линда..."
    MC "(Она такая нежная со своим языком…)"

    scene ml_bedroom_morning_scene6_v1_p15
    MC "Ах! ААА..."
    Mom "(Похоже, его соски особенно чувствительны.)"
    Mom "(Он явно наслаждается, когда я щелкаю языком по ним.)"

    scene ml_bedroom_morning_scene6_v1_p16
    if renpy.loadable("patch.rpy"):
        MC "(Мне сейчас так тяжело ... не могу поверить, что мама так долго меня привлекала.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Мне сейчас так тяжело ... не могу поверить, Линда так долго меня привлекала.)"
    MC "(Интересно, была ли это одна из ее фантазий, обо мне и о ней?)"

    scene ml_bedroom_morning_scene6_v1_p16a
    if renpy.loadable("patch.rpy"):
        MC "Ох... О, Мам!"
    if not renpy.loadable("patch.rpy"):
        MC "Ох... О, Линда!"
    Mom "Тебе нравится, когда я целую твою шею вот так?"
    MC "Да…"

    scene ml_bedroom_morning_scene6_v1_p17
    Mom "Теперь ты можешь делать все, что захочешь. Я получил свое удовольствие-пришло время для вас, чтобы иметь некоторые слишком."
    MC "Что ты имеешь в виду?"
    Mom "Я буду лежать на кровати. Остальное зависит от тебя."

    scene ml_bedroom_morning_scene6_v1_p18
    menu:
        "Для начала, сделать маме массаж ног." if renpy.loadable("patch.rpy"):

            scene ml_bedroom_morning_scene6_v1_p19a
            MC "У тебя красивые ноги."
            Mom "Хехе... Спасибо. Ты что, фетешист?"
            MC "Что?!"

            scene ml_bedroom_morning_scene6_v1_p19b
            Mom "Успокойся - я просто дразню тебя."
            Mom "МММ ... приятно, когда ты массируешь их вот так."
            MC "Тебе это нравится? Тогда я перейду к стопам."

            scene ml_bedroom_morning_scene6_v1_p19c
            Mom "ААА... Твой отец никогда не делает ничего подобного, для меня."
            Mom "Твои пальцы удивительные."
            jump ml_bedroom_morning_scene6_v1_label_after_ch2

        "Для начала, сделать Линде массаж ног." if not renpy.loadable("patch.rpy"):

            scene ml_bedroom_morning_scene6_v1_p19a
            MC "У тебя красивые ноги."
            Mom "Хехе... Спасибо. Ты что, фетешист?"
            MC "Что?!"

            scene ml_bedroom_morning_scene6_v1_p19b
            Mom "Успокойся - я просто дразню тебя."
            Mom "МММ ... приятно, когда ты массируешь их вот так."
            MC "Тебе это нравится? Тогда я перейду к стопам."

            scene ml_bedroom_morning_scene6_v1_p19c
            Mom "ААА... Боб никогда не делает ничего подобного, для меня."
            Mom "Твои пальцы удивительные."
            jump ml_bedroom_morning_scene6_v1_label_after_ch2

        "Начать с бедер мамы." if renpy.loadable("patch.rpy"):
            jump ml_bedroom_morning_scene6_v1_label_after_ch2
        "Начать с бедер Линды." if not renpy.loadable("patch.rpy"):
            jump ml_bedroom_morning_scene6_v1_label_after_ch2

label ml_bedroom_morning_scene6_v1_label_after_ch2:
    scene ml_bedroom_morning_scene6_v1_p20
    if renpy.loadable("patch.rpy"):
        C "Можешь раздвинуть ноги еще немного, мама?"
    if not renpy.loadable("patch.rpy"):
        MC "Можешь раздвинуть ноги еще немного, Линда?"
    Mom "Конечно."
    MC "Идеально."

    scene ml_bedroom_morning_scene6_v1_p21
    Mom "Ooх..."
    Mom "(Его пальцы так близко к моей киске ... я хочу, чтобы он подошел немного ближе, и просто вставил их внутрь меня.)"
    MC "Твоя кожа такая мягкая."

    scene ml_bedroom_morning_scene6_v1_p22
    Mom "Хитрость в том, отшелушивающий скраб и увлажняющий крем, два раза в день."
    MC "Ты не против, если я коснусь твоей груди?"
    Mom "Пожалуйста, вперед."

    scene ml_bedroom_morning_scene6_v1_p23
    MC "Вау…"
    Mom "Ты можешь даже сжать их."
    Mom "Только не будь слишком грубый."

    scene ml_bedroom_morning_scene6_v1_p24
    Mom "Aхх…"
    MC "(Это чертовски круто!)"
    MC "(Я надеюсь, что смогу поиграть с ними, без бюстгальтера!)"

    scene ml_bedroom_morning_scene6_v1_p25
    Mom "Если бы на нас не было нижнего белья, я бы просто потянула тебя на себя."
    Mom "МММ... Я хотела бы чувствовать его член, входящий глубоко в мою влажную киску."

    scene ml_bedroom_morning_scene6_v1_p26
    Mom "Я уже чувствую твой твердый член, прижимающийся к моим черным трусикам."
    Mom "К сожалению, мне нужно идти. Если я проведу еще минуту в постели, я опоздаю на работу."
    Mom "Увидимся вечером, милый."
    if renpy.loadable("patch.rpy"):
        MC "Я люблю тебя, мама."
    if not renpy.loadable("patch.rpy"):
        MC "Я люблю тебя, Линда."
    Mom "Я тоже тебя люблю."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ ml_bedroom_morning_scene6 = False
    $ day_time +=1
    $ ml_work_day_scene2 = True
    $ can_ml_work_day_scene2 = False
    $ can_sms2_from_ml = True
    $ can_hide_windows = False
    jump parents_bedroom_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
