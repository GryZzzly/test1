image bob_office_bg = "/images/Bob_work/office/M/office.jpg"

default bob_office_locked = False

label bob_office_M1:
    if day_time == 1:
        jump bob_office_M2
    if day_time == 2:
        jump bob_office_D1


label bob_office_M2:
    hide screen displayTextScreen
    scene bob_office_bg
    $ can_map = False

    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen bob_office_M_scr



label office_leave:
    if day_time == 1:
        show screen bob_office_M_scr
    if day_time == 2:
        show screen bob_office_D_scr
    if bob_office_locked == True:
        $ clickable = False
        if renpy.loadable("patch.rpy"):
            MC "Я не могу сейчас уйти. Я должен поговорить с папой."
        else:
            MC "Я не могу сейчас уйти. Я должен поговорить с Бобом."
        $ clickable = True
        jump bob_office_M1

    if bob_safenote in inventory.items:
        $ clickable = False
        MC "Я не могу сейчас уйти. Я должен вернуть записку."
        $ clickable = True
        jump bob_office_M1
    else:
        hide screen bob_office_M_scr
        hide screen bob_office_D_scr
        $ renpy.sound.play ( "sfx/door_open.mp3", "sound")
        jump bob_reception_morning1

label bob_officelocked:
    $ clickable = False
    if day_time == 1:
        show screen bob_reception_M_scr
    if day_time == 2:
        show screen bob_reception_D_scr
    MC "Мне нужна магнитная карта, чтобы попасть в офис."
    $ clickable = True
    jump bob_reception_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
