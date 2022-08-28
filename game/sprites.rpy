# Background images
image room = "images/bg/room.png"
image voeu = "images/bg/voeu.png"
image world = "images/bg/world.png"
image forest = "images/bg/forest.png"
image garden = "images/bg/garden.png"
image lake_shallow = "images/bg/lake_shallow.png"
image lake_transparent = "images/bg/lake_transparent.png"
image lake_deep = "images/bg/lake_deep.png"

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
image crystal_cyan = "images/boules/Boules_3.png"

# Lake images
image lake_mousehole = "images/items/hole_alpha.png"
image lake_axolotl = "images/fish/Axolotl.png"
image lake_boot = "images/fish/Boot.png"
image lake_fish1:
    contains lake_wavy_patrol("images/fish/Fish1.png", 500, 60, 212)
image lake_fish21:
    contains lake_love_patrol("images/fish/Fish2_1.png", 360, 500, 2)
image lake_fish22:
    contains lake_love_patrol("images/fish/Fish2_2.png", 300, 400, 2, 0.5)
image lake_fish23:
    contains lake_love_patrol("images/fish/Fish2_3.png", 450, 600, 2, 1.2)
image lake_rainbow_fish:
    contains lake_rainbow_patrol("images/fish/RainbowFish.png")
image fish_shadow1 = "images/fish/Fish_shadow1.png"

# CG
python:
    nb_cg = 7
    for i in range(1, nb_cg):
        renpy.image("cg"+str(i), Image("images/cg/cg"+str(i)+".png"))
