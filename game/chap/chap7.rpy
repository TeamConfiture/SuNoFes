label chap7:
    call titlepage(7)
    "Un chat en position de combat semble s'entraîner avec acharnement."
    x "Woosh ! Comme un chat ! Sois plus violent que le cours du torrent !"
    x "Woosh ! Comme un chat ! Sois plus puissant que les ouragans !"
    x "Woosh ! Comme un chat ! Sois plus ardent que le feu des volcans !"
    x "MIAOU ! Par le pouvoir du prisme Rouge, transforme-moi !"
    "Rien ne se passe…"
    x "Miaou… Pourquoi ne suis-je pas plus fort ? Jamais je n'arriverai à battre Jaune en étant comme ça."
    blanche "Il fait chaaaaaauud. J'ai soif."
    x "Qui va là ?! Qui ose perturber l'entraînement de Red ?!"
    red "Viens te battre ! C'est la guerre !"
    blanche " Oh ! Un chat ?! Il se rue vers moi ! Aaaah !"
    red "MIAOU ! Oui, la guerre !"
    "Le chat me griffe."
    blanche "Aïe ! Aïe ! Mais euh ! Je n'ai rien fait ! Pourquoi tu m'attaques ?"
    red "Quel étrange bête, tu ne sais pas te battre ? Pour survivre ici, il faut savoir user de ses pattes."
    blanche "Mais, je ne veux pas me battre ! Je viens juste ici pour récupérer la dernière boule de cristal : le Rouge ardent !"
    red "Sacrilège ! Quel outrage à Maîtressse Arc-en-Ciel ! Tu oses me défier, moi, Red, Gardien de Couleur ?! Viens par là !"
    "Le chat se met en position de combat."
    blanche "Non ! Non ! Calme-toi ! Je viens en paix ! Je veux juste t'emprunter pour une nuit ta boule de cristal. C'est pour mon papa !"
    red "Bats-toi ! Vile être qui veut piller mes terres !"
    blanche "Zut, il ne m'écoute pas. Je vais devoir essayer de me défendre…"
    call screen chap7_simon_says('chap7_2', 'simon_game_defeat')

label simon_game_defeat:
    red "Hmpf… Hmpf… Pas mal, pas mal pour un intrus. Mais, Red a gagné ! Il en faut plus que ça pour me battre"
    call screen chap7_simon_says('chap7_2', 'simon_game_defeat')

