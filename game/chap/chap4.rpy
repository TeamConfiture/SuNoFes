label chap4:
    call titlepage(4)
    scene garden
    with dissolve
    x "Colchiques dans les prés ! Fleurissent, fleurissent. Colchiques dans les prés ! C'est la fin de l'été."
    "Un chat chantonne tout en arrosant joyeusement de magnifiques fleurs."
    show emeraude at right
    show blanche surprised open at left
    with dissolve
    blanche "C'est… C'est si joli ! Ça brille de partout ! C'est si vert !" with vpunch
    show blanche surprised close at left
    x "Ho, ho, il en faut peu pour être heureux, vraiment très peu pour être heureux."
    x "Émeraude est satisfaite du nécessaire !"
    emeraude "Un peu d'eau fraîche et de verdure !"
    "Le chat tournoie sur lui-même, faisant répandre l'eau autour de lui."
    emeraude "Que nous prodigue la nature. Quelques rayons de miel et de soleil."
    show blanche smile open at left
    blanche "Haha, tu es marrante, Émeraude !"
    show blanche neutral open at left
    blanche "Moi, je m'appelle [player_name] !"
    show blanche neutral close at left
    emeraude "[player_name] ! Vas-y secoue-toi et danse ! "
    show blanche surprised open at left
    blanche "Oh non, je m'excuse. Je viens pour autre chose…"
    show blanche surprised close at left
    emeraude "Dis-moi, c'est quoi ton problèèème ?"
    show blanche neutral open at left
    blanche "Je viens pour récupérer la boule Vert… C'est pour mon papa…"
    show blanche neutral close at left
    emeraude "Ça ne tient pas à toi ! Ça ne tient pas à moi !"
    emeraude "Quand Madame Arc-en-Ciel nous dit ce que l'on peut être !"
    emeraude "Moi, je m'appelle Émeraude, gardien de Couleurs."
    emeraude "Boule de Cristal, du pareil au même."
    emeraude "Moi, je m'appelle Émeraude, gardien de Couleurs."
    emeraude "Quand je rêve de Madame Arc-en-Ciel, c'est Émeraude qui saigne."
    show blanche neutral open at left
    blanche "J'ai l'impression que tout ce que tu dis, ce sont des paroles de différentes chansons."
    show blanche neutral close at left
    emeraude "C'est pas ma faute, et quand je donne ma langue au chat, je vois les autres…"
    emeraude "Tout prêts à se jeter sur moi… C'est pas ma faute à moi !"
    show blanche pout open at left
    blanche "Arf… Cela va être difficile de communiquer…"
    show blanche neutral open at left
    blanche "Réfléchissons..."
    show blanche surprised open at left
    show crystal_green at crystal_position with dissolve
    blanche "Ah ! Je sais déjà que tu as un contrat avec Madame Arc-en-Ciel pour garder ta boule de cristal."
    show blanche cry open at left
    blanche "Mais, s'il te plaît, juste pour une nuit, pour mon papa. C'est ma mission."
    show blanche cry close at left
    emeraude "Ma mission n'a qu'une seule façon ! De tourner le monde ! De le changer !"
    show blanche cry open at left
    blanche "S'il te plaît, aide-moi !"
    blanche "Mon papa a aussi une mission de la part de Madame Arc-en-Ciel !"
    show blanche neutral open at left
    blanche "Il m'a dit qu'il est très important comme Madame Arc-en-Ciel !"
    show blanche cry open at left
    blanche "Mais il est malade, alors il ne peut rien faire…."
    show blanche neutral open at left
    blanche "C'est pour ça que je veux lui remonter le moral ! Une dernière fois…"
    show blanche neutral close at left
    emeraude "Non, non, non, non ! Je ne peux pas m'en passer ! Non, non, non, non !"
    show blanche cry open at left
    hide crystal_green at crystal_position with dissolve
    blanche "Zut, comment je peux convaincre Émeraude…"

    menu:
        "Tirer une de ses oreilles et lui crier de dessus d'arrêter de chanter":
            $ bad +=1
            show blanche pout open at left
            blanche "Arrête de chanter et écoute-moi !!!" with vpunch
            show blanche pout close at left
            emeraude "Est-ce que tu m'entends ? Hé ho !"
            show blanche pout open at left
            blanche "ARRÊTE DE CHANTER !" with vpunch
            blanche "Il faut que je récupère cette boule de cristal rapidement !"
            blanche "Je n'ai pas le temps de discuter avec toi !"
            show blanche pout close at left
            emeraude "J'ai pas le teeemps !!! Mon espriiiiiit glisse ailleurs !"
            show blanche cry open at left
            blanche "S'il te plaît…"
            show blanche cry close at left
            "Je commence à pleurer."
            emeraude "..."
        "Faire les yeux du Chat Potté [encore]":
            $ neutral +=1
            show blanche cry close at left
            "Cela a marché avec Violet, peut-être que ça marchera aussi avec Émeraude."
            "Je lui fais les yeux du Chat Potté."
            emeraude "[player_name] a les yeux revolver. [player_name] a le regard qui tue."
            emeraude "[player_name] m'a touchée, c'est foutu."
        "Demander en chantant":
            $ good +=1
            show blanche neutral open at left
            blanche "Comment puis-je oublier ce coin de paradis ?"
            show blanche smile open at left
            blanche "Ce petit bout de terre où vit encore mon père ?"
            show blanche neutral open at left
            blanche "Comment pourrais-je faire pour récupérer la boule de cristal ?"
            show blanche cry open at left
            blanche "Et qu'on… Hmpf. AÏÏÏeeeuhhh."
            show blanche cry close at left
            "J'ai mordu ma langue."
            emeraude "Ho ho. Je… Je t'aime comme une chanson d'amour, baby. Ho ho."

    emeraude "À l'aide ! J'ai besoin de quelqu'un ! À l'aide ! Pas n'importe qui ! À l'aide ! Tu sais, j'ai besoin de [player_name] !"
    show blanche surprised open at left
    blanche "Que ? Quoi ?! Qu'est-ce qui se passe ?!"
    show blanche surprised close at left
    emeraude "Je troque ma boule de cristal contre une aide."
    emeraude "J'échangerai ma vie à moi, confortable et sans lacune."
    emeraude "Il existe un memory virtuel et différent."
    emeraude "Où chaque seconde fait de nous des combattants."
    emeraude "Notre seul espoir est de tout réassocier..."
    show blanche surprised open at left
    blanche "Un memory…"
    show blanche neutral open at left
    blanche "Bon, on y va et on saura ce que je dois faire."
    hide emeraude at right
    hide blanche neutral open at left
    with dissolve
    call screen chap4_memory_game('chap4_2', 'memory_game_timeout')

