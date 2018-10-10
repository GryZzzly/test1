image Z_ES1_bg = "images/Zuri_home/outside/E/scenes/Z_ES1/bg.jpg"

default zuri_inhome = True
label zuri_home_E_label:
    $ can_hide_windows = False
    hide screen displayTextScreen
    scene Z_ES1_bg
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    call screen zuri_home_E_scr


label zuri_inhome_E_label:
    $ can_hide_windows = False
    $ clickable = False
    show screen zuri_home_E_scr
    Zuri "Я сейчас занята., [player_name]"
    $ clickable = True
    jump zuri_home_E_label


label zuri_home_E_label2:
    show screen week_day_viewer
    show screen time_skip_button
    show screen day_time_viewer
    show screen map_button
    show screen new_message_incoming1
    hide screen displayTextScreen
    scene Z_ES1_bg
    show screen zuri_home_E_scr
    $ can_hide_windows = False
    $ clickable = False
    MC "Должен ли я сидеть на диване, как хочет Зури, или я должен попробовать поговорить с ней?"
    $ clickable = True
    jump zuri_home_E_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
