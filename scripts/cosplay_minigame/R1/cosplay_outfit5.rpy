image cosplay_outfit5_p1 = "images/cosplay_minigame/5/1.jpg"
image cosplay_outfit5_p2a = "images/cosplay_minigame/5/2a.jpg"
image cosplay_outfit5_p2b = "images/cosplay_minigame/5/2b.jpg"
image cosplay_outfit5_p2c = "images/cosplay_minigame/5/2c.jpg"
image cosplay_outfit5_p3 = "images/cosplay_minigame/5/3.jpg"
image cosplay_outfit5_p3a = "images/cosplay_minigame/5/3a.jpg"
image cosplay_outfit5_p3b = "images/cosplay_minigame/5/3b.jpg"
image cosplay_outfit5_p3c = "images/cosplay_minigame/5/3c.jpg"


label cosplay_outfit5_label:
    hide screen cloth_shop_open_screen_notclickable
    if cosplay_outfit5_first_time == True:
        scene caroline_cloth_shop_afternoon_scene1_p4a with dissolve
        Caroline "Мм... Я сейчас пойду переодеться. Но…"
        MC "Ты в порядке, Кэролайн?"
        Caroline "Да, это просто... Этот наряд довольно..."
        Caroline "Я не думаю, что он слишком открытый, чтобы смотреть."
        MC "Расслабься-я не возражаю. Это только для фото сессии."
        Caroline "Ты уверена?"
        MC "Абсолютно!"

        scene cosplay_outfit5_p1
        Caroline "Я с гордостью представляю, фиолетовый кролик!"
        Caroline "Она Волшебная девушка и гордый борец за правду и справедливость!"
        MC "Теперь это интересный костюм!"
        Caroline "Еще один дорогой - мне пришлось импортировать их из Японии."
        Caroline "Я пытаюсь покрыть столько различных ниш рынка, сколько я могу - и непристойная супергероиня - та, которая не была затронута."
        MC "Он отлично выглядит на тебе! Я уверен, что они будут продавать как горячие пирожки!"
        Caroline "Все, спасибо!"
        $ cosplay_outfit5_first_time = False
        $ caroline_after_cosplay_outfit5 = True
        call screen outfit5_screen1
    scene cosplay_outfit5_p1 with dissolve
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ cosplay_unlock_switch += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        call screen cosplay_menu_score_screen
    call screen outfit5_screen1

screen outfit5_screen1:
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
        action [Hide("displayTextScreen"), Jump("outfit5_down1"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit5_middle1"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit5_up1"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Hide("displayTextScreen"), Jump("outfit5_rotate1"),]


label outfit5_down1:
    scene cosplay_outfit5_p2a
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit5_p2a with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit5_label

label outfit5_middle1:
    scene cosplay_outfit5_p2b
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit5_p2b with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit5_label

label outfit5_up1:
    scene cosplay_outfit5_p2c
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit5_p2c with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit5_label

label outfit5_rotate1:
    MC "Ты можешь обернуться?"
    Caroline "Конечно."
    jump cosplay_outfit5_label2



label cosplay_outfit5_label2:
    scene cosplay_outfit5_p3 with dissolve
    if cosplay_pic_count == 4:
        $ cosplay_score1 = cosplay_score
        $ cosplay_unlock_switch += 1
        $ cosplay_score = cosplay_score / 2
        $ cosplay_pic_count = 0
        call screen cosplay_menu_score_screen
    call screen outfit5_screen2

screen outfit5_screen2:
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
        action [Hide("displayTextScreen"), Jump("outfit5_down2"),]
    imagebutton:
        xpos 1680
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddle.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowMiddleHover.png"
        action [Hide("displayTextScreen"), Jump("outfit5_middle2"),]
    imagebutton:
        xpos 1680
        ypos 353
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUp.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/ArrowUpHover.png"
        action [Hide("displayTextScreen"), Jump("outfit5_up2"),]

    imagebutton:
        xpos 1808
        ypos 488
        focus_mask True
        idle "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/Rotate.png"
        hover "images/cosplay_minigame/HUD_Cosplay/CosplayMinigame/RotateHover.png"
        action [Hide("displayTextScreen"), Jump("outfit5_rotate2"),]

label outfit5_down2:
    scene cosplay_outfit5_p3a
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit5_p3a with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit5_label2

label outfit5_middle2:
    scene cosplay_outfit5_p3b
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit5_p3b with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit5_label2

label outfit5_up2:
    scene cosplay_outfit5_p3c
    $ cosplay_score_add = renpy.random.choice( [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    $ cosplay_score = cosplay_score_add + cosplay_score
    $ renpy.pause()
    $ renpy.sound.play('/sfx/photo_take.wav', loop=False)
    scene cosplay_outfit5_p3c with flash3
    $ cosplay_score_add = 0
    $ cosplay_pic_count += 1
    $ renpy.pause(2)
    jump cosplay_outfit5_label2

label outfit5_rotate2:
    MC "Ты можешь обернуться?"
    Caroline "Конечно."
    jump cosplay_outfit5_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
