screen chap7_simon_says(next_label, previous_label):
    default simon = SimonGame(
        buttons = [
            {"auto": "images/items/arrows/Fl_bottom_%s.png", "xalign": 0.5, "yalign": 0.8},
            {"auto": "images/items/arrows/Fl_up_%s.png", "xalign": 0.5, "yalign": 0.2},
            {"auto": "images/items/arrows/Fl_left_%s.png", "xalign": 0.3, "yalign": 0.5},
            {"auto": "images/items/arrows/Fl_right_%s.png", "xalign": 0.7, "yalign": 0.5},
        ],
        completion_action = Jump(next_label),
        failure_action = Jump(previous_label)
    )
    add simon
    textbutton "Show again":
        ypos 100
        action Function(simon.update_simon_demonstration)
