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
define narrator = Character(None, window_background="gui/textbox_noname.png", window_xsize=1803, window_ysize=388, what_xpos=38, what_ypos=126, what_italic=True)
define x = Character('???', who_color="#ffffff")
define blanche = Character('[player_name]', who_color="#ffffff")
define madame = Character(_('Arc-en-Ciel'), who_color="#ffffff")
define grosso = Character(_('Grosso'), who_color="#ffffff")
define maigrichon = Character(_('Maigrichon'), who_color="#ffffff")
define noir = Character(_('Père Noir'), who_color="#000000")
define violet = Character(_('Violet'), who_color="#753799")
define indigo = Character(_('Indigo'), who_color="#202A7F")
define grosso_maigrichon = Character(_('Les deux'), who_color="#ffffff")
define cameraman = Character(_('Caméraman'), who_color="#ffffff")
define cyan = Character(_('Cyan'), who_color="#216d77")
define emeraude = Character(_('Émeraude'), who_color="#ffffff")
define piou = Character(_('Piou'), who_color="#ffd000")
define jaune = Character(_('Jaune'), who_color="#ffee00")
define orange = Character(_('Orange'), who_color="#ff7b00")
define red = Character(_('Red'), who_color="#af1212")
define axolotl = Character(_('Picaru'), who_color="#dab6ca")
