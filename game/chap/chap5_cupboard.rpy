init python:
    import math
    def cheese_market_cheese_positions():
        # How to edit this:
        # 1 - Add the following line at the start of the drag_race
        # print(drags[0].drag_name + " " + str(drags[0].get_placement()))
        # 2 - Move the image you want to use into the desired spot
        # 3 - Look at the console output to know which cheese to update
        # 3a - The 'base_name' is the start of the first printed string
        # 3b - The 'props' index is the last number in the first printed string
        # 3c - The x/y values are the first values in the printed tuple
        # 3d - Note that all angles MUST have a match
        cheese_market_info = [
                # The comments indicate the cupboard(left to right) and level (bottom to top)
                {
                    "base_name": "fr1", "props": [
                        # 1-2
                        {"x": 706, "y": 562}, {"x": 699, "y": 477},
                        # 1-3
                        {"x": 608, "y": 345, "angle": 180, "layer": 0},
                        # 1-4
                        {"x": 515, "y": 100},
                        # 2-2
                        {"x": 1520, "y": 667},
                        # 2-3
                        {"x": 1366, "y": 439, "layer": 1},
                    ],
                }, {
                    "base_name": "fr1a", "props": [
                        # 2-3
                        {"x": 1173, "y": 439, "layer": 1}, {"x": 1294, "y": 346, "layer": 1},
                        # 2-5
                        {"x": 1498, "y": -84}, {"x": 1051, "y": -82},
                    ],
                }, {
                    "base_name": "fr2", "props": [ # Emmental
                        # 1-3
                        {"x": 295, "y": 300},
                        {"x": -4, "y": 304},
                        # 1-4
                        {"x": 759, "y": 86},
                        # 2-2
                        {"x": 1032, "y": 669},
                        # 2-4
                        {"x": 1144, "y": 145},
                        {"x": 1633, "y": 152},
                    ],
                }, {
                    "base_name": "fr2a", "props": [ # Emmental mais avec du poison
                        # 1-2
                        {"x": 6, "y": 529}, {"x": 766, "y": 552},
                        # 1-5
                        {"x": 765, "y": -194},
                        # 2-2
                        {"x": 1475, "y": 657},
                        # 2-5
                        {"x": 1695, "y": -97},
                    ],
                }, {
                    "base_name": "fr3", "props": [ # Gouda
                        # 1-1
                        {"x": 704, "y": 811},
                        # 1-2
                        {"x": 476, "y": 557},
                        # 1-4
                        {"x": 521, "y": 23, "layer": 1},
                        # 2-2
                        {"x": 1306, "y": 666},
                    ],
                }, {
                    "base_name": "fr3a", "props": [ # Gouda
                        # 1-1
                        {"x": 481, "y": 799},
                        # 2-4
                        {"x": 1414, "y": 158}, {"x": 1313, "y": 157}, {"x": 1217, "y": 154},
                        # 2-3
                        {"x": 998, "y": 430}, {"x": 1544, "y": 440, "layer": 0},
                    ],
                }, {
                    "base_name": "fr4", "props": [ # Roquefort
                        # 1-1
                        {"x": -40, "y": 824, "angle": 90}, {"x": 175, "y": 837, "angle": 90},
                        {"x": 294, "y": 849, "angle": 90},
                        # 1-2
                        {"x": 273, "y": 534},
                        # 2-5
                        {"x": 1307, "y": -88},
                    ],
                }, {
                    "base_name": "fr4a", "props": [ # Roquefort
                        # 1-1
                        {"x": 51, "y": 800, "angle": 90},
                        # 1-3
                        {"x": 139, "y": 303},
                        # 1-4
                        {"x": 208, "y": 89},
                        # 2-4
                        {"x": 1019, "y": 143, "layer": 0}, {"x": 1508, "y": 149, "layer": 0},
                    ],
                }, {
                    "base_name": "fr5", "props": [
                        # 1-3
                        {"x": 450, "y": 263}, {"x": 618, "y": 297, "angle": 30},
                        # 1-4
                        {"x": 3, "y": 117}, {"x": 40, "y": 58},
                        {"x": 374, "y": 70, "angle": 320},
                    ],
                }, {
                    "base_name": "fr5a", "props": [
                        # 1-3
                        {"x": 490, "y": 320, "layer": 1},
                        {"x": 727, "y": 298, "angle": 30}, {"x": 788, "y": 264, "angle": 30},
                        # 2-2
                        {"x": 1222, "y": 687},
                        # 2-3
                        {"x": 1144, "y": 321, "angle": 320, "layer": 2},
                    ],
                },
            ]
        return cheese_market_info

    def cheese_market_build_request_list(cheese_index, request_count = 10, guaranteed_rainbows = 2):
        request_count = min(request_count, sum([cheese_index[i] for i in cheese_index]))
        generated_list = []
        collected_dict = cheese_index.copy()
        modulo = math.floor((request_count / (guaranteed_rainbows or 1))) or 1
        while len(generated_list) < request_count:
            cheese_label = renpy.random.choice([k for k in collected_dict])
            if collected_dict[cheese_label] >= 1 and ((len(generated_list) + 1) % modulo or 'a' in cheese_label):
                # 0-size dicts are allowed to guarantee equiprobability
                generated_list.append(cheese_label)
                collected_dict[cheese_label] -= 1
        return generated_list

