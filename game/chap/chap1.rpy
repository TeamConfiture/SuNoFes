label chap1:
    call titlepage(1)
    scene mulberry_search
    show mulberry at mulberry_position
    show blanche surprised open at left
    with dissolve 
    blanche "Woah ! Tout est violet ! Il y a pleins de fleurs !!!" with vpunch
    show blanche smile open at left 
    blanche "Je vais en cueillir une pour mon papa."
    show blanche smile close at left 
    show violet at right with dissolve
    x "MIAAOOOUUU !" with vpunch
    show blanche cry open at left 
    blanche "Aïeeeuuuuhhh" with vpunch
    show blanche cry close at left 
    "Un chat vient de me griffer au moment où j'allais cueillir une fleur."
    show blanche cry open at left
    blanche "Méchant ! Méchant chat ! Tu m'as fait mal !"
    show blanche cry close at left 
    x "Eh toi, tu n'as aucun respect pour les lieux ! On ne cueille pas des fleurs sans autorisation."
    show blanche surprised open at left
    blanche "Un chat qui parle ! C'est la première fois que j'en vois un !"
    show blanche surprised close at left
    x "Comment ça ? Bien sûr que je parle et tout le monde le sait !"
    x "Toi, tu n'as pas dû sortir souvent pour dire de telles âneries."
    show blanche neutral open at left
    blanche "Oh ! Il y a de la lavande ici ! Oh ! Il y a des lilas là-bas !"
    show blanche neutral close at left
    x "Eh tu m'écoutes ?!" with vpunch
    show blanche surprised open at left
    blanche "Ah ! Oui… Pardon, monsieur le chat."
    show blanche neutral close at left
    x "Monsieur le chat ?! Vraiment ?!"
    x "Tss, la jeunesse n'a plus aucun respect envers les gardiens de Couleurs. Ça donne des surnoms à tout va, maintenant."
    violet "Je m'appelle Violet Evagaden. Mais, appelle-moi Violet. Souviens-toi-en."
    show blanche surprised open at left
    blanche "Tu es un gardien de Couleurs ?!" with vpunch
    show blanche surprised close at left
    violet "En effet. Je suis le gardien du Violet."
    show blanche neutral open at left
    blanche "Trop bien ! Moi aussi ! Je suis le gardien de [player_name] !"
    show blanche neutral close at left
    violet "Non, mais j'hallucine ! C'est que cet enfant se moque de moi, ma parole !"
    violet "Toi, un gardien de Couleurs ? Il y en a que sept et ce sont tous des chats !"
    violet "Tu ne peux pas être un gardien, c'est impossible !"
    show blanche cry open at left
    blanche "Oh, vraiment ? C'est dommage. Je voulais aussi être gardien…"
    show blanche cry close at left
    violet "Eh… Ne pleure pas ! Tu sais, c'est une vraie corvée ce métier. On doit constamment surveiller cette boule en mousse que tu vois là."
    show crystal_purple at crystal_position with dissolve
    show blanche surprised open at left
    blanche "Oh ! Mais ! C'est une des sept boules de cristal !" with vpunch
    show blanche surprised close at left
    violet "En effet ! Elle est jolie, hein ?"
    show blanche smile open at left
    hide crystal_purple at crystal_position with dissolve
    blanche "Je peux l'avoiiiiirrr ????"
    show blanche smile close at left
    violet "Sapristi ! Tu es malade ?!! Si je la perds, pouf, plus violet !"
    violet "Plus de violet, plus de mûres, plus de manger pour moi…"
    violet "Et Madame Arc-en-Ciel va me gronder."
    violet "Brrr, j'imagine déjà sa colère."
    show blanche cry open at left
    blanche "Mais ! Je suis là pour récupérer cette boule de cristal."
    show blanche cry close at left
    violet "Non, je n'ai pas le droit de te la donner."

    menu:
        "Faire les yeux du chat potté":
            $ encore =_("(encore)")
            "Je lui fais les yeux du chat potté."
            violet "Oh nooooooooooon pas ces yeeeuuxxx. Ils sont trop mignons."
            show blanche cry open at left
            blanche "S'il te plaaaîîîîîîît !"
            show blanche cry close at left
        "Demander poliment.":
            show blanche neutral open at left
            blanche "Est-ce que je peux récupérer ta boule de cristal, s'il te plaît ?"
            show blanche neutral close at left
            violet "Non, c'est ma propriété !"
            show blanche cry open at left
            blanche "Mais, j'ai vraiment besoin de cette boule de cristal."
            show blanche cry close at left
            "Je commence à pleurer."
        "Lui arracher la boule des mains.":
            show blanche pout close at left
            "J'essaye de lui arracher la boule des mains."
            violet "MIAAOOOUUU !" with vpunch
            show blanche cry open at left
            blanche "Aïeeeuuuuhhh"
            show blanche cry close at left
            "Mais, Violet me griffe."
            violet "Vilain enfant ! On ne t'a jamais appris les bonnes manières ?!" with vpunch
            show blanche cry open at left
            blanche "Pardon… Mais, j'ai vraiment besoin de cette boule de cristal."
            show blanche cry close at left
            "Je commence à pleurer."

    violet "Bon, ok, ok ! Je te la prête… Mais, pour une journée et seulement si tu m'aides !"
    show blanche surprised open at left
    blanche "C'est vrai ?!" with vpunch
    show blanche surprised close at left
    violet "J'ai besoin que tu me cueilles une mûre spéciale ! Elle est quelque part dans le jardin. J'en ai besoin pour écrire des lettres."
    show blanche surprised open at left
    blanche "Mais comment je vais la trouver ?!"
    show blanche surprised close at left
    violet "C'est une mûre qui brille de mille feux, tu ne vas pas la rater."
    hide blanche
    hide violet
    with dissolve
    call mulberry_search
    hide mulberry
    show violet at right
    show blanche smile close at left
    with dissolve
    violet "C'est bien ça ! Félicitations, tu as trouvé la mûre que je voulais !"
    violet "Il faudra que tu me rendes la boule avant minuit ! Sinon, plus de violet…"
    show blanche neutral open at left
    blanche "Plus de mûre, plus de manger pour toi… et Madame Arc-en-Ciel, pas contente !"
    show blanche neutral close at left
    violet "Tout à fait !"
    violet "Tiens, voilà la boule !"
    # TODO : <anime boule + Noir gagne une couleur>
    show blanche smile open at left
    blanche "Youpi !!! Encore six !" with vpunch
    show blanche smile close at left
    violet "Six ? Attends ?! Ne me dis pas que tu veuilles récupérer toutes les boules ?!"
    show blanche neutral open at left
    blanche "Bah oui ? Pourquoi ? Elles sont si jolies."
    show blanche neutral close at left
    violet "Erf… Petit enfant, fais attention. C'est dangereux ce que tu fais. Si Madame Arc-en-Ciel l'apprend, c'en est fini de toi… Et pour nous les gardiens aussi…"
    violet "Erf… Je regrette déjà de te prêter ma boule."
    "Je lui tapote la tête."
    show blanche smile open at left
    blanche "N'aies pas peur ! Pas de problème pour moi ! Je cours vite ! Elle ne saura rien !"
    show blanche smile close at left
    violet "Si tu le dis…"
    violet "J'imagine que tu vas au Lac Indigo maintenant ?"
    show blanche neutral open at left
    blanche "Oui !"
    show blanche neutral close at left
    violet "Bon, prends soin de toi."
    # scene cg1 with dissolve
    "Violet me fait un signe d'au revoir."
    show blanche neutral open at left
    blanche "Oui ! Merci Violet ! Je te promets que je te rendrai la boule !"
    scene mulberry_search with dissolve
    "Quelque part dans le jardin des violettes…"
    x "Maigrichon, j'en ai marre de ces patrouilles nocturnes… Il ne se passe jamais rien."
    show maigrichon at left
    show grosso at right
    with dissolve
    maigrichon "Grosso, ne m'en parle pas, j'ai tellement sommeil… zzzz"
    grosso "AAAHHH" with vpunch
    maigrichon "Que ? Quoi ?! Ça ne va pas de crier comme ça ?!!!"
    grosso "Là-bas ! Au vol !"
    maigrichon "Quoi ?! Un enfant ? Avec…"
    grosso_maigrichon "UNE BOULE DE CRISTAL ???!!!" with vpunch
    maigrichon "Vite, suivons-le !!!"
    grosso "Et prévenons Madame Arc-en-Ciel !"
    hide maigrichon
    hide grosso
    with dissolve
    "Les gardes parcourent le jardin des violettes et disparaissent par le petit chemin du fond."
    jump chap2

