﻿label titlepage(chapNum):
    stop music fadeout 1.0
    scene black with dissolve
    define chap_label = "Chapitre "
    image prologue = "images/bg/world.png"
    image chap = "images/bg/world.png"

    if chapNum == 0:
        show prologue
        show expression VBox(Text(_("Prologue"), size=125, yalign=0.5, xalign=0.5, color="#000")) as text:
            yalign 0.25
            xalign 0.5
        with dissolve
    else:
        if persistent.lang is None:
            $ chap_label = "Chapter "
        show chap
        show expression VBox(Text(chap_label + str(chapNum), size=125, yalign=0.5, xalign=0.5, color="#000")) as text:
            yalign 0.4
            xalign 0.25
        with dissolve
    $ renpy.pause (2.5)
    return

# Le jeu commence ici
label start:
    call titlepage(chap)
    scene world with dissolve
    $ renpy.pause (2.5)
    "Il était une fois, dans un royaume lointain nommé Couleurs, existaient sept boules de cristal."
    "Chacune d’elle représentait une couleur de l’arc-en-ciel. Elles étaient les fondations du royaume."
    "Sans elles, il n’y aurait plus de couleurs dans le monde."
    "Bien gardées par Madame Arc-en-Ciel, le royaume vivait en parfaite harmonie."
    "Jusqu’au jour où un petit enfant décide de faire un voeu assez particulier..."
    scene voeu with dissolve
    x "Ô Madame Arc-en-ciel ! Faîtes que je puisse réaliser mon souhait."
    python:
        player_name = renpy.input("", default='Blanche', length=10)
        player_name = player_name.strip()
        if not player_name:
            player_name="Blanche"

    "Mon nom est [player_name] et mon papa s’appelle Noir."
    "Je n’ai jamais connu ma maman. Mais, ce n’est pas grave, car mon papa s’occupe bien de moi !"
    "Aujourd’hui, pendant que mon papa dormait, j’ai décidé de fuguer et de faire un tour du royaume !"
    "Je vais aller récupérer toutes les boules de cristal ! Héhé !"
    "D’après mon papa, elles sont très jolies !"
    "J’ai volé une carte de royaume sur le bureau de mon papa."
    blanche "D’après la carte, la boule de cristal la plus proche est dans le jardin de violettes !"
    blanche "C’est parti !"
    return
