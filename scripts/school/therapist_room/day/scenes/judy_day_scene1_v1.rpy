label judy_day_menu_v1_label:

    scene judy_scene1_v1_p7
    $ can_hide_windows = True
    menu:
        "Talk about Celia’s been selling grades." if Judy_scene1_v1 == 1:
            jump judy_day_scene1_v1_label
        "Cancel":
            jump therapist_room_morning1


label judy_day_scene1_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    scene judy_scene1_v1_p1

    Judy "С возвращением, [player_name]. Я всегда рада, что ученик решил продолжить терапию."
    Judy "Есть ли что-то особенное, что вы хотел бы обсудить?"
    MC "Спасибо, Джуди. Да, на самом деле. Мне было интересно, хотя ... Это все, что сказано в терапии конфиденциально?"
    Judy "Если вы не планируете убивать себя или кого-то еще, тогда да. Это полностью конфиденциально."

    scene judy_scene1_v1_p2
    MC "Потрясающие! Правильно, я думаю, что я понял как отомстить Селии."
    Judy "Да неужели?"
    MC "Я был на ее компьютере, и узнал, что она продает лучшие оценки за тысячи долларов! У нее должно быть не менее $10,000!"
    MC "Я собираюсь использовать эту информацию, чтобы шантажировать ее"

    scene judy_scene1_v1_p3
    Judy "Не нужно этого делать."
    MC "Да?"
    Judy "Это страшная идея."
    MC "Что? Почему?!"

    scene judy_scene1_v1_p4
    Judy "Ты не можешь просто шантажировать ее. Селия-грозная женщина. Будут последствия."
    MC "Но я так много работал, чтобы получить эти доказательства…"
    Judy "Ты можешь использовать их. Просто нужно быть осторожним."
    MC "Что ты имеешь в виду?"

    scene judy_scene1_v1_p5
    Judy "Ты должны работать постепенно. Начни с покупки веб-камеры. Я дам тебе ее адрес Skipe, и ты сможешь анонимно шантажировать ее."
    Judy "Это действительно важно, что бы не делать все слишком быстро. Она может бросить все или пойти в полицию."
    MC "Хорошая идея! Почему ты помогаешь мне?"
    Judy "Селия проголосовала против повышения зарплат школьному персоналу на последней конференции. Давай скажем просто, это мой способ отомстить этой суке!"
    MC "Да, я никогда не знал."

    scene judy_scene1_v1_p5
    Judy "Первое, что нужно - пойти написать ей письмо и положить его в ее кабинет в комнате отдыха. Ты можешь взять конверт со стола возле двери."
    Judy "Затем создай поддельный логин скайп вечером, и дождись пока она с тобой свяжеться."
    MC "Спасибо, Джуди. Я надеюсь, что это сработает."
    Judy "Поверь мне, так и будет. Теперь поторопись и напиши свою записку с требованиями."
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ Judy_scene1_v1 = 3
    $ can_envelope_from_Judy_v1 = 1
    $ can_hide_windows = False
    jump therapist_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
