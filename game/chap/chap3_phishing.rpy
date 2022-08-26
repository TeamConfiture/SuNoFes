screen chap3_lake_phishing():
    add 'lake_deep'
    add Spirited(
        sprite_list = ['fish_shadow1'],
        direction_range = (160, 200),
        renewal_rate = 1,
        ttl_range = (2, 4),
        initial_count = 0,
        speed_range = (0, 100),
        spawn_box = (100, 100, -100, -100),
        )
    add PoorMansAnimatedImageButton(
        idle_image = "lake_fish1",
        action = Jump('lake_phishing_fish1'),
        focus_mask = True,
        xpos = 0.3,
        ypos = 0.5,
        )
    for f in ["21", "22", "23"]:
        add PoorMansAnimatedImageButton(
            idle_image = "lake_fish"+f,
            action = Jump('lake_phishing_fish2'),
            focus_mask = True,
            xpos = 0.35,
            ypos = 0.2,
            )
    if lake_phishing_fished_fish1 or lake_phishing_fished_fish2:
        # The king of the lake waits to see whether there is danger
        # before showing up
        add PoorMansAnimatedImageButton(
            idle_image = "lake_rainbow_fish",
            action = Jump('chap3_2'),
            focus_mask = True,
            xpos = 0.,
            ypos = 0.,
            )
    if not lake_phishing_fished_boot:
        imagebutton:
            idle "lake_boot"
            action Jump('lake_phishing_boot')
            focus_mask True
            xpos 0.72
            ypos 0.55
    if not lake_phishing_fished_axolotl:
        imagebutton:
            idle "lake_axolotl"
            action Jump('lake_fishing_axolotl')
            focus_mask True
            xpos 0.31
            ypos 0.75
    add 'lake_transparent'
    add MouseHole('lake_shallow', filter_image = 'lake_mousehole')
    if lake_phishing_fished_axolotl:
        imagebutton:
            idle "lake_axolotl"
            action Jump('lake_fishing_axolotl_revealed')
            focus_mask True
            xpos 0.68
            yoffset -60

transform axolotl_position:
    xpos 0.68
    yoffset -60

label lake_phishing_fish1:
    if lake_phishing_fished_axolotl:
        show axolotl at axolotl_position
    if not lake_phishing_fished_fish1:
        $ lake_phishing_fished_fish1 = True
        cyan "Ça ressemble à une truite Arc-En-Ciel d'après-toi ? Remets-le à l'eau et plus vite que ça."
    else:
        cyan "*Soupire*"
    call screen chap3_lake_phishing

label lake_phishing_fish2:
    if lake_phishing_fished_axolotl:
        show axolotl at axolotl_position
    if not lake_phishing_fished_fish2:
        $ lake_phishing_fished_fish2 = True
        cyan "Tu veux que je mange une famille de poissons ? Et puis quoi encore ! Laisse-les nager en paix."
    else:
        cyan "..."
    call screen chap3_lake_phishing

label lake_phishing_boot:
    if lake_phishing_fished_axolotl:
        show axolotl at axolotl_position
    $ lake_phishing_fished_boot = True
    cyan "Oh merveilleux ! Je ne voulais pas me mouiller pour aller la récupérer."
    cyan "Picaru l'avait soutirée à Maigrichon pendant qu'il marchait un peut trop près du bassin pendant une ronde."
    call screen chap3_lake_phishing

label lake_fishing_axolotl:
    $ lake_phishing_fished_axolotl = True
    cyan "Picaru ! Comment vas-tu depuis le temps ?"
    play sound renpy.random.choice(audio.Axo_Partial_Happy)
    axolotl "Pica !"
    cyan "Tu m'as manqué petit farceur, reste me tenir compagnie veux-tu ?"
    play sound renpy.random.choice(audio.Axo_Full_Happy)
    axolotl "Picaruuuu."
    call screen chap3_lake_phishing

label lake_fishing_axolotl_revealed:
    if lake_phishing_fished_axolotl:
        show axolotl at axolotl_position
    $ lake_phishing_talked_axolotl += 1
    if lake_phishing_talked_axolotl == 1:
        play sound renpy.random.choice(audio.Axo_Full_Question)
        axolotl "Picaru ?"
    elif lake_phishing_talked_axolotl == 2:
        play sound renpy.random.choice(audio.Axo_Full_Angry)
        axolotl "Picaru !"
    elif lake_phishing_talked_axolotl == 3:
        play sound renpy.random.choice(audio.Axo_Full_Attack)
        axolotl "Pi. Ca. Ruuuuuuuuuuuuuuu !"
        cyan "Laisse Picaru tranquille, veux-tu ?"
    else:
        cyan "..."
    call screen chap3_lake_phishing
