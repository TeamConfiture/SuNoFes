##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##                       Codes / Déclaration de variables

##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##=========================================================================##
##                       Initialisation de l'audio                         ##
##=========================================================================##

## Définit les volumes par défaut de l'ensemble des canaux existants :

# define config.default_music_volume = 1
# define config.default_sound_volume = 1
# define config.default_voice_volume = 1
# define config.default_audio_volume = 1

##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##                       Gestion des effets sonores

##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.



##=========================================================================##
##                    Sons Interfaces (Channel Sound)                      ##
##=========================================================================##

##===============Sons Menu (Interface/UI)============##

define sound.Hover_Button = ["audio/UI/Hover_Button_01.ogg","audio/UI/Hover_Button_02.ogg","audio/UI/Hover_Button_03.ogg","audio/UI/Hover_Button_04.ogg"]
define sound.Start_Button = ["audio/UI/Start_Button_01.ogg"]
define sound.Click_Button = ["audio/UI/Click_Button_01.ogg","audio/UI/Click_Button_02.ogg","audio/UI/Click_Button_03.ogg"]
define sound.Return_Button = ["audio/UI/Return_Button_01.ogg"]

##=============Sons des boules de cristales===============##

## VioletWorld
define sound.Violet_Ball = ["audio/CristalsBall/.ogg"]

## IndigoWorld
define sound.Indigo_Ball = ["audio/CristalsBall/.ogg"]

## CyanWorld
define sound.Cyan_Ball = ["audio/CristalsBall/.ogg"]

## GreenWorld
define sound.Green_Ball = ["audio/CristalsBall/.ogg"]

## YellowWorld
define sound.Yellow_Ball = ["audio/CristalsBall/.ogg"]

## OrangeWorld
define sound.Orange_Ball = ["audio/CristalsBall/.ogg"]

## RedWorld
define sound.Red_Ball = ["audio/CristalsBall/.ogg"]

##=========================================================================##
##                 Sons d'interaction (Channel Sound)                      ##
##=========================================================================##

##=============Quand on sélectionne une carte===============##

define sound.Card_Select = ["audio/Interactions/Card_Select_01.ogg","audio/Interactions/Card_Select_02.ogg"]

##=============Quand les cartes se rassemblent===============##

define sound.Card_Together = ["audio/Interactions/Cards_Together_01.ogg"]

##=============Quand on attrape un objet===============##

define sound.Grab = ["audio/Interactions/Grab_01.ogg"]

##=============Quand on attrape un fromage===============##

define sound.Grab_Cheese = ["audio/Interactions/Grab_Cheese_01.ogg"]

##=============Quand on trouve la mûr===============##

define sound.Paillete = ["audio/Interactions/Paillette_01.ogg"]

##=============Quand on débloque un morceau de vitrail===============##

define sound.Unlock_Puzzle = ["audio/Interactions/Unlock_Puzzle_01.ogg"]

##=============Mini-Jeu les flèches===============##

define sound.Arrow = ["audio/Interactions/Arrow_01.ogg","audio/Interactions/Arrow_02.ogg"]

##============Mini-jeu coupure de fruit================##

define sound.Cut_Fruit = ["audio/Interactions/Cut_Fruit_01.ogg"]

##============Dépot du fromage dans le panier en osier================##

define sound.Cheese_Depot = ["audio/Interactions/Cheese_Depot_01.ogg"]

##============Dépot d'un objet dans une boite en bois================##

define sound.Wood_Depot = ["audio/Interactions/Wood_Depot_01.ogg"]

##============Mini-Jeu de Pêche================##

define sound.Fishing = ["audio/Interactions/Fishing_01.ogg"]

##=========================================================================##
##                     Voice acting (Channel Voice)                        ##
##=========================================================================##

##=============Sons des personnages===============##

