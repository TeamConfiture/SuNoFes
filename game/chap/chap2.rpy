label chap2:
    call titlepage(2)
    scene star with dissolve 
    "Le soleil se couche… Au loin, un chat observe le crépuscule avec attention."
    show indigo at right with dissolve
    indigo "Aaaah… Ces étoiles sont si belles ! Un voyageur m'a autrefois dit que chacun de ces ensembles de points lumineux avaient des noms dans la langue de Molière."
    indigo "Si seulement je pouvais les connaître… Je serais alors en mesure de décrire le ciel que je vois et de pouvoir transmettre ces formidables connaissances aux futurs voyageurs qui s'arrêteront près de mon lac !"
    show blanche neutral open at left with dissolve
    blanche "Oh ! Il m'a l'air chouette ce lac ! Je vais mettre les pieds dans l'eau !"
    show blanche neutral close at left
    indigo "Non ! MIAOUUUUUU !" with vpunch
    show blanche surprised open at left
    blanche "Ah ! Mais, c'est quoi ça ?"
    show blanche surprised close at left
    indigo "Ce sont des ronces. Tu ne connais pas ? Quand on s'approche trop, elles te griffent aussi durement que si j'avais voulu t'attaquer."

    menu:
        "Le prendre de haut":
            show blanche pout open at left
            blanche "Bien sûr que si je connais, tu me prends pour qui ?"
            show blanche pout close at left
            indigo "Ce n'est pas l'impression que tu me donnais quand tu courais il y a 5 minutes…"
            indigo "Ma foi, comme tu es ici, il est de mon devoir de t'expliquer tout ce qu'il y a à savoir sur ce lieu. "
        "Se confondre platement en excuses":
            show blanche pout open at left
            blanche "Non mais j'ai cru que c'étaient des petits sapins, je pensais en ramener un pour Noël…"
            show blanche pout close at left
            indigo "Tu pourrais éviter de me prendre pour une courge, s'il te plaît ?"
            indigo "Ce lieu est connu pour son lac incontournable. Tous les voyageurs qui me rendent visite sont là pour admirer cette vue sublime. Il est donc proscrit de prendre quoi que ce soit de ce paysage."
            indigo "En parlant de ça, il est coutume ici de repartir de mon lac en ayant découvert quelque chose alors suis-moi. Regarde ! On peut apercevoir un cygne devant et là, des canards…"
        "Admettre son erreur":
            show blanche cry open at left
            blanche "Je suis désolé, je n'avais jamais vu de ronces de ma vie."
            show blanche cry close at left
            indigo "Ce n'est pas grave. Viens avec moi, je vais t'expliquer tout ce qu'il y a à savoir sur ce lieu."
            show blanche surprised open at left
            blanche "Mais…"
            show blanche surprised close at left
            indigo "Ne discute pas, c'est la coutume de repartir de mon lac en ayant découvert quelque chose. Tu vois là-bas ? Ce sont des roseaux ! On peut apercevoir un cygne devant et là, ce sont des canards, tu te rends compte de tout ce qui peut vivre ici ? Sans oublier les…"

    show blanche surprised open at left
    blanche "Ah ! Je… Je ne suis pas venu ici pour visiter le lac."
    show blanche surprised close at left
    "Le chat a l'air renfrogné."
    indigo "Vraiment ? Si tu n'es pas là pour admirer la beauté du paysage, alors que veux-tu exactement ?! Sache que sur mon chemin, nul n'est venu avec un autre objectif !"
    show blanche cry open at left
    blanche "Ne te… Ne vous fâchez pas, je suis seulement venu récupérer la boule bleue qui est sur l'autel de l'autre côté du lac."
    show blanche cry close at left
    indigo "Mmmmh, et à quoi te servirait-elle cette boule ? Au demeurant, étant le gardien du lac Indigo, je ne peux te laisser outrager notre grande maîtresse Madame Arc-En-Ciel ! Ce n'est pas un simple bleu, mais le plus noble d'entre eux : l'indigo. Pour ce qui est de la boule, je ne peux pas te la céder."
    show blanche surprised open at left
    blanche "Pardon ! Je ne voulais pas vous froisser ! Mais…"
    show blanche cry open at left
    blanche "Il me faut absolument cette boule. Il en va de la vie de mon père ! Je veux lui montrer à quoi ressemblent les couleurs de l'Arc-en-Ciel !"
    show blanche cry close at left
    indigo "Bien qu'elle ne me soit d'aucune utilité et que ton intention soit louable, je ne peux faire d'écart au serment que j'ai prêté à Madame Arc-En-Ciel le jour où elle m'a confié ce poste de gardiennage."
    show blanche cry open at left
    blanche "Vous ne pourriez pas faire une toute petite exception pour moi ?"
    show blanche cry close at left
    indigo "Je ne fais des exceptions qu'aux personnes qui m'ont prouvé leur valeur intellectuelle. Pas à n'importe qui. Si tu veux cette boule, il va falloir prouver ta valeur !"
    show blanche surprised open at left
    blanche "Et comment je peux prouver ma valeur ?"
    show blanche surprised close at left

    menu:
        "Je vous fais un cours de maths ?":
            pass
        "Je vous bats aux échecs ?":
            pass

    indigo "Non, non et encore non, je ne suis qu'un chat, je n'ai pas besoin de voir tout ça. Moi, ce qui m'intéresse, c'est de connaître le nom de ces ensembles de points lumineux."
    show blanche neutral open at left
    blanche "Tu parles des étoiles qui forment des constellations ?"
    show blanche neutral close at left
    indigo "Sûrement. Tout ce que je sais, c'est qu'un voyageur m'a une fois donné le nom de toutes ces jolies choses. Malheureusement, je n'ai pas pu associer ces appellations avec ces étoiles."
    show blanche smile open at left
    blanche "Je peux t'aider ! Je les connais tous !"
    show blanche smile close at left
    indigo "Vraiment ? Montre moi donc."

    # TODO: Mini-jeu afficher les constellations + les noms /  associer le nom à la bonne constallation
    # if all_completed:
    #    indigo "Génial, merci ! Bon, je vais réfléchir ..."
    #    blanche "S'il vous plaîîîîîîîîîît !"
    #    indigo "Bon, bon, ok c'est d'accord. Motus et bouche cousue et je veux revoir la boule sur son autel au plus vite. Si les gardes l'apprennent s'en est fini de moi !"
    #    blanche "Youpi ! Merci beaucoup ! Je vous en serai éternellement reconnaissant !"
    # TODO: <illu chat qui fait signe d'adieu et blanche qui tient la boule>
    # TODO: <Noir gagne une couleur>
    hide blanche
    hide indigo
    with dissolve
    "Un bateau apparaît sur le lac"
    show maigrichon at left
    show grosso at right
    with dissolve
    grosso "Il s'enfuit, il s'enfuit ! Rame plus vite, Maigrichon !" with vpunch
    maigrichon "T'es drôle toi, aide-moi plutôt !"
    grosso "Si tu ne veux pas finir aux oubliettes avec moi, je te conseille de te dépêcher."
    hide maigrichon at left
    hide grosso at right
    with dissolve
    # TODO: Apparaît le souvenir de Mme Arc-en-ciel (en mode hologramme)
    madame "Quoi ?! On me vole mes 7 boules de cristal et vous ne faites rien ??! Vous n'êtes qu'une bande d'incapables ! Vous, comme les autres chats gardiens, je vous ai confié une mission et vous n'êtes même pas capables de la tenir !"
    madame "Récupérez mes boules avant minuit sinon vous finirez dans les oubliettes de mon château jusqu'à la fin de vos jours !!!!"
    indigo "Messieurs, bien le bonsoir, que me vaut votre visite impromptue à cette heure aussi tardive ?"
    grosso "On nous a signalé un vol de boule, on vient voir ce qu’il en est."
    maigrichon "Eh, mais elle est passée où ta boule à toi ? T’es vraiment pas doué… L’enfant est parti par où ?"
    grosso "Je vois ses traces de pas, allons-y !"
    maigrichon "Et toi, Indigo, pour l’amour de Madame Arc-En-Ciel, tiens-toi à carreau, ça suffit les bêtises."

