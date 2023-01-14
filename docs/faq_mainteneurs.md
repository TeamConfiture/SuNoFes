# FAQ

*Pour voir toutes les questions simplement, utiliser la table des matières générée par Github dans l'interface web*

- [FAQ](#faq)
  - [Comment mettre à jour les textes ou corriger des erreurs ?](#comment-mettre-à-jour-les-textes-ou-corriger-des-erreurs-)
  - [Comment utiliser les sons ?](#comment-utiliser-les-sons-)
  - [Comment utiliser les images ?](#comment-utiliser-les-images-)
  - [Comment publier une nouvelle version ?](#comment-publier-une-nouvelle-version-)

<div id="faq-translation-guideline" />

## Comment mettre à jour les textes ou corriger des erreurs ?

Que ce soit en français ou en anglais, les corrections de texte doivent être effectuées dans les dossiers de traduction sous `game/tl`.

Le plus simple pour identifier où se trouve le texte à corriger est généralement de faire une recherche globale du texte fautif dans le sous-dossier de la langue à corriger et de modifier la ligne de résultat correspondante.

Les traductions peuvent se présenter sous deux formes présentées ci-après. Dans le premier cas, éditer la ligne non commentée ; dans le deuxième cas, éditer la ligne commençant par `new`.

```py
# game/chap/chap0.rpy:55
translate english start_637de622:

    # blanche "C'est parti !"
    blanche "Let's go"

translate english strings:

    # game/chap/chap0.rpy:1
    old "C'est parti !"
    new "Let's go!"
```

Une fois la correction effectuée, commiter les modifications sur une nouvelle branche et ouvrir une pull request

<div id="faq-sounds-guideline" />

## Comment utiliser les sons ?

Les fichiers de son sont systématiquement référencés dans le fichier `game/sdmanager.rpy` dans des variables dépendantes de l'usage prévu pour le son (ex: Les sons pour Blanche disant 'Non' sont définis dans la variable `sound.Blanche_No`).

Dans le code, l'usage de ces variables doit systématiquement se faire de manière randomisée avec `renpy.random.choice` si seul un des sons doit être joué. Exemples :

```py
# On se moque d'avoir plusieurs musiques jouées dans le cas du thème sonore
label play_music:
    play music music.Theme_Violet fadein 1.0

# On veut un unique son pour les réactions de personnage
label disappointed:
    play voice renpy.random.choice(sound.Blanche_No) fadein 1.0
    blanche "Ce n'est pas ce que je cherche"

# On veut un unique son pour les interactions dans les mini-jeux
screen get_a_click():
    imagebutton:
        auto "music_button_%s"
        action Play('sound', renpy.random.choice(sound.Paillete))
```

<div id="faq-images-guideline" />

## Comment utiliser les images ?

Les fichiers d'images sont généralement référencés dans le fichier `game/sprites.rpy` dans des variables leur servant d'alias (ex: L'image de mûre `images/items/mulberry_base.png` a l'alias `mulberry` dans le fichier).

Sauf exception due à des contraintes techniques ou usage dans le fichier `game/characters.rpy`, seuls ces alias doivent être référencés dans les autres fichiers. Ils peuvent être utilisés partout où le chemin complet du fichier serait une option valide. Exemple :

```py
screen mulberry_button(success_label = None):
    imagebutton:
        idle "mulberry"
        hover "mulberry_button"
        focus_mask True
        action Jump(success_label)
```

<div id="faq-release-guideline" />

## Comment publier une nouvelle version ?

Après avoir vérifié que toutes les modifications prévues pour la version sont bien intégrées :

* Mettre à jour le fichier `CHANGELOG.md` pour que sa première sous-section contienne les changements de la release (ou ne le faites pas, espèces de malpropres)
* Lancer manuellement l'action `Create release tag` en précisant le numéro de version pour lequel créer le tag (ex: `2.0.0`). L'action effectue les opérations suivantes :
  * Mise à jour du numéro de version présent dans le fichier `game/options.rpy`
  * Création d'un nouveau tag pour le numéro de version (ex: `v2.0.0`)
* Une fois l'action précédente terminée, lancer manuellement l'action `Publish` en précisant le numéro de version à publier (ex: `2.0.0`) et les cibles de publication (itch.io et github par défaut)