#####
# Cette section est dédiée à la récupération d'UNE mûre
# Si vous êtes capables de faire plus court, lâchez-vous
# Je hais ren'py
#
# La mûre est affichée deux fois, une fois en fond pour persister
# lors des dialogues, et une fois en tant que bouton.

# Chasse à la mûre
label mulberry_search:
    if 'mulberry_found' in vars() and mulberry_found:
        return
    else:
        $ mulberry_found = False
        window hide
        # La position de cette mûre n'est pas modifiée avec l'autoreload,
        # il faut faire un cycle de dialogue avant
        hide mulberry
        call screen wait_for_mulberry_click

# Gestion du clic sur la mûre ici
screen wait_for_mulberry_click():
    button: # Button that covers the whle background
        action Jump ("onclick_mulberry_background")
    hbox at mulberry_position:
        imagebutton:
            idle "mulberry"
            hover "mulberry_button"
            focus_mask True
            action Jump ("onclick_mulberry")
    
label onclick_mulberry:
    $ mulberry_found = True
    jump mulberry_search

label onclick_mulberry_background:
    show mulberry at mulberry_position
    show violet at right
    violet "Alors tu as trouvé ?"
    hide violet
    show blanche pout close at left
    blanche "Pas encore…"
    hide blanche
    jump mulberry_search
