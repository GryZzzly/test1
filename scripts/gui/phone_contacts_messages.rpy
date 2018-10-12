init -2 python:

    import renpy.store as store
    import renpy.exports as renpy
    from operator import attrgetter


    sms = None
    con_page = 0


default Zuri_unread_alert = True



screen contact_screen:
    key "hide_windows" action NullAction()
    zorder 102
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        action [Hide("phone_main_screen"),Hide("contact_screen")]
    imagebutton xalign 0.5 yalign 0.5 focus_mask True idle Transform("images/game_gui/phone/sms/contacts.png", zoom=.7) hover Transform("images/game_gui/phone/sms/contacts.png", zoom=.7) action NullAction()
    imagebutton xalign 0.501 yalign 0.75 focus_mask True idle Transform("images/game_gui/phone/Phone_Button_Idle.png", zoom=.7) hover Transform("images/game_gui/phone/Phone_Button_Hover.png", zoom=.7) action [Play ("sound", "sfx/phone_click2.mp3"), Show("phone_main_screen"),Hide("contact_screen")]

    $ x_c = 12
    $ y_c = 312
    $ i_c = 0
    default sorted_con = sorted(inventory.contact, key=attrgetter('name'))
    $ next_con_page = con_page + 1
    $ prev_con_page = con_page - 1
    if next_con_page > int(len(inventory.contact)/6):
        $ next_con_page = 0
    if prev_con_page < int(len(inventory.contact)/6):
        $ prev_con_page = 0
    for contact in sorted_con:
        if i_c+1 <= (con_page+1)*6 and i_c+1>con_page*6:
            $ x_c += 123
            if i_c%2==0:
                $ y_c += 106
                $ x_c = 848
            $ c_pic = Transform(contact.image_idle, zoom=.63)

            $ c_hover = Transform(contact.image_hover, zoom=.63)
            if contact.name == "Линда":
                imagebutton idle c_pic hover c_hover xpos x_c ypos y_c action [Play ("sound", "sfx/phone_click2.mp3"), SetVariable("Contact", Contact), SetVariable("Linda_unread_alert", True),Hide("contact_screen"), Show("m_from_Linda"), ] hovered [ Play ("sound", "sfx/phone_click.mp3"),]
            if contact.name == "Linda" and Linda_unread_alert == False:
                add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.7) xpos x_c ypos y_c anchor (0,0)

            if contact.name == "Сара":
                imagebutton idle c_pic hover c_hover xpos x_c ypos y_c action [Play ("sound", "sfx/phone_click2.mp3"), SetVariable("Contact", Contact),SetVariable("Sara_unread_alert", True),Hide("contact_screen"), Show("m_from_Sara")] hovered [ Play ("sound", "sfx/phone_click.mp3"),]
            if contact.name == "Sara" and Sara_unread_alert == False:
                add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.7) xpos x_c ypos y_c anchor (0,0)

            if contact.name == "Каролина":
                imagebutton idle c_pic hover c_hover xpos x_c ypos y_c action [Play ("sound", "sfx/phone_click2.mp3"), SetVariable("Contact", Contact),SetVariable("Caroline_unread_alert", True),Hide("contact_screen"),Show("m_from_Caroline")] hovered [ Play ("sound", "sfx/phone_click.mp3"),]
            if contact.name == "Каролина" and Caroline_unread_alert == False:
                add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.7) xpos x_c ypos y_c anchor (0,0)

            if contact.name == "Зури":
                imagebutton idle c_pic hover c_hover xpos x_c ypos y_c action [Play ("sound", "sfx/phone_click2.mp3"), SetVariable("Contact", Contact), SetVariable("Zuri_unread_alert", True),Hide("contact_screen"), Show("m_from_Zuri"), ] hovered [ Play ("sound", "sfx/phone_click.mp3"),]
            if contact.name == "Зури" and Zuri_unread_alert == False:
                add Transform("images/game_gui/phone/sms/Alert1.png", zoom=.7) xpos x_c ypos y_c anchor (0,0)

        $ i_c += 1
        if len(inventory.contact)>1:
            imagebutton idle Transform("images/game_gui/phone/sms/Arrow_Right.png", zoom=.7) hover Transform("images/game_gui/phone/sms/Arrow_Right_Hover.png", zoom=.7) xalign 0.559 yalign 0.69 focus_mask True action [Play ("sound", "sfx/phone_click2.mp3"), SetVariable('con_page', next_con_page), Show("contact_screen")] hovered [ Play ("sound", "sfx/phone_click.mp3"),]
            imagebutton idle Transform("images/game_gui/phone/sms/Arrow_Left.png", zoom=.7) hover Transform("images/game_gui/phone/sms/Arrow_Left_Hover.png", zoom=.7) xalign 0.439 yalign 0.69 focus_mask True action [Play ("sound", "sfx/phone_click2.mp3"), SetVariable('con_page', prev_con_page), Show("contact_screen")] hovered [ Play ("sound", "sfx/phone_click.mp3"),]



