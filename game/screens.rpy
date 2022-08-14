################################################################################
## Initialisation
################################################################################
init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    font "gui/font/augie.ttf"
    bold True
    color "#666666"
    hover_color "#666666"
    underline False
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    xsize 500
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    ysize 500
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## Écrans de jeu
################################################################################

## Écran des dialogues #########################################################
##
## L’écran des dialogues est utilisé pour afficher les dialogues du joueur. Il
## prend deux paramètres, who(qui) et what(quoi) qui sont respectivement le
## nom du personnage en train de parler et le texte à afficher. (Le paramètre
## who(qui) peut être None si aucun nom n’est donné.)
##
## Cet écran affiche le texte correspondant à what. Il peut également créer un
## texte avec le paramètre who et l’identifiant « window » est utilisé pour
## déterminer les styles à appliquer.
##
## https://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## Si il y a une side image, l'afficher au-dessus du texte. Ne pas
    ## l'afficher sur la version téléphone - pas assez de place.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu
    
## Rendre la boîte du nom personnalisable à travers l'objet Character.
init python:
    config.character_id_prefixes.append('namebox')

    # Gallery's initialisation
    album = Gallery()
    album.button("title")

    # Music Room initialisation
    musicroom = MusicRoom(fadeout=1.0,loop=True,single_track=True)
    musicroom.add("music/You Make Me Back.mp3", always_unlocked=True)
    musicroom.add("music/Diamond.mp3", always_unlocked=True)
    musicroom.add("music/Yofukashino Uta.mp3", always_unlocked=True)
    musicroom.add("music/Dorohedoro Zombie Slushi.mp3", always_unlocked=True)
    musicroom.add("music/Eating food and fighting Wizards.mp3", always_unlocked=True)
    musicroom.add("music/El Canto del Colibrí.mp3", always_unlocked=True)

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    adjust_spacing False

## Écran de saisie #############################################################
##
## Cet écran est utilisé pour afficher renpy.input. Le paramètre prompt est
## utilisé pour passer le texte par défaut.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    window:
        xalign 0
        yalign 0
        background None
        vbox:
            xpos 0.43
            xsize gui.dialogue_width
            ypos 0.48
            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Écran des choix #############################################################
##
## Cet écran est utilisé pour afficher les choix qui seront fait par le joueur
## dans le jeu. Le premier paramètre, items, est une liste d'objets contenant
## chacun des champs de texte et d'action.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is button
style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is button_text
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Écran des menus rapides #####################################################
##
## Les menus rapides sont affichés dans le jeu pour permettre un accès rapide à
## certaines fonctions.

screen quick_menu():
    ## Assure qu'il apparaît au-dessus des autres screens.
    zorder 100
    if quick_menu:
        hbox:
            xalign 0.95
            yalign 0.65
            spacing 30
            textbutton _("Retour") action Rollback()
            textbutton _("Historique") action ShowMenu('history')
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Sauvegarde") action ShowMenu('save')
            textbutton _("Préf.") action ShowMenu('preferences')

default quick_menu = True

style quick_button:
    color '#000'
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Screens du menu principal et du menu de jeu
################################################################################

## Écran de navigation #########################################################
##
## Cet écran est disponible dans le menu principal et dans le menu de jeu. Il
## fournit l’accès aux autres menus et permet le démarrage du jeu.

screen navigation():
    hbox:
        style_prefix "navigation"
        xalign 0.5
        yalign 0.9

        if main_menu:
            textbutton _("Nouvelle partie") action Start()

        textbutton _("Charger") action ShowMenu("load")
        textbutton _("Préférences") action ShowMenu("preferences")
        textbutton _("Extra") action ShowMenu("extra")
        
        if _in_replay:
            textbutton _("Fin de la rediffusion") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Menu") action MainMenu()

        if renpy.variant("pc"):
            textbutton _("Quitter") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button:
    properties gui.button_properties("navigation_button")
    left_margin 30
    right_margin 30
    hover_foreground Frame(["gui/button/mm_button_hover.png"])