## Blanche
define sound.Blanche_Amazement = ["audio/Characters/Blanche/Blanche_Amazement_01.ogg","audio/Characters/Blanche/Blanche_Amazement_02.ogg","audio/Characters/Blanche/Blanche_Amazement_03.ogg","audio/Characters/Blanche/Blanche_Amazement_04.ogg","audio/Characters/Blanche/Blanche_Amazement_05.ogg"]
define sound.Blanche_Angry = ["audio/Characters/Blanche/Blanche_Angry_01.ogg","audio/Characters/Blanche/Blanche_Angry_02.ogg"]
define sound.Blanche_Cry = ["audio/Characters/Blanche/Blanche_Cry_01.ogg"]
define sound.Blanche_Exclamation = ["audio/Characters/Blanche/Blanche_Exclamation_01.ogg","audio/Characters/Blanche/Blanche_Exclamation_02.ogg","audio/Characters/Blanche/Blanche_Exclamation_03.ogg","audio/Characters/Blanche/Blanche_Exclamation_04.ogg"]
define sound.Blanche_Gasp = ["audio/Characters/Blanche/Blanche_Gasp_01.ogg","audio/Characters/Blanche/Blanche_Gasp_02.ogg"]
define sound.Blanche_Laugh = ["audio/Characters/Blanche/Blanche_Laugh_01.ogg","audio/Characters/Blanche/Blanche_Laugh_02.ogg","audio/Characters/Blanche/Blanche_Laugh_03.ogg"]
define sound.Blanche_Moan = ["audio/Characters/Blanche/Blanche_Moan_01.ogg","audio/Characters/Blanche/Blanche_Moan_02.ogg"]
define sound.Blanche_No = ["audio/Characters/Blanche/Blanche_No_01.ogg","audio/Characters/Blanche/Blanche_No_02.ogg"]
define sound.Blanche_Question = ["audio/Characters/Blanche/Blanche_Question_01.ogg","audio/Characters/Blanche/Blanche_Question_02.ogg","audio/Characters/Blanche/Blanche_Question_03.ogg","audio/Characters/Blanche/Blanche_Question_04.ogg","audio/Characters/Blanche/Blanche_Question_05.ogg","audio/Characters/Blanche/Blanche_Question_06.ogg"]
define sound.Blanche_Sigh = ["audio/Characters/Blanche/Blanche_Sigh_01.ogg","audio/Characters/Blanche/Blanche_Sigh_02.ogg","audio/Characters/Blanche/Blanche_Sigh_03.ogg","audio/Characters/Blanche/Blanche_Sigh_04.ogg"]
define sound.Blanche_Sniffing = ["audio/Characters/Blanche/Blanche_Sniffing_01.ogg","audio/Characters/Blanche/Blanche_Sniffing_02.ogg","audio/Characters/Blanche/Blanche_Sniffing_03.ogg"]
define sound.Blanche_Yes = ["audio/Characters/Blanche/Blanche_Yes_01.ogg","audio/Characters/Blanche/Blanche_Yes_02.ogg"]
define sound.Blanche_Yes_Haughty = ["audio/Characters/Blanche/Blanche_YesHaughty_01.ogg","audio/Characters/Blanche/Blanche_YesHaughty_02.ogg","audio/Characters/Blanche/Blanche_YesHaughty_03.ogg","audio/Characters/Blanche/Blanche_YesHaughty_04.ogg"]

## Noir
define sound.Noir_Speak = ["audio/Characters/Noir/Noir_Reflexion.ogg"]
define sound.Noir_Angry = ["audio/Characters/Noire/Noir_Angry_01.ogg","Noir_Angry_02.ogg","Noir_annoying_01.ogg"]
define sound.Noir_Happy = ["audio/Characters/Noir/.ogg"]
define sound.Noir_Cry = ["audio/Characters/Noir/.ogg"]
define sound.Noir_Yes = ["audio/Characters/Noir/Noir_DoubleYes_01.ogg","audio/Characters/Noir/ShortYes_01.ogg","audio/Characters/Noir/Noir_ShortYes_02.ogg","audio/Characters/Noir/NoirShortYes_03.ogg","audio/Characters/Noir/NoirShortYes_04.ogg"]
define sound.Noir_No = ["audio/Characters/Noir/NoirNo_01.ogg"]
define sound.Noir_Gasp = ["audio/Characters/Noir/NoirGaps_01.ogg"]
define sound.Noir_Exlamation = ["audio/Characters/Noir/NoirExclamation_01.ogg"]

## Arc-en-Ciel
define sound.ArcEnCiel_Angry = ["audio/Characters/ArcEnCiel/ArcEnCiel_Angry_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Angry_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Angry_03.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Angry_04.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Angry_05.ogg"]
define sound.ArcEnCiel_Cry = ["audio/Characters/ArcEnCiel/ArcEnCiel_Cry_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Cry_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Cry_03.ogg"]
define sound.ArcEnCiel_Exasperate = ["audio/Characters/ArcEnCiel/ArcEnCiel_Exasperate_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Exasperate_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Exasperate_03.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Exasperate_04.ogg"]
define sound.ArcEnCiel_Exclamation = ["audio/Characters/ArcEnCiel/ArcEnCiel_Exclamation_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Exclamation_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Exclamation_03.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Exclamation_04.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Exclamation_05.ogg"]
define sound.ArcEnCiel_Gasp = ["audio/Characters/ArcEnCiel/ArcEnCiel_Gasp_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Gasp_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Gasp_03.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Gasp_04.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Gasp_05.ogg"]
define sound.ArcEnCiel_Hey = ["audio/Characters/ArcEnCiel/ArcEnCiel_Hey_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Hey_02.ogg"]
define sound.ArcEnCiel_No = ["audio/Characters/ArcEnCiel/ArcEnCiel_No_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_No_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_No_03.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_No_04.ogg"]
define sound.ArcEnCiel_Question = ["audio/Characters/ArcEnCiel/ArcEnCiel_Question_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Question_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Question_03.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Question_04.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Question_05.ogg"]
define sound.ArcEnCiel_Sigh = ["audio/Characters/ArcEnCiel/ArcEnCiel_Sigh_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Sigh_02.ogg"]
define sound.ArcEnCiel_Sniffing = ["audio/Characters/ArcEnCiel/ArcEnCiel_Sniffing_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Sniffing_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Sniffing_03.ogg"]
define sound.ArcEnCiel_Yes = ["audio/Characters/ArcEnCiel/ArcEnCiel_Yes_01.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Yes_02.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Yes_03.ogg","audio/Characters/ArcEnCiel/ArcEnCiel_Yes_04.ogg"]

