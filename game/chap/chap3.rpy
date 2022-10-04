label chap3:
    call titlepage(3)
    scene forest 
    play music music.Theme_Cyan fadein 1.0 volume 0.7
    show blanche surprised open at left
    with dissolve
    play sound renpy.random.choice(sound.Blanche_Amazement)
    blanche "Oh ! C'est... C'est le duo des Cyanmois que je vois au loin !" with vpunch
    show blanche neutral open at left
    blanche "Le présentateur Cyan est très connu du grand public pour son émission Jean Racine et des Saules."
    show blanche smile open at left
    blanche "D'après mon papa, lui et son frère vont à travers les forêts du monde présenter aux autres chats les beautés de la nature."
    show blanche neutral open at left
    blanche "Il faut que j'aille leur parler !"
    show blanche neutral close at left
    show cyan at right with dissolve
    play sound renpy.random.choice(sound.Cyan_Speak)
    cyan "Bonjour à toutes et tous !"
    cyan "Bienvenue dans Jean Racine et des Saules, l'émission d'Art et Culture la plus connue du Monde 2 ! "
    show blanche neutral open at left
    blanche "Bonjour. Désolé de te déranger, je voudrais savoir…"
    hide blanche neutral close at left
    hide cyan at right
    show cyan2
    play sound renpy.random.choice(sound.Cameraman_Angry_Low)
    cameraman "Chuuuuuuuuuut !" with vpunch
    show cyan2 at right with move
    show cyan at left with dissolve
    play sound renpy.random.choice(sound.Cyan_Speak)
    cyan "Nous voici donc dans la forêt Arc-en-Ciel, très connue pour sa rivière, mais surtout pour ses truites."
    cyan "Admirez donc ces magnifiques chênes centenaires, ces hêtres majestueux et ces petits sapins."
    cyan "Tous sont le fruit d'une collaboration entre l'être humain et la nature."
    cyan "Observons maintenant les truites."
    play sound renpy.random.choice(sound.Cameraman_Embarassed)
    cameraman "Je suis désolé chaton, mais nous n'avons pas réussi à trouver de truites Arc-en-Ciel dans la rivière. Nous avons seulement quelques truites farios."
    cameraman "Un simple amateur de poisson verra la différence. Je coupe la bande vidéo le temps de trouver une solution."
    play sound renpy.random.choice(sound.Cyan_Exclamation)
    cyan "Mais c'est horrible ! Qu'allons-nous dire à nos téléspectateurs ?!" with vpunch
    cyan "Nous ne pouvons pas les décevoir."
    cyan "Présenter la forêt Arc-en-Ciel sans ses truites, c'est comme présenter des crêpes sans oeufs."
    cyan "C'est impensable ! Inimaginable !" with vpunch
    play sound renpy.random.choice(sound.Cameraman_Speak)
    cameraman "Cela peut prendre plusieurs heures : les truites Arc-en-Ciel se font de plus en plus rares dans la rivière depuis les sécheresses des dernières années et leur pêche intensive."
    show cyan2 at farRight
    show cyan at center
    with move
    show blanche neutral open at farLeft with dissolve
    play sound renpy.random.choice(sound.Blanche_Question)
    blanche "Excuse-moi, j'ai une question à te poser : je cherche la bou..."
    show blanche neutral close at farLeft
    play sound renpy.random.choice(sound.Cameraman_Angry)
    cameraman "Ça suffit comme ça ! On est en plein tournage, ouste !" with vpunch

    menu:
        "Le traiter de méchant":
            $ bad +=1
            show blanche pout open at farLeft
            play sound renpy.random.choice(sound.Blanche_Sniffing)
            blanche "Méchant ! T'es trop méchant ! Je boude."
            show blanche pout close at farLeft
            play sound renpy.random.choice(sound.Cameraman_Speak)
            cameraman "Ce n'est pas ce que j'ai voulu dire, mais tu m'as compris. Tu nous gênes."
            show blanche cry open at farLeft
            blanche "Pourquoi t'es aussi méchant ? Qu'est-ce que j'ai fait ?"
            show blanche cry close at farLeft
            cameraman "Je n'aime pas les enfants, c'est tout."
            show blanche neutral open at farLeft
            blanche "Ne sous-estime pas les enfants ! On est capable de faire pleins de choses !"
            show blanche neutral close at farLeft
            cyan "Ah oui ? Comment pourrais-tu nous aider ?"
        "Partir chercher la boule ailleurs":
            $ neutral +=1
            play sound renpy.random.choice(sound.Cyan_Happy)
            cyan "Oh que vois-je ? Un visiteur venu d'ailleurs ! Ne t'en va pas !"
            cyan "Que viens-tu faire ici ?"
            show blanche cry open at farLeft
            blanche "C'est que... C'est un peu compliqué, vous n'allez sans doute pas me comprendre."
            show blanche cry close at farLeft
            cyan "De quoi s'agit-il ?"
        "Lui répondre poliment":
            $ good +=1
            show blanche pout open at farLeft
            play sound renpy.random.choice(sound.Blanche_Yes_Haughty)
            blanche "Excuse-moi, mais j'ai l'impression que je ne gêne plus tant que ça."
            blanche "Poser une simple question ne devrait pas être un problème."
            show blanche pout close at farLeft
            play sound renpy.random.choice(sound.Cameraman_Embarassed)
            cameraman "Bon, OK, mais pas longtemps alors."
            show blanche neutral open at farLeft
            blanche "Merci."
            show blanche neutral close at farLeft
            cyan "Hum ? Qu'y a-t-il ?"

    show blanche neutral open at farLeft
    blanche "Je recherche actuellement la boule Cyan."
    blanche "Je vous propose un marché : je vous pêche une truite Arc-en-Ciel et en échange vous m'aidez à trouver la boule Cyan. Ça vous va ?"
    show blanche neutral close at farLeft
    play sound renpy.random.choice(sound.Cameraman_Angry)
    cameraman "Mais, c'est que ce gosse est cinglé ?!" with vpunch
    cyan "Hum... Pourquoi je devrais te croire ?"
    show blanche cry open at farLeft
    blanche "C'est... C'est que..."
    show blanche cry close at farLeft
    show crystal_cyan at Position(xalign=0.30, yalign=0.5) with dissolve
    cyan "Cette boule Cyan que tu cherches est en ma possession."
    cyan "Nous ne sommes pas censés nous en séparer. Cela fait partie des clauses de notre contrat et le duo Cyanmois ne saurait faillir !"
    hide crystal_cyan at Position(xalign=0.30, yalign=0.5) with dissolve
    show blanche smile open at farLeft
    blanche "Croyez-moi ! Je suis un expert de la pêche ! Mon papa Noir m'a appris quand j'étais jeune !" with vpunch
    show blanche cry open at farLeft
    play sound renpy.random.choice(sound.Blanche_Sniffing)
    blanche "Mais maintenant il est très malade, il ne peut plus se lever..."
    show blanche neutral open at farLeft
    blanche "Il m'a raconté qu'il aimerait voir les couleurs de l'arc-en-ciel une dernière fois."
    show blanche smile open at farLeft
    blanche "C'est pour ça que j'aimerais lui faire une surprise !"
    show blanche neutral close at farLeft
    play sound renpy.random.choice(sound.Cyan_Exclamation)
    cyan "L'enfant de Noir ?!" with vpunch
    cyan "C'est une légende vivante en matière de pêche !"
    show blanche smile open at farLeft
    play sound renpy.random.choice(sound.Blanche_Yes)
    blanche "Oui ! Noir est mon papa ! Je ne pensais pas que mon papa était si connu !"
    show blanche cry open at farLeft
    blanche "À la maison, tout est noir et blanc. Il n'y a pas beaucoup de couleur."
    blanche "C'est peut-être pour ça que je n'ai jamais rien su de sa notoriété."
    show blanche cry close at farLeft
    cyan "Noir était un grand pêcheur. J'avais fait un de mes tout premiers reportages sur la rivière Dark Quidor, une rivière très sombre qui absorbe tous les malheurs du monde."
    cyan "À cette époque, ton père espérait attraper le brochet doré, une légende locale."
    cyan "Malheureusement, le malheur est venu auprès de ton père. Son amour de la pêche l'aura aveuglé à jamais."
    cyan "Je me souviens que tous les journaux de l'époque en avaient parlé, c'est une véritable tragédie."
    show blanche cry open at farLeft
    blanche "Oui, je le sais..."
    blanche "Depuis quelque temps, son état se dégrade. J'espère que j'aurai le temps de lui montrer les sept couleurs de l'arc-en-ciel."
    show blanche cry close at farLeft
    cyan "Bon, dans ce cas, c'est d'accord."
    show blanche neutral open at farLeft
    blanche "C'est vrai ?!" with vpunch
    show blanche neutral close at farLeft
    cameraman "Mais, Cyan, c'est de la folie !" with vpunch
    cyan "On n'a pas trop le choix sinon le reportage est foutu. Alors si ça peut faire plaisir à Noir, je veux bien faire ce geste."
    cyan "Tu vois ce lac d'où démarre la rivière ? C'est là que se trouvait plein de truites Arc-en-Ciel par le passé."
    cyan "Je te fournis la canne à pêche et je te souhaite bonne chance."
    cyan "J'aimerais reprendre le tournage dans un quart d'heure maximum."
    cyan "Ne traîne pas trop."
    scene lake_shallow with dissolve
    call screen chap3_lake_phishing

