

label CR2_minigame_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene caroline_cloth_shop_afternoon_scene1_p1
    $ can_hide_windows = True
    Caroline "Привет снова, [player_name]. Вернулся, чтобы помочь мне с несколькими косплейными фотосессиями?"
    if CR2_CSfirstvisit == True:
        MC "Конечно, Кэролайн! Что у тебя есть на этот раз?"

        scene caroline_cloth_shop_afternoon_scene1_p3

        Caroline "У меня есть реально классные вещи. Дайте мне знать, когда ты будеш готов."
        Caroline "У меня сильное чувство, что тебе это действительно понравится."
        $ CR2_CSfirstvisit = False
    menu:
        "Конечно! Мы можем начать.":
            $ can_hide_windows = False
            jump cosplay_menu_label
        "Не сейчас.":
            $ can_hide_windows = False
            jump cloth_shop_open_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
