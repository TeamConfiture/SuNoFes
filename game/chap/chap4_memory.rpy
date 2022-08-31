screen chap4_memory_game(next_chapter_label, timeout_label):
    default play_timer = 30
    python:
        card_bg = { "auto": "images/cards/back_%s.jpg", }

    default memory = Memory(
        cards = [
            { "selected_image": "images/cards/rick_resized.jpg", **card_bg },
            { "selected_image": "images/cards/griffin_card.png", **card_bg },
            { "selected_image": "images/cards/kimi_card.png", **card_bg, },
        ],
        completion_actions = Jump(next_chapter_label),
        xalign = 0.5, yalign = 0.5,
        spacing = 20,
        )
    timer 0.1:
        repeat True
        action If(play_timer > 0, true=SetScreenVariable('play_timer', play_timer - 0.1), false=Jump(timeout_label))
    add memory
    text (format(play_timer, '.0f') if play_timer > 0 else "0"):
        xalign 0.9 yalign 0.5
        size 200
        color "#34f"
