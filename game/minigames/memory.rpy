# @Author Ayowel
init python:
    import math
    class Memory(renpy.display.layout.Grid):
        """
        Implements a memory game in renpy

        # Parameters

        `cards`
            An array of base cards to use. Cards are a dict with initialization arguments
            for an ImageButton instance with the following exceptions:
            
            * You may provide the 'auto' parameter
            * You may provide a default 'selected_image' parameter for all selected_ states

        `cols`
            The number of columns to use for the game

        `reveal_count`
            How many times a card should be duplicated and how many cards a player should have to reveal at once

        `failure_reveal_time`
            How long to wait before hiding cards again if they do not match (in seconds)
        
        `failure_overtime`
            How long to wait after revealing a card before allowing a player to select new cards

        `turn_time`
            How long it should take to turn a card when it is revealed/hidden

        `failure_actions`
            Actions to run when the player fails to match cards

        `play_actions`
            Actions to run when the player turns several cards

        `completion_actions`
            Actions to run when the player successfully reveals all cards

        Also supports any other parameter a `grid` supports

        # Examples

        Simple game with restart button

        ```rpy
        screen memory():
            python:
                card_bg = { "auto": "images/sprites/back_%s.png" }
            default memory = Memory(
                cards = [
                    { "selected_image": "images/cards/rick_resized.jpg", **card_bg },
                    { "selected_image": "images/cards/griffin_card.png", **card_bg },
                    { "selected_image": "images/cards/kimi_card.png", **card_bg, },
                ], completion_actions = Jump("next_chapter"),
                )
            add memory
        ```

        Game with turn limit and automatic restart upon reaching it

        ```rpy
        init:
            $ play_count = 5
        screen hidden_balls():
            python:
                card_bg = { "auto": "images/cards/back_%s.jpg", }
                def on_play():
                    renpy.run(SetVariable('play_count', store.play_count - 1))
                    if store.play_count <= 0:
                        renpy.run(SetVariable('play_count', 5))
                        renpy.current_screen().scope['memory'].restart()

            default memory = Memory(
                cards = [
                    { "selected_image": "images/cards/rick_resized.jpg", **card_bg },
                    { "selected_image": "images/cards/griffin_card.png", **card_bg },
                    { "selected_image": "images/cards/kimi_card.png", **card_bg, },
                ],
                completion_actions = Jump("chap1"),
                play_actions = Function(on_play),
                )
            add memory
            text str(play_count)
        ```
        """

        active = True
        revealed_cards = []
        scheduled_cleanup = None
        scheduled_overtime = None

        def __init__(self, cards = [], cols = 3, rows = None,
                reveal_count = 2, failure_reveal_time = 1., failure_overtime = 0.3, turn_time = 0.5,
                failure_actions = None, play_actions = None, completion_actions = None, **kwargs):
            rows = rows or math.ceil(len(cards)*reveal_count/cols)
            super(Memory, self).__init__(cols = cols, rows = rows, allow_underfull = True, **kwargs)
            self.cards_info = cards
            self.reveal_count = reveal_count
            self.reveal_time = failure_reveal_time
            self.turn_time = turn_time
            self.failure_overtime = failure_overtime
            self.failure_reveal_time = failure_reveal_time
            self.failure_actions = failure_actions
            self.play_actions = play_actions
            self.completion_actions = completion_actions
            # Indicates, for each displayed card, the base index of the card
            self.cards_map = [i for i in range(len(cards))]*self.reveal_count
            self.renew_deck()

        def renew_deck(self):
            """
            Initialize the deck, in the future this will also shuffle it if required
            """
            renpy.random.shuffle(self.cards_map)
            for i in range(len(self.cards_map)):
                self.add(self.new_card(i))
        
        def new_card(self, pos):
            """
            Internal function used to generate a new card instance

            `pos`
                Index in the internal card map of the card to generate
            """
            index = self.cards_map[pos]
            card_info = self.cards_info[index].copy()
            selected = card_info.pop('selected_image')
            for key in ['selected_idle_image', 'selected_hover_image', 'selected_activate_image', 'selected_insensitive_image']:
                card_info[key] = card_info.get(key, selected)
            return ManageableImageButton(
                **card_info,
                action = Function(Memory.on_card_click, self, pos),
                animator = SelectedCardAnimator(self.turn_time),
                )

        def on_card_click(self, i):
            """
            Callback function used when clicking a card

            `i`
                Index of the card in the internal card map
            """
            if self.active and len(self.revealed_cards) < self.reveal_count and not self.children[i].selected:
                self.children[i].selected = not self.children[i].selected
                self.revealed_cards.append(i)
                if len(self.revealed_cards) >= self.reveal_count:
                    if len(set([self.cards_map[i] for i in self.revealed_cards])) == 1:
                        self.revealed_cards = []
                        if len(set([c.selected for c in self.children])) == 1:
                            # If all cards are selected, we win
                            renpy.run(self.completion_actions)
                    else:
                        renpy.run(self.failure_actions)
                        self.scheduled_cleanup = self.st + self.reveal_time
                        renpy.redraw(self, 0)
                    renpy.run(self.play_actions)
                        
        def verify_pending_processings(self):
            """
            Ensure that we're not waiting for a future event.

            If we are, and it is time, process it.
            Else reschedule a redraw to guarantee we will be notified when we want to run it
            """
            if self.scheduled_cleanup:
                # Timeout for card turning if player made a mistake
                if self.scheduled_cleanup <= self.st:
                    for i in self.revealed_cards:
                        self.children[i].selected = False
                        self.children[i].per_interact()
                    self.revealed_cards = []
                    self.scheduled_cleanup = None
                    if self.failure_overtime:
                        self.active = False
                        self.scheduled_overtime = self.st + self.failure_overtime
                        renpy.redraw(self, self.failure_overtime)
                else:
                    renpy.redraw(self, self.scheduled_cleanup - self.st)
            if self.scheduled_overtime:
                # Timeout for allowing user to select a card again after hiding cards after a mistake
                if self.scheduled_overtime <= self.st:
                    self.active = True
                    self.scheduled_overtime = None
                else:
                    renpy.redraw(self, self.scheduled_overtime - self.st)

        def restart(self):
            """
            Reset the game's state. At this point this does NOT reshuffle the deck
            """
            self.active = True
            self.revealed_cards = []
            for c in self.children:
                if c.selected:
                    renpy.redraw(c, 0)
                c.selected = False

        def render(self, width, height, st, at):
            if st == 0:
                self.restart()
            self.st = st
            self.verify_pending_processings()
            return super(Memory, self).render(width, height, st, at)
