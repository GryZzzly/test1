init python:

    def MaxScale2(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight
        
        if xscale > yscale:
            maxscale2 = xscale
        else:
            maxscale2 = yscale
        
        return im.FactorScale(img, maxscale2, maxscale2)

    def MinScale2(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight
        
        if xscale < yscale:
            minscale2 = xscale
        else:
            minscale2 = yscale
        
        return im.FactorScale(img, minscale2, minscale2)

    maxnumx2 = 3
    maxnumy2 = 3
    maxthumbx2 = config.screen_width / (maxnumx2 + 1)
    maxthumby2 = config.screen_height / (maxnumy2 + 1)
    maxperpage2 = maxnumx2 * maxnumy2
    gallery_page2 = 0
    closeup_page2 = 0


    class Scenes_GalleryItem:
        def __init__(self, name, images, thumb, thumb_hover, locked2="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.thumb_hover = thumb_hover
            self.locked2 = locked2
            self.refresh_lock2()
        
        def num_images2(self):
            return len(self.images)
        
        def refresh_lock2(self):
            self.num_unlocked2 = 0
            lockme2 = False
            for img in self.images:
                if not img in scenes_gallery_photos.storage:
                    lockme2 = True
                else:
                    self.num_unlocked2 += 1
            self.is_locked2 = lockme2

    class Scenes_Gallery_photos(store.object):
        def __init__(self,):
            self.storage = []
        
        def add1(self, img): 
            self.storage.append(img)

    class addgimage_scenes(Action):
        
        def __init__(self, img):
            self.img = img
        
        def __call__(self):
            scenes_gallery_photos.storage.append(self.img)
            renpy.restart_interaction()



    scenes_gallery_photos = Scenes_Gallery_photos()
    scenes_gallery_items = []
    scenes_gallery_items.append(Scenes_GalleryItem("sara_pad_lose_v1", ["img1_sara_evening_pad_lose"], "thumb1_idle_sara_evening_pad_lose","thumb1_hover_sara_evening_pad_lose" ))
    scenes_gallery_items.append(Scenes_GalleryItem("sara_pad_win_v1", ["img2_sara_evening_pad_win"], "thumb2_idle_sara_evening_pad_win","thumb2_hover_sara_evening_pad_win" ))
    scenes_gallery_items.append(Scenes_GalleryItem("sara_night_visit_v1", ["img3_sara_night_visit_v1"], "thumb3_idle_sara_night_visit_v1","thumb3_hover_sara_night_visit_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("sara_botlle_game_v1", ["img4_sara_botlle_game_v1"], "thumb4_idle_sara_botlle_game_v1","thumb4_hover_sara_botlle_game_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("celia_toilet_kiss_v1", ["img5_celia_toilet_kiss_v1"], "thumb5_idle_celia_toilet_kiss_v1","thumb5_hover_celia_toilet_kiss_v1 " ))
    scenes_gallery_items.append(Scenes_GalleryItem("celia_toilet_fuck_v1", ["img6_celia_toilet_fuck_v1"], "thumb6_idle_celia_toilet_fuck_v1","thumb6_hover_celia_toilet_fuck_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("celia_vibrator_classroom_v1", ["img7_celia_vibrator_classroom_v1"], "thumb7_idle_celia_vibrator_classroom_v1","thumb7_hover_celia_vibrator_classroom_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("caroline_ass_cosplay_v1", ["img8_caroline_ass_cosplay_v1"], "thumb8_idle_caroline_ass_cosplay_v1","thumb8_hover_caroline_ass_cosplay_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("violet_blowjob_v1", ["img9_violet_blowjob_v1"], "thumb9_idle_violet_blowjob_v1","thumb9_hover_violet_blowjob_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("caroline_visit_bjfjhj_v1", ["img10_caroline_visit_bjfjhj_v1"], "thumb10_idle_caroline_visit_bjfjhj_v1","thumb10_hover_caroline_visit_bjfjhj_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("mom_car_v1", ["img11_mom_car_v1"], "thumb11_idle_mom_car_v1","thumb11_hover_mom_car_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("ml_work_hj_v1", ["img12_mom_work_hj_v1"], "thumb12_idle_mom_work_hj_v1","thumb12_hover_mom_work_hj_v1" ))
    scenes_gallery_items.append(Scenes_GalleryItem("ml_room_fj_v1", ["img13_ml_room_fj_v1"], "thumb13_idle_ml_room_fj_v1","thumb13_hover_ml_room_fj_v1 " ))

    scenes_gallery_items.append(Scenes_GalleryItem("MLR2_ES3_rep", ["img14_MLR2_ES3_rep"], "thumb14_idle_MLR2_ES3_rep","thumb14_hover_MLR2_ES3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR2_NS2_rep", ["img15_MLR2_NS2_rep"], "thumb15_idle_MLR2_NS2_rep","thumb15_hover_MLR2_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("MLR2_weekend_rep", ["img16_MLR2_weekend_rep"], "thumb16_idle_MLR2_weekend_rep","thumb16_hover_MLR2_weekend_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR2_AS1_rep", ["img17_CR2_AS1_rep"], "thumb17_idle_CR2_AS1_rep","thumb17_hover_CR2_AS1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR2_AS2_rep", ["img18_CR2_AS2_rep"], "thumb18_idle_CR2_AS2_rep","thumb18_hover_CR2_AS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("CR2_NS2_rep", ["img19_CR2_NS2_rep"], "thumb19_idle_CR2_NS2_rep","thumb19_hover_CR2_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Z_ES2_rep", ["img20_Z_ES2_rep"], "thumb20_idle_Z_ES2_rep","thumb20_hover_Z_ES2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Z_ES3_rep", ["img21_Z_ES3_rep"], "thumb21_idle_Z_ES3_rep","thumb21_hover_Z_ES3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("Z_ES4_rep", ["img22_Z_ES4_rep"], "thumb22_idle_Z_ES4_rep","thumb22_hover_Z_ES4_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("SR2_NS2_rep", ["img23_SR2_NS2_rep"], "thumb23_idle_SR2_NS2_rep","thumb23_hover_SR2_NS2_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("SR2_ES1_rep", ["img24_SR2_ES1_rep"], "thumb24_idle_SR2_ES1_rep","thumb24_hover_SR2_ES1_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("SR2_NS3_rep", ["img25_SR2_NS3_rep"], "thumb25_idle_SR2_NS3_rep","thumb25_hover_SR2_NS3_rep " ))
    scenes_gallery_items.append(Scenes_GalleryItem("SR2_NS4_rep", ["img26_SR2_NS4_rep"], "thumb26_idle_SR2_NS4_rep","thumb26_hover_SR2_NS4_rep " ))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
