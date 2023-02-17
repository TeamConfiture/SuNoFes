label win_noir_color_7(red = True):
    scene noir_colors_6 with dissolve
    play sound sound.Unlock_Puzzle
    pause 1
    scene noir_colors_7 with dissolve
    pause 2
    scene dojo
    if red:
        show rouge at right
    show blanche neutral open at left
    with dissolve
    return

label chap7:
    call titlepage(7)
    scene dojo
    with dissolve
    play music music.Theme_Red fadein 1.0 volume 0.7
    "Un chat en position de combat semble s'entraîner avec acharnement."
    show rouge at right with dissolve
    voice renpy.random.choice(audio.Red_Angry)
    x "Woosh ! Comme un chat ! Sois plus violent que le cours du torrent !" with vpunch
    x "Woosh ! Comme un chat ! Sois plus puissant que les ouragans !" with vpunch
    x "Woosh ! Comme un chat ! Sois plus ardent que le feu des volcans !" with vpunch
    voice renpy.random.choice(audio.Red_Speak)
    x "MIAOU ! Par le pouvoir du prisme Rouge, transforme-moi !" with vpunch
    "Rien ne se passe…"
    x "Miaou… Pourquoi ne suis-je pas plus fort ? Jamais je n'arriverai à battre Jaune en étant comme ça."
    show blanche cry open at left with dissolve
    voice renpy.random.choice(audio.Blanche_Moan)
    blanche "Il fait chaaaaaauud. J'ai soif."
    show blanche cry close at left
    voice renpy.random.choice(audio.Red_Angry)
    x "Qui va là ?! Qui ose perturber l'entraînement de Red ?!" with vpunch
    red "Viens te battre ! C'est la guerre !"
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Gasp)
    blanche " Oh ! Un chat ?! Il se rue vers moi ! Aaaah !" with vpunch
    voice renpy.random.choice(audio.Red_Angry)
    red "MIAOU ! Oui, la guerre !"
    "Le chat me griffe."
    show blanche cry open at left
    voice renpy.random.choice(audio.Blanche_Cry)
    blanche "Aïe ! Aïe ! Mais euh ! Je n'ai rien fait ! Pourquoi tu m'attaques ?" with vpunch
    show blanche cry close at left
    voice renpy.random.choice(audio.Red_Speak)
    red "Quel étrange bête, tu ne sais pas te battre ? Pour survivre ici, il faut savoir user de ses pattes."
    show crystal_red at Position(xpos=0.47, yalign=0.5) with dissolve
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Gasp)
    blanche "Mais, je ne veux pas me battre ! Je viens juste ici pour récupérer la dernière boule de cristal : le Rouge ardent !"
    show blanche surprised close at left
    hide crystal_red at Position(xpos=0.47, yalign=0.5) with dissolve
    voice renpy.random.choice(audio.Red_Angry)
    red "Sacrilège ! Quel outrage à Maîtressse Arc-en-Ciel ! Tu oses me défier, moi, Red, Gardien de Couleur ?! Viens par là !"
    "Le chat se met en position de combat."
    show blanche surprised open at left
    blanche "Non ! Non ! Calme-toi ! Je viens en paix ! Je veux juste t'emprunter pour une nuit ta boule de cristal. C'est pour mon papa !" with vpunch
    show blanche surprised close at left
    voice renpy.random.choice(audio.Red_Speak)
    red "Bats-toi ! Vile être qui veut piller mes terres !"
    show blanche cry open at left
    voice renpy.random.choice(audio.Blanche_Sigh)
    blanche "Zut, il ne m'écoute pas. Je vais devoir essayer de me défendre…"
    hide blanche cry close at left
    hide rouge at right
    with dissolve
    call screen chap7_simon_says('chap7_2', 'simon_game_defeat')

label simon_game_defeat:
    show rouge at right with dissolve
    voice renpy.random.choice(audio.Red_Speak)
    red "Hmpf… Hmpf… Pas mal, pas mal pour un intrus. Mais, Red a gagné ! Il en faut plus que ça pour me battre."
    hide rouge at right with dissolve
    call screen chap7_simon_says('chap7_2', 'simon_game_defeat')

