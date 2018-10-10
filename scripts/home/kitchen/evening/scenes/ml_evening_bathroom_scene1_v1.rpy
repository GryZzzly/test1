image ml_evening_bathroom_scene_v1_p1 = "images/home/kitchen/evening/scenes/ml_evening_bathroom_scene_v1/1.jpg"
image ml_evening_bathroom_scene_v1_p2 = "images/home/kitchen/evening/scenes/ml_evening_bathroom_scene_v1/2.jpg"

image ml_evening_bathroom_scene2_v1_p1 = "images/home/kitchen/evening/scenes/ml_evening_bathroom_scene2_v1/1.jpg"
image ml_evening_bathroom_scene2_v1_p2 = "images/home/kitchen/evening/scenes/ml_evening_bathroom_scene2_v1/2.jpg"

screen ml_evening_bathroom_scene_v1_screen:
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/pc/cd/empty.png"
        hover "images/game_gui/pc/cd/empty.png"
        action [Hide("ml_evening_bathroom_scene_v1_screen"),Jump("kitchen_evening1")]


label ml_evening_bathroom_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button
    if ml_can_evening_bathroom_scene_v1 == False:
        show screen kitchen_evening
        show screen ml_evening_bathroom_scene_v1_screen
        MC "Я уже знаю, кто там."
        $ can_hide_windows = False
        jump kitchen_evening1
    $ renpy.music.stop(channel="music2", fadeout=1)
    $ renpy.music.play('/sfx/Sneaky Snitch.mp3', channel="music1", loop=True, fadein = 2)
    if ml_evening_bathroom_vist_scene_v1 == 1 and ml_can_evening_bathroom_scene_v1 == True:
        scene ml_evening_bathroom_scene_v1_p1 with dissolve
        $ can_hide_windows = True
        if renpy.loadable("patch.rpy"):
            MC "(Как раз вовремя! Похоже, мама собирается принять ванну!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Как раз вовремя! Похоже, что Линда собирается принять ванну!)"
        MC "(Черт... У нее лучшие бедра, которые я когда-либо видел...)"
        MC "(Ни одна девушка в моей школе даже не похожа!)"

        scene ml_evening_bathroom_scene_v1_p2
        if renpy.loadable("patch.rpy"):
            MC "(Я не могу помочь, но чувствую, это неправильно… Она моя мать, и я не должен думать о ней так.)"
        if not renpy.loadable("patch.rpy"):
            MC "(Я не могу помочь, но чувствую, что это неправильно… Она мой друг, и я не должен думать об этих вещах.)"
        MC "(С другой стороны, просто посмотрите на эту задницу. Она идеальная!)"
        MC "(Я могу почти видеть ее влагалище под той обтягивающей набедренной повязкой, которую она носит!)"
        $ ml_can_evening_bathroom_scene_v1 = False
        $ ml_evening_bathroom_vist_scene_v1 = 2
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ can_hide_windows = False
        jump kitchen_evening1
    if ml_evening_bathroom_vist_scene_v1 == 2 and ml_can_evening_bathroom_scene_v1 == True:
        scene black
        $ can_hide_windows = True
        if renpy.loadable("patch.rpy"):
            MC "(Я немного поздно вернулся. Надеюсь, я не пропустил маму в ванной!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Я немного поздновато. Я надеюсь, что я не пропустил как Линда моеться!)"

        scene ml_evening_bathroom_scene2_v1_p1 with dissolve
        MC "(Фух! Как раз вовремя!)"
        MC "(И она тоже голая! Замечательно!)"
        MC "(Интересно, как часто она занимаеться, чтобы быть в такой форме.)"

        scene ml_evening_bathroom_scene2_v1_p2
        if renpy.loadable("patch.rpy"):
            MC "(Я бы отдал свою правую руку, чтобы девочки в моей школе имели сиськи, как у мамы! Им нет равных!)"
        if not renpy.loadable("patch.rpy"):
            MC "(Я бы отдал свою правую руку, чтобы девочки в моей школе имели сиськи, как у Линды! Им нет равных!)"
        MC "(Я был бы настолько отвлечен в классе, что не было бы время на учебу. Ха-ха!)"
        MC "(Хорошо, я лучше уйду отсюда, пока не попался…)"
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
        $ ml_can_evening_bathroom_scene_v1 = False
        $ ml_evening_bathroom_scene_v1 = False
        $ can_hide_windows = False
        jump kitchen_evening1

label ml_evening_bathroom_locked_scene_v1_label:
    hide screen week_day_viewer
    hide screen time_skip_button
    hide screen day_time_viewer
    hide screen map_button

    if ml_can_evening_bathroom_scene_v1 == False:
        show screen kitchen_evening
        show screen ml_evening_bathroom_scene_v1_screen
        MC "Я уже знаю, кто там."
        $ can_hide_windows = False
        jump kitchen_evening1
    else:
        $ renpy.sound.play("sfx/door_locked.mp3")
        show screen kitchen_evening_notclickable
        MC "Заперто! Интересно, кто там…?"
        MC "Если бы у меня была камера-шпион, я мог бы ее использовать, чтобы увидеть кто за дверью!"
        hide screen kitchen_evening_notclickable
        $ can_hide_windows = False
        jump kitchen_evening1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