screen m_from_Linda:
    key "hide_windows" action NullAction()
    key "rollforward" action NullAction()
    key "rollback" action NullAction()
    zorder 102
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        action [Hide("phone_main_screen"),Hide("contact_screen"),Hide("m_from_Linda")]
    imagebutton xalign 0.5 yalign 0.5 focus_mask True idle Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) hover Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) action NullAction()
    imagebutton xalign 0.448 yalign 0.292 focus_mask True idle Transform("images/game_gui/phone/sms/SMSML.png", zoom=.44) hover Transform("images/game_gui/phone/sms/SMSML.png", zoom=.44) action NullAction()
    imagebutton xalign 0.501 yalign 0.75 focus_mask True idle Transform("images/game_gui/phone/Phone_Button_Idle.png", zoom=.7) hover Transform("images/game_gui/phone/Phone_Button_Hover.png", zoom=.7) action [Play ("sound", "sfx/phone_click2.mp3"), Show("phone_main_screen"),Hide("m_from_Linda")]

    frame:
        background Transform("images/game_gui/phone/sms/SMS_Selected_Reading1.png" , zoom=.7)
        align (0.498, 0.540)

        has side "c":
            area (5, 5, 250, 368)
        viewport id "vp":
            draggable True
            mousewheel True
            has vbox:
                xfill True
                at left
                spacing 10
            for sms in sms_box.sms_s:
                $ s_pic = sms.simage
                if sms.sname == "sLinda" and  sms.sphoto1==True:
                    frame:
                        style "frame_gui1"
                        imagebutton idle Transform(s_pic, zoom=.5) hover Transform(s_pic, zoom=.5) xpos 0 ypos 0 clicked [Play ("sound", "sfx/phone_click2.mp3"), Show("sms_photo_view",),SetVariable("sms", sms),] hovered [ Play ("sound", "sfx/phone_click.mp3"),]

                if sms.sname == "sLinda" and sms.sphoto1==False:
                    frame:
                        style "frame_gui1"
                        xfill True
                        text ("{size=-5}[sms.mtext]{/size}")

screen m_from_Sara:
    key "hide_windows" action NullAction()
    key "rollforward" action NullAction()
    key "rollback" action NullAction()
    zorder 102
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        action [Hide("phone_main_screen"),Hide("contact_screen"),Hide("m_from_Sara")]
    imagebutton xalign 0.5 yalign 0.5 focus_mask True idle Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) hover Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) action NullAction()
    imagebutton xalign 0.448 yalign 0.292 focus_mask True idle Transform("images/game_gui/phone/sms/SMSSara.png", zoom=.44) hover Transform("images/game_gui/phone/sms/SMSSara.png", zoom=.44) action NullAction()
    imagebutton xalign 0.501 yalign 0.75 focus_mask True idle Transform("images/game_gui/phone/Phone_Button_Idle.png", zoom=.7) hover Transform("images/game_gui/phone/Phone_Button_Hover.png", zoom=.7) action [Play ("sound", "sfx/phone_click2.mp3"), Show("phone_main_screen"),Hide("m_from_Sara")]

    frame:
        background Transform("images/game_gui/phone/sms/SMS_Selected_Reading1.png" , zoom=.7)
        align (0.498, 0.540)

        has side "c":
            area (5, 5, 250, 368)
        viewport id "vp":
            draggable True
            mousewheel True
            has vbox:
                xfill True
                at left
                spacing 10
            for sms in sms_box.sms_s:
                $ s_pic = sms.simage
                if sms.sname == "sSara" and  sms.sphoto1==True:
                    frame:
                        style "frame_gui1"
                        imagebutton idle Transform(s_pic, zoom=.5) hover Transform(s_pic, zoom=.5) xpos 0 ypos 0 clicked [Play ("sound", "sfx/phone_click2.mp3"), Show("sms_photo_view",),SetVariable("sms", sms),] hovered [ Play ("sound", "sfx/phone_click.mp3"),]

                if sms.sname == "sSara" and sms.sphoto1==False:
                    frame:
                        style "frame_gui1"
                        xfill True
                        text ("{size=-5}[sms.mtext]{/size}")
