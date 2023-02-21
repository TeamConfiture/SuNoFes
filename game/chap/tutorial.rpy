label tutorial:
    scene room with dissolve
    if renpy.variant('pc'):
        "Pour avancer dans la narration, appuyez sur la barre Espace ou sur le bouton gauche de votre souris."
    else:
        "Pour avancer dans la narration, tapotez votre écran."
    "L'histoire de ce jeu se déroulera ainsi sous vos yeux, écran après écran."
    "Vous serez amené à faire des choix qui affecteront le récit, comme celui que je vais bientôt vous présenter."
    "Avez-vous bien compris jusqu'à maintenant ?"
    menu:
        with dissolve
        "Oui":
            "Parfait. Poursuivons..."
        "Non":
            "Je vois, je vais essayer de détailler un peu plus. Ce jeu appartient au genre des Romans Intéractifs (Visual Novel en anglais)."
            "Il s'agit d'un genre dans lequel vous suivez une histoire narrée par le biais de textes et d'illustrations."
            "Ces illustrations peuvent aussi bien représenter des lieux, que des personnages ou des objets."
            show blanche neutral open at Transform(
                pos = (822, 270), crop = (120, 0, 180, 890),
                rotate = 1, zoom = 0.7, alpha = 0.2, 
                ) with dissolve
            "Votre rôle dans l'histoire est de choisir une orientation au récit en influant sur les décisions, tantôt anodines, tantôt importantes, que prendront les personnages."
            "Les conséquences de certains choix que vous ferez apparaîtront immédiatement, tandis que d'autres pourront mettre de multiples chapitres à se révêler - lorsqu'elles existent."
            "La vie des personnages du récit est entre vos mains, j'espère que vous aimerez leurs histoires et partagerez leurs joies et leurs peines."
    "Au fait, je ne me suis pas présenté !"
    # TODO: add big red arrow
    show tutorial_arrow at Transform(pos = (0.215, 0.63)) with dissolve
    x "Je suis quelqu'un de mystérieux, voyez comme des points d'interrogation sont apparus au-dessus de la boîte de dialogue où ce que je vous dis depuis tout à l'heure apparaît."
    x "Lorsqu'un personnage parle dans l'histoire, son nom apparaîtra dans la boîte là où se trouvent les points d'interrogation."
    x "Lorsque la boîte de nom n'est pas visible, cela correspond à une description d'une action, d'un lieu, ... Bref, une information qui n'est pas une phrase prononcée par un personnage du récit."
    hide tutorial_arrow with dissolve
    "La douce voix de l'inconnu vous rappelle une personne proche."
    show tutorial_arrow at Transform(pos = (float(__("tutorial_rollback_arrow_location")), 0.63)) with dissolve
    if renpy.variant('pc'):
        x "A tout moment pendant la narration, vous pouvez revenir en arrière avec la molette de votre souris ou en cliquant sur ce bouton pour relire une information importante. Ce retour en arrière a des limites mais pourrait vous être utile."
    else:
        x "A tout moment pendant la narration, vous pouvez revenir en arrière en appuyant sur ce bouton pour relire une information importante. Ce retour en arrière a des limites mais pourrait vous être utile."
    show tutorial_arrow at Transform(pos = (float(__("tutorial_history_arrow_location")), 0.63)) with move
    x "Si vous voulez relire un échange qui a eu lieu dans le passé, vous pouvez utiliser l'historique, où tout ce qui est dit reste consigné."
    show tutorial_arrow at Transform(pos = (float(__("tutorial_preferences_arrow_location")), 0.63)) with move
    x "Configurez le jeu durant une partie en cliquant sur ce bouton. Certains paramètres de jouabilité peuvent requérir que vous reveniez en arrière dans la narration pour s'appliquer correctement."
    show tutorial_arrow at Transform(pos = (float(__("tutorial_fastforward_arrow_location")), 0.63)) with move
    if renpy.variant('pc'):
        x "Lorsque vous reprenez une partie ou en lancez une nouvelle, utilisez l'avance rapide ou appuyez sur TAB pour rejoindre facilement le dernier point de l'histoire non découvert."
    else:
        x "Lorsque vous reprenez une partie ou en lancez une nouvelle, utilisez l'avance rapide pour rejoindre facilement le dernier point de l'histoire non découvert."
    show tutorial_arrow at Transform(pos = (float(__("tutorial_autoforward_arrow_location")), 0.63)) with move
    x "Après avoir configuré la vitesse de l'avance automatique dans les préférences, activez-la en appuyant sur ce bouton pour que l'histoire se déroule sans que vous ayez à intervenir."
    show tutorial_arrow at Transform(pos = (float(__("tutorial_save_arrow_location")), 0.63)) with move
    x "Lorsque vous souhaitez sauvegarder votre progression, cliquez sur ce bouton et sélectionnez un emplacement de sauvegarde."
    hide tutorial_arrow with dissolve
    if renpy.variant('pc'):
        x "Enfin, appuyez sur 'H' pour voir la scène derrière la boite de texte dans son ensemble, et sur 'S' pour faire des captures d'écran."
    x "Maintenant que nous avons fait le tour des éléments qui persisteront tout au long de l'histoire, passons à quelques éléments que vous pourriez rencontrer de façons plus... occasionnelle."

    if renpy.variant('pc'):
        x "Je pense par exemple à des boutons, ou des objets à trouver. Je viens d'ajouter un objet à la pièce, trouvez-le et cliquez dessus, puis cliquez n'importe où pour continuer."
    else:
        x "Je pense par exemple à des boutons, ou des objets à trouver. Je viens d'ajouter un objet à la pièce, trouvez-le et appuyez dessus, puis appuyez n'importe où pour continuer."
    call screen tutorial_button(_("Trouvez l'objet clignotant dans la pièce")) with dissolve
    x "Bien joué ! Je l'ai fait clignoter pour vous faciliter la tâche, mais ce ne sera pas toujours aussi simple."

    if renpy.variant('pc'):
        x "Quelqu'un a laissé trainer une botte dans la chambre, mettez-la dans le panier avec un cliquer-déplacer, puis cliquez n'importe où pour vous lancer dans l'aventure."
    else:
        x "Quelqu'un a laissé trainer une botte dans la chambre, mettez-la dans le panier en appuyant sur l'écran en continu, puis appuyez n'importe où pour vous lancer dans l'aventure."
    call screen tutorial_dragdrop(_("Déplacez la botte dans le panier")) with dissolve

    x "Merci, j'ai de plus en plus de mal à atteindre des points aussi hauts. Je vais ranger ça pendant que vous jouez. Je me demande où peut bien être passée l'autre."
    x "Je vous ai appris tout ce que je pouvais, vous en apprendrez plus lors de votre aventure. Prenez les bonnes décisions par la suite."
    x "Bonne partie."
    return
