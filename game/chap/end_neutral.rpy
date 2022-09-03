label end_neutral:
    call titlepage("", _("Fin neutre"))
    scene room
    show noir bandeau hurt open at right
    with dissolve
    noir "Urgh… Aaahh !!!" with vpunch
    show noir bandeau hurt close at right
    "Noir crie de douleur."
    show blanche surprised open at left with easeinleft
    blanche "Papa ! Hmpf… Hmpf…"
    show blanche surprised close at left
    "J'ai couru comme j'ai pu à la maison."
    show blanche surprised open at left
    blanche "Papa ! Tu vas bien ?! Regarde, je t'ai amené les sept boules de cristal !"
    show blanche surprised close at left
    show noir bandeau sigh open at right
    noir "Urgh… [player_name], c'est toi ?"
    show noir bandeau sigh close at right
    show blanche neutral open at left
    blanche "Je voulais te faire une surprise et te montrer l'Arc-en-Ciel ! Comme tu es tout le temps malade, j'ai décidé de t'amener les sept boules de l'Arc-en-Ciel ! Regarde ! Tada !"
    show blanche neutral close at left
    show noir bandeau hurt open at right
    noir "Ah… [player_name], pourquoi as-tu fait ça ? Kof, kof."
    show noir bandeau sigh open at right
    noir "Cela va perturber l'équilibre du royaume. Madame Arc-en-Ciel ne sera pas contente."
    noir "Va remettre ces boules de cristal, là où elles doivent être. Kof, kof."
    show noir bandeau sigh close at right
    show blanche cry open at left
    blanche "Je voulais seulement te faire une surprise…" 
    show blanche cry close at left
    show noir bandeau sigh open at right
    noir "On risque d'avoir des ennuis si Madame Arc-en-Ciel découvre que tu as volé ses boules."
    show noir bandeau sigh close at right
    show blanche cry open at left
    blanche "Mais, regarde Papa ! Ces couleurs sont jolies, non ? Tu… Tu n'aimes pas mon cadeau ?"
    show blanche cry close at left
    "Je commence à pleurer."
    show blanche cry open at left
    blanche "J'ai fait tout le royaume pour te montrer l'Arc-en-Ciel. Il fait si noir ici, c'est si triste."
    blanche "Je voulais seulement que tu ailles mieux en voyant ces jolies couleurs !!!"
    blanche "Mais, tu n'y fais pas du tout attention. Madame Arc-en-Ciel, par-ci, Madame Arc-en-Ciel, par là ! Je le sais ! Les gardiens de Couleurs n'ont pas arrêté de me dire que c'était dangereux ce que je faisais !"
    blanche "Pourtant... Poutant, j'ai fait tout ça parce que tu es toujours triste, malade et plein d'idées noires."
    blanche "C'est si mal que ça de vouloir voir les couleurs avec toi ? Je pensais qu'en voyant ces jolies choses, tu irais mieux." 
    show blanche cry close at left
    show noir bandeau sigh open at right
    noir "Je… C'est très joli, [player_name]."
    noir "Je vais mieux merci…"
    show noir bandeau sigh close at right
    show end_spirited_front
    show end_spirited_back behind noir
    "Des particules lumineuses noires apparaissent autour de Noir."
    show blanche cry open at left
    blanche "Tu mens. Tu es en train de disparaître."
    show blanche cry close at left
    noir "…"
    show noir bandeau sigh open at right
    noir "Viens là…"
    show noir bandeau sigh close at right
    "Papa sourit et utilise ses dernières forces pour se lever et me prendre dans ses bras."
    show blanche cry open at left
    blanche "Sniff… Sniff…"
    show blanche cry close at left
    show noir bandeau hurt open at right
    noir "Ne pleure pas..."
    noir "Même si je perds de plus en plus de luminosité et que je ne deviens qu'une simple ombre qui disparaît à la lumière, sache que j'ai eu une vie merveilleuse."
    noir "Je ne regrette pas d'avoir vécu à tes côtés."
    show noir bandeau hurt close at right
    "À ces mots, il prend mes mains, les embrasse et les place au niveau de son coeur."
    show blanche cry open at left
    blanche "Ton coeur, il bat faiblement…"
    show blanche cry close at left
    show noir bandeau smile open at right
    noir "Je n'ai aucun regret [player_name] alors… Souris pour moi. Souris pour toi. Vis ta vie."
    noir "[player_name], profite de ta vie et ne regrette rien."
    noir "Ceci n'est pas un adieu, ceci est juste un au revoir."
    show noir bandeau smile close at right
    "Papa pointe mon coeur du bout de son doigt."
    show noir bandeau smile open at right
    noir "Je serai toujours là à tes côtés dans cette petite place au fond de ton coeur."
    show noir bandeau smile close at right
    show blanche cry open at left
    blanche "Papa…"
    show blanche cry close at left
    show noir bandeau smile open at right
    noir "Prends bien soin de toi, [player_name]."
    show blanche cry open at left
    show noir bandeau smile close at right
    blanche "PAPA ! Non, ne me laisse pas !!!" 
    show blanche cry close at left
    show noir bandeau smile open at right
    noir "Au revoir [player_name]."
    show noir bandeau smile close at right
    show blanche cry open at left
    blanche "PAPA !!!"
    show blanche cry close at left
    hide end_spirited_front
    hide end_spirited_back behind noir
    scene neutral
    with dissolve
    #<illu noir qui prend blanche dans ses bras, une partie de son corps est dans un état de paillettes lumineuses noires (exemple)>
    noir "Merci de m'avoir fait voir l'arc-en-ciel une dernière fois…"
    scene black with dissolve
    "C'est ainsi que Noir, mon père, disparut dans l'obscurité…"
    "Quant aux boules de cristal..."
    "Les gardes de Madame Arc-en-Ciel les récupérèrent et m'amenèrent devant elle."
    "Par chance, après avoir expliqué ma situation, Madame Arc-en-Ciel me pardonna pour tout ce que j'avais fait pour mon père..."
    "FIN"
    python:
        persistent.reached_end_neutral = True
        renpy.save_persistent()