label memory_game_timeout:
    show emeraude at right with dissolve
    emeraude "Oh non ! Encore une fois !"
    hide emeraude at right with dissolve
    call screen chap4_memory_game('chap4_2', 'memory_game_timeout')

label chap4_2:
    scene garden
    show emeraude at right
    show blanche neutral close at left
    with dissolve
    emeraude "Yeah ! Bravo ! Oui, viens danser ! Oui, c'est la vie, la la la la la !"
    emeraude "Voilà, voilà, voilà, voilà la boule de cristal."
    scene noir_colors_3 with dissolve
    pause 2
    scene noir_colors_4 with dissolve
    pause 2
    scene garden
    show emeraude at right
    show blanche neutral close at left
    with dissolve
    emeraude "Et si mon heure sonne, oh oh. Pleure pas rigole, oh oh. On m'appelle l'Émeraude."
    show blanche neutral open at left
    blanche "Merci ! Merci Émeraude ! Tu me sauves !"
    show blanche surprised open at left
    blanche "Zut, il ne me reste plus beaucoup de temps."
    show blanche neutral open at left
    blanche "Il faut que je me dépêche."
    hide blanche neutral close at left with dissolve
    emeraude "Libérée, délivrée, je n'ai plus de boules à m'occuper, libérée, délivrée, c'est décidé, c'est fini !"
    emeraude "J'ai laissé mon contrat en été, perdu avec [player_name] !"
    emeraude "La boule Vert est pour moi le prix de la liberté !" 
    hide emeraude at right with dissolve
    "Quelques minutes plus tard…"
    show emeraude at right with dissolve
    emeraude "Poum, poum, poum, poum !"
    show maigrichon at farLeft
    show grosso at nearLeft
    with dissolve
    grosso "Émeraude !" with vpunch
    grosso "Dis-moi as-tu vu un enfant de cette taille ?"
    emeraude "Je ne sais pas."
    emeraude "Comment te dire ?"
    emeraude "J'aurais peur de tout foutre en l'air !"
    grosso "Ah oui…"
    grosso "C'est vrai qu'il faut chanter…"
    grosso "C'est oui ou bien c'est non ?"
    maigrichon "Ah !" with vpunch
    maigrichon "La boule Vert n'est plus là !"
    grosso "Encore une de perdue ?!"
    grosso "Aaah… Où est-ce que cet enfant a-t-il bien pu aller ?"
    hide maigrichon at farLeft
    hide grosso at nearLeft
    with dissolve
    "Emeraude les voit s'en aller."
    emeraude "Minuit se lève, en haut des tours, les voix se taisent et tout devient aveugle et sourd, la nuit camoufle, pour quelques heures, la zone [player_name] de ces nuisibles visiteurs !"
    jump chap5
