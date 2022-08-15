label chap1:
    $ chap += 1
    call titlepage(chap)
    #TODO: mettre le bg
    #TODO: mettre les expressions de Blanche, position à gauche et Violet, position à droite
    "Woah ! Tout est violet ! Et il y a pleins de fleurs !!!"
    "Je vais en cueillir une pour mon papa."
    show violet at right with dissolve
    x "MIAAOOOUUU !"
    "Aïeeeuuuuhhh"
    "Un chat vient de me griffer au moment où j'allais cueillir une fleur."
    show blanche cry open at left with dissolve
    blanche "Méchant ! Méchant chat ! Tu m'as fait mal !"
    x "Eh toi, tu n'as aucun respect pour les lieux ! On ne cueille pas des fleurs sans autorisation."
    show blanche surprised open at left
    blanche "Un chat qui parle ! C'est la première fois que j'en vois un !"
    x "Comment ça ? Bien sûr que je parle et tout le monde le sait !"
    x "Toi, tu n'as pas dû sortir souvent pour dire de telles âneries."
    blanche "Oh ! Il y a de la lavande ici ! Oh ! Il y a des lilas là-bas !"
    x "Eh tu m'écoutes ?!"
    show blanche cry close at left
    blanche "Ah ! Oui… Pardon, monsieur le chat."
    x "Monsieur le chat ?! Vraiment ?!"
    x "Tss, la jeunesse n'a plus aucun respect envers les gardiens de Couleurs. Ça donne des surnoms à tout va, maintenant."
    violet "Je m'appelle Violet Evagaden. Mais, appelle-moi Violet. Souviens-toi-en."
    show blanche neutral close at left
    blanche "Tu es un gardien de Couleurs ?"
    violet "Affirmatif. Je suis le gardien de Violet"
    show blanche neutral open at left
    blanche "Trop bien ! Moi aussi ! Je suis le gardien de [player_name] !"
    violet "Non, mais j'hallucine ! C'est que cet enfant se moque de moi, ma parole !"
    violet "Un gardien de Couleurs, il y en a que sept ! Et ce ne sont que des chats !"
    violet "Tu ne peux pas être un gardien, c'est impossible !"
    show blanche cry close at left
    blanche "Oh, vraiment ? C'est dommage. Je voulais aussi être gardien…"
    violet "Eh… Ne pleure pas ! Tu sais, c'est une vraie corvée ce métier. On doit constamment surveiller cette boule en mousse que tu vois là."
    show blanche surprised close at left
    blanche "Oh ! Mais ! C'est une des sept boules de cristal !"
    violet "Affirmatif ! Elle est jolie, hein ?"
    show blanche smile open at left
    blanche "Je peux l'avoiiiiirrr ????"
    violet "Sapristi ! T'es malade ?!! Si je la perds, pouf, plus violet !"
    violet "Plus de violet, plus de mûres, plus de manger pour moi !"
    violet "Et… Madame Arc-en-Ciel va me gronder…"
    violet "Brrr, j'imagine déjà sa colère."
    show blanche cry close at left
    blanche "Mais, je suis venu ici récupérer cette boule de cristal."
    violet "Non, je n'ai pas le droit de te la donner."

    menu:
        "Faire les yeux du chat potté":
            "Je lui fais les yeux du chat potté."
            violet "Oh nooooooooooon pas ces yeeeuuxxx. Ils sont terribles."
            blanche "S'il te plaaaîîîîîîît !"
        "Demander poliment.":
            blanche "Est-ce que je peux récupérer ta boule de cristal, s'il te plaît ?"
            violet "Non, c'est ma propriété !"
            blanche "Mais, j'ai vraiment besoin de cette boule de cristal."
            "Je commence à pleurer."
        "Lui arracher la boule des mains.":
            "J'essaye de lui arracher la boule des mains."
            violet "MIAAOOOUUU !"
            blanche "Aïeeeuuuuhhh"
            "Mais, Violet me griffe."
            violet "Vilain enfant ! On ne t'a jamais appris les bonnes manières ?!"
            blanche "Pardon… Mais, j'ai vraiment besoin de cette boule de cristal."
            "Je commence à pleurer."

    violet "Bon, ok, ok ! Je te la prête… Mais, pour une journée et seulement si tu m'aides !"
    show blanche surprised open at left
    blanche "C'est vrai ?!"
    violet "J'ai besoin que tu me cueilles une mûre spéciale ! Elle est quelque part dans le jardin. J'en ai besoin pour écrire des lettres."
    show blanche neutral close at left
    blanche "Mais, comment je vais la trouver ?!"
    violet "C'est une mûre qui brille de mille feux, tu ne vas pas la rater."
    # TODO: rendre le chat cliquable et une mûre cliquable
    # if found:
    #     violet "C'est bien ça ! Bravo, tu as trouvé la mûre que je voulais !"
    # else:
    #     violet "Alors tu as trouvé ?"
    #     show blanche pout close at left
    #     blanche "Pas encore…"
    #loop

    violet "Il faudra que tu me rendes la boule avant minuit ! Sinon, plus de violet…"
    show blanche smile close at left
    blanche "Plus de mûre, plus de manger pour toi ! Et Madame Arc-en-Ciel, pas contente !"
    violet "Affirmatif !"
    violet "Tiens, voilà la boule !"
    # TODO : <anime boule + Noir gagne une couleur>
    show blanche smile open at left
    blanche "Youpi !!! Encore six !"
    violet "Six ? Attends ?! Ne me dis pas que tu veuilles récupérer toutes les boules ?!"
    show blanche neutral close at left
    blanche "Bah oui ? Pourquoi ? Elles sont si jolies."
    violet "Erf… Petit enfant, fais attention. C'est dangereux ce que tu fais. Si Madame Arc-en-Ciel l'apprend, c'en est fini de toi… Et pour nous les gardiens aussi…"
    violet "Erf… Je regrette déjà de te prêter ma boule."
    "Je lui tapote la tête."
    show blanche smile open at left
    blanche "N'aies pas peur ! Pas de problème pour moi ! Je cours vite ! Elle ne saura rien !"
    violet "Si tu le dis…"
    violet "J'imagine que tu vas au Lac Indigo maintenant ?"
    blanche "Oui !"
    violet "Bon, prends soin de toi."
    "Violet me fait un signe d'au revoir."
    show blanche smile close at left
    blanche "Oui ! Merci Violet ! Je te promets que je te rendrai la boule !"
    hide blanche
    hide violet
    # TODO : <illu chat qui fait signe d'adieu et blanche qui tiens la boule>


    "Quelques parts dans le jardin des violettes…"
    x "Maigrichon, j'en ai marre de ces patrouilles nocturnes… Il ne se passe jamais rien."
    show maigrichon at left
    show grosso at right
    with dissolve
    maigrichon "Grosso, ne m'en parle pas, j'ai tellement sommeil… zzzz"
    grosso "AAAHHH" with vpunch
    maigrichon "Que ? Quoi ?! Ça ne va pas de crier comme ça ?!!!"
    grosso "Là-bas ! Au vol !"
    maigrichon "Quoi ?! Un enfant ? Avec…"
    grosso_maigrichon "UNE BOULE DE CRISTAL ???!!!"
    maigrichon "Vite, suivons-le !!!"
    grosso "Et prévenons Madame Arc-en-ciel !"
    "Les gardes parcourent le jardin des violettes. Ayant perdu Blanche de vue, ils disparaissent par le petit chemin du fond."
    return
