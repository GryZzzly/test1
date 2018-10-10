


default SR2_MS1 = True
default SR2_MS2 = False
default can_SR2_MS2 = False
default SR2_grounded = False
default SR2_AS1 = True
default SR2_AS2 = False
default can_SR2_AS1 = True
default can_SR2_AS2 = True
default SR2_NS1 = False
default SR2_AS3 = False
default can_SR2_AS3 = True
default SR2_NS2 = False
default SR2_AS3_v_loop = False
default SR2_AS4 = False
default SR2_NS2_foot_ch = False
default SR2_NS2_blow_ch = False
default can_SR2_AS4 = True
default SR2_ES1 = False
default SR2_AS5 = False
default can_SR2_AS5 = True
default SR2_NS3 = False
default SR2_AS6 = False
default can_SR2_AS6 = True
default SR2_NS4 = False
default S_N_inbed = True
default SR2_bath = False
default can_SR2_bath = True


label money_less10:
    if day_time == 1:
        show screen mc_room_morning_notclickable

    if day_time == 2:
        show screen mc_room_day_notclickable

    if day_time == 3:
        show screen mc_room_evening_notclickable

    if day_time == 4:
        show screen mc_room_night_notclickable
    $ inventory.earn(10)
    MC "+10$"
    jump mc_room_morning1



label sleeping_after_scene:
    $ can_ml_work_day_scene1 = True
    $ can_school_intercom = True
    $ next_day = True
    $ next_day_sister_nerdy_scene4_v1 = True
    $ can_sis_nerdy_school_scene1_v1 = True
    $ can2_sis_nerdy_school_scene1_v1 = True
    $ can_sis_nerdy_evening_scene1_v1 = True
    $ can_sis_nerdy_night_sleeping1_v1 = True
    $ can_lily_work_in_progress = True
    $ sara_door_open = True
    $ can_celia_school_morning_scene1v1 = True
    $ ml_can_salon_morning_scene = True
    $ ml_can_salon_morning_scene2 = True
    $ ml_can_salon_morning_scene_dish_wash = False
    $ ml_can_kitchen_morning_scene4 = True
    $ ml_can_bedroom_morning_scene5 = True
    $ ml_can_evening_bathroom_scene_v1 = True
    $ ml_can_ml_and_f_bedroom_night_scene_v1 = True
    $ d__can_ml_and_f_bedroom_mornig_scene = True
    $ caroline_can_room_morning_scenes = True
    $ caroline_can_door_locked = True
    $ caroline_room_can_night_scene1 = True
    $ caroline_salon_can_evening_scene1 = True
    $ caroline_mc_room_can_evening_scene3 = True
    $ can_sara_scene3_v1 = True
    $ can_caroline_morning_scene4_after = False
    $ can_toilet_after_sara_scene4_1 = True
    $ can_ml_work_day_scene2 = True
    $ can_celia_morning_school_work_in_pr = True

    if can_CR2_MS1 == False:
        $ CR2_MS1  = False

    if can_CR2_MS2 == False:
        $ CR2_MS2  = False
        $ CR2_MS3 = True
        $ can_CR2_MS2 = True

    if can_CR2_MS3a == True:
        $ CR2_MS3a = True
        $ can_CR2_MS3a = False

    if can_CR2_ES1_day2 == True and CR2_ES1_day2_firsttime == True:
        $ CR2_ES1_day = 2

    if can_CR2_ES1_day3 == True and CR2_ES1_day3_firsttime == True:
        $ CR2_ES1_day = 3

    if can_CR2_ES2_day2 == True and CR2_ES2_day2_firsttime == True:
        $ CR2_ES2_day = 2

    if can_CR2_ES2_day3 == True and CR2_ES2_day3_firsttime == True:
        $ CR2_ES2_day = 3

    if CR2_NS3 == True:
        $ CR2_NS3 = False

    $ can_Bob_work_minigame = True
    $ can_CR2_ES2 = True
    $ can_CR2_ES1 = True
    $ can_MLR2_MS1_talk = True
    $ can_MLR2_MS1_kiss = True
    $ can_ml_workR2 = True
    $ can_MLR2_ES2 = True
    $ MLR2_Sleep = True
    $ can_B2_AS1_day = True
    $ MLR2_can_MS1 = True
    if can_Zv2_MS2_q == True and can2_Zv2_MS2_q == True:

        $ Zv2_MS2_q5 = True
        $ Zv2_MS2_q6 = True
        $ Zv2_MS2_q7 = True
        $ can2_Zv2_MS2_q = False
    if Zv2_ES4 == 1:
        $ Zv2_ES4_counter += 1
        if Zv2_ES4_counter == 3:
            $ Zv2_ES4 = True
            $ Bobv2_MS1_q5 = True
            if Zv2_lie_counter > 1:
                $ sms1_fromZuri = True
                $ company_profit = 2
            if Zv2_true_counter > 1:
                $ sms2_fromZuri = True
                $ company_profit = 1

    $ can_SR2_MS2 = True
    $ SR2_bath = False
    if celia_school_morning_scene2v1 == 1 and can1_celia_school_morning_scene2v1 == True:
        $ can1_celia_school_morning_scene2v1 = False
        $ celia_school_morning_scene1v1 = 1
        $ celia_school_morning_scene2v1 = 0
    if celia_school_morning_scene2v1 == 1:
        $ can1_celia_school_morning_scene2v1 = True
        $ can_school_intercom = False
        $ can_celia_morning_school_work_in_pr = False
    if week_day == 1:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 2:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 3:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 4:
        $ week_day += 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 5:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 6:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
    if week_day == 7:
        $ week_day = 1
        $ day_time = 1
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        $ renpy.hide("mc_sleep_night_bed", layer="screens")
        $ renpy.hide("mc_sleep_night", layer="screens")
        $ renpy.hide("ml_mc_room_night_sleeping_p1", layer="screens")
        hide screen mc_room_night_notclickable
        if caroline_mc_room_moenig_scene5 == True:
            $ day_time = 2
            jump caroline_mc_room_morning_scene5_label
        if Sara_points == 2 and SR2_swimming_card == True:
            jump SR2_swimming_card_label
        else:
            jump mc_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
