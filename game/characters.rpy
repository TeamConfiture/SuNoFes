# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les positions
define left = Position(xpos=0.30)
define farLeft = Position(xpos=0.20)
define nearLeft = Position(xpos=0.40)
define center = Position(xpos=0.5)
define right = Position(xpos=0.70)
define farRight = Position(xpos=0.80)
define nearRight = Position(xpos=0.60)

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

define blancheSpriteSize = 0.55
define guardSpriteSize = 0.5
define catSpriteSize = 0.50

image blanche cry close = im.FactorScale("images/blanche/Blanche_cry_close.png", blancheSpriteSize)
image blanche cry open = im.FactorScale("images/blanche/Blanche_cry_open.png", blancheSpriteSize)
image blanche neutral close = im.FactorScale("images/blanche/Blanche_neutral_close.png", blancheSpriteSize)
image blanche neutral open = im.FactorScale("images/blanche/Blanche_neutral_open.png", blancheSpriteSize)
image blanche pout close = im.FactorScale("images/blanche/Blanche_pout_close.png", blancheSpriteSize)
image blanche pout open = im.FactorScale("images/blanche/Blanche_pout_open.png", blancheSpriteSize)
image blanche smile close = im.FactorScale("images/blanche/Blanche_smile_close.png", blancheSpriteSize)
image blanche smile open = im.FactorScale("images/blanche/Blanche_smile_open.png", blancheSpriteSize)
image blanche surprised close = im.FactorScale("images/blanche/Blanche_surprised_close.png", blancheSpriteSize)
image blanche surprised open = im.FactorScale("images/blanche/Blanche_surprised_open.png", blancheSpriteSize)
image blanche neutralf close = im.Flip(im.FactorScale("images/blanche/Blanche_neutral_close.png", blancheSpriteSize), horizontal="True")
image blanche neutralf open = im.Flip(im.FactorScale("images/blanche/Blanche_neutral_open.png", blancheSpriteSize), horizontal="True")

image noir bandeau hurt close = im.FactorScale("images/noir/bandeau/hurt_close.png", blancheSpriteSize)
image noir bandeau hurt open = im.FactorScale("images/noir/bandeau/hurt_open.png", blancheSpriteSize)
image noir bandeau neutral close = im.FactorScale("images/noir/bandeau/neutral_close.png", blancheSpriteSize)
image noir bandeau neutral open = im.FactorScale("images/noir/bandeau/neutral_open.png", blancheSpriteSize)
image noir bandeau sigh close = im.FactorScale("images/noir/bandeau/sigh_close.png", blancheSpriteSize)
image noir bandeau sigh open = im.FactorScale("images/noir/bandeau/sigh_open.png", blancheSpriteSize)
image noir bandeau smile close = im.FactorScale("images/noir/bandeau/smile_close.png", blancheSpriteSize)
image noir bandeau smile open = im.FactorScale("images/noir/bandeau/smile_open.png", blancheSpriteSize)
image noir bandeau surprised close = im.FactorScale("images/noir/bandeau/surprised_close.png", blancheSpriteSize)
image noir bandeau surprised open = im.FactorScale("images/noir/bandeau/surprised_open.png", blancheSpriteSize)

image noir neutral close = im.FactorScale("images/noir/neutral_close.png", blancheSpriteSize)
image noir neutral open = im.FactorScale("images/noir/neutral_open.png", blancheSpriteSize)
image noir smile close = im.FactorScale("images/noir/smile_close.png", blancheSpriteSize)
image noir smile open = im.FactorScale("images/noir/smile_open.png", blancheSpriteSize)
image noir surprised close = im.FactorScale("images/noir/surprised_close.png", blancheSpriteSize)
image noir surprised open = im.FactorScale("images/noir/surprised_open.png", blancheSpriteSize)

