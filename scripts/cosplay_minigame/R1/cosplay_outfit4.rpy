image cosplay_outfit4_p1 = "images/cosplay_minigame/4/1.jpg"
image cosplay_outfit4_p2a = "images/cosplay_minigame/4/2a.jpg"
image cosplay_outfit4_p2b = "images/cosplay_minigame/4/2b.jpg"
image cosplay_outfit4_p2c = "images/cosplay_minigame/4/2c.jpg"
image cosplay_outfit4_p3 = "images/cosplay_minigame/4/3.jpg"
image cosplay_outfit4_p3a = "images/cosplay_minigame/4/3a.jpg"
image cosplay_outfit4_p3b = "images/cosplay_minigame/4/3b.jpg"
image cosplay_outfit4_p3c = "images/cosplay_minigame/4/3c.jpg"


label cosplay_outfit4_label:
    hide screen cloth_shop_open_screen_notclickable
    scene cosplay_outfit4_p1 with dissolve
    if cosplay_outfit4_first_time == True:
        Caroline "Я заметил это, пока я заказывал костюмы горничной от французского ритейлера."
        Caroline "Это похоже на мулен Руж."
        MC "Да, это тоже будет продано. Сколько стоит каждая из них? Это выглядит довольно дорогим материалом!"
        Caroline "Они от бутик-дизайнера, поэтому каждый полный наряд идет, чуть более $600."
        MC "$600?!"
        Caroline "И это составляет пятнадцать процентов прибыли по каждому."
        MC "Боже!"
        Caroline "Так что да, мне действительно нужно это продать! ХАХА!"
        $ cosplay_outfit4_first_time =False
        call screen outfit4_screen1
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ cosplay_unlock_switch += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        call screen cosplay_menu_score_screen
    call screen outfit4_screen1

screen outfit4_screen1:
    imagebutton:
        xpos 1679
        ypos 0
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ScoreCount.png"
    text "{size=+20}{color=#00ff00}[cosplay_score]{/color}{/size}" xpos 1832 ypos 8
    imagebutton:
        xpos 1679
        ypos 73
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/PicCount.png"
    text "{size=+20}{color=#00ff00}[cosplay_pic_count]/4{/color}{/size}" xpos 1800 ypos 78
    imagebutton:
        xpos 1680
        ypos 623
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowDown.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowDownHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_down1"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_middle1"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_up1"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_rotate1"),]


label outfit4_down1:
    scene cosplay_outfit4_p2a
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit4_p2a with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit4_label

label outfit4_middle1:
    scene cosplay_outfit4_p2b
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit4_p2b with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit4_label

label outfit4_up1:
    scene cosplay_outfit4_p2c
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit4_p2c with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit4_label

label outfit4_rotate1:
    MC "Ты можешь обернуться?"
    Caroline "Конечно."
    jump cosplay_outfit4_label2



label cosplay_outfit4_label2:
    scene cosplay_outfit4_p3 with dissolve
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ cosplay_unlock_switch += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        call screen cosplay_menu_score_screen
    call screen outfit4_screen2

screen outfit4_screen2:
    imagebutton:
        xpos 1679
        ypos 0
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ScoreCount.png"
    text "{size=+20}{color=#00ff00}[cosplay_score]{/color}{/size}" xpos 1832 ypos 8
    imagebutton:
        xpos 1679
        ypos 73
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/PicCount.png"
    text "{size=+20}{color=#00ff00}[cosplay_pic_count]/4{/color}{/size}" xpos 1800 ypos 78
    imagebutton:
        xpos 1680
        ypos 623
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowDown.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowDownHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_down2"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_middle2"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_up2"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Hide("displayTextScreen"), Jump("outfit4_rotate2"),]

label outfit4_down2:
    scene cosplay_outfit4_p3a
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit4_p3a with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit4_label2

label outfit4_middle2:
    scene cosplay_outfit4_p3b
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit4_p3b with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit4_label2

label outfit4_up2:
    scene cosplay_outfit4_p3c
    $ renpy.pause()
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit4_p3c with flash3
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit4_label2

label outfit4_rotate2:
    MC "Ты можешь обернуться?"
    Caroline "Конечно."
    jump cosplay_outfit4_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
