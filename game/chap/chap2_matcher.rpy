screen chap2_match_screen():
    python:
        def generate_stars_mapping(count = 4):
            mapping = ([i for i in range(count)], [i for i in range(count)])
            renpy.random.shuffle(mapping[0])
            renpy.random.shuffle(mapping[1])
            return mapping
    default mapping = generate_stars_mapping(len(chap2_stars))
    default matcher = CardMatcher(
        anchor_definitions = {
            k+1: {
                "group": 1 if k < len(chap2_stars) else 2,
                "xpos": config.screen_width * (v + 1) / (len(chap2_stars) + 1) - 12,
                "ypos": (370 if k < len(chap2_stars) else 660)
                } for k, v in enumerate(mapping[0] + mapping[1])
        },
        anchor_rules = [(1,5), (2,6), (3, 7), (4, 8)],
        auto_base_button = "images/sprites/buzzer_%s.png", # If changing this, substract half the width to the xpos in anchor_definitions
        linked_base_button = Null(),
        rope_collection = [
            {"rope": "images/sprites/line_pull.png", "start_token": "images/sprites/buzzer_disabled.png", "end_token": "images/sprites/buzzer_disabled.png"},
            {"rope": "images/sprites/line_pull.png", "start_token": "images/sprites/buzzer_disabled.png"},
            ],
        rule_groups = {
            1: { "is_receiver": False },
            2: { "is_emitter": False },
        },
        rope_transforms = {1: 0},
        rope_pull_list = [1],
        completion_actions = [Jump("chap2_completed")]
    )
    add matcher
    for k, v in enumerate(mapping[0]):
        add chap2_stars[k][0]:
            yalign 0.1
            xpos (v + 1) / (len(chap2_stars) + 1)
            xanchor 0.5
    for k, v in enumerate(mapping[1]):
        add 'star_card':
            yalign 0.9
            xpos (v + 1) / (len(chap2_stars) + 1)
            xanchor 0.5
        text chap2_stars[k][1]:
            color '#fff'
            yalign 0.81
            xpos (v + 1) / (len(chap2_stars) + 1)
            xanchor 0.5
