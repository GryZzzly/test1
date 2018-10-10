image school_intercom_p1 = "images/school/school_entrance/morning/scenes/intercom/1.jpg"
image school_intercom_p2 = "images/school/school_entrance/morning/scenes/intercom/2.jpg"
default can_school_intercom = True

label school_entrance_intercom_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    scene school_intercom_p1 with dissolve
    $ can_hide_windows = True
    $ renpy.sound.play("sfx/intercom.mp3")
    $ renpy.pause(2)
    "Внимание! Внимание!"
    scene school_intercom_p2
    $ renpy.sound.play("sfx/intercom.mp3")
    $ renpy.pause(2)
    "[player_name], пожалуйста, идите в кабинет учителя. Это срочно."
    "Повторяю - [player_name], Пожалуйста, идите в кабинет учителя! Селия ждёт тебя!"
    MC "Да? Интересно, что это может быть..."
    $ can_school_intercom = False
    $ can_hide_windows = False
    jump school_entrance_morning2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