style navigation_button_text is gui_button_text
style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    color u"#000"
    size 50

## Écran du menu principal #####################################################
##
## Utilisé pour afficher le menu principal quand Ren'Py démarre.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    ## Ceci assure que tout autre screen de menu est remplacé.
    tag menu
    add gui.main_menu_background
    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation
    if gui.show_name:
        text "[config.name!t]":
            style "main_menu_title"

style main_menu_vbox is vbox

style main_menu_text is gui_text
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text
style main_menu_title:
    properties gui.text_properties("title")
    xalign 0.5
    yalign 0.4
    color u"#fff"

## Écran du menu de jeu ########################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.
screen game_menu(title,returnFrom, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    if title=="main_menu":
        add gui.main_menu_background
    else:
        add gui.secondary_menu_background
        text title:
            style "secondary_menu_title"

    frame:
        style "game_menu_navigation_frame"
    frame:
        style "game_menu_content_frame"
        if scroll == "viewport":
            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True
                transclude
        elif scroll == "vpgrid":
            vpgrid:
                cols 1
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True
                transclude
        else:
            transclude

    if title=="main_menu":
        key "game_menu" action ShowMenu("main_menu")
    else:
        use return(returnFrom)

screen return(returnFrom):
    hbox:
        xalign 0.5
        yalign 1.0
        spacing 50
        if returnFrom == "history" or returnFrom == "game":
            textbutton _("Retour"):
                style "return_button"
                action Return()
        else:
            textbutton _("Retour"):
                style "return_button"
                action ShowMenu(returnFrom)
        textbutton _("Menu"):
            style "return_button"
            action ShowMenu('main_menu')


style game_menu_outer_frame is empty
style game_menu_outer_frame:
    bottom_padding 0
    top_padding 0
    # background "gui/overlay/game_menu.png"
style game_menu_navigation_frame is empty
style game_menu_navigation_frame:
    xsize 0
    yfill True
style game_menu_content_frame is empty
style game_menu_content_frame:
    top_margin 300
    xalign 0.5
style game_menu_viewport is gui_viewport
style game_menu_viewport:
    xsize 1380
style game_menu_side is gui_side
style game_menu_side:
    spacing 0
style game_menu_scrollbar is gui_vscrollbar
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_label is gui_label
style game_menu_label:
    xpos 75
    ysize 180
style game_menu_label_text is gui_label_text
style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button is navigation_button
style return_button:
    yoffset -100
style return_button_text is navigation_button_text
style return_button_text:
    size 50

## Écran de chargement et de sauvegarde ########################################
##
## Ces écrans permettent au joueur d’enregistrer le jeu et de le charger
## à nouveau. Comme ils partagent beaucoup d’éléments communs, ils sont
## tous les deux implémentés dans un troisième écran, appelé fichiers_slots
## (emplacement_de_fichier).
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu
    use file_slots(_("Sauvegarde"),"game")

screen load():
    tag menu
    use file_slots(_("Charger"))

screen file_slots(title,returnFrom="main_menu"):
    # default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Sauvegardes automatiques"), quick=_("Sauvegardes rapides"))
    use game_menu(title,returnFrom):
        fixed:
            ## Cette instruction s’assure que l’évènement enter aura lieu avant
            ## que l’un des boutons ne fonctionne.
            order_reverse True
            grid 3 2 :
                style_prefix "slot"
                xalign 0.5
                yoffset -25
                xspacing 65
                yspacing 15
                for i in range(6):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add AlphaMask(FileScreenshot(slot), "gui/slot_mask.png")
                        if FileTime(slot, format=_("{#file_time}%A %d %B %Y, %H:%M"), empty=_("emplacement vide")) == "emplacement vide":
                            yalign 1.0
                            text _("Emplacement vide"):
                                style "slot_empty_text"
                        else:
                            text FileTime(slot, format=_("{#file_time}%A %d %B %Y, %H:%M"), empty=_("emplacement vide")):
                                style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)

