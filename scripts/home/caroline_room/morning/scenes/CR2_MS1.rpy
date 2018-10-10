image CR2_MS1_p1 = "/images/home/caroline_room/morning/scenes/CR2_MS1/1.jpg"
image CR2_MS1_p2 = "/images/home/caroline_room/morning/scenes/CR2_MS1/2.jpg"
image CR2_MS1_p3 = "/images/home/caroline_room/morning/scenes/CR2_MS1/3.jpg"
image CR2_MS1_p4a = "/images/home/caroline_room/morning/scenes/CR2_MS1/4a.jpg"
image CR2_MS1_p4b = "/images/home/caroline_room/morning/scenes/CR2_MS1/4b.jpg"
image CR2_MS1_p4c = "/images/home/caroline_room/morning/scenes/CR2_MS1/4c.jpg"
image CR2_MS1_p5a = "/images/home/caroline_room/morning/scenes/CR2_MS1/5a.jpg"
image CR2_MS1_p5b = "/images/home/caroline_room/morning/scenes/CR2_MS1/5b.jpg"
image CR2_MS1_p5c = "/images/home/caroline_room/morning/scenes/CR2_MS1/5c.jpg"
image CR2_MS1_p5d = "/images/home/caroline_room/morning/scenes/CR2_MS1/5d.jpg"


label CR2_MS1_label:
    if can_CR2_MS1 == False:
        show screen caroline_room_morning
        $ clickable = False
        MC "Я уже говорил с ней."
        $ clickable = True
        jump caroline_room_morning1
    else:
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        scene CR2_MS1_p1 with dissolve
        $ can_hide_windows = True
        MC "(Там есть Кэролайн, ее нос похоронен в книге, как всегда!)"
        MC "(Она всегда была умной!)"
        MC "Эй, Кэролайн! Что происходит?"

        scene CR2_MS1_p2

        Caroline "Ой! Здравствуй, [player_name]. Я не слышала, как ты пришел."
        Caroline "Не так много - просто перерыв на работе. Теперь, когда я на самом деле получаю прибыль, я должна ДЕЙСТВИТЕЛЬНО подумать о том, чтобы сообщить о моих доходах правительству."
        MC "Ух, звучит скучно!"
        Caroline "Это действительно так! Вот почему я беру заслуженный отдых."

        scene CR2_MS1_p3

        MC "Что за книга?"
        Caroline "Это новелла. Девочка приходит на работу на завод в Детройте, но вскоре оказывается соблазнены мускулистым руководителем."
        MC "Это звучит как настоящая пьеса..."


        scene CR2_MS1_p4a

        Caroline "Я слышу сарказм в твоем голосе. Это типичный массовый мусор, но он меня развлекает."
        MC "Там много эротических сцен?"
        scene CR2_MS1_p4b

        Caroline "Хе-хе ... Поверь, ты не должен задавать такие вопросы."
        MC "Эй, я серьезно!"
        Caroline "Конечно, роман есть роман."

        scene CR2_MS1_p4c

        Caroline "У него даже есть предупреждение «Не для детей»."
        Caroline "Я имею в виду, я на восьмой главе, и я уже видела главного героя в таких сценах."
        Caroline "И две из них, происходят в ее заднице!"
        MC "Я никогда не думал, что есть такая грязная литература!"

        scene CR2_MS1_p4b

        Caroline "Ты должен забрать пару книг. И можешь наслаждаться дешевой грязью."
        $ renpy.music.stop(channel="music1", fadeout=1)
        $ renpy.music.play('/sfx/Deadly_Roulette.mp3', channel="music2", loop=True, fadein = 2)
        menu:
            "Взять Кэролайн за задницу.":
                scene CR2_MS1_p5a

                MC "(Я думаю, что теперь буду пощупывать ее задницу. Мы заключили эту сделку, и Кэролайн должна уделять мне БОЛЬШЭ времени,которое я потратил чтобы ее магазин мог работать!)"
                MC "(Я уверен, что она не будет против быстрого выдавливания. Что самое худшее, что может случиться?)"
                MC "(К тому же, она сидит в трусах. Она, вероятно, ожидает, что это произойдет...?)"

                scene CR2_MS1_p5b

                MC "(Мягкий и теплый! Точно так же, как я себе это помню!)"
                Caroline "Эй! Что ты делаешь?"
                MC "Помнишь о договоре?"

                scene CR2_MS1_p5c
                if renpy.loadable("patch.rpy"):
                    Caroline "Да, но что, если мама войдет прямо сейчас."
                    Caroline "Или, не дай бог, Сара! Что она подумает, увидев, что ее брат лапает задницу ее сестры?"
                else:
                    Caroline "Да, но что, если Линда войдет прямо сейчас."
                    Caroline "Или, не дай Бог, Сара! ЧЧто она подумает, если увидит тебя трогающи мою попку?"
                MC "Но..."

                scene CR2_MS1_p5d

                Caroline "Мы можем дурачиться на моей работе, но все, что дома слишком рискованно."
                if renpy.loadable("patch.rpy"):
                    Caroline "Я не против на нашей сделки - у нас есть хорошее занятие. Давай не рисковать, чтобы мама или папа не узнали. Окей?"
                else:
                    Caroline "Я не против на нашей сделки - у нас есть хорошее занятие. Давай не рисковать, чтобы Боб или Линда не узнали. Окей?"
                MC "Да, я думаю, ты права, Кэролайн.."
                Caroline "Хорошо. Давай просто притворимся, что этого не было. Хорошо?"
                MC "Я понимаю."
                $ can_CR2_MS1 = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump caroline_room_morning1
            "Не рисковать брать Кэролайн за задницу.":

                scene CR2_MS1_p5a

                MC "(Это не стоит риска, хватать ее попку прямо сейчас.)"
                if renpy.loadable("patch.rpy"):
                    MC "(Это могло бы смутить ее - плюс мама или папа, или Сара могла зайти!)"
                    MC "(ЛЮБОЙ из них будет волноваться, если увидят, как я пощупываю задницу Кэролайн. Мы должны, вероятно, сохранить нашу отношения на рабочем месте.)"
                else:
                    MC "(Это могло бы ее разозлить - Плюс, мама или папа, или даже Сара могла просто зайти!)"
                    MC "(ЛЮБОЙ из них будет волноваться, если увидят, как я пощупываю задницу Кэролайн. Мы должны, вероятно, сохранить нашу отношения на рабочем месте.)"
                $ can_CR2_MS1 = False
                $ renpy.music.stop(channel="music1", fadeout=1)
                $ renpy.music.play('/sfx/Sock Hop.mp3', channel="music2", loop=True, fadein = 2)
                $ can_hide_windows = False
                jump caroline_room_morning1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
