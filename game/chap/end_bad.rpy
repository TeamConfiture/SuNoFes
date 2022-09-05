label end_bad:
    call titlepage("", _("Fin triste"))
    scene monochrome 
    show maigrichon at farRight
    show grosso at nearRight
    show blanche neutral close at left
    with dissolve
    grosso "On te tient maintenant ! Rends-nous les boules tout de suite !" with vpunch
    show blanche surprised open at left
    blanche "Oh non ! Les gardes de Madame Arc-en-Ciel ! Fuyons !" with vpunch
    hide blanche surprised close at left with easeoutleft
    "Je cours de toutes mes forces."
    grosso "Pas si vite !"
    hide grosso at nearRight with easeoutleft
    hide maigrichon at farRight behind grosso with easeoutleft
    show blanche cry open at left with easeinright
    blanche "Hmpf... Hmpf..."
    show blanche surprised open at left
    blanche "Ah !" with vpunch
    blanche "Oh non ! Une impasse !"
    show blanche surprised close at left
    show grosso at nearRight with easeinright
    show maigrichon at farRight behind grosso with easeinright
    grosso "Ha ha ! Tu ne peux plus t'échapper maintenant, hein ?"
    grosso "Viens là !"
    show blanche cry open at left
    show maigrichon at farRight behind blanche
    show grosso at center behind blanche with move
    blanche "Ah ! Aïe !" with vpunch
    show blanche cry close at left
    "Le garde m'attrape une main et m'arrache les boules de cristal."
    show blanche cry open at left
    blanche "Non ! Non ! Pas les boules de cristal !" with vpunch
    blanche "S'il vous plaît ! C'est pour mon père !"
    show blanche cry close at left
    grosso "Madame Arc-en-Ciel a bien été formelle à ce sujet."
    grosso "Aucun étranger ne doit s'emparer des boules ! Ce sont les ordres."
    grosso "Maigrichon ! Passe-moi les menottes, on l'embarque !"
    grosso "Finie la rigolade ! Tu vas voir ce qu'il en coûte de s'opposer aux représentants de Madame Arc-en-Ciel !"
    show blanche cry open at left
    blanche "Ah ! Aïe !" with vpunch
    show blanche cry close at left
    "Le garde me menotte les mains."
    show blanche cry open at left
    blanche "S'il vous plaît ! Je peux tout vous expliquer !"
    show blanche cry close at left
    grosso "On n'a pas que ça à faire. Tu iras t'expliquer avec les chauves-souris dans ta cellule."
    show blanche cry open at left
    blanche "S'il vous plaît ! S'il vous plaît !"
    blanche "Pitié, juste cinq minutes ! Il faut que je montre ces boules à mon papa !"
    show blanche cry close at left
    "Nous passons devant la maison."
    show blanche cry open at left
    blanche "Oh non, Papa !"
    hide maigrichon at farRight
    hide grosso at center
    show noir bandeau hurt open at right
    show end_spirited_back behind noir
    with dissolve
    show blanche cry close at left
    noir "Kof, kof…" with vpunch
    show noir bandeau hurt close at right
    "Mon papa tourne la tête au-dehors."
    show blanche cry open at left
    blanche "Pardon, Papa ! Je m'excuse... Pardon. J'ai fait une grosse bêtise."
    hide blanche cry close at left with dissolve
    show noir bandeau hurt open at right
    show end_spirited_front
    noir "Kof, kof... On dirait qu'il y a de l'agitation dehors..." with vpunch
    noir "Kof, kof... [player_name] ! Tu peux m'apporter un verre d'eau ? Kof, kof... "
    noir "[player_name] ?"
    noir "[player_name:.2]... [player_name] ?"
    noir "[player_name:.2]..."
    hide end_spirited_back behind noir
    hide noir bandeau hurt close at right
    hide end_spirited_front
    with dissolve
    scene black with dissolve
    "Tels furent les derniers mots de mon papa avant de se transformer en un nuage de poussière noire..."
    scene bad with dissolve
    "Quant à moi, j'ai fini dans les geôles du palais Arc-en-Ciel sans jamais avoir pu m'expliquer."
    "FIN"
    python:
        persistent.reached_end_bad = True
        persistent.last_reached_end = 'bad'
        renpy.save_persistent()