style page_label is gui_label
style page_label:
    xpadding 75
    ypadding 5
style page_label_text is gui_label_text
style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
style page_button is gui_button
style page_button:
    properties gui.button_properties("page_button")
style page_button_text is gui_button_text
style page_button_text:
    properties gui.button_text_properties("page_button")
style slot_button is gui_button
style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text is gui_button_text
style slot_button_text:
    properties gui.button_text_properties("slot_button")
style slot_time_text is slot_button_text
style slot_time_text:
    font "gui/font/augie.ttf"
    size 18
    color u"#939393"
style slot_empty_text is slot_button_text
style slot_empty_text:
    font "gui/font/augie.ttf"
    size 48
    color u"#fff"
    yoffset -50
style slot_name_text is slot_button_text
style slot_name_text:
    font "gui/font/augie.ttf"
    size 24
    color u"#000000"

## Écran des préférences #######################################################
##
## L’écran de préférences permet au joueur de configurer le jeu pour mieux
## correspondre à ses attentes.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu
    use game_menu(_("Préférences"), "main_menu", scroll="viewport"):
        vbox:
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 100
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Affichage")
                        textbutton _("Fenêtre") action Preference("display", "window")
                        textbutton _("Plein écran") action Preference("display", "fullscreen")

                #if renpy.variant("pc"):
                #    vbox:
                #        null height (8 * gui.pref_spacing)
                #        style_prefix "radio"
                #        label _("Langue")
                #       textbutton "English" action [Language("english"), SetVariable('persistent.lang', "english")]
                #        textbutton "Français" action [Language(None), SetVariable('persistent.lang', None)]
                vbox:
                    style_prefix "check"
                    label _("Avance rapide")
                    textbutton _("Texte non lu") action Preference("skip", "toggle")
                    textbutton _("Après les choix") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            ## Des boites vbox additionnelles de type "radio_pref" ou
            ## "check_pref" peuvent être ajoutées ici pour ajouter des
            ## préférences définies par le créateur du jeu.
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Vitesse du texte")
                    bar value Preference("text speed")
                    label _("Avance automatique")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("Volume de la musique")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Volume des sons")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Volume des voix")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Couper tous les sons"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

### Preferences labels in preferences menu
style pref_label is gui_label
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
style pref_label_text is gui_label_text
style pref_label_text:
    yalign 1.0
style pref_vbox is vbox
style pref_vbox:
    xsize 338

### Radio settings in preferences menu
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_button_text:
    properties gui.button_text_properties("radio_button")
style radio_vbox is pref_vbox
style radio_vbox:
    spacing gui.pref_button_spacing

### Check settings in preferences menu
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text is gui_button_text
style check_button_text:
    properties gui.button_text_properties("check_button")
style check_vbox is pref_vbox
style check_vbox:
    spacing gui.pref_button_spacing

### Slider settings in preferences menu
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_slider:
    xsize 525
style slider_button is gui_button
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
style slider_button_text is gui_button_text
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style slider_vbox:
    xsize 675

## Écran des extras #######################################################
##
## Il s’agit d’un écran qui permet d'accéder aux musiques, images débloquées
## et aux crédits
style secondary_menu_title is secondary_menu_text
style secondary_menu_title:
    properties gui.text_properties("title")
    font "gui/font/augie.ttf"
    size 128
    xalign 0.5
    yalign 0.0
    color u"#fff"

screen extra():
    tag menu
    use game_menu(_("Extra"), "main_menu"):
        # Content of the screen
        hbox:
            spacing 75
            vbox:
                imagebutton:
                    auto "gui/extra/gui_gallery_btn_%s.png"
                    action ShowMenu('gallery')
            vbox:
                imagebutton:
                    auto "gui/extra/gui_music_btn_%s.png"
                    action ShowMenu('music')
            vbox:
                imagebutton:
                    auto "gui/extra/gui_credits_btn_%s.png"
                    action ShowMenu('credits')

