label chap6:
    call titlepage(6)
    scene piano
    with dissolve
    play music music.Theme_Orange fadein 1.0 volume 0.7
    "On entend au loin du Mozart. Un clavier couleur d'orange est posé là, bien au centre de l'orangeraie."
    "Un chat est en train de jouer."
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Amazement)
    blanche "Oh ! On dirait les quatre saisons de Vivaldi !" with vpunch
    show blanche neutral open at left
    blanche "À moins que ça ne soit le Menuet de Bach ?"
    show blanche neutral close at left
    show orange at right with dissolve
    voice renpy.random.choice(audio.Orange_Irritated)
    x "Mais de qui oses-tu donc te moquer ? Moi, Orange, votre serviteur, j'étais en train de jouer le Requiem de herr Wolfgang Amadeus Mozart, cette oeuvre à jamais incomplète, mais qui représente tout le génie du grand maître !"
    show blanche cry open at left
    voice renpy.random.choice(audio.Blanche_Sniffing)
    blanche "Excuse-moi, je ne m'y connais pas trop dans l'art musical."
    show blanche neutral open at left
    blanche "Mon papa était plutôt adepte de la pêche."
    show blanche smile open at left
    blanche "Il était très connu ! Tu en as peut-être entendu parlé ? Il s'appelle Noir !"
    show blanche smile close at left
    voice renpy.random.choice(audio.Orange_Speak)
    orange "Noir... Je connais très bien ce nom."
    orange "Ton père venait souvent ici après sa rupture..."
    orange "Il disait que sa vie n'avait plus aucun sens, mais que, dans ce lieu, cela n'avait plus d'importance."
    orange "Il restait là, allongé, pendant des heures à écouter votre bon vieux serviteur pester contre ses fausses notes."
    orange "Mais ce qui lui a véritablement redonné le sourire, c'est quand je me suis arrêté, triomphant, après avoir réussi à jouer le Requiem sans aucune erreur."
    orange "Paradoxalement, cela a été aussi la dernière fois que je l'ai vu dans mon antre d'agrumes..."
    show blanche neutral open at left
    voice renpy.random.choice(audio.Blanche_Laugh)
    blanche "Mon papa a toujours été comme ça, très empathique."
    show blanche smile open at left
    blanche "En fait, ce qui compte le plus pour lui, c'est le bonheur des autres, pas son propre bonheur."
    show blanche neutral open at left
    blanche "Le bien-être des gens lui redonne la santé. C'est comme si le soleil dans la vie des autres, lui rendait le sien !"
    show blanche cry open at left
    voice renpy.random.choice(audio.Blanche_Moan)
    blanche "Mais, c'est un cadeau à double tranchant..."
    blanche "Si les gens sont tristes, ça le rend très malade..."
    blanche "Là, mon papa n'est pas bien du tout ! Il est encore plus mal en point que d'habitude."
    show blanche neutral open at left
    blanche "C'est pour ça que je suis ici."
    blanche "Je veux récupérer la boule Orange pour lui rendre le sourire !"
    show blanche neutral close at left
    show crystal_orange at crystal_position with dissolve
    voice renpy.random.choice(audio.Orange_Speak)
    orange "C'est que je suis bien embêté..."
    orange "Non pas par le contrat que j'ai passé avec Madame Arc-en-Ciel, je me sens redevable vis-à-vis de ton père de m'avoir tenu compagnie pendant tout ce temps."
    orange "Mais, tu ne peux pas prendre la boule comme ça. Elle t'échapperait des mains."
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Exclamation)
    blanche "Ah bon ?"
    show blanche surprised close at left
    orange "Cette boule est un peu particulière..."
    orange "En effet, elle nécessite une certaine maîtrise de soi avant d'être manipulable."
    hide crystal_orange at crystal_position with dissolve
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Question)
    blanche "C'est vrai ? Comment on fait ça ?"
    show blanche surprised close at left
    voice renpy.random.choice(audio.Orange_Speak)
    orange "Il faut maîtriser la musique des agrumes. Il faut sentir ton corps vibrer en entendant le jus s'écouler."
    orange "De cette façon, tu pourras toujours entendre la musique des fluides, même celle de cette mystérieuse boule de cristal."
    orange "Moi par exemple, j'utilise une baguette. Avec ça, les agrumes se coupent, se déchirent et chantent selon ma volonté."
    orange "Si tu ne l'avais pas remarqué, mon piano est un peu spécial, chaque touche fait chanter une orange ou, pour les notes les plus aiguës, un citron."

    menu: 
        "Le prendre pour un fou":
            $ bad +=1
            show blanche pout open at left
            voice renpy.random.choice(audio.Blanche_Angry)
            blanche "Tu... Tu es fou ?!" with vpunch
            blanche "Tu crois vraiment ce que tu es en train de me raconter ?!"
            blanche "Comment des agrumes peuvent produire du son ? Comment est-ce que ça va me permettre de prendre la boule ?"
            show blanche pout close at left
            voice renpy.random.choice(audio.Orange_Irritated)
            orange "Eh bien, vas-y, essaye donc puisque tu as tellement confiance en toi !"
            orange "Mais je te garantis qu'après ça, tu reviendras me supplier de t'apprendre."
            orange "Après tout, il s'agit d'un art !"
            orange "Même si tu parviens à en maîtriser les rudiments pour emmener la boule, il ne suffit pas d'une vie pour comprendre les agrumes !"
            show blanche pout open at left
            voice renpy.random.choice(audio.Blanche_Yes_Haughty)
            blanche "Bien sûr ! Et moi, je suis Madame Arc-en-Ciel ! Bon, voyons voir…"
            show blanche pout close at left
            "On entend des bruits de verre."
            show blanche surprised open at left
            voice renpy.random.choice(audio.Blanche_Gasp)
            blanche "Aaaaaaah !" with vpunch
            show blanche surprised open at left
            blanche "Mais pourquoi elle m'échappe sans cesse des mains cette boule ?!"
            show blanche surprised close at left
            voice renpy.random.choice(audio.Orange_Speak)
            orange "Je viens de te le dire, mais tu ne veux pas m'écouter."
            orange "Tu manques de doigté."
        "Le prendre au sérieux":
            $ good +=1
            show blanche surprised open at left
            voice renpy.random.choice(audio.Blanche_Exclamation)
            blanche "Vraiment ? Tu peux m'apprendre ?" with vpunch
            show blanche neutral open at left
            blanche "Cela m'intéresse, surtout la musique de l'eau !"
            show blanche neutral close at left
            voice renpy.random.choice(audio.Orange_Speak)
            orange "Navré, je ne traite que les agrumes."
            orange "Cepedant, je peux te donner les bases pour apprendre avec l'eau."
            show blanche surprised open at left
            voice renpy.random.choice(audio.Blanche_Exclamation)
            blanche "C'est vrai ?! Est-ce qu'on pourrait commencer maintenant ?!" with vpunch
            show blanche surprised close at left
            voice renpy.random.choice(audio.Orange_Speak)
            orange "Pour sûr, allons-y."
        "Exiger qu'il démarre l'entraînement":
            $ neutral +=1
            show blanche neutral open at left
            blanche "Est-ce qu'on peut commencer l'entraînement ?"
            show blanche cry open at left
            voice renpy.random.choice(audio.Blanche_Sigh)
            blanche "Je n'ai malheureusement pas beaucoup de temps..."
            show blanche cry close at left
            voice renpy.random.choice(audio.Orange_Speak)
            orange "Doucement, doucement, si tu t'excites trop tu ne vas pas pouvoir ressentir les émotions des fruits et des fluides."
            orange "Tu n'écouteras que ta frustration." 
            voice renpy.random.choice(audio.Blanche_Moan)
            show blanche cry open at left
            blanche "Bon... D'accord."
            show blanche cry close at left
            orange "Ne sois pas bougon, viens je vais te montrer."
            show blanche neutral open at left
            blanche "Youpi ! On commence par quoi au juste ?" with vpunch
            show blanche neutral close at left

    orange "Tout d'abord il faut couper les agrumes."
    orange "Montre-moi comment tu te dépatouilles. 1... 2... 3..."
    hide blanche neutral close at left
    hide orange at right
    with dissolve
    call screen chap6_sprite_cutter('chap6_2', 'sprite_cutter_failed')