image mme hologramme = im.FactorScale("images/mmeaec/mme_hologramme.png", blancheSpriteSize)
image mme angry close = im.FactorScale("images/mmeaec/mme_angry_close.png", blancheSpriteSize)
image mme angry open = im.FactorScale("images/mmeaec/mme_angry_open.png", blancheSpriteSize)
image mme blush close = im.FactorScale("images/mmeaec/mme_blush_close.png", blancheSpriteSize)
image mme blush open = im.FactorScale("images/mmeaec/mme_blush_open.png", blancheSpriteSize)
image mme ignore close = im.FactorScale("images/mmeaec/mme_ignore_close.png", blancheSpriteSize)
image mme ignore open = im.FactorScale("images/mmeaec/mme_ignore_open.png", blancheSpriteSize)
image mme neutral close = im.FactorScale("images/mmeaec/mme_neutral_close.png", blancheSpriteSize)
image mme neutral open = im.FactorScale("images/mmeaec/mme_neutral_open.png", blancheSpriteSize)
image mme sad close = im.FactorScale("images/mmeaec/mme_sad_close.png", blancheSpriteSize)
image mme sad open =  im.FactorScale("images/mmeaec/mme_sad_open.png", blancheSpriteSize)

# Flip
image mme angryf close = im.Flip(im.FactorScale("images/mmeaec/mme_angry_close.png", blancheSpriteSize), horizontal="True")
image mme angryf open = im.Flip(im.FactorScale("images/mmeaec/mme_angry_open.png", blancheSpriteSize), horizontal="True")
image mme neutralf close = im.Flip(im.FactorScale("images/mmeaec/mme_neutral_close.png", blancheSpriteSize), horizontal="True")
image mme neutralf open = im.Flip(im.FactorScale("images/mmeaec/mme_neutral_open.png", blancheSpriteSize), horizontal="True")

image grosso = im.FactorScale("images/gardes/grosso.png", guardSpriteSize)
image maigrichon = im.FactorScale("images/gardes/maigrichon.png", guardSpriteSize)

image violet = im.FactorScale("images/chats/violet.png", catSpriteSize)
image indigo = im.FactorScale("images/chats/indigo.png", catSpriteSize)
image cyan = im.FactorScale("images/chats/cyan.png", catSpriteSize)
image cyan2 = im.FactorScale("images/chats/cyan2.png", catSpriteSize)
image emeraude = im.FactorScale("images/chats/emeraude.png", catSpriteSize)
image jaune = im.FactorScale("images/chats/jaune.png", catSpriteSize)
image orange = im.FactorScale("images/chats/orange.png", catSpriteSize)
image rouge = im.FactorScale("images/chats/red.png", catSpriteSize)

# Déclarez les personnages utilisés dans le jeu.
define narrator = Character(None, window_background="textbox", what_italic=True, what_ypos=0.3)
define x = Character('???', window_background="char_textbox unknown")
define blanche = Character('[player_name]')
define madame = Character(_('Arc-en-Ciel'), window_background="char_textbox arcenciel")
define grosso = Character(_('Grosso'))
define maigrichon = Character(_('Maigrichon'))
define noir = Character(_('Père Noir'), window_background="char_textbox noir")
define violet = Character(_('Violet'), window_background="char_textbox violet")
define indigo = Character(_('Indigo'), window_background="char_textbox indigo")
define grosso_maigrichon = Character(_('Les deux'))
define cameraman = Character(_('Caméraman'), window_background="char_textbox cameraman")
define cyan = Character(_('Cyan'), window_background="char_textbox cyan")
define emeraude = Character(_('Émeraude'), window_background="char_textbox emeraude")
define piou = Character(_('Piou'), window_background="char_textbox piou")
define jaune = Character(_('Jaune'), window_background="char_textbox jaune")
define orange = Character(_('Orange'), window_background="char_textbox orange")
define red = Character(_('Red'), window_background="char_textbox red")
define axolotl = Character(_('Picaru'), window_background="char_textbox axolotl")
