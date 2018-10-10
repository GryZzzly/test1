

label cloth_shop_window_unlock_label:
    hide screen map_button
    $ clickable = False
    if CR2_before_robber == False:
        show screen cloth_shop_room2_robbery_screen
    else:
        show screen cloth_shop_room2_screen_notclickable
    "Разблокировать окно?"
    window hide
    menu:
        "Да.":

            $ renpy.sound.play("sfx/window_unlock.mp3")
            $ cloth_shop_window_unlock = True
            $ clickable = True
            jump cloth_shop_room2_label
        "Нет.":
            $ clickable = True
            jump cloth_shop_room2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
