image SR2_weekend_sunbed_p1 = "images/Weekend_Events/Sara/R2/SunBed/1.jpg"
image SR2_weekend_sunbed_p2 = "images/Weekend_Events/Sara/R2/SunBed/2.jpg"
image SR2_weekend_sunbed_p3 = "images/Weekend_Events/Sara/R2/SunBed/3.jpg"
image SR2_weekend_sunbed_p4 = "images/Weekend_Events/Sara/R2/SunBed/4.jpg"
image SR2_weekend_sunbed_p5 = "images/Weekend_Events/Sara/R2/SunBed/5.jpg"
image SR2_weekend_sunbed_p6 = "images/Weekend_Events/Sara/R2/SunBed/6.jpg"

label SR2_SunBed_label:
    if SR2_after_sunbed == True:
        show screen swimming_poll_scr
        $ can_hide_windows = False
        $ clickable = False
        MC "We've already been there."
        $ music_continue = False
        $ clickable = True
        jump swimming_poll_label
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
        scene SR2_weekend_swimming_pool_p2
        $ can_hide_windows = True
        MC "Как насчет того, чтобы расслабиться на шезлонгах?"
        Sara "Круто."
        Sara "ААА! Там есть пара свободных! Быстрее! Следуй за мной!"

        scene SR2_weekend_sunbed_p1

        MC "Ах... они идеальны. У тебя отличное место.."
        MC "Большинство других стульев стоят в тени."
        Sara "Да, когда ты будешь приходишь сюда так часто, как я, ты узнаешь, где лучшие места!"
        Sara "Мы получим - по крайней мере - два хороших часа солнечного света."

        scene SR2_weekend_sunbed_p2

        MC "Потрясающе."
        Sara "Mмм… Не возражаешь, если я отойду на пару минут??"
        MC "Делай, что хочешь, Сара. Просто отдыхай."
        Sara "Благодарю, [player_name]."

        scene SR2_weekend_sunbed_p3

        MC "(Черт, я никогда не понимал, насколько тонким был ее купальник, до сих пор.)"
        MC "(Только посмотрите, как мало это оставляет фантазии, между бедер.)"
        MC "(Еще полдюйма, и я смогу увидеть ее киску!)"

        scene SR2_weekend_sunbed_p4

        Sara "Ты тоже не собираешься спать?"
        MC "Я просто любуюсь, как ты прекрасна.."
        Sara "[player_name]…"
        Sara "Ты заставляешь меня краснеть на людях."
        Sara "Могу ... могу я подержать тебя за руку, пока сплю?"
        MC "Конечно, Сара."

        scene SR2_weekend_sunbed_p5

        MC "(Она такая очаровательная. Мне нравится, как она думала, что ей нужно спросить моего разрешения.)"
        MC "(Ее руки так мягки по отношению к моим. Я мог бы очень легко заснуть прямо сейчас.)"
        MC "Сара, я люблю тебя."
        Sara "..."

        scene SR2_weekend_sunbed_p6

        MC "Сара?"
        Sara "Zzz…."
        MC "(Все ... похоже, что она настолько довольна, что сразу уснула.)"
        MC "Сладких снов, Сара."
        $ SR2_after_sunbed = True
        $ can_hide_windows = False
        jump swimming_poll_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
