image caroline_room_evening_scene4_p1 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/1.jpg"
image caroline_room_evening_scene4_p2 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/2.jpg"
image caroline_room_evening_scene4_p3 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/3.jpg"
image caroline_room_evening_scene4_p4 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/4.jpg"
image caroline_room_evening_scene4_p5 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/5.jpg"
image caroline_room_evening_scene4_p6 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/6.jpg"
image caroline_room_evening_scene4_p7 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/7.jpg"
image caroline_room_evening_scene4_p8 = "/images/home/caroline_room/evening/scenes/caroline_room_evening_scene4/8.jpg"

label caroline_room_evening_scene4_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_room_evening_scene4 == 3:
        show screen caroline_room_evening_not_clickable
        MC "Я уже говорил с ней."
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Miami Viceroy.mp3', channel="music1", loop=True, fadein = 2)
    scene caroline_room_evening_scene4_p1 with dissolve
    $ can_hide_windows = True
    Caroline "Ха-ха! Я не могу в это поверить!"
    MC "(Кажеться, она радуется переменам!)"
    MC "Эй, Кэролайн! Что смешно?"

    scene caroline_room_evening_scene4_p2
    Caroline "О! Хиии! Я не видела, как ты пришел."
    Caroline "Ничего смешного - я просто ... Ты должен увидеть это."
    Caroline "Вот - сядь рядом со мной! Быстро! Это потрясающе!"

    scene caroline_room_evening_scene4_p3
    MC "Хорошо ... что я должен увидеть?"
    Caroline "Это мои отчеты о прибылях и убытках за последний год!"
    MC "Что значат эти красные числа?"
    Caroline "Те месяцы, когда я потеряла деньги, - но посмотри на последний!"
    MC "А? Там черное."
    Caroline "Это означает, что я получила прибыль! И посмотри! Этого почти достаточно, чтобы погасить долги за последние четыре месяца!"
    Caroline "Большая часть этого, в конечном итоге, поступает из онлайн-продаж."

    scene caroline_room_evening_scene4_p4
    MC "Ааа, так что ты на самом деле говоришь, что не могла бы сделать это без меня?"
    Caroline "Я никогда этого не говорила."
    MC "Кто взял все эти фотографии, для твоего сайта и магазина?"

    scene caroline_room_evening_scene4_p5
    Caroline "Ха-ха! Я благодарен, что вы сняли фотографии, но помните, что я провел МЕСЯЦЫ; создание бизнес-счетов, организация доставки, поиск места для аренды."
    Caroline "Вы, безусловно, помогли - но я все-таки сделал львиную долю работы."
    MC "Отлично! Отлично! Я понял! ха-ха!"
    MC "Скажи - ты помнишь то, что произошло, в течение последнего косплея?"

    scene caroline_room_evening_scene4_p6
    MC "Я бы очень хотел снова это сделать."
    Caroline "Ч-Что?"
    MC "Ты знаеш - когда ты потерлась об мой член?"
    MC "Не хочешь снова это сделать?"

    scene caroline_room_evening_scene4_p7
    Caroline "[player_name]... Это было просто для нас, когда мы немного веселились."
    Caroline "Нужно просто выпустить пар."
    MC "Но, меня действительно привлекают."
    if renpy.loadable("patch.rpy"):
        Caroline "Извини ... Я так не чувствую. Ты мой брат. Мы веселились вместе и сделали то, что не должны. Давайте не будем говорить об этом снова. пожалуйста..."
    if not renpy.loadable("patch.rpy"):
        Caroline "Извини ... Я так не чувствую. Ты мой друг. Мы веселились вместе и сделали то, что не должны. Давайте не будем говорить об этом снова. пожалуйста..."
    MC "Извини ... Я просто подумал ... может быть, тебе тоже понравилось."
    Caroline "(Вздох) Дай мне немного времени, подумать."
    MC "Ладно ... Увидимся позже, Кэролайн."

    scene caroline_room_evening_scene4_p8
    Caroline "(Что я сделала? Он уже привлек меня? Или я его возбудила, стоя в этих сексуальных нарядах?)"
    Caroline "(Я не могу поверить, что я сама…)"
    $ caroline_room_evening_scene4 = 3
    $ caroline_mc_room_moenig_scene5 = True
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
