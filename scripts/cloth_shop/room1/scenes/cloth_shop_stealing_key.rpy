image cloth_shop_stealing_key_p1 = "images/cloth_shop/room1/day/scenes/cloth_shop_stealing_key/1.jpg"
image cloth_shop_stealing_key_p2 = "images/cloth_shop/room1/day/scenes/cloth_shop_stealing_key/2.jpg"
image cloth_shop_stealing_key_p3 = "images/cloth_shop/room1/day/scenes/cloth_shop_stealing_key/3.jpg"
image cloth_shop_stealing_key_p4 = "images/cloth_shop/room1/day/scenes/cloth_shop_stealing_key/4.jpg"

label cloth_shop_stealing_key_label:
    $ can_hide_windows = True
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene cloth_shop_stealing_key_p1 with dissolve
    MC "Хм .. Давай проверим.."
    MC "Отлично! Окно все еще открыто, но я все равно не должен шуметь."
    scene cloth_shop_stealing_key_p2
    MC "Ладно ... Я внутри. Где она могла спрятать свой запасной ключ..?"
    MC "Вероятно, я должен проверить ящики."
    scene cloth_shop_stealing_key_p3
    MC "Пожалуйста, будь здесь.."
    scene cloth_shop_stealing_key_p4
    MC "Бинго! Прекрасно - с этим я могу попасть в ее спальню ночью.."
    MC "На всякий случай, конечно!"
    $ cloth_shop_window_unlock = 3
    $ inventory.add(caroline_spare_key)
    $ can_hide_windows = False
    jump map_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