screen m_from_Caroline:
    key "hide_windows" action NullAction()
    key "rollforward" action NullAction()
    key "rollback" action NullAction()
    zorder 102
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        action [Hide("phone_main_screen"),Hide("contact_screen"),Hide("m_from_Caroline")]
    imagebutton xalign 0.5 yalign 0.5 focus_mask True idle Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) hover Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) action NullAction()
    imagebutton xalign 0.448 yalign 0.292 focus_mask True idle Transform("images/game_gui/phone/sms/SMSCaroline.png", zoom=.44) hover Transform("images/game_gui/phone/sms/SMSCaroline.png", zoom=.44) action NullAction()
    imagebutton xalign 0.501 yalign 0.75 focus_mask True idle Transform("images/game_gui/phone/Phone_Button_Idle.png", zoom=.7) hover Transform("images/game_gui/phone/Phone_Button_Hover.png", zoom=.7) action [Play ("sound", "sfx/phone_click2.mp3"), Show("phone_main_screen"),Hide("m_from_Caroline")]

    frame:
        background Transform("images/game_gui/phone/sms/SMS_Selected_Reading1.png" , zoom=.7)
        align (0.498, 0.540)

        has side "c":
            area (5, 5, 250, 368)
        viewport id "vp":
            draggable True
            mousewheel True
            has vbox:
                xfill True
                at left
                spacing 10
            for sms in sms_box.sms_s:
                $ s_pic = sms.simage
                if sms.sname == "sCaroline" and  sms.sphoto1==True:
                    frame:
                        style "frame_gui1"
                        imagebutton idle Transform(s_pic, zoom=.5) hover Transform(s_pic, zoom=.5) xpos 0 ypos 0 clicked [Play ("sound", "sfx/phone_click2.mp3"), Show("sms_photo_view",),SetVariable("sms", sms),] hovered [ Play ("sound", "sfx/phone_click.mp3"),]

                if sms.sname == "sCaroline" and sms.sphoto1==False:
                    frame:
                        style "frame_gui1"
                        xfill True
                        text ("{size=-5}[sms.mtext]{/size}")

screen m_from_Zuri:
    key "hide_windows" action NullAction()
    key "rollforward" action NullAction()
    key "rollback" action NullAction()
    zorder 102
    imagebutton:
        xpos 0
        ypos 0
        idle "images/game_gui/icons/inventory_close.png"
        hover "images/game_gui/icons/inventory_close.png"
        action [Hide("phone_main_screen"),Hide("contact_screen"),Hide("m_from_Zuri")]
    imagebutton xalign 0.5 yalign 0.5 focus_mask True idle Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) hover Transform("images/game_gui/phone/sms/SMS_Selected_Reading.png", zoom=.7) action NullAction()
    imagebutton xalign 0.448 yalign 0.292 focus_mask True idle Transform("images/game_gui/phone/sms/SMSZuri.png", zoom=.44) hover Transform("images/game_gui/phone/sms/SMSZuri.png", zoom=.44) action NullAction()
    imagebutton xalign 0.501 yalign 0.75 focus_mask True idle Transform("images/game_gui/phone/Phone_Button_Idle.png", zoom=.7) hover Transform("images/game_gui/phone/Phone_Button_Hover.png", zoom=.7) action [Play ("sound", "sfx/phone_click2.mp3"), Show("phone_main_screen"),Hide("m_from_Zuri")]

    frame:
        background Transform("images/game_gui/phone/sms/SMS_Selected_Reading1.png" , zoom=.7)
        align (0.498, 0.540)

        has side "c":
            area (5, 5, 250, 368)
        viewport id "vp":
            draggable True
            mousewheel True
            has vbox:
                xfill True
                at left
                spacing 10
            for sms in sms_box.sms_s:
                $ s_pic = sms.simage
                if sms.sname == "sZuri" and  sms.sphoto1==True:
                    frame:
                        style "frame_gui1"
                        imagebutton idle Transform(s_pic, zoom=.5) hover Transform(s_pic, zoom=.5) xpos 0 ypos 0 clicked [Play ("sound", "sfx/phone_click2.mp3"), Show("sms_photo_view",),SetVariable("sms", sms),] hovered [ Play ("sound", "sfx/phone_click.mp3"),]

                if sms.sname == "sZuri" and sms.sphoto1==False:
                    frame:
                        style "frame_gui1"
                        xfill True
                        text ("{size=-5}[sms.mtext]{/size}")

screen sms_photo_view:
    key "hide_windows" action NullAction()
    zorder 103
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle sms.sphoto
        hover sms.sphoto
        action [Hide("sms_photo_view")]
    if CR2_NS3_MCtalk == True and Caroline_unread_alert == True and can_CR2_NS3 == True:
        timer 0.1 action Show("say22")

