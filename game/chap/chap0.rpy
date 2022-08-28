label titlepage(chapNum, chap_label = _("Chapitre {}")):
    stop music fadeout 1.0
    scene black with dissolve
    image background_image = "gui/main_menu.png"

    show background_image
    show expression VBox(Text(__(chap_label).format(chapNum), substitute = False, size=125, yalign=0.5, xalign=0.5, color="#fff")) as text:
        yalign 0.42
        xalign 0.5
    with dissolve
    $ renpy.pause (2.5)
    return

# Le jeu commence ici
label start:
    show screen konami_trigger
    call titlepage("", _("Prologue"))
    scene world with dissolve
    $ renpy.pause (2.5)
    "Il était une fois, dans un royaume lointain nommé Couleurs, sept boules de cristal."
    hide screen konami_trigger
    show screen hidden_balls
    "Chacune d'elles représentait une couleur de l'arc-en-ciel. Elles étaient les fondations du royaume."
    "Sans elles, il n'y aurait plus de couleurs dans le monde."
    "Bien gardées par Madame Arc-en-Ciel, le royaume vivait en parfaite harmonie."
    hide screen hidden_balls
    "Jusqu'au jour où un petit enfant décide de faire un voeu assez particulier…"
    scene voeu with dissolve
    x "Ô Madame Arc-en-ciel ! Faites que je puisse réaliser mon souhait."
    scene identite with dissolve
    python:
        player_name = None
        while player_name == None:
            player_name = renpy.input("", default='Blanche', length=10)
            player_name = player_name.strip()
            if not player_name:
                player_name="Blanche"
            # Small easter egg
            if player_name.lower() == _("noir") or player_name.lower() == _("noire"):
                renpy.say(None, _("Oh non, c'est le nom de mon papa."))
                player_name=None

    scene room with dissolve
    show blanche neutral open at left with dissolve
    blanche "Mon nom est [player_name] et mon papa s'appelle Noir."
    blanche "Je n'ai jamais connu ma maman. Mais, ce n'est pas grave, car mon papa s'occupe bien de moi !"
    blanche "Aujourd'hui, pendant que mon papa dormait, j'ai décidé de fuguer et de faire un tour du royaume !"
    show blanche smile open at left
    blanche "Je vais aller récupérer toutes les boules de cristal ! Héhé !"
    show blanche neutral open at left
    blanche "D'après mon papa, elles sont très jolies !"
    blanche "J'ai volé une carte du royaume sur le bureau de mon papa."
    blanche "D'après la carte, la boule de cristal la plus proche est dans le jardin de violettes !"
    show blanche smile open at left
    blanche "C'est parti !"
    jump chap1
    return

screen hidden_balls():
    add InvisibleImage("images/boules/Boules_1.png", 100, 300):
        xalign 0.
        yalign 0.6
    add InvisibleImage("images/boules/Boules_2.png", 100, 300):
        xalign 0.13
        yalign 0.28
    add InvisibleImage("images/boules/Boules_3.png", 100, 300):
        xalign 0.32
        yalign 0.1
    add InvisibleImage("images/boules/Boules_4.png", 100, 300):
        xalign 0.5
        yalign 0.
    add InvisibleImage("images/boules/Boules_5.png", 100, 300):
        xalign 0.68
        yalign 0.1
    add InvisibleImage("images/boules/Boules_6.png", 100, 300):
        xalign 0.85
        yalign 0.28
    add InvisibleImage("images/boules/Boules_7.png", 100, 300):
        xalign 1.
        yalign 0.6

screen konami_trigger():
    add KonamiCode(lambda: renpy.jump("fast_chapter_jump"))

label fast_chapter_jump:
    call screen fast_chapter_jump_screen

screen fast_chapter_jump_screen():
    $ labels = sorted([l for l in renpy.get_all_labels() if l.startswith("start") or l.startswith("chap")])
    $ lines_count = 3
    $ columns_count = math.floor((len(labels)+lines_count-1)/lines_count)
    modal True
    frame:
        background "gui/main_menu.png"
        xsize 1.
        ysize 1.

        hbox:
            yalign 0.1
            xalign 0.5
            text _("Cheat - Voyage rapide"):
                size 125
                color "#222"
                yalign 0.42
                xalign 0.5
        grid columns_count lines_count:
            xalign 0.5
            yalign 0.5
            spacing 30
            for l in labels:
                textbutton l action Jump(l) style "navigation_button"
            for i in range(0, columns_count*lines_count-len(labels)):
                textbutton str(i)