label sprite_cutter_failed:
    show blanche neutral close at left
    show orange at right
    with dissolve
    voice renpy.random.choice(audio.Orange_Irritated)
    orange "Non, pas comme ça ! Essaye encore !"
    show blanche cry open at left
    voice renpy.random.choice(audio.Blanche_Moan)
    blanche "Mais, c'est long !"
    show blanche cry close at left
    voice renpy.random.choice(audio.Orange_Speak)
    orange "Mais, non ! Je t'assure ! Tu vas y arriver !"
    hide blanche neutral close at left
    hide orange at right
    with dissolve
    call screen chap6_sprite_cutter('chap6_2', 'sprite_cutter_failed')

label chap6_2:
    show blanche surprised open at left
    show orange at right
    with dissolve
    voice renpy.random.choice(audio.Blanche_Exclamation)
    blanche "Oh ! Je m'attendais pas du tout à obtenir un son si parfait." with vpunch
    show blanche surprised close at left
    voice renpy.random.choice(audio.Orange_Speak)
    orange "C'est la magie des agrumes, mon enfant. Maintenant, tu devrais tenter de prendre la boule."
    orange "Je suis persuadé que tu vas y arriver."
    show blanche smile open at left
    voice renpy.random.choice(audio.Blanche_Laugh)
    blanche "Oh ! C'est incroyable, j'ai réussi à l'attraper !"
    scene noir_colors_5 with dissolve
    play sound sound.Unlock_Puzzle
    pause 1
    scene noir_colors_6 with dissolve
    pause 2
    scene piano
    show orange at right
    show blanche smile close at left
    with dissolve
    voice renpy.random.choice(audio.Orange_Speak)
    orange "Tu vois ! Je te l'avais dit !"
    orange "Que vas-tu donc faire de cette boule maintenant qu'elle est entre tes mains ?"
    show blanche neutral open at left
    blanche "Je vais repartir pour récupérer la dernière boule de couleur et retrouver mon papa !"
    show blanche neutral close at left
    orange "Avant ça, tiens. Je te donne une brique de jus d'orange."
    orange "Tu pourras la donner à ton père, je suis sûr que ça lui remontera le moral."
    show blanche smile open at left
    voice renpy.random.choice(audio.Blanche_Laugh)
    blanche "Merci ! Je n'oublierai pas ton aide !"
    show blanche neutral open at left
    blanche "À bientôt !"
    hide blanche neutral close at left 
    hide orange at right
    with dissolve
    "Quelques minutes plus tard..."
    voice renpy.random.choice(audio.Grosso_Gasp)
    x "Hmpf, Hmpf..."
    "Grosso et Maigrichon arrivent essouflés devant Orange."
    show maigrichon at farLeft
    show grosso at nearLeft
    show orange at right
    with dissolve
    voice renpy.random.choice(audio.Grosso_Angry)
    grosso "Hmpf, Hmpf... Arrête cet enf... Hmpf, Hmpf..."
    voice renpy.random.choice(audio.Maigrichon_Angry)
    maigrichon "Oui ! Cet enfant ne doit pas s'échapper ! Hmpf, Hmpf..."
    voice renpy.random.choice(audio.Orange_Speak)
    orange "Un petit remontant messieurs ?"
    orange "J'ai un de ces jus d'agrumes dont vous me direz des nouvelles."
    voice renpy.random.choice(audio.Grosso_Yes)
    grosso "Pourquoi pas... J'ai la gorge sèche."
    voice renpy.random.choice(audio.Maigrichon_Angry)
    maigrichon "Grosso !" with vpunch
    grosso "Bon, bon, plus tard alors, allons-y !"
    "Grosso et Maigrichon quittent Orange, le laissant seul devant son piano."
    stop music fadeout 2.0
    jump chap7
