image ml_kitchen_morning_scene4_v1_p1 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/1.jpg"
image ml_kitchen_morning_scene4_v1_p2 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/2.jpg"
image ml_kitchen_morning_scene4_v1_p3 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/3.jpg"
image ml_kitchen_morning_scene4_v1_p4 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/4.jpg"
image ml_kitchen_morning_scene4_v1_p5 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/5.jpg"
image ml_kitchen_morning_scene4_v1_p6 = "images/home/kitchen/morning/scenes/ml_morning_kitchen_scene4_v1/6.jpg"

screen ml_kitchen_morning_scene4_V1__screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("ml_kitchen_morning_scene4_V1__screen"),Jump("kitchen_morning1")]


label ml_kitchen_morning_scene4_V1_label:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if ml_can_bedroom_morning_scene5 == False:
        show screen kitchen_morning
        show screen ml_kitchen_morning_scene4_V1__screen
        show screen kitchen_morning_notclickable
        MC "Я уже говорил с ними."
        jump kitchen_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Malt Shop Bop.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_kitchen_morning_scene4_v1_p1 at pandown1
    $ can_hide_windows = True
    $ renpy.pause(2)
    if renpy.loadable("patch.rpy"):
        MC "(Похоже, тетя сегодня в гостях!)"
        MC "(Она довольно близкий, член семьи. Мы видим ее почти каждую неделю.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Похоже у Линды сегодня гости!)"
        MC "(Она довольно близкий, член семьи. Мы видим ее почти каждую неделю.)"

    scene ml_kitchen_morning_scene4_v1_p2
    if renpy.loadable("patch.rpy"):
        MC "(Что странно, мамы  тетя такие разные личности!)"
        MC "(В то время как мама - трудолюбивая женщина сориентированная на карьере, тетя - ходячая, говорящая, кукла Барби.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Что странно, мамы  тетя такие разные личности!)"
        MC "(В то время как мама - трудолюбивая женщина сориентированная на карьере, тетя - ходячая, говорящая, кукла Барби.)"
    MC "(Она проводит большую часть своего свободного времени в дневных санаториях, шопингах и тусовоках вместе с друзьями.)"

    scene ml_kitchen_morning_scene4_v1_p3
    Mom "Ах! Вот ты где!"
    Mom "Я думала, что мне придётся прийти и разбудить тебя."

    if renpy.loadable("patch.rpy"):
        MC "Привет мама! Привет, Тетя!"
    if not renpy.loadable("patch.rpy"):
        MC "Привет."
        $ Auntie_name = "Подруга Линды"
    Auntie "Привет, [player_name]."
    Mom "Иди я тебя поцелую."

    scene ml_kitchen_morning_scene4_v1_p4
    Mom "Поцелуй!"
    Auntie "Так или иначе я говорила Маргарет - если ты хочешь выйти в ТОМ платье, тогда мы НЕ будем сидеть за одним и тем же столом во время ланча."
    Auntie "Я СЕРЬЕЗНО - кто носит бежевое платье?!"

    scene ml_kitchen_morning_scene4_v1_p2
    Mom "О, да... Действительно…"
    if renpy.loadable("patch.rpy"):
        Mom "(Бог, она [Auntie_name] не имеют каких-либо других интересов, кроме одежды и моды?!)"
    if not renpy.loadable("patch.rpy"):
        Mom "(Бог, у моей подруги нет никаких других интересов, кроме одежды и моды?!)"
    Mom "(Я должна изменить тему, пока она не свела меня с ума.)"
    Mom "Ну, [player_name] ищет работу. Не так ли?"
    Auntie "Действительно?"

    scene ml_kitchen_morning_scene4_v1_p5
    Auntie "У меня есть бассейн, который нужно регулярно чистить."
    Auntie "Если тебе иньересно, я буду платить тебе за уборку."
    Auntie "Ну как?"
    if renpy.loadable("patch.rpy"):
        MC "Конечно! Спасибо, тетя!"
    if not renpy.loadable("patch.rpy"):
        MC "Конечно! благодарю."

    scene ml_kitchen_morning_scene4_v1_p6
    Auntie "Прекрасно! Я придумаю дату когда ты сможешь прийти."
    if renpy.loadable("patch.rpy"):
        Mom "Спасибо, сестренка. Я очень ценю это."
    if not renpy.loadable("patch.rpy"):
        Mom "Спасибо. Я очень ценю это."
    if renpy.loadable("patch.rpy"):
        Auntie "Ой, ну же! У меня есть деньги, которые я могу потратить на своего любимого племянника!"
    if not renpy.loadable("patch.rpy"):
        Auntie "Ой, ну же! У меня есть деньги, которые я могу потратить на тебя!"
    if renpy.loadable("patch.rpy"):
        MC "Спасибо, тетя!"
    if not renpy.loadable("patch.rpy"):
        MC "Спасибо!"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ aunt_house_unlocked = True
    $ ml_kitchen_morning_scene = False
    $ ml_bedroom_morning_scene5 = True
    $ ml_can_bedroom_morning_scene5 = False
    $ ml_salon_morning_visit = 5
    $ au_bath_event_unlock = True
    $ can_hide_windows = False
    jump kitchen_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
