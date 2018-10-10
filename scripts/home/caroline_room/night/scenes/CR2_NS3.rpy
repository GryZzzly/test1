image CR2_NS3_p1 = "images/home/caroline_room/night/scenes/CR2_NS3/1.jpg"
image CR2_NS3_p2 = "images/home/caroline_room/night/scenes/CR2_NS3/2.jpg"

label CR2_NS3_label:
    if can_CR2_NS3 == True:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene CR2_NS3_p1 with dissolve
        $ can_hide_windows = True
        MC "Черт возьми.. (Она все еще пила, даже после этого СМС. Я вижу, что ей действительно нужно полностью очистить свой разум.)"
        Caroline "Aх..."
        MC "(Да? Она проснулась?)"
        scene CR2_NS3_p2 with dissolve
        Caroline "Mмм... Ч-что... [player_name].. "
        MC "(мое имя? Она говорит во сне?)"
        MC "Глоток (Я вижу ее сосок.)"
        Caroline "Ты .. ... лучше ......"
        MC "(Я ничего не понимаю... Я только надеюсь, что у нее будет хороший сон со мной.)"
        $ can_CR2_NS3 = False
        $ CR2_NS3_MCtalk = False
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump caroline_room_morning1
    else:
        show screen caroline_room_night
        $ clickable = False
        MC "Она пьяна. Нет смысла будить ее."
        $ clickable =  True
        $ can_hide_windows = False
        jump caroline_room_morning1



screen say22(who=player_name1, what="Drunk Caroline!? She's a mess after that robbery! She's probably in her bedroom. Maybe I should check on her?"):
    key "hide_windows" action NullAction()
    modal True
    zorder 104
    style_prefix "say"
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("phone_main_screen"),Hide("contact_screen"),Hide("m_from_Caroline"), Hide("say22"), SetVariable("CR2_NS3_MCtalk",False)]
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"

                text who id "who" style "say_label"

        text what id "what" style "say_dialogue"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
