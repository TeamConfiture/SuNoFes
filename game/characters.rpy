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

image blanche cry close = Transform("images/blanche/Blanche_cry_close.png", zoom = blancheSpriteSize)
image blanche cry open = Transform("images/blanche/Blanche_cry_open.png", zoom = blancheSpriteSize)
image blanche neutral close = Transform("images/blanche/Blanche_neutral_close.png", zoom = blancheSpriteSize)
image blanche neutral open = Transform("images/blanche/Blanche_neutral_open.png", zoom = blancheSpriteSize)
image blanche pout close = Transform("images/blanche/Blanche_pout_close.png", zoom = blancheSpriteSize)
image blanche pout open = Transform("images/blanche/Blanche_pout_open.png", zoom = blancheSpriteSize)
image blanche smile close = Transform("images/blanche/Blanche_smile_close.png", zoom = blancheSpriteSize)
image blanche smile open = Transform("images/blanche/Blanche_smile_open.png", zoom = blancheSpriteSize)
image blanche surprised close = Transform("images/blanche/Blanche_surprised_close.png", zoom = blancheSpriteSize)
image blanche surprised open = Transform("images/blanche/Blanche_surprised_open.png", zoom = blancheSpriteSize)
image blanche neutralf close = Transform("images/blanche/Blanche_neutral_close.png", xzoom = -blancheSpriteSize, yzoom = blancheSpriteSize)
image blanche neutralf open = Transform("images/blanche/Blanche_neutral_open.png", xzoom = -blancheSpriteSize, yzoom = blancheSpriteSize)

image noir bandeau hurt close = Transform("images/noir/bandeau/hurt_close.png", zoom = blancheSpriteSize)
image noir bandeau hurt open = Transform("images/noir/bandeau/hurt_open.png", zoom = blancheSpriteSize)
image noir bandeau neutral close = Transform("images/noir/bandeau/neutral_close.png", zoom = blancheSpriteSize)
image noir bandeau neutral open = Transform("images/noir/bandeau/neutral_open.png", zoom = blancheSpriteSize)
image noir bandeau sigh close = Transform("images/noir/bandeau/sigh_close.png", zoom = blancheSpriteSize)
image noir bandeau sigh open = Transform("images/noir/bandeau/sigh_open.png", zoom = blancheSpriteSize)
image noir bandeau smile close = Transform("images/noir/bandeau/smile_close.png", zoom = blancheSpriteSize)
image noir bandeau smile open = Transform("images/noir/bandeau/smile_open.png", zoom = blancheSpriteSize)
image noir bandeau surprised close = Transform("images/noir/bandeau/surprised_close.png", zoom = blancheSpriteSize)
image noir bandeau surprised open = Transform("images/noir/bandeau/surprised_open.png", zoom = blancheSpriteSize)

image noir neutral close = Transform("images/noir/neutral_close.png", zoom = blancheSpriteSize)
image noir neutral open = Transform("images/noir/neutral_open.png", zoom = blancheSpriteSize)
image noir smile close = Transform("images/noir/smile_close.png", zoom = blancheSpriteSize)
image noir smile open = Transform("images/noir/smile_open.png", zoom = blancheSpriteSize)
image noir surprised close = Transform("images/noir/surprised_close.png", zoom = blancheSpriteSize)
image noir surprised open = Transform("images/noir/surprised_open.png", zoom = blancheSpriteSize)

image mme hologramme = Transform("images/mmeaec/mme_hologramme.png", zoom = blancheSpriteSize)
image mme angry close = Transform("images/mmeaec/mme_angry_close.png", zoom = blancheSpriteSize)
image mme angry open = Transform("images/mmeaec/mme_angry_open.png", zoom = blancheSpriteSize)
image mme blush close = Transform("images/mmeaec/mme_blush_close.png", zoom = blancheSpriteSize)
image mme blush open = Transform("images/mmeaec/mme_blush_open.png", zoom = blancheSpriteSize)
image mme ignore close = Transform("images/mmeaec/mme_ignore_close.png", zoom = blancheSpriteSize)
image mme ignore open = Transform("images/mmeaec/mme_ignore_open.png", zoom = blancheSpriteSize)
image mme neutral close = Transform("images/mmeaec/mme_neutral_close.png", zoom = blancheSpriteSize)
image mme neutral open = Transform("images/mmeaec/mme_neutral_open.png", zoom = blancheSpriteSize)
image mme sad close = Transform("images/mmeaec/mme_sad_close.png", zoom = blancheSpriteSize)
image mme sad open =  Transform("images/mmeaec/mme_sad_open.png", zoom = blancheSpriteSize)

# Flip
image mme angryf close = Transform("images/mmeaec/mme_angry_close.png", xzoom = -blancheSpriteSize, yzoom = blancheSpriteSize)
image mme angryf open = Transform("images/mmeaec/mme_angry_open.png", xzoom = -blancheSpriteSize, yzoom = blancheSpriteSize)
image mme neutralf close = Transform("images/mmeaec/mme_neutral_close.png", xzoom = -blancheSpriteSize, yzoom = blancheSpriteSize)
image mme neutralf open = Transform("images/mmeaec/mme_neutral_open.png", xzoom = -blancheSpriteSize, yzoom = blancheSpriteSize)

image grosso = Transform("images/gardes/grosso.png", zoom = guardSpriteSize)
image maigrichon = Transform("images/gardes/maigrichon.png", zoom = guardSpriteSize)

image violet = Transform("images/chats/violet.png", zoom = catSpriteSize)
image indigo = Transform("images/chats/indigo.png", zoom = catSpriteSize)
image cyan = Transform("images/chats/cyan.png", zoom = catSpriteSize)
image cyan2 = Transform("images/chats/cyan2.png", zoom = catSpriteSize)
image emeraude = Transform("images/chats/emeraude.png", zoom = catSpriteSize)
image jaune = Transform("images/chats/jaune.png", zoom = catSpriteSize)
image orange = Transform("images/chats/orange.png", zoom = catSpriteSize)
image rouge = Transform("images/chats/red.png", zoom = catSpriteSize)

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
