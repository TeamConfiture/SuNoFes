# Background images
image room = "images/bg/room.png"
image voeu = "images/bg/voeu.png"
image world = "images/bg/world.png"
image forest = "images/bg/forest.png"
image garden = "images/bg/garden.png"

# Individual sprites
image mulberry = "images/items/mulberry_base.png"
image mulberry_button = "images/items/mulberry.png"

image crystal_purple = "images/boules/Boules_1.png"

# CG
python:
    nb_cg = 7
    for i in range(1, nb_cg):
        renpy.image("cg"+str(i), Image("images/cg/cg"+str(i)+".png"))
