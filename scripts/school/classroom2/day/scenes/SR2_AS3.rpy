image SR2_AS3_p1 = "images/school/classroom2/day/scenes/SR2_AS3/1.jpg"
image SR2_AS3_p2 = "images/school/classroom2/day/scenes/SR2_AS3/2.jpg"
image SR2_AS3_p3 = "images/school/classroom2/day/scenes/SR2_AS3/3.jpg"
image SR2_AS3_p4 = "images/school/classroom2/day/scenes/SR2_AS3/4.jpg"
image SR2_AS3_p5 = "images/school/classroom2/day/scenes/SR2_AS3/5.jpg"

label SR2_AS3_label:
    if can_SR2_AS3 == False:
        show screen classroom2_day
        $ clickable = False
        MC "Я уже говорил с ней.."
        $ clickable = True
        jump classroom2_morning1
    if not SR2_vibrator in inventory.items:
        show screen classroom2_day
        $ clickable = False
        MC "Я до сих пор не купил этот вибратор."
        $ clickable = True
        jump classroom2_morning1
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
        $ can_hide_windows = True
        scene SR2_AS3_p1 with dissolve

        MC "*ПССС! Сара ... я все понял.."
        Sara "ХМ?"
        MC "Я пошел в секс-шоп вечером и купил тебе вибратор. Он в моей ком..."

        scene SR2_AS3_p2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/RetroFuture Clean.mp3', channel="music2", loop=True, fadein = 2)

        Sara "ВИБРАТОР!?"
        Sara "У тебя есть вибратор.?!"
        MC "(Черт! Она слишком громкая! Если она не будет осторожна, кто-нибудь услышит ее!)"
        MC "(Не понимаю, почему она так удивлена! Мы говорили об этом!)"

        scene SR2_AS3_p3

        MC "Тише! Если ты не будешь осторожна, то половина твоих одноклассников услышит тебя!"
        Sara "(Оппс! Я не думала об этом... я была так шокирована, что этого никогда не случалось со мной.)"
        MC "Теперь я могу снять руку? Или ты собираешься объявить всем, что делала мне минет?"
        Sara "Mмм хмм..."

        scene SR2_AS3_p4

        Sara "Прости, я просто ... немного растерялась."
        MC "Все нормально. Увидимся позже. Ты прийдешь ко мне?"
        MC "Я смогу дать тебе его, когда мы встретимся."

        scene SR2_AS3_p5

        Sara "(Глоток) Хорошо, я буду в твоей спальне.."
        if renpy.loadable("patch.rpy"):
            MC "Наверное, лучше подождать, пока мама уснет."
        else:
            MC "Наверное, лучше подождать, пока Линда уснет."
        Sara "Да, тогда увидимся."
        if renpy.loadable("patch.rpy"):
            MC "Ты, вероятно, должен искать хорошее место, чтобы спрятать его. Я не хочу, чтобы мама нашла его, когда уберет твою комнату."
        else:
            MC "Ты, вероятно, должен искать хорошее место, чтобы спрятать его. Я не хочу, чтобы Линда нашла его, когда уберет твою комнату."
        Sara "Не волнуйся, я знаю несколько мест, где она не будет смотреть."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        $ can_SR2_AS3 = False
        $ SR2_NS2 = True
        $ S_N_inbed = False
        jump classroom2_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
