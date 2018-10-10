


label bob_work_locked_label:
    hide screen map_button
    $ clickable = False
    if day_time == 3:
        show screen bob_work_outside_E_scr
    if day_time == 4:
        show screen bob_work_outside_N_scr

    MC "Закрыто. Стойка регистрации открыта только утром и днем."
    if day_time == 3:
        hide screen bob_work_outside_E_scr
    if day_time == 4:
        hide screen bob_work_outside_N_scr
    $ clickable = True
    jump bob_work_outside_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
