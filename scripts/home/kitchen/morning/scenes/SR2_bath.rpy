image SR2_bath_p1 = "images/home/kitchen/morning/scenes/SR2_bath/1.jpg"
image SR2_bath_p2 = "images/home/kitchen/morning/scenes/SR2_bath/2.jpg"
image SR2_bath_p3 = "images/home/kitchen/morning/scenes/SR2_bath/3.jpg"
label SR2_bath_label:

    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if can_SR2_bath == False:
        show screen kitchen_morning_notclickable
        MC "Я уже знаю, кто там."
        jump kitchen_morning1

    if camera in inventory.items:

        if camera.selected == True:
            $ renpy.music.stop(channel="music2", fadeout=1)
            $ renpy.music.play('/sfx/March of the Spoons.mp3', channel="music1", loop=True, fadein = 2)
            $ can_hide_windows = True
            scene SR2_bath_p1 with dissolve
            MC "А? Что она делает?"
            MC "Она должна была принять душ."
            scene SR2_bath_p2
            MC "Она снова сонная? Эти игры однажды убьют ее."
            scene SR2_bath_p3
            MC "Серьезно!? Она планирует вздремнуть в ванной комнате?"
            MC "..."
            if renpy.loadable("patch.rpy"):
                MC "Надеюсь, мама ее не заметит."
            else:
                MC "Надеюсь, Линда ее не заметит."
            $ can_SR2_bath = False
            jump kitchen_morning1

        if not camera.selected:
            show screen kitchen_morning_notclickable
            MC "Она заперта! Интересно, кто там…?"
            MC "Если бы у меня была только шпионская камера, я мог бы использовать ее, чтобы посмотреть кто задверью!"
            $ renpy.music.stop(channel="music1", fadeout=1)
            $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
            $ can_hide_windows = False
            jump kitchen_morning1

    if not camera.selected:
        show screen kitchen_morning_notclickable
        MC "Она заперта! Интересно, кто там…?"
        MC "Если бы у меня была только шпионская камера, я мог бы использовать ее, чтобы посмотреть кто задверью!"
        jump kitchen_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
