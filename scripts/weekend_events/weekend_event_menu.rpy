


label weekend_event_menu_label:
    $ can_hide_windows = False
    if renpy.loadable("patch.rpy"):
        $ Mom_name = "Мама"
    else:
        $ Mom_name = "Линда"
    menu:

        "{color=#00ff00}Пойти с Сарой в бассейн.{/color}" if SR2_weekend_swimming_pool == True and week_day == 5:
            $ SR2_after_waterslide = False
            $ SR2_after_swimming = False
            $ SR2_after_sunbed = False
            $ SR2_after_lemonade = False
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            jump SR2_weekend_swimming_pool_label

        "(Сара выходные события.) (disabled)" if SR2_weekend_swimming_pool == False and week_day == 5:
            jump day_time_changer

        "([Mom_name] выходные.) (disabled)" if MLR2_weekend_event == False and week_day == 5:
            jump day_time_changer
        "{color=#f00}{alpha=0.4}Заблокировано: отдых с([Mom_name].){/alpha}{/color} (disabled)" if MLR2_weekend_event == True and not red_wine in inventory.items and week_day == 5:
            jump day_time_changer

        "{color=#00ff00}[Mom_name] выходные.{/color}" if MLR2_weekend_event == True and red_wine in inventory.items and week_day == 5:
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            $ renpy.hide("mc_sleep_night_bed", layer="screens")
            $ renpy.hide("mc_sleep_night", layer="screens")
            $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
            jump MLR2_weekend_label
        "Назад.":

            jump day_time_changer
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