## Axo
define sound.Axo_Full_Angry = ["audio/Characters/Axo/Axo_Full_Angry_01.ogg"]
define sound.Axo_Full_Attack = ["audio/Characters/Axo/Axo_Full_Attack_01.ogg","audio/Characters/Axo/Axo_Full_Attack_02.ogg"]
define sound.Axo_Full_Happy = ["audio/Characters/Axo/Axo_Full_Happy_01.ogg"]
define sound.Axo_Full_Question = ["audio/Characters/Axo/Axo_Full_Question_01.ogg"]
define sound.Axo_Partial_Happy = ["audio/Characters/Axo/Axo_Partial_Happy_01.ogg"]
define sound.Axo_Partial_Question = ["audio/Characters/Axo/Axo_Partial_Question_01.ogg"]

## Grosso
define sound.Grosso_Angry = ["audio/Characters/Grosso/Grosso_Angry_01.ogg","audio/Characters/Grosso/Grosso_Angry_02.ogg","audio/Characters/Grosso/Grosso_Angry_03.ogg","audio/Characters/Grosso/Grosso_Angry_04.ogg"]
define sound.Grosso_Cry = ["audio/Characters/Grosso/Grosso_Cry_01.ogg","audio/Characters/Grosso/Grosso_Cry_02.ogg","audio/Characters/Grosso/Grosso_Cry_03.ogg"]
define sound.Grosso_Gasp = ["audio/Characters/Grosso/Grosso_Gasp_01.ogg","audio/Characters/Grosso/Grosso_Gasp_02.ogg","audio/Characters/Grosso/Grosso_Gasp_03.ogg"]
define sound.Grosso_No = ["audio/Characters/Grosso/Grosso_No_01.ogg","audio/Characters/Grosso/Grosso_No_02.ogg","audio/Characters/Grosso/Grosso_No_03.ogg","audio/Characters/Grosso/Grosso_No_04.ogg"]
define sound.Grosso_Question = ["audio/Characters/Grosso/Grosso_Question_01.ogg","audio/Characters/Grosso/Grosso_Question_02.ogg","audio/Characters/Grosso/Grosso_Question_03.ogg","audio/Characters/Grosso/Grosso_Question_04.ogg"]
define sound.Grosso_Sigh = ["audio/Characters/Grosso/Grosso_Sigh_01.ogg","audio/Characters/Grosso/Grosso_Sigh_02.ogg","audio/Characters/Grosso/Grosso_Sigh_03.ogg","audio/Characters/Grosso/Grosso_Sigh_04.ogg"]
define sound.Grosso_Yes = ["audio/Characters/Grosso/Grosso_Yes_01.ogg","audio/Characters/Grosso/Grosso_Yes_02.ogg","audio/Characters/Grosso/Grosso_Yes_03.ogg","audio/Characters/Grosso/Grosso_Yes_04.ogg"]

#Maigrichon
define sound.Maigrichon_Angry = ["audio/Characters/Maigrichon/Maigrichon_Angry_01.ogg","audio/Characters/Maigrichon/Maigrichon_Angry_02.ogg"]
define sound.Maigrichon_Exclamation = ["audio/Characters/Maigrichon/Maigrichon_Exclamation_01.ogg","audio/Characters/Maigrichon/Maigrichon_Exclamation_02.ogg","audio/Characters/Maigrichon/Maigrichon_Exclamation_03.ogg"]
define sound.Maigrichon_No = ["audio/Characters/Maigrichon/Maigrichon_No_01.ogg","audio/Characters/Maigrichon/Maigrichon_No_02.ogg","audio/Characters/Maigrichon/Maigrichon_No_03.ogg"]
define sound.Maigrichon_Sigh = ["audio/Characters/Maigrichon/Maigrichon_Sigh_01.ogg","audio/Characters/Maigrichon/Maigrichon_Sigh_02.ogg","audio/Characters/Maigrichon/Maigrichon_Sigh_03.ogg"]
define sound.Maigrichon_Yes = ["audio/Characters/Maigrichon/Maigrichon_Yes_01.ogg","audio/Characters/Maigrichon/Maigrichon_Yes_02.ogg","audio/Characters/Maigrichon/Maigrichon_Yes_03.ogg"]

