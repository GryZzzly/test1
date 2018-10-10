image Table_morning_Classroom_v1_desk_p1 = "images/school/classroom2/day/scenes/Table_Classroom_v1/RenPy1.png"

label Table_morning_Classroom_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    show Table_morning_Classroom_v1_desk_p1
    show celia_school_morning_scene1v1_celia
    if celia_school_morning_scene1bv1 == 0:
        MC "Я не могу рыться в ее стол, пока она тут."
        jump classroom2_morning2
    else:
        MC "Я не могу рыться в ее стол, пока она тут."
        jump classroom2_morning2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
