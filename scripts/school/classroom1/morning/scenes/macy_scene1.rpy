image macy_scene1_p1 = "images/school/classroom1/morning/scenes/macy_scene1/1.jpg"
image macy_scene1_p2 = "images/school/classroom1/morning/scenes/macy_scene1/2.jpg"
image macy_scene1_p3 = "images/school/classroom1/morning/scenes/macy_scene1/3.jpg"
image macy_scene1_p4 = "images/school/classroom1/morning/scenes/macy_scene1/4.jpg"
image macy_scene1_p5 = "images/school/classroom1/morning/scenes/macy_scene1/5.jpg"
image macy_scene1_p6 = "images/school/classroom1/morning/scenes/macy_scene1/6.jpg"
image macy_scene1_p7 = "images/school/classroom1/morning/scenes/macy_scene1/7.jpg"
image macy_scene1_p8 = "images/school/classroom1/morning/scenes/macy_scene1/8.jpg"
image macy_scene1_p9 = "images/school/classroom1/morning/scenes/macy_scene1/9.jpg"

label macy_scene1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if macy_work_inprogress == True:
        show screen classroom1_morning_notclickable
        $ renpy.show("workinprogress2", layer="screens",)
        " Доступно в ближайшее время."
        $ renpy.hide("workinprogress2", layer="screens",)
        jump classroom1_morning1

    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene macy_scene1_p1 with dissolve
    $ can_hide_windows = True
    MC "(Ах! Вот она! Мэйси. Она самый добрый человек в этой школе...)"
    MC "(Она была единственной, кто верил в меня и сказала, что у меня есть шанс с Селией!)"
    scene macy_scene1_p2
    MC "Эй, Мейси! Что происходит?"
    Macy "…"
    MC "Мэйси?"
    Macy "(Я могу держать его! Я могу держать его!)"
    scene macy_scene1_p3
    Macy "Хахахаха! Я-я не могу поверить, что ты на самом деле это сделал! ха-ха!"
    Macy "Спроси нашего учителя - Ха-ха! Должен признаться, у тебя есть яйца! ха-ха!"
    MC "Привет! Ты обещала не смеяться над этим!"
    Macy "Сожалею! Ха-ха! Ты сумасшедший!"
    scene macy_scene1_p4
    MC "Заткнись!"
    Macy "Ладно ладно!"
    Macy "..."
    Macy "Тебе даже пришлось пойти и поговорить с психотерапевтом! Нет, это слишком много! ха-ха!"
    MC "С меня довольно! Знаешь что? Пошла ты! "
    scene macy_scene1_p5
    MC "(Эхх.. Это будет длинный день..)"
    scene black
    $ renpy.pause(3, hard=True)
    scene macy_scene1_p6
    Macy "…"
    Macy "Буу!"
    MC "Я не сплю."
    MC "Сделай.."
    Macy "Подожи! Позволь мне начать с начала."
    scene macy_scene1_p7
    Macy "Прости. Я не должна была смеяться над тобой. Это было плохо, я знаю."
    Macy "Ты знаешь меня! Я не такая ... Это просто .. все говорили об этом.."
    MC "Расслабься. Все нормально."
    scene macy_scene1_p8
    Macy "Итак ... Ты меня ненавидишь?!?"
    MC "Нет! Все в порядке."
    Macy "Хорошо…"
    MC "Теперь я знаю, что это было глупо даже спросить ее, что... Кроме того, в школе..."
    scene macy_scene1_p9
    Macy "{size=-15}Ты можешь просто спросить меня, идиот...{/size}"
    $ macy_work_inprogress = True
    $ day_time += 1
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump classroom1_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
