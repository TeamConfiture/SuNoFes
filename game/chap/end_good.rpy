label end_good:
    call titlepage("", _("Fin heureuse"))
    $ achievement.grant("achievement_ending_good")
    $ achievement.sync()
    play music music.Theme_Good_End fadein 1.0 volume 0.5
    scene monochrome
    show blanche smile open at left
    with dissolve
    voice renpy.random.choice(audio.Blanche_Laugh)
    blanche "Héhé ! J'ai réussi à avoir les sept boules de cristal ! J'espère que Papa sera content."
    show blanche smile close at left
    show mme angryf open at right with dissolve
    voice renpy.random.choice(audio.ArcEnCiel_Hey)
    x "Un instant ! C'est donc toi, le petit enfant qui sème la zizanie dans ce royaume." with vpunch
    x "Que fais-tu ? Rends-moi mes boules ! Pourquoi les avoir prises ?!"
    x "Tu ne sais donc pas que cela perturbe l'équilibre de ce monde ?!"
    show mme angryf close at right
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Gasp)
    blanche "Ah ! Euh…" with vpunch
    blanche "C'est Madame Arc-en-Ciel ?"
    blanche  "Oh non ! Vite ! Fuyons !" with vpunch
    show mme angryf close at right
    show blanche surprised close at left
    "Mais, à peine ai-je pu faire un pas, que Madame Arc-en-Ciel m'attrape."
    show blanche cry open at left
    voice renpy.random.choice(audio.Blanche_Sniffing)
    blanche "Ne me faites pas de mal. C'est… C'est que mon papa… Mon papa Noir… Il… Il est malade et je voulais lui montrer les couleurs pour le voir sourire."
    show blanche cry close at left
    show mme neutralf open at right
    voice renpy.random.choice(audio.ArcEnCiel_Question)
    madame "Un instant… Papa ? Noir ? Il… Il est malade ?"
    madame "Tu… Tu serais donc son enfant ?"
    show mme neutralf close at right
    show blanche neutral open at left
    voice renpy.random.choice(audio.Blanche_Yes)
    blanche "Oui, Madame Arc-en-Ciel…"
    show blanche neutral close at left
    madame "..."
    show blanche surprised open at left
    blanche "Je vous promets, Madame Arc-en-Ciel, je vous emprunte les boules juste pour un instant ! Après, je vous les rendrai !"
    show blanche cry open at left
    voice renpy.random.choice(audio.Blanche_Moan)
    blanche "Laissez-moi juste les montrer à mon papa !"
    show blanche cry close at left
    show mme neutralf open at right
    voice renpy.random.choice(audio.ArcEnCiel_Sigh)
    madame "Amène-moi à ton père."
    show mme neutralf close at right
    show blanche surprised open at left
    voice renpy.random.choice(audio.Blanche_Question)
    blanche "Hein ?"
    show blanche surprised close at left
    show mme angryf open at right
    voice renpy.random.choice(audio.ArcEnCiel_Angry)
    madame "Amène-moi à ton père, tout de suite !" with vpunch
    show mme angryf close at right
    show blanche surprised open at left
    blanche "Euh… Oui ! Oui !"
    show blanche surprised close at left
    "Nous partons en direction du Quartier des Monochromes..."
    scene room
    show mme neutral close at farLeft
    show blanche neutral close at nearLeft
    show noir bandeau hurt close at right
    show end_spirited_front
    show end_spirited_back behind noir
    with dissolve
    "Une fois entrés dans la maison, Madame Arc-en-Ciel découvre mon papa allongé sur le lit sans aucune force."
    "Le constat était sans appel. Mon papa allait bientôt s'éteindre."
    show mme sad close at farLeft
    "En voyant la scène, Madame Arc-en-Ciel, qui était connue pour n'exprimer aucun sentiment, autre que la colère, s'effondre et commence à murmurer."
    show mme sad open at farLeft
    voice renpy.random.choice(audio.ArcEnCiel_Sigh)
    madame "Mon vieil ami, Noir… Que s'est-il passé depuis tout ce temps…"
    madame "Est-ce le poids de la noirceur de ce monde qui t'a mis dans cet état-là ?"
    show mme sad close at farLeft
    show noir bandeau hurt open at right
    voice renpy.random.choice(audio.Noir_Gasp)
    noir "Urgh… Urgh…"
    show noir bandeau hurt close at right
    "Noir gémit."
    show noir bandeau sigh open at right
    noir "Ciel… Est-ce toi ?"
    show noir bandeau sigh close at right
    show mme ignore open at farLeft
    voice renpy.random.choice(audio.ArcEnCiel_No)
    madame "Repose-toi… Garde tes forces."
    show mme ignore close at farLeft
    show noir bandeau sigh open at right
    voice renpy.random.choice(audio.Noir_Speak)
    noir "Je suis désolé… Je ne mérite pas d'être ton partenaire de route. Je n'ai pas réussi à faire honneur à la tâche que tu m'as confiée."
    show noir bandeau sigh close at right
    show mme ignore open at farLeft
    madame "Ne dis pas de sottises."
    show mme ignore close at farLeft
    show noir bandeau hurt open at right
    voice renpy.random.choice(audio.Noir_Angry)
    noir "Urgh… Aaahh !!!" with vpunch
    show noir bandeau hurt close at right
    "Noir crie de douleur."
    show blanche cry open at nearLeft
    show mme sad close at farLeft
    voice renpy.random.choice(audio.Blanche_Gasp)
    blanche "Papa !" with vpunch
    voice renpy.random.choice(audio.Blanche_Cry)
    blanche "Papa ! Tu vas bien ?! Regarde, je t'ai amené les sept boules de Cristal ! Tu as vu leur couleur ?"
    show blanche cry close at nearLeft
    show noir bandeau hurt open at right
    noir "[player_name], tu…"
    show noir bandeau smile close at right
    "Noir se tait un instant puis sourit."
    show noir bandeau smile open at right
    voice renpy.random.choice(audio.Noir_Yes)
    noir "C'est très joli mon enfant. Mais, n'oublie pas de rendre ça à Mam- Madame Arc-en-Ciel."
    show noir bandeau smile close at right
    show blanche smile open at nearLeft
    voice renpy.random.choice(audio.Blanche_Yes)
    blanche "Oui !"
    show blanche smile close at nearLeft
    "Je lui souris jusqu'aux oreilles."
    show noir bandeau smile open at right
    voice renpy.random.choice(audio.Noir_Speak)
    noir "Peux-tu me laisser un instant avec Madame Arc-en-Ciel ? J'aimerais discuter avec elle."
    noir "En attendant, tu pourrais me ramener des fleurs ?"
    show noir bandeau smile close at right
    show blanche neutral open at nearLeft
    voice renpy.random.choice(audio.Blanche_Question)
    blanche "Des fleurs ? Oh ! D'accord Papa !"
    hide blanche neutral close at nearLeft with easeoutleft
    "Je m'éloigne de lui et de Madame Arc-en-Ciel."
    "J'imagine qu'ils ont des choses à se dire..."
    hide noir bandeau smile close at right
    hide end_spirited_front
    hide end_spirited_back behind noir
    hide mme sad close at farLeft
    with dissolve
    "Quelque minutes plus tard..."
    show noir bandeau smile close at right
    show end_spirited_front
    show end_spirited_back behind noir
    show mme sad close at left
    with dissolve
    madame "..."
    noir "..."
    show noir bandeau smile open at right
    noir "Ne lui en tiens pas rigueur. L'enfant est encore jeune…"
    show noir bandeau smile close at right
    show mme blush open at left
    voice renpy.random.choice(audio.ArcEnCiel_Sigh)
    madame "Montrez mes boules de cristal à quelqu'un qui ne peut voir… C'est insensé."
    show mme blush close at left
    "Madame Arc-en-Ciel pose sa main au niveau des yeux de Noir."
    show noir bandeau surprised open at right
    voice renpy.random.choice(audio.Noir_Exclamation)
    noir "Huh ? Ciel ? Que fais-tu ?" with vpunch
    show noir bandeau surprised close at right
    show mme angry open at left
    voice renpy.random.choice(audio.ArcEnCiel_Exasperate)
    madame "Ne discute pas."
    show mme angry close at left
    "Madame Arc-en-Ciel émet une lumière et concentre cette énergie sur Noir."
    "Noir reprend des couleurs."
    hide end_spirited_front
    hide end_spirited_back behind noir
    with dissolve
    show noir bandeau surprised open at right
    noir "Que… Que se passe-t-il ? Je sens comme une force revenir en moi."
    voice renpy.random.choice(audio.Noir_Gasp)
    noir "Oh !"
    show noir bandeau surprised close at right with dissolve
    "Son bandeau tombe et révèle ses yeux… arc-en-ciel."
    show noir surprised close at right with dissolve
    "Noir se lève."
    show noir smile open at right
    noir "Je… Merci… Merci de m'avoir guéri."
    show noir smile close at right
    show mme blush close at left
    madame "..."
    show mme blush close at left
    show noir smile open at right
    voice renpy.random.choice(audio.Noir_Speak)
    noir "Je croyais… Je croyais que tu me haïssais… C'est pour cette raison que tu ne voulais plus me voir."
    show noir smile close at right
    show mme ignore open at left
    voice renpy.random.choice(audio.ArcEnCiel_Exasperate)
    madame "Tsss… Avec mes responsabilités au sein du royaume, j'ai très peu de temps pour moi ou pour qui que ce soit."
    show mme blush open at left
    voice renpy.random.choice(audio.ArcEnCiel_Angry)
    madame "Je ne t'ai guéri que pour le bien de Couleurs."
    show mme blush close at left
    show noir neutral open at right
    voice renpy.random.choice(audio.Noir_Speak)
    noir "Couleurs n'a pas besoin d'un moins que rien comme moi."
    show noir neutral close at right
    show mme sad open at left
    madame "Mais, [player_name] a besoin de toi."
    show mme sad close at left
    show noir smile open at right
    voice renpy.random.choice(audio.Noir_Yes)
    noir "C'est vrai. Tu n'as pas tort..."
    show noir smile close at right
    "Noir sourit."
    show mme blush open at left
    voice renpy.random.choice(audio.ArcEnCiel_Yes)
    madame "Et moi aussi…"
    show mme blush close at left
    show noir surprised open at right
    voice renpy.random.choice(audio.Noir_Gasp)
    noir "Hum ?"
    show noir surprised close at right
    show mme blush open at left
    voice renpy.random.choice(audio.ArcEnCiel_Angry)
    madame "Moi aussi, j'ai besoin de toi."
    show mme blush close at left
    show noir smile open at right
    noir "Oh ? Vraiment ?"
    show noir smile close at right
    show mme angry open at left
    voice renpy.random.choice(audio.ArcEnCiel_Exasperate)
    madame "Tss… Ce n'est pas ce que tu crois. Je suis le soleil qui illumine ce monde et toi, tu es la lune qui le protège de l'obscurité..."
    show mme blush open at left
    madame "Il était évident qu'il fallait que je te sauve. C'est tout ce que je voulais dire."
    show mme blush close at left
    show noir smile open at right
    voice renpy.random.choice(audio.Noir_Speak)
    noir "Oh… Oui, je vois."
    show noir smile close at right
    show mme blush close at left
    madame "..."
    noir "..."
    "Madame Arc-en-Ciel et Noir se regardent les yeux dans les yeux."
    show mme angry open at left
    voice renpy.random.choice(audio.ArcEnCiel_Exasperate)
    madame "Disons que pour Couleurs, je suis peut-être quelqu'un, mais sans toi, je ne suis rien."
    show mme blush open at left
    voice renpy.random.choice(audio.ArcEnCiel_Sigh)
    madame "C'est pour ça que je t'ai sauvé."
    show mme blush close at left
    show noir smile open at right
    noir "Pfft, hahaha."
    show noir smile close at right
    "Noir rit et prend dans ses bras Madame Arc-en-Ciel."
    show mme blush open at left
    show noir smile close at center with ease
    voice renpy.random.choice(audio.ArcEnCiel_Hey)
    madame "Hé ! Ne me touche p-" with vpunch
    show blanche neutralf open at right with easeinright
    blanche "Papa ! Je t'ai ramené pleins de fleurs !"
    show blanche neutralf open at right
    voice renpy.random.choice(audio.Blanche_Exclamation)
    blanche "Oh ! Papa, tu es debout ! Trop bien ! Tu n'es plus malade !"
    blanche "Hein ? Mais pourquoi vous vous faites un câlin ? Moi aussi, j'en veux un !"
    show blanche neutralf close at right
    "C'est ainsi que je pars en direction de Papa et Mam... Madame Arc-en-Ciel."
    scene good with dissolve
    "FIN"
    python:
        persistent.reached_end_good = True
        persistent.last_reached_end = 'good'
        if persistent.reached_end_good and persistent.reached_end_neutral and persistent.reached_end_neutral:
            achievement.grant("achievement_ending_all")
            achievement.sync()
        renpy.save_persistent()