screen new_message_incoming1:
    key "hide_windows" action NullAction()
    zorder 105

    if can_sms1_from_sara == 1 and day_time == 4:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Sara2,),addSms(sms_Sara1),]
        timer 2.25 action [SetVariable("can_sms1_from_sara",3), SetVariable("Sara_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")
    if can_sms2_from_sara == 1 and day_time == 3:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Sara3),addSms(sms_Sara4),]
        timer 2.25 action [SetVariable("can_sms2_from_sara",3), SetVariable("Sara_unread_alert", False),SetVariable("can1_sms2_from_sara",False)]
        timer 2.26 action Hide ("new_message_incoming1")
    if can_sms3_from_sara == 1 and day_time == 4:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup
        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Sara5),addSms(sms_Sara6),]

        timer 2.25 action [SetVariable("can_sms3_from_sara",3), SetVariable("Sara_unread_alert", False)]
        timer 2.26 action Hide ("sms3_from_sara")

    if sms4_sara == True and day_time == 1:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup
        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Sara7),addSms(sms_Sara8),]

        timer 2.25 action [SetVariable("sms4_sara",False), SetVariable("Sara_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")

    if sms5_sara == True and day_time == 1:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup
        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Sara9),addSms(sms_Sara10),]

        timer 2.25 action [SetVariable("sms5_sara",False), SetVariable("Sara_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")
    if sms6_sara == True and day_time == 4:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup
        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Sara11),addSms(sms_Sara12),]

        timer 2.25 action [SetVariable("sms6_sara",False), SetVariable("Sara_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")

    if sms7_sara == True and day_time == 1:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup
        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Sara13),addSms(sms_Sara14),]

        timer 2.25 action [SetVariable("sms7_sara",False), SetVariable("Sara_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")


    if can_sms1_from_ml == True and day_time == 3:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Linda1),addSms(sms_Linda2),]
        timer 2.25 action [SetVariable("can_sms1_from_ml",False), SetVariable("Linda_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")
    if can_sms2_from_ml == True and day_time == 4:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Linda3),addSms(sms_Linda4),]
        timer 2.25 action [SetVariable("can_sms2_from_ml",False), SetVariable("Linda_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")
    if can_sms3_from_ml == True and day_time == 1:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Linda5),addSms(sms_Linda6),]
        timer 2.25 action [SetVariable("can_sms3_from_ml",False), SetVariable("Linda_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")
    if sms4_ml == True and day_time == 4:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Linda7),addSms(sms_Linda8),]
        timer 2.25 action [SetVariable("sms4_ml",False), SetVariable("Linda_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")

    if sms1_fromZuri == True and day_time == 3:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Zuri2),addSms(sms_Zuri1),addContact(cZuri),]
        timer 2.25 action [SetVariable("sms1_fromZuri",False), SetVariable("Zuri_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")
    if sms2_fromZuri == True and day_time == 3:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Zuri4),addSms(sms_Zuri3),addContact(cZuri),SetVariable("zuri_inhome", True)]
        timer 2.25 action [SetVariable("sms2_fromZuri",False), SetVariable("Zuri_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")

    if sms1_fromC == True and day_time == 3:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Caroline1),addSms(sms_Caroline2)]
        timer 2.25 action [SetVariable("sms1_fromC",False), SetVariable("Caroline_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")

    if sms2_fromC == True and day_time == 4:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"),SetVariable("CR2_NS3", True), addSms(sms_Caroline3),addSms(sms_Caroline4)]
        timer 2.25 action [SetVariable("sms2_fromC",False), SetVariable("Caroline_unread_alert", False), SetVariable("CR2_NS3_MCtalk", True)]
        timer 2.26 action Hide ("new_message_incoming1")
    if sms3_fromC == True and day_time == 4:
        imagebutton:
            xpos 1600
            ypos 400
            idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
            hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup

        timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Caroline5),addSms(sms_Caroline6)]
        timer 2.25 action [SetVariable("sms3_fromC",False), SetVariable("Caroline_unread_alert", False)]
        timer 2.26 action Hide ("new_message_incoming1")


transform phone_pickup:
    xpos 1700 ypos 550
    yoffset 600
    easein 0.9 yoffset 100

screen sms3_from_sara:
    key "hide_windows" action NullAction()
    zorder 105
    imagebutton:
        xpos 1600
        ypos 400
        idle Transform("images/game_gui/phone/NewMessage.png", zoom=.7,)
        hover Transform("images/game_gui/phone/NewMessage.png", zoom=.7) at phone_pickup
    timer 0.001 action [Play("sound", "sfx/phone_vibrate.mp3"), addSms(sms_Sara5),addSms(sms_Sara6),]

    timer 2.25 action [SetVariable("can_sms3_from_sara",3), SetVariable("Sara_unread_alert", False)]
    timer 2.26 action Hide ("sms3_from_sara")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