label chap3_2:
    scene forest
    show blanche smile open at farLeft
    show cyan2 at farRight
    show cyan at center
    with dissolve 
    # TODO : illu pêche
    blanche "Voilà ta truite Arc-en-Ciel !"
    show blanche neutral open at farLeft
    blanche "Ça faisait longtemps que je n'en avais pas pêché d'aussi grosse."
    show blanche neutral close at farLeft
    play sound renpy.random.choice(sound.Cyan_Happy)
    cyan "Mais, c'est extraordinaire !" with vpunch
    cyan "Je ne m'attendais pas à présenter une perle rare dans mon émission !"
    cyan "Tu as bien mérité ta récompense, voici la boule Cyan. Je compte sur toi pour me la rendre au plus vite car Madame Arc-en-Ciel ne voit pas toujours d'un très bon oeil ce genre d'arrangement."
    scene noir_colors_2 with dissolve
    pause 2
    scene noir_colors_3 with dissolve
    pause 2
    scene forest
    show cyan2 at farRight
    show cyan at center
    show blanche smile open at farLeft
    with dissolve
    blanche "Ne t'inquiète pas, je fais au plus vite, merci encore !"
    hide blanche smile close at farLeft with dissolve
    "Je m'éloigne et cours le long de la rivière."
    "Pendant ce temps, la prise de vue des Cyanmois reprend."
    show cyan2 at right
    show cyan at left
    with move 
    play sound renpy.random.choice(sound.Cyan_Speak)
    cyan "Voyez donc chers téléspectateurs !"
    cyan "Un admirateur exceptionnel de l'émission nous a donné cette truite Arc-en-Ciel fraîchement pêchée dans la rivière."
    cyan "Un véritable exemple…"
    play sound renpy.random.choice(sound.Grosso_Angry)
    x "Coupe cette caméra, s'il te plaît." with vpunch
    show cyan2 at farRight
    show cyan at nearRight
    with move
    show grosso at nearLeft behind cyan
    show maigrichon at farLeft behind grosso
    with dissolve
    cameraman "Mais…"
    maigrichon "Ne discute pas. On a quelques mots à vous dire à tous les deux."
    cyan "Je suppose que vous venez de nous voir remettre la boule Cyan à cet enfant et que vous désapprouvez cette démarche."
    cyan "Je ne prendrai même pas la peine de vous expliquer, vous ne comprendriez pas."
    cyan "Je sais également ce que je risque et j'en suis tout à fait conscient."
    grosso "Pfff… Pathétique."
    grosso "Dis-nous au moins où cet enfant est parti, cela nous facilitera la tâche et permettra peut-être d'alléger ta peine."
    cyan "N'y comptez pas."
    play sound renpy.random.choice(sound.Maigrichon_Exclamation)
    maigrichon "Je l'ai vu remonter le cours de la rivière de toute façon. Dépêchons-nous !"
    "Grosso et Maigrichon partent en direction des hautes herbes."
    stop music fadeout 2.0
    jump chap4
