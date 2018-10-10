
label caroline_room_locked_label:
    show screen corridor_night_notclickable
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if caroline_door_locked_visit == 1:
        MC "Закрыто... Я думаю, что у нее есть запасной ключ!"
        $ caroline_door_locked_visit = 2
        $ caroline_can_door_locked = False
        jump corridor_night1
    if caroline_can_door_locked == False and caroline_door_locked_visit == 2:
        MC "Закрыто... Я думаю, что у нее есть запасной ключ!"
        jump corridor_night1
    if caroline_can_door_locked == True and caroline_door_locked_visit == 2:
        MC "Она заперта так же, как и раньше! Насколько я помню, в магазине должен быть запасной ключ !"
        jump corridor_night1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
