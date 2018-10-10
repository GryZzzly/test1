image delilah_scene1_p1 = "images/school/pool/morning/scenes/delilah_scene1/1.jpg"
image delilah_scene1_p2 = "images/school/pool/morning/scenes/delilah_scene1/2.jpg"
image delilah_scene1_p3 = "images/school/pool/morning/scenes/delilah_scene1/3.jpg"
image delilah_scene1_p4 = "images/school/pool/morning/scenes/delilah_scene1/4.jpg"
image delilah_scene1_p5 = "images/school/pool/morning/scenes/delilah_scene1/5.jpg"



label delilah_scene1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if delilah_work_inprogress == True:
        $ can_hide_windows = False
        show screen pool_morning_notclickable
        $ renpy.show("workinprogress2", layer="screens",)
        " Доступно в ближайшее время."
        $ renpy.hide("workinprogress2", layer="screens",)
        jump pool_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene delilah_scene1_p1 with dissolve
    $ can_hide_windows = True
    MC "…."
    MC "(Черт.. Она горячая..)"
    MC "(Я не видел ее здесь раньше... Она новая студентка?)"
    $ Delilah_name = "???"
    Delilah "Как долго ты собираешся смотреть на меня так?"
    Delilah "Ты знаешь, что я могу видеть твое отражение в воде, правда?"
    scene delilah_scene1_p2
    MC "Ах !? Ха-ха .. Извини.."
    Delilah "Кстати, меня зовут Далила."
    $ Delilah_name = "Delilah"
    Delilah "Ты заинтересован в присоединении к клубу по плаванию?"
    Delilah "Нам, конечно, нужен кто-то, чтобы делать грязную работу."
    MC "Грязную работу?"
    Delilah "Знаешь .. Держи это место ОЧЕНЬ чистым."
    MC "Не совсем .. (я не хочу ничего чистить!)"
    scene delilah_scene1_p3
    Delilah "Да? Нет? После инцидента с Селией?"
    Delilah "Работа здесь может быть очень полезна для тебя."
    scene delilah_scene1_p4
    Delilah "Просто подумай об этом... Я — девушка... Я, конечно, могу найти кого-то идеального для тебя."
    MC "Идеально подходит для меня? (у нее есть кто-то в виду?)"
    Delilah "Да, идеально подходит для тебя! Дай подумать... Хм.. "
    Delilah "Вероятно, какая-то жирная и глупая девушка, наверняка, будет отчаянно заинтересована тобой. "
    Delilah "Без обид - Конечно! Я только говорю правду."
    MC "(Эта сука! Она насмехается надо мной!)"
    MC "…"
    scene delilah_scene1_p5
    Delilah "Ну, если ты передумаешь, ты знаешь, где меня найти."
    $ delilah_work_inprogress = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump pool_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
