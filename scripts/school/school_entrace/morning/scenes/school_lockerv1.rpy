image school_lockerv1_p1 = "images/school/school_entrance/morning/locker/1.jpg"
image school_lockerv1_p2 = "images/school/school_entrance/morning/locker/2.jpg"
image school_lockerv1_p3 = "images/school/school_entrance/morning/locker/3.jpg"

label school_lockerv1_morning_label:
    scene school_lockerv1_p1
    call screen school_lockerv1_morning_screen1

label school_open_lockerv1_morning_label:
    $ b_clickable = True
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    scene school_lockerv1_p2
    call screen school_open_lockerv1_morning_screen

label empty_envelope_pen_usev1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show screen school_open_lockerv1_morning_screen
    $ b_clickable = False
    if empty_envelope in inventory.items and not empty_envelope.selected:
        MC "I could use those pens to write that empty envelope."
        hide screen school_open_lockerv1_morning_screen
        jump school_open_lockerv1_morning_label
    if empty_envelope in inventory.items and empty_envelope.selected:
        scene school_lockerv1_p3
        hide screen school_open_lockerv1_morning_screen
        MC "(Хорошо.. Давай напишем, как мы планировали, Джуди.)"
        scene black
        $ renpy.sound.play("sfx/writing.mp3")
        $ renpy.pause(3, hard=True)
        $ can_empty_envelope_school_lockerv1 = 3
        $ inventory.drop(empty_envelope)
        $ inventory.add(envelope)
        $ b_clickable = True
        jump school_entrance_morning1
    else:
        MC "Это мои ручки."
        hide screen school_open_lockerv1_morning_screen
        jump school_open_lockerv1_morning_label
screen school_lockerv1_morning_screen1:
    key "hide_windows" action NullAction()
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/school/school_entrance/morning/locker/door_lockerv1.png"
        if b_clickable == True:
            hover "images/school/school_entrance/morning/locker/door_lockerv1_hover.png"
            hovered Show("displayTextScreen", displayText = "Открыть")
            action [Hide("displayTextScreen"),Jump("school_open_lockerv1_morning_label")]
            unhovered Hide("displayTextScreen")
    if b_clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("school_entrance_morning1")]


screen school_open_lockerv1_morning_screen:
    key "hide_windows" action NullAction()
    if can_empty_envelope_school_lockerv1 == 1 and empty_envelope.selected and empty_envelope in inventory.items:
        imagebutton:
            xpos 0
            ypos -1
            focus_mask True
            idle "images/school/school_entrance/morning/locker/penv1.png"
            if b_clickable == True:
                hover "images/school/school_entrance/morning/locker/penv1_hover.png"
                hovered Show("displayTextScreen", displayText = "Ручки")
                action [Hide("displayTextScreen"),Jump("empty_envelope_pen_usev1_label")]
                unhovered Hide("displayTextScreen")
    else:
        imagebutton:
            xpos 0
            ypos -1
            focus_mask True
            idle "images/school/school_entrance/morning/locker/penv1.png"
            if b_clickable == True:
                hover "images/school/school_entrance/morning/locker/penv1_hover.png"
                hovered Show("displayTextScreen", displayText = "Ручки")
                action [Hide("displayTextScreen"),Jump("empty_envelope_pen_usev1_label")]
                unhovered Hide("displayTextScreen")
    if b_clickable == True:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/game_gui/goback_button_idle.png"
            hover "images/game_gui/goback_button_hover.png"
            action [Jump("school_entrance_morning1")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
