image caroline_room_morning_scene3_p1 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/1.jpg"
image caroline_room_morning_scene3_p2 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/2.jpg"
image caroline_room_morning_scene3_p3 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/3.jpg"
image caroline_room_morning_scene3_p4 = "/images/home/caroline_room/morning/scenes/caroline_room_morning_scene3/4.jpg"

label caroline_room_morning_scene3_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_can_room_morning_scenes == False:
        show screen caroline_room_morning_not_clickable
        MC "Я уже говорил с ней."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)

    scene caroline_room_morning_scene3_p1 with dissolve
    $ can_hide_windows = True
    MC "(Да? Что случилось с Кэролайн?)"
    MC "(Это совсем не похоже на нее. Она, как правило, одна из самых счастливых, самых оптимистичных людей, которых я когда-либо встречал!)"
    if renpy.loadable("patch.rpy"):
        MC "(Даже мама вовлечена - это должно быть серьезно.)"
    if not renpy.loadable("patch.rpy"):
        MC "(Даже Линда участвовала - это должно быть серьезно.)"

    scene caroline_room_morning_scene3_p2
    Mom "Слушай, я могу помочь с ипотекой еще пару месяцев."
    if renpy.loadable("patch.rpy"):
        Mom "Но после этого, мы будем полагаться, почти полностью на сверхурочные вашего отца, чтобы свести конци с концами."
    if not renpy.loadable("patch.rpy"):
        Mom "Но после этого, мы будем полагаться, почти полностью сверхурочные Боба, чтобы свести конци с концами."
    if renpy.loadable("patch.rpy"):
        Caroline "Я знаю. (сопение) Мам, ты прости меня."
    if not renpy.loadable("patch.rpy"):
        Caroline "я знаю. (сопение) Извините, Линда."
    Caroline "Я действительно думал, что эта идея с магазином будет работать!"

    scene caroline_room_morning_scene3_p3
    if renpy.loadable("patch.rpy"):
        Mom "Возможно, тебе стоит подумать о сокращении потерь? Твой отец может быть в состоянии помочь с работой?"
    if not renpy.loadable("patch.rpy"):
        Mom "Возможно, тебе стоит подумать о сокращении потерь? Боб может помочь в управлении фирмы?"
    Caroline "Нет, нет! Поверь мне - у меня есть план как сделать мой магазин прибыльным."
    Caroline "Я не могу это делать сама по себе. Мне понадобится помощь, чтобы получить вещи."
    Caroline "Могу ли я одолжить денег [player_name], чтобы помочь своему магазину?"
    Mom "Конечно-до тех пор, пока он не возражает."

    scene caroline_room_morning_scene3_p4
    Caroline "Ты мог бы помочь мне, [player_name]?"
    MC "Что нужно сделать?"
    Caroline "Просто прийди в мой магазин, днем. У меня все будет готово. Тогда мы можем начать."
    $ caroline_can_room_morning_scenes = False
    $ caroline_morning_scenes_visit = 4
    $ cosplay_shop_unlocked = True
    $ cloth_shop_minigame_unlocked = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
