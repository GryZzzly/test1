image CR2_MS2_p1 = "/images/home/caroline_room/morning/scenes/CR2_MS2/1.jpg"
image CR2_MS2_p2 = "/images/home/caroline_room/morning/scenes/CR2_MS2/2.jpg"
image CR2_MS2_p3 = "/images/home/caroline_room/morning/scenes/CR2_MS2/3.jpg"
image CR2_MS2_p4 = "/images/home/caroline_room/morning/scenes/CR2_MS2/4.jpg"
image CR2_MS2_p5 = "/images/home/caroline_room/morning/scenes/CR2_MS2/5.jpg"

label CR2_MS2_label:
    if can_CR2_MS2 == False:
        show screen caroline_room_morning
        $ clickable = False
        MC "Я уже говорил с ней."
        $ clickable = True
        jump caroline_room_morning1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music1", loop=True, fadein = 2)
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    scene CR2_MS2_p1 with dissolve
    $ can_hide_windows = True
    Caroline "Нет, вы не понимаете - мне нужны деньги, чтобы заплатить арендную плату!"
    Caroline "..."
    Caroline "Я не могу ждать два месяца для утверждения. Мне это нужно прямо сейчас!"
    MC "(Дерьмо ... Похоже, у Кэролайн все не так хорошо, с банком.)"

    scene CR2_MS2_p2

    Caroline "Как вы можете назвать это займом, если для получения одобрения требуется два месяца?!"
    Caroline "..."
    Caroline "Фу, отлично ... Я не знаю, как я буду поддерживать свой бизнес на плаву тем временем."
    Caroline "…"
    MC "(Сейчас она выглядит подавленной. Я, вероятно, должен вмешаться.)"
    Caroline "Хорошо ... Спасибо за ваше время ... Вы позвоните мне, если что-то изменится?"
    Caroline "Спасибо..."

    scene CR2_MS2_p3

    MC "Эй, Кэролайн, я не мог не подслушать конец твоего разговора."
    Caroline "Это не то, что тебе нужно знать."
    MC "Я просто хочу, чтобы ты знала, что я здесь, чтобы помочь, если ты нуждаешься."

    scene CR2_MS2_p4

    Caroline "Моя аренда должна быть оплачена, но у меня нет наличных денег. А это будет через несколько месяцев после того, как банк сможет утвердить кризисный кредит! Как ты мне поможешь?"
    MC "Я мог бы дать тебе кредит сам - или даже дать немного денег, чтобы помочь тебе встать на ноги."
    Caroline "Я ... мм…"

    scene CR2_MS2_p5

    Caroline "Нет. Я не могу. Я уже взрослая. Я должна начать стоять на своих ногах и сражаться своими собственными силами за победу."
    MC "Но, Кэролайн."
    Caroline "Никаких возражений. Я должна разобраться в этом самостоятельно."

    scene CR2_MS2_p3

    Caroline "Спасибо за беспокойство. Это много значит для меня."
    $ can_CR2_MS2 = False
    $ renpy.music.stop(channel="music1", fadeout=1)
    $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
    $ can_hide_windows = False
    jump caroline_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