## Écran des images #######################################################
screen gallery():
    tag menu
    use game_menu("Gallery", "extra"):
        hbox:
            grid 2 2:
                add album.make_button(name="title", unlocked="gui/slot.png", locked="gui/slot_lock.png", xalign=0.5, yalign=0.5)
                add album.make_button(name="title", unlocked="gui/slot.png", locked="gui/slot_lock.png", xalign=0.5, yalign=0.5)
                add album.make_button(name="title", unlocked="gui/slot.png", locked="gui/slot_lock.png", xalign=0.5, yalign=0.5)
                add album.make_button(name="title", unlocked="gui/slot.png", locked="gui/slot_lock.png", xalign=0.5, yalign=0.5)
                spacing 100

## Écran des musiques #######################################################
style music_button is button
style music_button_text is text:
    color "#666666"
    hover_color "#F233A7"
    selected_color "#F233A7"
    size 72

screen music():
    tag menu
    use game_menu("Music", "extra"):
        vbox:
            xalign 0.5
            ypos -25
            spacing 50
            hbox:
                grid 2 3:
                    xspacing 200
                    yspacing 50
                    # The buttons that play each track.
                    textbutton "Track 1" action musicroom.Play("music/You Make Me Back.mp3"):
                        style "music_button"
                    textbutton "Track 2" action musicroom.Play("music/Diamond.mp3"):
                        style "music_button"
                    textbutton "Track 3" action musicroom.Play("music/Yofukashino Uta.mp3"):
                        style "music_button"
                    textbutton "Track 4" action musicroom.Play("music/Dorohedoro Zombie Slushi.mp3"):
                        style "music_button"
                    textbutton "Track 5" action musicroom.Play("music/Eating food and fighting Wizards.mp3"):
                        style "music_button"
                    textbutton "Track 6" action musicroom.Play("music/El Canto del Colibrí.mp3"):
                        style "music_button"
                    # null height 20
            hbox:
                xalign 0.5
                spacing 25
                # Buttons that let us advance tracks.
                imagebutton auto "gui/button/left_%s.png" action musicroom.Previous()
                imagebutton auto "gui/button/pause_%s.png" action musicroom.Stop()
                imagebutton auto "gui/button/right_%s.png" action musicroom.Next()

## Écran des crédits #######################################################
style credits_text_name is gui_text:
    size 75
    color u"#F233A7"
    xalign 0.5
style credits_text_role is gui_text:
    size 35
    color u"#000000"
    xalign 0.5
style credits_text_link is gui_text:
    size 25
    color u"#666666"
    xalign 0.5
style credits_frame is gui_frame:
    background None
    xalign 0.5
    yalign 0.5

screen credits():
    tag menu
    use game_menu("Credits", "extra"):
        grid 2 2:
            spacing 50
            xalign 0.5
            yalign 0.5
            frame:
                style "credits_frame"
                vbox:
                    text _("Kimi"):
                        style "credits_text_name"
                    text _("Directeur, UI Designeur, et Développeuse"):
                        style "credits_text_role"
                    text _("{a=https://linktr.ee/KimiNako}https://linktr.ee/KimiNako{/a}"):
                        style "credits_text_link"
            frame:
                style "credits_frame"
                vbox:
                    text _("Pepotrouille"):
                        style "credits_text_name"
                    text _("Développeuse et artiste des sprites"):
                        style "credits_text_role"
                    text _("{a=https://pepotrouille.itch.io}https://pepotrouille.itch.io{/a}"):
                        style "credits_text_link"
            frame:
                style "credits_frame"
                vbox:
                    text _("yyyyj"):
                        style "credits_text_name"
                    text _("Développeur et scénariste"):
                        style "credits_text_role"
                    text _("{a=https://itch.io/profile/yyyyj}https://itch.io/profile/yyyyj{/a}"):
                        style "credits_text_link"
            null

