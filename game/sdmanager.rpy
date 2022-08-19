##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##                       Quelques informations utiles

##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##=========================================================================##
##                           Les formats audios                            ##
##=========================================================================##

# Fomat audio accepté :
# Opus
# Ogg Vorbis
# MP3
# MP2
# FLAC
# WAV (uncompressed 16-bit signed PCM only)
# Qualité = Wav / Flac / Ogg

##=========================================================================##
##               Structures et gestion du son dans renpy                   ##
##=========================================================================##

##===============Les différents canaux============##

# Plusieurs canaux pour l'audio sont déjà préconfigurés:
# - sound pour tous les sons audios.
# - music pour toutes les musiques du jeux
# - voice pour toutes les voix des personnages
# - audio permet de jouer plusieurs sons à la fois ( attention à ne pas en jouer plus d'une dizaine, saturation du son tout ça... )
# J'indiquerai entre parenthèse le cannal à utiliser lors de l'appel de variable pour faire jouer le son.
# Ou au mieux je le fais.

##===============Gérer les volumes par groupes via des mixers============##

# La gestion des volumes passe par plusieurs types de "gestionnaire" (en son on appelle ça des mixers / submixer / Master)
# Dans renpy cela fonctionne en terme de hierachie:
#     Main mixer => SubMixer => Channel => Track
#     Toutes les valeurs seront comprises entre 0 à 1. Si vous devez gérer le volume en dépassant le chiffre 1, revoyez le volume de votre son d'origine avant import.
#
# Vue que tous ces "gestionnaires" sont reliés les uns aux autres :
#     - Main mixer = 0.8 ( 80 du volume )
#     - SubMixer = 1
#     - Channel = 0.50
#     - Track = 0.25
# Alors en résultat de sortie on aura:
#     0.8 * 1.0 * 0.5 * 0.25 = 0.1 soit 10%
#
# Dans la grande majorité des cas il est fortement conseillé:
#     1. De toujours laisser le Main mixer au max, soit à 1.0 et de bien le définir comme étant 1 le maximum.
#     2. D'utiliser les channels dans les options du jeu pour le joueur
# En dehors de ces 2 points, c'est open bar.

# Fade in et Fade Out permet de gérer des fondus audios. Principalement utilisé pour la music uniquement.
# A tester : Fade out de la lecture en cours + fade in du prochain audio = un crossfade : Un fondu enchainé.

##===============Faire déclencher les sons dans Renpy============##

# Lorsque vous voulez jouer un son / une musique ou un voice acting voici le modèle à suivre:
# Exemple 1: Je veux faire jouer un son en oneshot direct à un moment clé donc :
#    play sound NomDeLaVariableDuSonDéclaréDansSDManager.RPY
#    ex: play sound UI_Hover
# On peut aussi réduire son volume indépendemment dés l'appel, si on juge le son trop élévée par rapport au reste des éléments sonores:
#    ex: play sound UI_Hover volume 0.5
# Valeur comprise entre 0 et 1, on peux aller jusqu'à 2,
# mais attention à la saturation lié au volume, c'est préférable de rééditer le son et de le réimporter

# Pour stoper le son/ musique etc...
# Exemple : stop sound ou stop music et si vous voulez que cela s'arrête doucement, faut ajouter fade out avec uen valeur comprise de 0 à 1, corespondant à un timer.

# Exemple 2: On peut aussi jouer une liste de son / musique
# ex: play music [ "a.ogg", "b.ogg" ] fadeout 1.0 fadein 1.0 avec un petit crossfade entre les éléments

##=========================================================================##
##                          Changement d'état ou pas                       ##
##=========================================================================##

# En fonction des besoins du projet on peut faire en sorte qu'une musique ne repprenne pas dés le début.
# Exemple :
# label market_side: (On est autour du marché)
#     play music market (On joue la music du marché)
#     "We're entering the market." (On entre dans le marché)
#     jump market_main (On saute à une autre partie du code lié au fait de rentrer dans le marché)
#
# label market_main:
#     play music market if_changed
#     "Maybe we just entered the market, maybe we were already there."
#     "If we were already there, the music didn't stop and start over, it just continued."
#      Avec la mention "if_changed" indiqué après "play music market" on lui dit
#     "Si la musique joue déjà alors ne fait rien" et la musique continue sans repprendre au début

##=========================================================================##
##               Créer un enchaînement de lecture (playlist)               ##
##=========================================================================##

# Une commande existe pour lister une suite de son ou de musique qui se joueront dans l'ordre déclaré.
# Exemple : play sound "woof.mp3" volume 0.25 => Se joue en premier
# queue sound "woof.mp3" volume 0.5 => Puis se joue en second
# queue sound "woof.mp3" volume 0.75 => Puis se joue en troisième...
# queue sound "woof.mp3" volume 1.0
# Ici on fait jouer une liste de son similaire à un volume différent pour créer des variations sonores.

##=========================================================================##
##      Faire lire des sons / Musiques à des débuts de lecture précis      ##
##=========================================================================##