label chap7_2:
    red "Hmpf… Hmpf… Etranger, je reconnais ma défaite. D'où vient ta puissance ? Aucun être n'a battu Red en dehors de Jaune. Qui est ton maître ?"
    blanche "Je n'ai rien fait ! Rien appris ! Je suis juste rapide."
    red "Sacre bleu ! Ainsi, tu es comme Jaune ! Quel est ton secret ? Apprends-moi ! Il faut que je sois le plus fort pour défendre ma boule de cristal !"
    blanche "Jaune ? Le chat avec son poussin ? Il t'a battu ? Mais, il ne fait que dormir !"
    red "La fourrure ne fait pas le chat. Les apparences sont parfois trompeuses. C'est un Gardien de Couleurs très puissant !"
    red "Alors, vas-tu m'apprendre tes techniques ?!"
    blanche "Je n'ai aucune technique ! Je suis juste là pour ta boule de cristal…"
    red "Mensonge ! Cela ne peut pas être un talent inné ! Je refuse d'y croire !"
    blanche "Il ne veut rien savoir… Que faire… Je veux juste récupérer sa boule…"
    menu:
        "L'assommer et prendre sa boule":
            blanche "Je sais ! Red ferme les yeux !"
            red "Oh ! Tu vas m'apprendre une technique ? D'accord, je ferme les yeux."
            "BOUM"
            "Le chat a perdu connaissance."
            blanche "Bon, c'était plus facile que je le pensais."
            blanche "J'espère que mon papa sera content. Être dans le noir, c'est triste. Lui montrer les couleurs de l'arc-en-ciel va sûrement lui remonter le moral."
            blanche "Il a toujours les yeux bandés… Tout ça pour s'habituer à voir la couleur noire le plus tôt possible, c'est triste."
            blanche "De ce qu'il m'a dit, c'est parce que ses yeux le refont penser à ma maman, mais le fait d'être \"Noir\" fait qu'il finira par ne voir que du noir… C'est triste."
            blanche "Il doit voir ces jolies couleurs une dernière fois."

        "Troquer une technique inventée contre sa boule":
            blanche "J'ai une idée ! Si je te donne une technique, tu me prêtes ta boule pour une nuit ?"
            red "Ah ! Quel choix cornélien ! Je ne peux rompre ma promesse avec Maîtresse Arc-en-Ciel…"
            red "Mais, si c'est pour une nuit pour ensuite être meilleur et lui faire honneur. J'accepte. Dis-moi tout, étranger."
            "Je lui explique une technique inventée de toutes pièces."
            "Quelques minutes plus tard."
            blanche "Voilà ! Tu sais tout maintenant !"
            red "Sacrilège, qui aurait cru que boire du lait te faisait grandir et devenir plus fort."
            red "Merci pour cette technique. Voilà ma boule."
            blanche "Merci ! Merci Red ! J'en prendrai soin ! Ne t'en fais pas je te la rendrai en temps et en heure !"
            red "Très bien, camarade."
            red "Cela dit, pourquoi en as-tu besoin ?"
            blanche "C'est pour mon papa ! Il ne va pas bien du tout… Il est tout le temps dans le noir et être dans le noir, c'est triste."
            blanche "De ce qu'il m'a dit, c'est parce que ses yeux lui refont penser à ma maman, mais le fait d'être \"Noir\" fait qu'il finira par ne voir que du noir. Il veut s'habituer à voir la couleur noire le plus tôt possible…"
            blanche "Voir mon papa dans cet état me rend triste. C'est pour ça que je veux lui montrer les couleurs de l'arc-en-ciel. Juste une dernière fois…"
            red "..."
            "Red me tapote la tête."
            red "Vaillant camarade, bon courage pour ta quête."
            blanche "Haha ! Merci Red !"

        "Réfléchir avec lui pour combattre Jaune et demander sa boule":
            blanche "Ah ! Je sais ! Tu n'as qu'à te bander les yeux comme mon papa ! Il arrive à voir partout sans ouvrir les yeux !"
            red "Est-ce une de tes techniques secrètes ?! Mais, je ne verrai rien, moi !"
            blanche "Jaune dort tout le temps. Il doit aussi avoir tout le temps les yeux fermés pour te battre, non ?"
            red "Maintenant que tu le dis… C'est décidé ! Prochain entraînement, on fait tout ça les yeux bandés !"
            red "Cela dit… Pourquoi ton papa a toujours les yeux bandés ? Il a aussi un ennemi puissant à combattre ?"
            blanche "Non du tout ! De ce qu'il m'a dit, c'est parce que ses yeux lui refont penser à ma maman, mais le fait d'être \"Noir\" fait qu'il finira par ne voir que du noir. Il veut s'habituer à voir la couleur noire le plus tôt possible…"
            blanche "Mais, là, il ne va pas bien du tout, et être dans le noir, c'est triste. C'est pour ça que je veux lui montrer les couleurs de l'arc-en-ciel. Juste une dernière fois…"
            blanche "C'est pour ça que j'aurai besoin de ta boule de cristal. C'est important."
            red "..."
            red "Prends la et rends-la moi après avoir réaliser ton souhait."
            blanche "C'est vrai ?! Je peux ?!"
            red "Tu m'as aidé. Je te rends la pareil, camarade."
            blanche "Merci ! Merci Red ! J'en prendrai soin !"

    blanche "Bon... Direction le Quartier des Monochromes ! Papa m'attend !"

    if good: 
        maigrichon "Dans cette direction ! J'ai vu l'enfant partir par là !"
        x "Décidément, il faut tout régler par soi-même."
        grosso "Ma… Madame Arc-en-Ciel !"

    if neutre: 
        maigrichon "Dans cette direction ! J'ai vu l'enfant partir par là !"
        grosso "Non, je l'ai vu partir par ici !"
        grosso_maigrichon "..."
        grosso_maigrichon "Oh nooon… On l'a encore perdu de vue…"

    if bad: 
        maigrichon "Dans cette direction ! J'ai vu l'enfant partir vers le Quartier des Monochromes !"
        grosso "À ses trousses !"
        maigrichon "Tu ne nous échapperas pas cette fois !"