## Écran de l'historique #######################################################
##
## Il s’agit d’un écran qui affiche l’historique des dialogues au joueur. Bien
## qu’il n'y ait rien de spécial sur cet écran, il doit accéder à l’historique
## de dialogue stocké dans _history_list.
##
## https://www.renpy.org/doc/html/history.html

## Ceci détermine quels tags peuvent être affichés sur le screen de
## l'historique.
define gui.history_allow_tags = { "alt", "noalt" }
style history_window is empty
style history_window:
    xfill True
    ysize gui.history_height
    ypos -275
style history_name is gui_label
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
style history_name_text is gui_label_text
style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    size 48
style history_text is gui_text
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#666666"
    size 48
style history_label is gui_label
style history_label:
    xfill True
style history_label_text is gui_label_text
style history_label_text:
    xalign 0.5

screen history():
    tag menu
    ## Cette instruction permet d’éviter de prédire cet écran, car il peut être
    ## très large
    predict False
    use game_menu(_("Historique"), "history"):
        vpgrid:
            area (-250, -50, 0.85, 0.85)
            cols 1
            yinitial 1.0 #0.0 pour commencer au début, 1.0 à la fin, de l'historique
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            arrowkeys True
            vbox:
                for h in _history_list:
                    window:
                        style "history_window"
                        ## Cela positionne correctement l'écran si history_height est
                        ## initialisé à None.
                        has fixed:
                            yfit True
                        if h.who:
                            label h.who:
                                style "history_name"
                                substitute False
                                ## Utilise pour la couleur du texte, la couleur par
                                ## défaut des dialogues du personnage si elle a été
                                ## initialisée.
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]
                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            style "history_text"
                            substitute False
                if not _history_list:
                    label _("L'historique des dialogues est vide.")

################################################################################
## Écrans additionnels
################################################################################

## Écran de confirmation #######################################################
##
## Cet écran est appelé quand Ren'Py souhaite poser une question au joueur dont
## la réponse est oui ou non.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):
    ## Cette instruction s’assure que les autres écrans resteront en arrière
    ## plan tant que cet écran sera affiché.
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Oui") action yes_action
                textbutton _("Non") action no_action
    ## Le clic bouton droit et la touche Echap. correspondent à la réponse
    ## "non".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

## Écran de l’indicateur d'avance rapide #######################################
##
## L’écran skip_indicator est affiché pour indiquer qu’une avance rapide est en
## cours.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator
screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 9
            text _("Avance rapide")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Cette transformation est utilisé pour faire clignoter les flèches l’une après
## l’autre.
transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Nous devons utiliser une police qui a le glyphe BLACK RIGHT-POINTING
    ## SMALL TRIANGLE.
    font "DejaVuSans.ttf"

## Écran de notification #######################################################
##
## Cet écran est utilisé pour affiché un message au joueur. (Par exemple, quand
## une sauvegarde rapide a eu lieu ou quand une capture d’écran vient d’être
## réalisée.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen
screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Écran NVL ###################################################################
##
## Cet écran est utilisé pour les dialogues et les menus en mode NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl
screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing
        ## Les dialogues sont affichés soit dans une vpgrid soit dans une vbox.
        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)
        else:
            use nvl_dialogue(dialogue)
        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"
    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None
                if d.who is not None:
                    text d.who:
                        id d.who_id
                text d.what:
                    id d.what_id


## Ce paramètre contrôle le maximum d’entrée dans le mode NVL qui peuvent être
## affichée simultanément.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

################################################################################
## Variantes pour les mobiles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Comme la souris peut ne pas être présente, nous remplaçons le menu rapide
## avec une version qui utilise des boutons plus gros et qui sont plus faciles à
## toucher du doigt.
screen quick_menu():
    variant "touch"
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            textbutton _("Retour") action Rollback()
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