label cheese_market_fail:
    "Ce n'est pas le fromage que je t'ai demandé !"
    call screen cheese_market()

screen cheese_market():
    # Modifier ces valeurs pour rediriger vers d'autres labels
    default next_label = 'chap5_2'
    default fail_scene = 'cheese_market_fail'
    # Valeurs internes
    default collected_cheese = set()
    default displayed_cheese = cheese_market_cheese_positions()
    default cheese_request_list = cheese_market_build_request_list({i["base_name"]: len(i["props"]) for i in displayed_cheese})
    default current_index = 0
    python:
        def drag_race(drags, drop):
            if drop:
                # Manually ensure that images' bytes overlap
                # This is done by sampling the overlapping area and is
                # not 100% accurate but sufficient in most cases
                drag = drags[0]
                drag_render = drag.render(drag.w, drag.h, 0, drag.at)
                drop_render = drop.render(drop.w, drop.h, 0, drop.at)
                drag_pos = drag.get_placement()
                drop_pos = drop.get_placement()
                common_pos = (max(drag_pos[0], drop_pos[0]), max(drag_pos[1], drop_pos[1]))
                common_width = (
                    min(drag_pos[0] + drag_render.get_size()[0], drop_pos[0] + drop_render.get_size()[0]) - common_pos[0],
                    min(drag_pos[1] + drag_render.get_size()[1], drop_pos[1] + drop_render.get_size()[1]) - common_pos[1],
                    )
                is_overlapping = False
                for i in range(100):
                    x_f = (i%10)/10
                    y_f = math.floor(i/10)/10
                    drag_projection = (
                        common_pos[0] + common_width[0] * x_f - drag_pos[0],
                        common_pos[1] + common_width[1] * y_f - drag_pos[1],
                    )
                    drop_projection = (
                        common_pos[0] + common_width[0] * x_f - drop_pos[0],
                        common_pos[1] + common_width[1] * y_f - drop_pos[1],
                    )
                    if drag_render.is_pixel_opaque(*drag_projection) and drop_render.is_pixel_opaque(*drop_projection):
                        is_overlapping = True
                        break
                if is_overlapping:
                    # Only if both images have opaque pixels in common do we check for validity
                    cupboard = renpy.current_screen().scope['cupboard']
                    cheese_request_list = renpy.current_screen().scope['cheese_request_list']
                    current_index = renpy.current_screen().scope['current_index']
                    collected_cheese = renpy.current_screen().scope['collected_cheese']
                    if cheese_request_list[current_index] in drags[0].drag_name:
                        cupboard.remove(cupboard.get_child_by_name(drags[0].drag_name))
                        # This also triggers a view update
                        renpy.run(SetScreenVariable('collected_cheese', [i for i in collected_cheese] + [drags[0].drag_name]))
                        renpy.run(SetScreenVariable('current_index', (current_index + 1) % len(cheese_request_list)))
                        if current_index + 1 == len(cheese_request_list):
                            # Exit the screen if we reached endd of array
                            renpy.run(Jump(renpy.current_screen().scope['next_label']))
                    else:
                        renpy.run(Jump(renpy.current_screen().scope['fail_scene']))

    # Background image
    add 'cupboard'
    # Generate fish row
    default top_fish_offset_front = [renpy.random.randint(0, 20) for _ in range(7)]
    default top_fish_offset_back = [renpy.random.randint(0, 40) for _ in range(7)]
    for i in range(7):
        image 'cheese_market_fish2_0':
            xpos 1585-i*100 ypos -240-top_fish_offset_back[i]
        image 'cheese_market_fish2_180':
            xpos 1650-i*100 ypos -230-top_fish_offset_front[i]
    draggroup:
        as cupboard
        for layer in [0, 1, 2, None]:
            for cheese_group in displayed_cheese:
                for index, cheese in enumerate(cheese_group['props']):
                    $ drag_name = cheese_group['base_name'] + "_" + str(cheese.get('angle', 0)) + "_" + str(index)
                    if cheese and cheese.get('layer') == layer and drag_name not in collected_cheese:

                        drag:
                            drag_name drag_name
                            child "cheese_market_" + cheese_group['base_name'] + "_" + str(cheese.get('angle', 0))
                            droppable False
                            dragged drag_race
                            drag_offscreen True
                            focus_mask True
                            xpos cheese['x'] ypos cheese['y']
        drag:
            drag_name "cheese_basket"
            child "images/fish/Boot.png"
            drag_offscreen True
            focus_mask True
            xpos 900 ypos 400
    # Show expected cheese
    if current_index < len(cheese_request_list):
        image "cheese_market_entrance_" + cheese_request_list[current_index]:
            xpos 255 ypos 90
    # Fade previous cheese
    if current_index > 0:
        image "cheese_market_exit_" + cheese_request_list[current_index-1]:
            xpos 255 ypos 90
