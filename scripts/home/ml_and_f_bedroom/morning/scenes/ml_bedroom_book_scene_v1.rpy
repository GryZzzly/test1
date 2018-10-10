image ml_bedroom_book_scene_v1_p1 = "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/1.jpg"
image ml_bedroom_book_scene_v1_p2 = "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/2.jpg"
image ml_bedroom_book_scene_v1_p3 = "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/3.jpg"
image ml_bedroom_book_scene_v1_p4 = "images/home/ml_and_f_bedroom/morning/scenes/ml_bedroom_book_scene_v1/4.jpg"

label ml_bedroom_book_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    scene ml_bedroom_book_scene_v1_p1 with dissolve
    $ can_hide_windows = True
    if renpy.loadable("patch.rpy"):
        MC "(Это похоже на книгу, которую мама читала, когда трахалась с отцом прошлой ночью!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Ах, это похоже на книгу, которую читала Линда, когда она трахалась с Бобом прошлой ночью!)"
    MC "(Хмм, что может быть интереснее секса?)"
    MC "(Нужно…)"


    if renpy.loadable("patch.rpy"):
        scene ml_bedroom_book_scene_v1_p2
        MC "Встречаться с своим ... сыном?"
    if not renpy.loadable("patch.rpy"):
        MC "Встречаться со своим ... очень молодым другом?"
    MC "Как сказать, если он ... сексуально привлекает вас?!"

    scene ml_bedroom_book_scene_v1_p3
    MC "Святые угодники!"
    MC "(Она просто читает это для удовольствия?)"
    MC "(Нет... она должна быть серьезной.)"
    MC "(То, как она поцеловала меня, в то утро, и то, как странно вела себя со меня.)"
    if renpy.loadable("patch.rpy"):
        MC "(Она думает о том, чтобы трахнуть меня, когда она с отцом?)"
    if not renpy.loadable("patch.rpy"):
        MC "(Она думает о том, чтобы трахнуть меня, когда она с Бобом?)"
    scene ml_bedroom_book_scene_v1_p4
    MC "Черт ... теперь все понятно."
    if renpy.loadable("patch.rpy"):
        MC "(Моя собственная мать хочет трахнуть меня!)"
        MC "(Как, черт возьми, я вообще должен реагировать на это?!)"
        MC "(Боже ... я больше никогда не смогу смотреть ей прямо в глаза!)"
        MC "(Маме повезло, что папа не обращает внимания на книги, которые она читает! Если он поймает ее с этим, он будет в ярости!)"
    if not renpy.loadable("patch.rpy"):
        MC "(Линда хочет трахнуть меня!)"
        MC "(Как, черт возьми, я вообще должен реагировать на это?!)"
        MC "(Боже ... я больше никогда не смогу смотреть ей прямо в глаза!)"
        MC "(Линде повезло, что Боб не обращает внимания на книги, которые она читает! Если он поймает ее с этим, он будет в ярости!)"
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ ml_bedroom_book_scene = False
    $ can_hide_windows = False
    jump salon_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