##=============Sons des chats===============##

## Violet
define sound.Violet_Speak = ["audio/Cats/Meow/CatMeow_04.ogg"]
define sound.Violet_Angry = ["audio/Cats/Hiss/CatHiss_01.ogg"]
define sound.Violet_Angry_Short = ["<from 2.3>audio/Cats/Hiss/CatHiss_01.ogg"]
define sound.Violet_Patronizing = ["<to 2.3>audio/Cats/Hiss/CatHiss_01.ogg"]
define sound.Violet_Happy = ["audio/Cats/Purr/CatPurr_04.ogg"]

## Indigo
define sound.Indigo_Speak = ["audio/Cats/Meow/CatMeow_05.ogg"]
define sound.Indigo_Angry = ["audio/Cats/Hiss/CatHiss_03.ogg"]
define sound.Indigo_Happy = ["audio/Cats/Purr/CatPurr_03.ogg"]

## Cyan/Cameraman
define sound.Cyan_Speak = ["audio/Cats/Meow/CatMeow_01.ogg"]
define sound.Cyan_Happy = ["audio/Cats/Purr/CatPurr_02.ogg"]
define sound.Cyan_Exclamation = ["audio/Cats/Purr/CatPurr_04.ogg"]
define sound.Cameraman_Speak = ["audio/Cats/Meow/CatMeow_02.ogg"]
define sound.Cameraman_Angry_Low = ["audio/Cats/Hiss/CatHiss_02.ogg"]
define sound.Cameraman_Angry = ["<to 2.3>audio/Cats/Hiss/CatHiss_01.ogg"]
define sound.Cameraman_Embarassed = ["audio/Cats/Meow/CatMeow_02.ogg"]

## Emeraude - this cat always has a 'singing' voice
define sound.Emeraude_Speak = ["audio/Cats/Meow/CatMeow_04.ogg"]
define sound.Emeraude_Happy = ["audio/Cats/Purr/CatPurr_04.ogg"]
define sound.Emeraude_No = ["audio/Cats/Hiss/CatHiss_01.ogg"]
define sound.Emeraude_Exclamation = ["audio/Cats/Purr/CatPurr_04.ogg"]

## Piou & Jaune
define sound.Piou_Speak = ["audio/Birds/Chick_04.ogg"]
define sound.Piou_Angry = ["audio/Birds/Chick_01.ogg", "audio/Birds/Chick_03.ogg"]
define sound.Piou_Cry = ["audio/Birds/Chick_02.ogg"]
define sound.Jaune_Speak = ["audio/Cats/Meow/CatMeow_02.ogg"]
define sound.Jaune_Sleepy = ["audio/Cats/Meow/CatMeow_03.ogg"]
define sound.Jaune_Angry = ["audio/Cats/Hiss/CatHiss_02.ogg"]

## Orange
define sound.Orange_Speak = ["audio/Cats/Meow/CatMeow_02.ogg"]
define sound.Orange_Irritated = ["audio/Cats/Hiss/CatHiss_01.ogg"]

## Red
define sound.Red_Speak = ["audio/Cats/Meow/CatMeow_02.ogg"]
define sound.Red_Angry = ["audio/Cats/Hiss/CatHiss_02.ogg"]
define sound.Red_Happy = ["audio/Cats/Purr/CatPurr_05.ogg"]


##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.
##
##                  Gestion des Musiques (Channel music)
##
##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##=============Musique Menu===============##

define music.Theme_Menu = ["music/Theme_Menu.ogg"]

##=============Musique InGame===============##

define music.Theme_Violet = ["music/Theme_Violet.ogg"]
define music.Theme_Indigo = ["music/Theme_Indigo.ogg"]
define music.Theme_Cyan = ["music/Theme_Cyan_Trumpetico.ogg"]
define music.Theme_Green = ["music/Theme_Green.ogg"]
define music.Theme_Yellow = ["music/Theme_Yellow_Kikou.ogg"]
define music.Theme_Orange = ["music/Theme_Orange_Gedine.ogg"]
define music.Theme_Red = ["music/Theme_Red_CrossingTheChasm.ogg"]

##=============Musique Générique===============##

define music.Theme_Prologue = ["music/Theme_Prologue_AlmostALoveStory.mp3"]
define music.Theme_Bad_End = ["music/.ogg"]
define music.Theme_Neutral_End = ["music/.ogg"]
define music.Theme_Good_End = ["music/.ogg"]
