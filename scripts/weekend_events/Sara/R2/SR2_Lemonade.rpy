image SR2_weekend_lemonade_p1 = "images/Weekend_Events/Sara/R2/Lemonade/1.jpg"
image SR2_weekend_lemonade_p2 = "images/Weekend_Events/Sara/R2/Lemonade/2.jpg"
image SR2_weekend_lemonade_p3 = "images/Weekend_Events/Sara/R2/Lemonade/3.jpg"
image SR2_weekend_lemonade_p4 = "images/Weekend_Events/Sara/R2/Lemonade/4.jpg"
image SR2_weekend_lemonade_p5 = "images/Weekend_Events/Sara/R2/Lemonade/5.jpg"
image SR2_weekend_lemonade_p6 = "images/Weekend_Events/Sara/R2/Lemonade/6.jpg"
image SR2_weekend_lemonade_p7 = "images/Weekend_Events/Sara/R2/Lemonade/7.jpg"

label SR2_Lemonade_label:
    if SR2_after_lemonade == True:
        show screen swimming_poll_scr
        $ can_hide_windows = False
        $ clickable = False
        MC "Мы уже были там."
        $ music_continue = False

        $ clickable = True
        jump swimming_poll_label
    else:
        hide screen week_day_viewer
        hide screen time_skip_button
        hide screen day_time_viewer
        hide screen map_button
        $ renpy.music.stop(channel="music2", fadeout=1)
        $ renpy.music.play('/sfx/Hackbeat.mp3', channel="music1", loop=True, fadein = 2)
        scene SR2_weekend_swimming_pool_p2
        $ can_hide_windows = True
        MC "Если подумать, я на самом деле очень хочу пить."
        MC "Ты хочешь что-нибудь выпить??"
        Sara "Конечно! На другой стороне комплекса стоит лимонад.."
        MC "Круто! пойдем."

        scene SR2_weekend_lemonade_p1

        MC "Хорошая идея, Сара. У меня не было приличного лимонада несколько месяцев.."
        Sara "Да, я был здесь со своими друзьями, когда был моложе. Это действительно хорошо!"
        Sara "Эй, когда ты в последний раз ходил в бассейн?"
        MC "Черт... много лет назад? Я даже не могу вспомнить."
        MC "Все, что я знаю наверняка, это то, что в последний раз, когда я был там, у меня не было великолепной девушки, сидящей напротив меня, в симпатичном купальнике."

        scene SR2_weekend_lemonade_p2

        Sara "Хе-хе ... прекрати! Ты заставишь меня краснеть.."
        Sara "И разве не ты сказал, чтобы прекратить флиртовать, на случай, если нас поймают??"
        MC "Расслабься. Здесь больше никого нет. Мы будем в порядке."
        jump lemonade_menu

