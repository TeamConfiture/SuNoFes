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

# GUI images
image textbox:
    "gui/textbox_noname.png"
    xalign 0.5 yalign 1.0

layeredimage char_textbox:
    xalign 0.5 yalign 1.0
    always:
        "gui/textbox_message.png"
    group character:
        attribute white default:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#999"))
        attribute unknown:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#666"))
        attribute arcenciel:
            AlphaMask("gui/textbox_rainbow.png", "gui/textbox_namebox.png")
        attribute axolotl:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#ff48a4"))
        attribute cameraman:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#215c77"))
        attribute cyan:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#216d77"))
        attribute emeraude:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#26a269"))
        attribute indigo:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#202A7F"))
        attribute jaune:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#986a44"))
        attribute noir:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#000"))
        attribute orange:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#ff7b00"))
        attribute piou:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#ffd000"))
        attribute red:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#af1212"))
        attribute violet:
            "gui/textbox_namebox.png" at Transform(matrixcolor = TintMatrix("#753799"))

# Individual sprites
image writing_feather:
    "images/items/feather.png"
    zoom 0.6
    yanchor 0.6
    block:
        alpha 1.
        pause 0.6
        ease 0.2 alpha 0.
        alpha 0.
        pause 0.6
        ease 0.2 alpha 1.
        repeat

image continue_button_idle = "gui/button/continue_button_idle.png"
image continue_button_hover = "gui/button/continue_button_hover.png"

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
image crystal_yellow = "images/boules/Boules_5.png"
image crystal_orange = "images/boules/Boules_6.png"
image crystal_red = "images/boules/Boules_7.png"

# Tutorial

transform tutorial_pointer_effect(yoffset_range=[0, 0], alpha_range=[0, 1]):
    parallel:
        ease 1 yoffset yoffset_range[0]
        ease 1 yoffset yoffset_range[1]
        repeat
    parallel:
        ease 1.3 alpha alpha_range[0]
        ease 1.3 alpha alpha_range[1]
        repeat

layeredimage tutorial_arrow:
    always:
        "images/items/arrows/Fl_bottom_idle.png"
        zoom 0.5
        anchor (0.5, 1.)
        yoffset -30
    at tutorial_pointer_effect([30, 0], [0.95, 0.7])

image tutorial_button_idle:
    "images/items/nighttable_item.png"
    xzoom -1
    matrixcolor BrightnessMatrix(0)
image tutorial_button_hover:
    "images/items/nighttable_item.png"
    xzoom -1
    matrixcolor BrightnessMatrix(0.2)

layeredimage tutorial_boot:
    always:
        "lake_boot"
    at Transform(zoom = 0.7)

image tutorial_basket:
    "cheese_market_basket"
    zoom 0.7

# Chap 2 - Sky images

image chap2_spirited = Spirited(
    sprite_list = ["images/sprites/small_firefly.png", "images/sprites/medium_firefly.png"],
    initial_count = 10,
    renewal_rate = 30,
    speed_range = (2, 10),
    direction_range = (80, 100),
    ttl_range = (1, 3),
)

# Lake images
image lake_mousehole = "images/items/hole_alpha.png"
image lake_axolotl = "images/fish/Axolotl.png"
image lake_boot = "images/fish/Boot.png"
image lake_fish1 = "images/fish/Fish1.png"
image lake_fish21 = "images/fish/Fish2_1.png"
image lake_fish22 = "images/fish/Fish2_2.png"
image lake_fish23 = "images/fish/Fish2_3.png"
image lake_rainbow_fish = "images/fish/RainbowFish.png"
image fish_shadow1 = "images/fish/Fish_shadow1.png"

## Cheese cupboard
image cheese_market_basket:
    contains cheese_cupboard_basket("images/items/cheese_basket.png", scale = 0.9)
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

# Noir
image end_spirited_back = Spirited(
    sprite_list = ["images/sprites/small_firefly_black.png", "images/sprites/medium_firefly_black.png", "images/sprites/big_firefly_black.png"],
    initial_count = 100,
    renewal_rate = 100,
    speed_range = (30, 40),
    direction_range = (60, 120),
    ttl_range = (10, 15),
    spawn_box = (config.screen_width/2 + 250, config.screen_height/2, -config.screen_width/4, 0),
)

image end_spirited_front = Spirited(
    sprite_list = ["images/sprites/small_firefly_black.png", "images/sprites/medium_firefly_black.png", "images/sprites/big_firefly_black.png"],
    initial_count = 5,
    renewal_rate = 5,
    speed_range = (30, 40),
    direction_range = (60, 120),
    ttl_range = (10, 15),
    spawn_box = (config.screen_width/2 + 250, config.screen_height/2, -config.screen_width/4, 0),
)

image neutral_end_spirited_final_long = Spirited(
    sprite_list = ["images/sprites/small_firefly_black.png", "images/sprites/medium_firefly_black.png", "images/sprites/big_firefly_black.png"],
    initial_count = 50,
    renewal_rate = 300,
    speed_range = (30, 40),
    roll_range = (0, 20),
    direction_range = (20, 60),
    ttl_range = (10, 40),
    spawn_box = (config.screen_width/2 - 220, 300, - config.screen_width/2 - 180, -200),
)

image neutral_end_spirited_final_short = Spirited(
    sprite_list = ["images/sprites/small_firefly_black.png", "images/sprites/medium_firefly_black.png", "images/sprites/big_firefly_black.png"],
    initial_count = 0,
    renewal_rate = 200,
    speed_range = (30, 40),
    roll_range = (0, 20),
    direction_range = (0, 70),
    ttl_range = (10, 30),
    spawn_box = (config.screen_width/2 - 220, 300, - config.screen_width/2 - 180, -200),
)

# main menu spiriteds
image spirited_main_menu_white = Spirited(
    sprite_list = ["images/sprites/small_firefly.png", "images/sprites/big_firefly.png", "images/sprites/medium_firefly.png"],
    initial_count = 30,
    renewal_rate = 50,
    speed_range = (10, 150),
    direction_range = (80, 100),
    ttl_range = (1, 3),
)
image spirited_main_menu_black = Spirited(
    sprite_list = ["images/sprites/small_firefly_black.png", "images/sprites/big_firefly_black.png", "images/sprites/medium_firefly_black.png"],
    initial_count = 30,
    renewal_rate = 50,
    speed_range = (10, 150),
    direction_range = (80, 100),
    ttl_range = (1, 3),
)

# CG
python:
    nb_cg = 7
    for i in range(1, nb_cg):
        renpy.image("cg"+str(i), Image("images/cg/cg"+str(i)+".png"))