# Grossomodo, une musique qui dure 3minutes et 45 secondes, commencera toujours à partir de 0 seconde en utilisant la commande de base:
#     play music
# Maintenant, je voudrai prendre qu'une portion de cette musique ( pour accentuer une scène dramatique, ou épique par exemple ) alors
# je vais le faire commencer qu'à partir de 2 min 30, là ou c'est intense dans la dite musique. Du coup je vais faire :
#    play music "<from 150 to 180>music.ogg" ( exprimé en seconde la valeur )
# et vu que la scène peut potentiellement durer plus de 30 secondes de jeu, je vais lui dire de faire une boucle sonore de la musique à cet endroit:
#     play music "<loop 150>music.ogg"
#     C'est comme si on avait posé une marque à 150 secondes, et que la musique, une fois terminée, se rejouait en partant de 150 seconde.


# Pour plus de détail sur l'audio dans Renpy la doc => https://www.renpy.org/doc/html/audio.html


##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##                       Codes / Déclaration de variables

##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.


import random

##define config.default_music_volume = 1     --
##define config.default_sound_volume = 1        |===> Partie à enlever du commentaire une fois l'audio posé et intégré.
##define config.default_voice_volume = 1        |
##define config.default_audio_volume = 1     --



##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##                       Gestion des effets sonores

##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.



##=========================================================================##
##                    Sons Interfaces (Channel Sound)                      ##
##=========================================================================##

##===============Sons Menu (Interface/UI)============##

define audio.UI_Hover = "audio/Menu/Hover_01.ogg"
define audio.UI_Click = "audio/Menu/Click_01.ogg"

##=============Sons des boules de cristales===============##

## VioletWorld
define audio.VioletBall = "audio/CristalsBall/.ogg"

## IndigoWorld
define audio.IndigoBall = "audio/CristalsBall/.ogg"

## CyanWorld
define audio.CyanBall = "audio/CristalsBall/.ogg"

## GreenWorld
define audio.GreenBall = "audio/CristalsBall/.ogg"

## YellowWorld
define audio.YellowBall = "audio/CristalsBall/.ogg"

## OrangeWorld
define audio.OrangeBall = "audio/CristalsBall/.ogg"

## RedWorld
define audio.RedBall = "audio/CristalsBall/.ogg"


##=========================================================================##
##                     Voice acting (Channel Voice)                        ##
##=========================================================================##

##=============Sons des personnages===============##

## Blanche
define audio.BlancheSpeak = "audio/Characters/Blanche/.ogg"
define audio.BlancheAngry = "audio/Characters/Blanche/.ogg"
define audio.BlancheHappy = "audio/Characters/Blanche/.ogg"
define audio.BlancheCry = "audio/Characters/Blanche/.ogg"

## Noire
define audio.NoireSpeak = "audio/Characters/Noire/.ogg"
define audio.NoireAngry = "audio/Characters/Noire/.ogg"
define audio.NoireHappy = "audio/Characters/Noire/.ogg"
define audio.NoireCry = "audio/Characters/Noire/.ogg"

## Arc-En-Ciel
define audio.ArcEnCielSpeak = "audio/Characters/ArcEnCiel/.ogg"
define audio.ArcEnCielAngry = "audio/Characters/ArcEnCiel/.ogg"
define audio.ArcEnCielHappy = "audio/Characters/ArcEnCiel/.ogg"
define audio.ArcEnCielCry = "audio/Characters/ArcEnCiel/.ogg"

## Guards
define audio.GuardsSpeak = "audio/Characters/Guards/.ogg"
define audio.GuardsAngry = "audio/Characters/Guards/.ogg"
define audio.GuardsHappy = "audio/Characters/Guards/.ogg"
define audio.GuardsCry = "audio/Characters/Guards/.ogg"

## Chicks
define audio.ChicksSpeak = renpy.random.choice( ("audio/Birds/Chick_1.ogg", "audio/Birds/Chick_2.ogg", "audio/Birds/Chick_3.ogg", "audio/Birds/Chick_4.ogg") )

##=============Sons des chats===============##

## Violet
define audio.VioletSpeak = "audio/Meow/CatMeow_4.ogg"
define audio.VioletAngry = "audio/Hiss/CatHiss_1.ogg"
define audio.VioletHappy = "audio/Purr/CatPurr_4.ogg"

## Indigo
define audio.IndigoSpeak = "audio/Meow/CatMeow_5.ogg"
define audio.IndigoAngry = "audio/Hiss/CatHiss_3.ogg"
define audio.IndigoHappy = "audio/Purr/CatPurr_3.ogg"

## Green
define audio.GreenSpeak = "audio/Meow/CatMeow_1.ogg"
define audio.GreenAngry = "audio/Hiss/CatHiss_1.ogg"
define audio.GreenHappy = "audio/Purr/CatPurr_2.ogg"

## Red
define audio.RedSpeak = "audio/Meow/CatMeow_2.ogg"
define audio.RedAngry = "audio/Hiss/CatHiss_2.ogg"
define audio.RedHappy = "audio/Purr/CatPurr_5.ogg"



##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##                  Gestion des Musiques (Channel music)

##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##=============Musique Menu===============##

define audio.MusicMenu = "music/.ogg"

##=============Musique InGame===============##

define audio.MusicViolet = "music/GardenOfFruits.ogg"
define audio.MusicIndigo = "music/.ogg"
define audio.MusicCyan = "music/.ogg"
define audio.MusicGreen = "music/.ogg"
define audio.MusicYellow = "music/.ogg"
define audio.MusicOrange = "music/.ogg"
define audio.MusicRed = "music/.ogg"

##=============Musique Générique===============##

define audio.MusicEnd= "music/.ogg"
