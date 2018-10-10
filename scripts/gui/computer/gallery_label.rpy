default can_gallery_scenes_ml_unlocked = True
default can_gallery_scenes_caroline_unlocked = True
default can_gallery_scenes_celia_unlocked = True
default can_gallery_scenes_sara_unlocked = True

default CR2_rep = True
default MLR2_rep = True
default Z_rep = True
default SR2_rep = True
label gallery_label:
    if can_gallery_scenes_sara_unlocked == True and Sara_points >= 2:
        $ scenes_gallery_photos.add1("img1_sara_evening_pad_lose")
        $ scenes_gallery_photos.add1("img2_sara_evening_pad_win")
        $ scenes_gallery_photos.add1("img3_sara_night_visit_v1")
        $ scenes_gallery_photos.add1("img4_sara_botlle_game_v1")
        $ can_gallery_scenes_sara_unlocked = False
    if can_gallery_scenes_celia_unlocked == True and Celia_points >= 2:
        $ scenes_gallery_photos.add1("img5_celia_toilet_kiss_v1")
        $ scenes_gallery_photos.add1("img6_celia_toilet_fuck_v1")
        $ scenes_gallery_photos.add1("img7_celia_vibrator_classroom_v1")
        $ can_gallery_scenes_celia_unlocked = False
    if can_gallery_scenes_caroline_unlocked == True and Caroline_points >= 2:
        $ scenes_gallery_photos.add1("img8_caroline_ass_cosplay_v1")
        $ scenes_gallery_photos.add1("img9_violet_blowjob_v1")
        $ scenes_gallery_photos.add1("img10_caroline_visit_bjfjhj_v1")
        $ can_gallery_scenes_caroline_unlocked = False
    if can_gallery_scenes_ml_unlocked == True and ml_points >= 2:
        $ scenes_gallery_photos.add1("img11_mom_car_v1")
        $ scenes_gallery_photos.add1("img12_mom_work_hj_v1")
        $ scenes_gallery_photos.add1("img13_ml_room_fj_v1")
        $ can_gallery_scenes_ml_unlocked = False

    if CR2_rep == True and Caroline_points >= 3:
        $ scenes_gallery_photos.add1("img17_CR2_AS1_rep")
        $ scenes_gallery_photos.add1("img18_CR2_AS2_rep")
        $ scenes_gallery_photos.add1("img19_CR2_NS2_rep")
        $ CR2_rep = False

    if MLR2_rep == True and ml_points >= 3:
        $ scenes_gallery_photos.add1("img14_MLR2_ES3_rep")
        $ scenes_gallery_photos.add1("img15_MLR2_NS2_rep")
        $ scenes_gallery_photos.add1("img16_MLR2_weekend_rep")
        $ MLR2_rep = False
    if Z_rep == True and Z_points >= 2:
        $ scenes_gallery_photos.add1("img20_Z_ES2_rep")
        $ scenes_gallery_photos.add1("img21_Z_ES3_rep")
        $ scenes_gallery_photos.add1("img22_Z_ES4_rep")
        $ Z_rep = False

    if SR2_rep == True and Sara_points >=3:
        $ scenes_gallery_photos.add1("img23_SR2_NS2_rep")
        $ scenes_gallery_photos.add1("img24_SR2_ES1_rep")
        $ scenes_gallery_photos.add1("img25_SR2_NS3_rep")
        $ scenes_gallery_photos.add1("img26_SR2_NS4_rep")
        $ SR2_rep = False
    scene main_deskop
    call screen scenes_gallery
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
