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

image mme hologramme = im.FactorScale("images/mmeaec/MME_AEC_3_B4.png", blancheSpriteSize)

image grosso = im.FactorScale("images/gardes/grosso.png", guardSpriteSize)
image maigrichon = im.FactorScale("images/gardes/maigrichon.png", guardSpriteSize)

image violet = im.FactorScale("images/chats/violet.png", catSpriteSize)
image indigo = im.FactorScale("images/chats/indigo.png", catSpriteSize)
image cyan = im.FactorScale("images/chats/cyan.png", catSpriteSize)
image cyan2 = im.FactorScale("images/chats/cyan2.png", catSpriteSize)
image emeraude = im.FactorScale("images/chats/emeraude.png", catSpriteSize)

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
