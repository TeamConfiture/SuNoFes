# Background images
image room = "images/bg/room.png"
image voeu = "images/bg/voeu.png"
image world = "images/bg/world.png"
image forest = "images/bg/forest.png"
image garden = "images/bg/garden.png"

# Individual sprites
image mulberry = "images/items/mulberry_base.png"
image mulberry_button = "images/items/mulberry.png"

image star_card = "images/items/star_card.png"
image star_leo = "images/items/star_leo.png"
image star_pisces = "images/items/star_pisces.png"
image star_piscis_austrinus = "images/items/star_piscis_austrinus.png"
image star_volans = "images/items/star_volans.png"

image boat = "images/items/boat.png"

image crystal_purple = "images/boules/Boules_1.png"
image crystal_indigo = "images/boules/Boules_2.png"

# CG
python:
    nb_cg = 7
    for i in range(1, nb_cg):
        renpy.image("cg"+str(i), Image("images/cg/cg"+str(i)+".png"))
