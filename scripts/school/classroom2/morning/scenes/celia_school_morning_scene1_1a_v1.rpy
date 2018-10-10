image celia_school_morning_scene1v1_p1 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/1.jpg"
image celia_school_morning_scene1v1_p2 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/2.jpg"
image celia_school_morning_scene1v1_p3 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/3.jpg"

image celia_school_morning_scene1v1_celia = "images/school/classroom2/morning/scenes/celia_school_morning_scene1v1/RenPy.png"

image celia_school_morning_scene1av1_p1 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1av1/1.jpg"
image celia_school_morning_scene1av1_p2 = "images/school/classroom2/morning/scenes/celia_school_morning_scene1av1/2.jpg"

label celia_school_morning_scene1v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ can_hide_windows = True
    if can_celia_school_morning_scene1v1 == True and talking_celia_school_morning_scene1v1 == 1:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

        scene celia_school_morning_scene1v1_p1 with dissolve
        Celia "Доброе утро, лапочка!"
        Celia "Все еще хочешь найти себе девушку?"

        scene celia_school_morning_scene1v1_p2
        MC "(Пошла ты! Я обещаю, что отомщу тебе!)"
        Celia "Или ты думаешь снова попросить своего учителя??"
        MC "(Грр ... Она смущает меня перед всем классом!)"

        scene celia_school_morning_scene1v1_p3
        Classmates "Ахахахах!"
        Celia "Вернись в класс, [player_name]. Урок вот-вот начнется."
        MC "(Бог ... Теперь я ее ненавижу! Интересно, как долго она будет помнить.)"

        $ can_celia_school_morning_scene1v1 = False
        $ talking_celia_school_morning_scene1v1 = 2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump classroom2_morning2

    if can_celia_school_morning_scene1v1 == True and talking_celia_school_morning_scene1v1 == 2:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

        scene celia_school_morning_scene1v1_p1 with dissolve
        Celia "Опять ты? Что ты хочешь спросить?"
        MC "Что? Нет!"

        scene celia_school_morning_scene1v1_p2
        Celia "Поэтому ты не хочешь пойти со мной..?"
        MC "Я имею в виду да?"
        Celia "Фу, какой неудачник. Вернись свой класс."
        MC "..."

        scene celia_school_morning_scene1v1_p3
        Classmates "Хахахахаха!"
        Blonde_Boy "Вау! Как жалко!"
        Brunette_Girl "О мой Бог! Это так потрясающе!"
        MC "(О Боже ... Это было чертовски ужасно…)"
        MC "(Я обещаю, я отомщу тебе, сука!)"
        $ can_celia_school_morning_scene1v1 = False
        $ talking_celia_school_morning_scene1v1 = 2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump classroom2_morning2


    if can_celia_school_morning_scene1v1 == True and talking_celia_school_morning_scene1v1 == 3:

        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

        scene celia_school_morning_scene1av1_p1 with dissolve
        MC "Привет, миссис Селия..."
        Celia "Если у вас есть вопросы ... просто ... просто спросите одного из своих одноклассников."

        scene celia_school_morning_scene1av1_p2
        MC "Вы уверены?"
        Celia "Да. Просто ... вернись в свой класс."
        MC "А? Хорошо."
        MC "(Она действует менее агрессивно, чем раньше!)"
        MC "(Я думаю, моя стратегия шантажа работает очень хорошо.)"
        $ can_celia_school_morning_scene1v1 = False
        $ talking_celia_school_morning_scene1v1 = 3
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump classroom2_morning2


    if can_celia_school_morning_scene1v1 == False:

        show celia_school_morning_scene1v1_celia
        show screen classroom2_morning_notclickable
        $ can_hide_windows = False
        MC "Я не хочу говорить с этой ... сукой."
        $ can_hide_windows = False
        jump classroom2_morning2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
