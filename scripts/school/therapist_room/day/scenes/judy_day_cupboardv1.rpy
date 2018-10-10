image judy_cupboardv1_p1 = "images/school/therapist_room/morning/scenes/judy_scene1_v1/cupboard1a.jpg"
label judy_day_cupboardv1_label:
    scene judy_cupboardv1_p1
    call screen judy_day_cupboardv1_screen

label judy_day_empty_envelopev1_label:
    $ inventory.add(empty_envelope)
    $ can_envelope_from_Judy_v1 = 3
    $ can_empty_envelope_school_lockerv1 = 1
    MC "Отлично, теперь мне нужна только ручка."
    MC "Я думаю, у меня есть несколько в моем шкафчике в школьном коридоре."
    jump judy_day_cupboardv1_label




screen judy_day_cupboardv1_screen:
    key "hide_windows" action NullAction()
    if can_envelope_from_Judy_v1 == 1:
        imagebutton:
            xpos 0
            ypos 0
            focus_mask True
            idle "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_envelopeb1_v1.png"
            hover "images/school/therapist_room/morning/scenes/judy_scene1_v1/judy_envelopeb1_v1_hover.png"
            action [Hide("displayTextScreen"),Jump("judy_day_empty_envelopev1_label")]
            hovered Show("displayTextScreen", displayText = "Пустой конверт")
            unhovered Hide("displayTextScreen")

    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        idle "images/game_gui/goback_button_idle.png"
        hover "images/game_gui/goback_button_hover.png"
        action [Jump("therapist_room_day1")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