label chap7_2:
    $ achievement.grant("achievement_chap7_minigame_done")
    $ achievement.sync()
    show rouge at right
    show blanche neutral close at left
    with dissolve
    voice renpy.random.choice(audio.Red_Speak)
    red "Hmpf… Hmpf… Etranger, je reconnais ma défaite. D'où vient ta puissance ? Aucun être n'a battu Red en dehors de Jaune. Qui est ton maître ?"
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Gasp)
    blanche "Je n'ai rien fait ! Rien appris ! Je suis juste rapide."
    show blanche surprised close at left
    red "Sacre bleu ! Ainsi, tu es comme Jaune ! Quel est ton secret ? Apprends-moi ! Il faut que je sois le plus fort pour défendre ma boule de cristal !"
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Question)
    blanche "Jaune ? Le chat avec son poussin ? Il t'a battu ? Mais, il ne fait que dormir !"
    show blanche surprised close at left
    red "La fourrure ne fait pas le chat. Les apparences sont parfois trompeuses. C'est un Gardien de Couleurs très puissant !"
    voice renpy.random.choice(audio.Red_Speak)
    red "Alors, vas-tu m'apprendre tes techniques ?!"
    show blanche surprised open at left
    blanche "Je n'ai aucune technique ! Je suis juste là pour ta boule de cristal…"
    show blanche surprised close at left
    voice renpy.random.choice(audio.Red_Angry)
    red "Mensonge ! Cela ne peut pas être un talent inné ! Je refuse d'y croire !"
    show blanche cry open at left
    voice renpy.random.choice(audio.Blanche_Moan)
    blanche "Il ne veut rien savoir… Que faire… Je veux juste récupérer sa boule…"
    menu:
        "L'assommer et prendre sa boule":
            $ bad +=1
            voice renpy.random.choice(audio.Blanche_Exclamation)
            show blanche neutral open at left
            blanche "Je sais ! Red ferme les yeux !"
            show blanche neutral close at left
            voice renpy.random.choice(audio.Red_Happy)
            red "Oh ! Tu vas m'apprendre une technique ? D'accord, je ferme les yeux."
            play sound renpy.random.choice(sound.Slap)
            show boum with vpunch
            hide boum
            hide rouge at right
            with dissolve
            "Le chat a perdu connaissance."
            show blanche neutral open at left
            blanche "Bon, c'était plus facile que je le pensais."
            call win_noir_color_7(red = False)
            blanche "J'espère que mon papa sera content. Être dans le noir, c'est triste. Lui montrer les couleurs de l'arc-en-ciel va sûrement lui remonter le moral."
            show blanche cry open at left
            voice renpy.random.choice(audio.Blanche_Moan)
            blanche "Il a toujours les yeux bandés… Tout ça pour s'habituer à voir la couleur noire le plus tôt possible, c'est triste."
            blanche "De ce qu'il m'a dit, c'est parce que ses yeux le refont penser à ma maman, mais le fait d'être \"Noir\" fait qu'il finira par ne voir que du noir… C'est triste."
            blanche "Il doit voir ces jolies couleurs une dernière fois."

        "Troquer une technique inventée contre sa boule":
            $ neutral +=1
            show blanche neutral open at left
            voice renpy.random.choice(audio.Blanche_Gasp)
            blanche "J'ai une idée ! Si je te donne une technique, tu me prêtes ta boule pour une nuit ?"
            show blanche neutral close at left
            voice renpy.random.choice(audio.Red_Speak)
            red "Ah ! Quel choix cornélien ! Je ne peux rompre ma promesse avec Maîtresse Arc-en-Ciel…"
            red "Mais, si c'est pour une nuit pour ensuite être meilleur et lui faire honneur. J'accepte. Dis-moi tout, étranger."
            hide blanche neutral close at left
            hide rouge at right
            with dissolve
            "Je lui explique une technique inventée de toutes pièces."
            "Quelques minutes plus tard."
            show blanche neutral open at left
            show rouge at right
            with dissolve
            blanche "Voilà ! Tu sais tout maintenant !"
            show blanche neutral close at left
            voice renpy.random.choice(audio.Red_Happy)
            red "Sacrilège, qui aurait cru que boire du lait te faisait grandir et devenir plus fort."
            red "Merci pour cette technique. Voilà ma boule."
            call win_noir_color_7()
            show blanche neutral open at left
            voice renpy.random.choice(audio.Blanche_Laugh)
            blanche "Merci ! Merci Red ! J'en prendrai soin ! Ne t'en fais pas je te la rendrai en temps et en heure !"
            show blanche neutral close at left
            voice renpy.random.choice(audio.Red_Speak)
            red "Très bien, camarade."
            red "Cela dit, pourquoi en as-tu besoin ?"
            show blanche neutral open at left
            blanche "C'est pour mon papa ! Il ne va pas bien du tout… Il est tout le temps dans le noir et être dans le noir, c'est triste."
            blanche "De ce qu'il m'a dit, c'est parce que ses yeux lui refont penser à ma maman, mais le fait d'être \"Noir\" fait qu'il finira par ne voir que du noir. Il veut s'habituer à voir la couleur noire le plus tôt possible…"
            show blanche cry open at left
            voice renpy.random.choice(audio.Blanche_Sniffing)
            blanche "Voir mon papa dans cet état me rend triste. C'est pour ça que je veux lui montrer les couleurs de l'arc-en-ciel. Juste une dernière fois…"
            show blanche cry close at left
            red "..."
            "Red me tapote la tête."
            voice renpy.random.choice(audio.Red_Speak)
            red "Vaillant camarade, bon courage pour ta quête."
            show blanche neutral open at left
            voice renpy.random.choice(audio.Blanche_Laugh)
            blanche "Haha ! Merci Red !"
            hide rouge at right with dissolve
            show blanche neutral close at left

        "Réfléchir avec lui pour combattre Jaune et demander sa boule":
            $ good +=1
            show blanche surprised open at left
            voice renpy.random.choice(audio.Blanche_Gasp)
            blanche "Ah ! Je sais ! Tu n'as qu'à te bander les yeux comme mon papa ! Il arrive à voir partout sans ouvrir les yeux !" with vpunch
            show blanche surprised close at left
            voice renpy.random.choice(audio.Red_Happy)
            red "Est-ce une de tes techniques secrètes ?! Mais, je ne verrai rien, moi !"
            show blanche neutral open at left
            blanche "Jaune dort tout le temps. Il doit aussi avoir tout le temps les yeux fermés pour te battre, non ?"
            show blanche neutral close at left
            voice renpy.random.choice(audio.Red_Speak)
            red "Maintenant que tu le dis… C'est décidé ! Prochain entraînement, on fait tout ça les yeux bandés !"
            red "Cela dit… Pourquoi ton papa a toujours les yeux bandés ? Il a aussi un ennemi puissant à combattre ?"
            show blanche surprised open at left
            blanche "Non du tout ! De ce qu'il m'a dit, c'est parce que ses yeux lui refont penser à ma maman, mais le fait d'être \"Noir\" fait qu'il finira par ne voir que du noir. Il veut s'habituer à voir la couleur noire le plus tôt possible…"
            show blanche cry open at left
            voice renpy.random.choice(audio.Blanche_Sniffing)
            blanche "Mais, là, il ne va pas bien du tout, et être dans le noir, c'est triste. C'est pour ça que je veux lui montrer les couleurs de l'arc-en-ciel. Juste une dernière fois…"
            blanche "C'est pour ça que j'aurai besoin de ta boule de cristal. C'est important."
            show blanche cry close at left
            red "..."
            red "Prends la et rends-la moi après avoir réaliser ton souhait."
            show blanche surprised open at left
            voice renpy.random.choice(audio.Blanche_Gasp)
            blanche "C'est vrai ?! Je peux ?!" with vpunch
            show blanche surprised close at left
            voice renpy.random.choice(audio.Red_Speak)
            red "Tu m'as aidé. Je te rends la pareil, camarade."
            call win_noir_color_7()
            show blanche neutral open at left
            blanche "Merci ! Merci Red ! J'en prendrai soin !"
            hide rouge at right with dissolve
            show blanche neutral close at left
    
    show blanche neutral open at left
    blanche "Bon... Direction le Quartier des Monochromes ! Papa m'attend !"
    hide blanche neutral open at left with dissolve
    if good > neutral and good > bad: 
        show maigrichon at left
        show grosso at right
        with dissolve
        voice renpy.random.choice(audio.Maigrichon_Angry)
        maigrichon "Dans cette direction ! J'ai vu l'enfant partir par là !" with vpunch
        voice renpy.random.choice(audio.ArcEnCiel_Exasperate)
        x "Décidément, il faut tout régler par soi-même."
        show mme neutral close
        hide maigrichon at left
        hide grosso at right
        with dissolve
        grosso_maigrichon "Ma… Madame Arc-en-Ciel !" with vpunch
        stop music fadeout 2.0
        jump end_good
    elif neutral > bad: 
        show maigrichon at left
        show grosso at right
        with dissolve
        voice renpy.random.choice(audio.Maigrichon_Angry)
        maigrichon "Dans cette direction ! J'ai vu l'enfant partir par là !" with vpunch
        voice renpy.random.choice(audio.Grosso_No)
        grosso "Non, je l'ai vu partir par ici !"
        grosso_maigrichon "..."
        voice renpy.random.choice(audio.Maigrichon_Sigh)
        voice renpy.random.choice(audio.Grosso_Sigh)
        grosso_maigrichon "Oh nooon… On l'a encore perdu de vue…"
        stop music fadeout 2.0
        jump end_neutral
    else: 
        show maigrichon at left
        show grosso at right
        with dissolve
        voice renpy.random.choice(audio.Maigrichon_Angry)
        maigrichon "Dans cette direction ! J'ai vu l'enfant partir vers le Quartier des Monochromes !" with vpunch
        voice renpy.random.choice(audio.Grosso_Angry)
        grosso "À ses trousses !"
        maigrichon "Tu ne nous échapperas pas cette fois !"
        stop music fadeout 2.0
        jump end_bad