label lemonade_menu:
    scene SR2_weekend_lemonade_p2
    window hide
    menu:
        "Могу ли я поговорить с тобой о том, что случилось с Лили??" if menu_q1 == True:
            scene SR2_weekend_lemonade_p1

            MC "На самом деле, Сара, можем ли мы поговорить о том, что случилось с Лили в твоей спальне на днях?"

            scene SR2_weekend_lemonade_p4

            Sara "Что?"
            MC "Ты бросила бутылку через всю комнату. Было совершенно ясно, что что-то, что мы сделали, разозлило тебя."

            scene SR2_weekend_lemonade_p3

            Sara "Я ... …."
            MC "На самом деле, если ты чувствуешь себя слишком взволнованной, не волнуйтесь. Мы можем поговорить о чем-то другом."
            Sara "Нет, все в порядке.."
            Sara "Думаю, я просто не могла смириться с мыслью, что ты с ней. Может, я и не так выгляжу, но я могу очень ... ревновать."
            MC "А? Причина?"

            scene SR2_weekend_lemonade_p4

            Sara "Почему?! Просто посмотри на них с их идеальными золотистыми светлыми волосами и их большой грудью."
            Sara "И взгляни на меня. Что у меня есть? Чашка, тусклые каштановые волосы и веснушки."

            scene SR2_weekend_lemonade_p3

            Sara "Я знаю, что это между нами не будет длиться вечно.."
            Sara "Когда-нибудь ты перейдешь к одной из этих здоровенных блондинистых дурочек. И тогда ты забудешь о простом маленьком человеке, как я."
            MC "(Черт... я никогда не понимал, что у нее проблемы с уверенностью в себе. Это еще одна причина ее грубой чрезмерной реакции на то, что Лили целует меня.)"
            MC "Сара ... ты не простая.."
            window hide
            menu:
                "Комплимент ее личности.":
                    scene SR2_weekend_lemonade_p3

                    MC "В жизни есть нечто большее, чем внешность. Большинство из тех пустышек, о которых ты говоришь, ужасные личности."
                    MC "Ты милая, добрая и очень заботливая. Я не изменил бы тебе."
                    Sara "… Благодарю. Они все еще красивее меня, - и, похоже, надо что-то думать."
                    $ menu_q1 = False
                    if menu_q1 == False and menu_q2 == False:
                        jump after_lemonade_menu
                    else:
                        jump lemonade_menu
                "Комплимент ее груди.":

                    scene SR2_weekend_lemonade_p3

                    MC "Я не знаю, почему ты так беспокоишься о размере своей груди."
                    Sara "Они крошечные. Почему ты думаешь, я ношу купальник, а не бикини?"
                    Sara "Я не имею ничего, чтобы показать."
                    MC "О чем ты вообще говоришь? Твоя грудь потрясающая.!"
                    MC "Некоторые ребята, любят большие сиськи."

                    scene SR2_weekend_lemonade_p4

                    MC "Другие парни любят маленькие сиськи; и твои чертовски восхитительны."
                    MC "Кроме того, более мелкие груди, как правило, имеют более чувствительные соски."
                    Sara "[player_name]!"
                    MC "Это просто факт! ха-ха!"

                    scene SR2_weekend_lemonade_p2

                    Sara "Ну ... может быть, когда-нибудь мы сможем попробовать твою небольшую теорию чувствительности груди."
                    MC "Я с нетерпением жду."

                    $ menu_q1 = False
                    if menu_q1 == False and menu_q2 == False:
                        jump after_lemonade_menu
                    else:
                        jump lemonade_menu
                "Комплимент ее глазам.":

                    scene SR2_weekend_lemonade_p3

                    MC "Сара, посмотри на меня."
                    Sara "Хмм?"

                    scene SR2_weekend_lemonade_p1

                    MC "Они абсолютно идеальны."
                    Sara "Не ври. Я всегда хотела чуть больше."
                    MC "Я не говорю о твоей груди. Я говорю о твоих глазах.."

                    scene SR2_weekend_lemonade_p4

                    Sara "Что?"
                    MC "Это самый потрясающий оттенок изумрудно-зеленого."
                    MC "Я думаю, что ты так сосредотачиваешься на тех частях себя, которые тебе не нравятся, что ты не понимаешь, насколько удивительны другие части тебя на самом деле."
                    MC "У тебя самые красивые ирисы, которые я видел."
                    Sara "Спасибо, [player_name]…"
                    $ menu_q1 = False
                    if menu_q1 == False and menu_q2 == False:
                        jump after_lemonade_menu
                    else:
                        jump lemonade_menu

        "Мы можем поговорить о том минете, который ты мне сделал?" if menu_q2 == True:
            scene SR2_weekend_lemonade_p1

            MC "Мы можем поговорить о том минете, который ты мне сделал?"

            scene SR2_weekend_lemonade_p5

            Sara "Мы на публике! Замолчи!"
            Sara "Что делать, если кто-то из школы услышит нас?!"
            Sara "Это было бы еще более неловко, чем когда ты пытался пригласить своего учителя!"
            MC "Можно попробовать не говорить об этом?"
            Sara "Хаха! Окей..."

            scene SR2_weekend_lemonade_p2

            Sara "Мы можем поговорить о минете в привате когда-нибудь."
            MC "Я с нетерпением жду этого."
            $ menu_q2 = False
            if menu_q1 == False and menu_q2 == False:
                jump after_lemonade_menu
            else:
                jump lemonade_menu

label after_lemonade_menu:
    scene SR2_weekend_lemonade_p5

    Sara "В любом случае! Мы провели здесь достаточно времени."
    Sara "Я догоню тебя, допивай!"
    MC "Конечно! Готово."

    scene SR2_weekend_lemonade_p6

    Sara "*SHLURP SHLURP*"
    Sara "*ГЛОТОК ГЛОТОК*"

    scene SR2_weekend_lemonade_p7

    Sara "Я выигрываю!"
    MC "(Ебена мать! У меня едва была возможность принести солому ко рту.)"
    MC "Отлично-ты выиграла! "
    Sara "Ура! Я дам тебе закончить, а потом мы сможем отправиться куда-нибудь, когда ты будешь готов."
    $ SR2_after_lemonade = True
    $ can_hide_windows = False
    jump swimming_poll_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
