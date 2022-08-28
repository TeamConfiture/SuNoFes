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
##                     Voice acting (Channel Voice)                        ##
##=========================================================================##

##=============Sons des personnages===============##

## Blanche
define sound.Blanche_Speak = ["audio/Characters/Blanche/.ogg"]
define sound.Blanche_Angry = ["audio/Characters/Blanche/.ogg"]
define sound.Blanche_Happy = ["audio/Characters/Blanche/.ogg"]
define sound.Blanche_Cry = ["audio/Characters/Blanche/.ogg"]

## Noir
define sound.Noir_Speak = ["audio/Characters/Noir/Noir_Reflexion.ogg"]
define sound.Noir_Angry = ["audio/Characters/Noire/Noir_Angry_01.ogg","Noir_Angry_02.ogg","Noir_annoying_01.ogg"]
define sound.Noir_Happy = ["audio/Characters/Noir/.ogg"]
define sound.Noir_Cry = ["audio/Characters/Noir/.ogg"]
define sound.Noir_Yes = ["audio/Characters/Noir/Noir_DoubleYes_01.ogg","audio/Characters/Noir/ShortYes_01.ogg","audio/Characters/Noir/Noir_ShortYes_02.ogg","audio/Characters/Noir/NoirShortYes_03.ogg","audio/Characters/Noir/NoirShortYes_04.ogg"]
define sound.Noir_No = ["audio/Characters/Noir/NoirNo_01.ogg"]
define sound.Noir_Gasp = ["audio/Characters/Noir/NoirGaps_01.ogg"]
define sound.Noir_Exlamation = ["audio/Characters/Noir/NoirExclamation_01.ogg"]

## Arc-En-Ciel
define sound.ArcEnCiel_Speak = ["audio/Characters/ArcEnCiel/.ogg"]
define sound.ArcEnCiel_Angry = ["audio/Characters/ArcEnCiel/.ogg"]
define sound.ArcEnCiel_Happy = ["audio/Characters/ArcEnCiel/.ogg"]
define sound.ArcEnCiel_Cry = ["audio/Characters/ArcEnCiel/.ogg"]

## Axo
define sound.Axo_Full_Angry = ["audio/Characters/Axo/Axo_Full_Angry_01.ogg"]
define sound.Axo_Full_Attack = ["audio/Characters/Axo/Axo_Full_Attack_01.ogg","audio/Characters/Axo/Axo_Full_Attack_02.ogg"]
define sound.Axo_Full_Happy = ["audio/Characters/Axo/Axo_Full_Happy_01.ogg"]
define sound.Axo_Full_Question = ["audio/Characters/Axo/Axo_Full_Question_01.ogg"]
define sound.Axo_Partial_Happy = ["audio/Characters/Axo/Axo_Partial_Happy_01.ogg"]
define sound.Axo_Partial_Question = ["audio/Characters/Axo/Axo_Partial_Question_01.ogg"]

## Guards
define sound.Guards_Speak = ["audio/Characters/Guards/.ogg"]
define sound.Guards_Angry = ["audio/Characters/Guards/.ogg"]
define sound.Guards_Happy = ["audio/Characters/Guards/.ogg"]
define sound.Guards_Cry = ["audio/Characters/Guards/.ogg"]

## Chicks
define sound.Chicks_Speak = ["audio/Birds/Chick_01.ogg","audio/Birds/Chick_02.ogg","audio/Birds/Chick_03.ogg","audio/Birds/Chick_04.ogg"]

##=============Sons des chats===============##

## Violet
define sound.Violet_Speak = ["audio/Meow/CatMeow_04.ogg"]
define sound.Violet_Angry = ["audio/Hiss/CatHiss_01.ogg"]
define sound.Violet_Happy = ["audio/Purr/CatPurr_04.ogg"]

## Indigo
define sound.Indigo_Speak = ["audio/Meow/CatMeow_05.ogg"]
define sound.Indigo_Angry = ["audio/Hiss/CatHiss_03.ogg"]
define sound.Indigo_Happy = ["audio/Purr/CatPurr_03.ogg"]

## Green
define sound.Green_Speak = ["audio/Meow/CatMeow_01.ogg"]
define sound.Green_Angry = ["audio/Hiss/CatHiss_01.ogg"]
define sound.Green_Happy = ["audio/Purr/CatPurr_02.ogg"]

## Red
define sound.Red_Speak = ["audio/Meow/CatMeow_02.ogg"]
define sound.Red_Angry = ["audio/Hiss/CatHiss_02.ogg"]
define sound.Red_Happy = ["audio/Purr/CatPurr_05.ogg"]


##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##                  Gestion des Musiques (Channel music)

##    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
##  .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

##=============Musique Menu===============##

define music.Theme_Menu = ["music/Theme_Menu.ogg"]

##=============Musique InGame===============##

define music.Theme_Violet = ["music/Theme_Violet.ogg"]
define music.Theme_Indigo = ["music/Theme_Indigo.ogg"]
define music.Theme_Cyan = ["music/.ogg"]
define music.Theme_Green = ["music/Theme_Green.ogg"]
define music.Theme_Yellow = ["music/.ogg"]
define music.Theme_Orange = ["music/.ogg"]
define music.Theme_Red = ["music/.ogg"]

##=============Musique Générique===============##

define music.Theme_Bad_End = ["music/.ogg"]
define music.Theme_Good_End = ["music/.ogg"]
