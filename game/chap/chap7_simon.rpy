screen chap7_simon_says(next_label, previous_label):
    python:
        def button_action(i):
            return Play('sound', sound.Arrow[i%len(sound.Arrow)])
    default simon = SimonGame(
        buttons = [
            {"auto": "images/items/arrows/Fl_bottom_%s.png", "xalign": 0.5, "yalign": 0.8, "action": button_action(0)},
            {"auto": "images/items/arrows/Fl_up_%s.png", "xalign": 0.5, "yalign": 0.2, "action": button_action(1)},
            {"auto": "images/items/arrows/Fl_left_%s.png", "xalign": 0.3, "yalign": 0.5, "action": button_action(2)},
            {"auto": "images/items/arrows/Fl_right_%s.png", "xalign": 0.7, "yalign": 0.5, "action": button_action(3)},
        ],
        completion_action = Jump(next_label),
        failure_action = Jump(previous_label),
        generated_len = 5,
    )
    add simon
    textbutton "Show again":
        ypos 100
        action Function(simon.update_simon_demonstration)
