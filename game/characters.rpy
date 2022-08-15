# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les positions
define left = Position(xpos=0.30)
define center = Position(xpos=0.5)
define right = Position(xpos=0.70)

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

define humanSpriteSize = 0.55
define catSpriteSize = 0.50

image blanche cry close = im.FactorScale("images/blanche/Blanche_cry_close.png", humanSpriteSize)
image blanche cry open = im.FactorScale("images/blanche/Blanche_cry_open.png", humanSpriteSize)
image blanche neutral close = im.FactorScale("images/blanche/Blanche_neutral_close.png", humanSpriteSize)
image blanche neutral open = im.FactorScale("images/blanche/Blanche_neutral_open.png", humanSpriteSize)
image blanche pout close = im.FactorScale("images/blanche/Blanche_pout_close.png", humanSpriteSize)
image blanche pout open = im.FactorScale("images/blanche/Blanche_pout_open.png", humanSpriteSize)
image blanche smile close = im.FactorScale("images/blanche/Blanche_smile_close.png", humanSpriteSize)
image blanche smile open = im.FactorScale("images/blanche/Blanche_smile_open.png", humanSpriteSize)
image blanche surprised close = im.FactorScale("images/blanche/Blanche_surprised_close.png", humanSpriteSize)
image blanche surprised open = im.FactorScale("images/blanche/Blanche_surprised_open.png", humanSpriteSize)

image grosso = im.FactorScale("images/gardes/grosso.png", humanSpriteSize)
image maigrichon = im.FactorScale("images/gardes/maigrichon.png", humanSpriteSize)

image violet = im.FactorScale("images/chats/violet.png", catSpriteSize)

# Déclarez les personnages utilisés dans le jeu.
define narrator = Character(None, window_background="gui/textbox_noname.png", window_xsize=1803, window_ysize=388, what_xpos=38, what_ypos=126, what_italic=True)
define x = Character('???', who_color="#ffffff")
define blanche = Character('[player_name]', who_color="#ffffff")
define madame = Character(_('Madame Arc-En-Ciel'), who_color="#ff90ec")
define grosso = Character(_('Grosso'), who_color="#ffffff")
define maigrichon = Character(_('Maigrichon'), who_color="#ffffff")
define noir = Character(_('Père Noir'), who_color="#000000")
define violet = Character(_('Violet'), who_color="#753799")
define indigo = Character(_('Indigo'), who_color="#48d4ff")
define grosso_maigrichon = Character(_('Les deux'), who_color="#ffffff")
