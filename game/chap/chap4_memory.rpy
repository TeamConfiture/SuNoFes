screen chap4_memory_game(next_chapter_label, timeout_label):
    default play_timer = 60
    default succeeded = 0
    timer 0.1: # Game timer, frozen if we succeed
        repeat True
        action If(play_timer > 0, true = If(succeeded == 0, true = SetScreenVariable('play_timer', play_timer - 0.1)), false = Jump(timeout_label))
    timer 0.5: # Delay before screen change on success
        repeat True
        action If(succeeded > 0, true = If(succeeded > 5, Jump(next_chapter_label), false = SetScreenVariable('succeeded', succeeded + 1)))
    python:
        def card_bg(id):
            return {
                "auto": "images/items/cards/Carte_dos_%s.png",
                "action": Play('sound', renpy.random.choice(sound.Card_Select)),
                }

    default memory = Memory(
        cards = [ { "selected_image": "images/items/cards/Carte" + str(i+1) + ".png", **card_bg(i) } for i in range(5) ],
        completion_actions = SetScreenVariable('succeeded', 1),
        pair_actions = Play('sound', renpy.random.choice(sound.Card_Together)),
        cols = 4, spacing = 20, null_entries = [6, 7],
        xalign = 0.5, yalign = 0.5,
        )
    add memory
    text (format(play_timer, '.0f') if play_timer > 0 else "0"):
        xalign 0.8 yalign 0.5
        size 200
        color "#fff"
