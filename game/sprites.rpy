# Background images
image room = "images/bg/room.png"
image voeu = "images/bg/voeu.png"
image world = "images/bg/world.png"
image forest = "images/bg/forest.png"
image garden = "images/bg/garden.png"
image lake_shallow = "images/bg/lake_shallow.png"
image lake_transparent = "images/bg/lake_transparent.png"
image lake_deep = "images/bg/lake_deep.png"
image cupboard = "images/bg/cupboard.png"

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
image crystal_green = "images/boules/Boules_4.png"

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

## Cheese cupboard
# Cheese draggables
image cheese_market_fr1_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr1.png", 0)
image cheese_market_fr1_180:
    contains cheese_cupboard_angle("images/items/fromages/Fr1.png", 180)
image cheese_market_fr1a_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr1a.png", 0)
image cheese_market_fr2_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr2.png", 0)
image cheese_market_fr2a_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr2a.png", 0)
image cheese_market_fr3_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr3.png", 0)
image cheese_market_fr3a_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr3a.png", 0)
image cheese_market_fr4_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr4.png", 0)
image cheese_market_fr4_90:
    contains cheese_cupboard_angle("images/items/fromages/Fr4.png", 90)
image cheese_market_fr4a_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr4a.png", 0)
image cheese_market_fr4a_90:
    contains cheese_cupboard_angle("images/items/fromages/Fr4a.png", 90)
image cheese_market_fr5_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr5.png", 0)
image cheese_market_fr5_30:
    contains cheese_cupboard_angle("images/items/fromages/Fr5.png", 30)
image cheese_market_fr5_320:
    contains cheese_cupboard_angle("images/items/fromages/Fr5.png", 320)
image cheese_market_fr5a_0:
    contains cheese_cupboard_angle("images/items/fromages/Fr5a.png", 0)
image cheese_market_fr5a_30:
    contains cheese_cupboard_angle("images/items/fromages/Fr5a.png", 30)
image cheese_market_fr5a_320:
    contains cheese_cupboard_angle("images/items/fromages/Fr5a.png", 320)
# Fish background
image cheese_market_fish2_0:
    contains cheese_cupboard_angle("images/fish/Fish2_1.png", 0)
image cheese_market_fish2_180:
    contains cheese_cupboard_angle("images/fish/Fish2_1.png", 180)
# Expected cheese arrival
image cheese_market_entrance_fr1:
    contains cheese_cupboard_entrance("images/items/fromages/Fr1.png", 0.8, xalign = 203/414, yalign = 175/304)
image cheese_market_entrance_fr1a:
    contains cheese_cupboard_entrance("images/items/fromages/Fr1a.png", 0.8, xalign = 203/414, yalign = 175/304)
image cheese_market_entrance_fr2:
    contains cheese_cupboard_entrance("images/items/fromages/Fr2.png", 0.9, xalign = 184/414, yalign = 156/304)
image cheese_market_entrance_fr2a:
    contains cheese_cupboard_entrance("images/items/fromages/Fr2a.png", 0.9, xalign = 184/414, yalign = 156/304)
image cheese_market_entrance_fr3:
    contains cheese_cupboard_entrance("images/items/fromages/Fr3.png", 0.8, xalign = 227/414, yalign = 144/304)
image cheese_market_entrance_fr3a:
    contains cheese_cupboard_entrance("images/items/fromages/Fr3a.png", 0.8, xalign = 227/414, yalign = 144/304)
image cheese_market_entrance_fr4:
    contains cheese_cupboard_entrance("images/items/fromages/Fr4.png", 0.9, xalign = 205/414, yalign = 167/304)
image cheese_market_entrance_fr4a:
    contains cheese_cupboard_entrance("images/items/fromages/Fr4a.png", 0.9, xalign = 205/414, yalign = 167/304)
image cheese_market_entrance_fr5:
    contains cheese_cupboard_entrance("images/items/fromages/Fr5.png", xalign = 183/414, yalign = 177/304)
image cheese_market_entrance_fr5a:
    contains cheese_cupboard_entrance("images/items/fromages/Fr5a.png", xalign = 183/414, yalign = 177/304)
# Expected cheese deletion
image cheese_market_exit_fr1:
    contains cheese_cupboard_exit("images/items/fromages/Fr1.png", 0.8, xalign = 203/414, yalign = 175/304)
image cheese_market_exit_fr1a:
    contains cheese_cupboard_exit("images/items/fromages/Fr1a.png", 0.8, xalign = 203/414, yalign = 175/304)
image cheese_market_exit_fr2:
    contains cheese_cupboard_exit("images/items/fromages/Fr2.png", 0.9, xalign = 184/414, yalign = 156/304)
image cheese_market_exit_fr2a:
    contains cheese_cupboard_exit("images/items/fromages/Fr2a.png", 0.9, xalign = 184/414, yalign = 156/304)
image cheese_market_exit_fr3:
    contains cheese_cupboard_exit("images/items/fromages/Fr3.png", 0.8, xalign = 227/414, yalign = 144/304)
image cheese_market_exit_fr3a:
    contains cheese_cupboard_exit("images/items/fromages/Fr3a.png", 0.8, xalign = 227/414, yalign = 144/304)
image cheese_market_exit_fr4:
    contains cheese_cupboard_exit("images/items/fromages/Fr4.png", 0.9, xalign = 205/414, yalign = 167/304)
image cheese_market_exit_fr4a:
    contains cheese_cupboard_exit("images/items/fromages/Fr4a.png", 0.9, xalign = 205/414, yalign = 167/304)
image cheese_market_exit_fr5:
    contains cheese_cupboard_exit("images/items/fromages/Fr5.png", xalign = 183/414, yalign = 177/304)
image cheese_market_exit_fr5a:
    contains cheese_cupboard_exit("images/items/fromages/Fr5a.png", xalign = 183/414, yalign = 177/304)

# CG
python:
    nb_cg = 7
    for i in range(1, nb_cg):
        renpy.image("cg"+str(i), Image("images/cg/cg"+str(i)+".png"))
