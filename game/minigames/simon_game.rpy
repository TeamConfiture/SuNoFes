# @Author Ayowel
init python:
    class SimonGame(renpy.display.layout.Container):
        """
        Create buttons and a simon with a set number of rounds

        # Arguments

        `buttons`
            An array of buttons to use for the game

        `ruleset`
            An array that contains the array indexes of the buttons to press (randomly generated if not provided)

        `completion_action`
            Renpy actions to perform if the player successfully completes all rounds

        `failure_action`
            Renpy actions to perform if the player fails at some point

        `downtime_duration`
            How long no button should be lit up during a demonstration

        `uptime_duration`
            How long a button should be lit up during a demonstration

        `first_simon_len`
            The number of buttons to press during the first round

        `simon_len_step`
            The number of additionnal buttons to press at each round

        # Examples

        * Create a simon with 3 buttons that has a 5-buttons pattern to complete

        ```rpy
        screen simon():
            default simon = SimonGame(
                buttons = [
                    {"auto": "images/sprites/buzzer_%s.png", "xpos": 100},
                    {"auto": "images/sprites/buzzer_%s.png", "xpos": 200},
                    {"auto": "images/sprites/buzzer_%s.png", "xpos": 300},
                ],
                ruleset = [0, 1, 2, 1, 0],
                completion_action = Jump("label_after_simon"),
                failure_action = Jump("label_you_noob")
            )
            add simon
        ```
        """
        # Flag used to know if post_init was called already or not
        is_fully_initialized = False
        # Self-update flag used when animating the buttons
        next_auto_update = None
        # Current index inputted by the player
        ruleset_index = 0
        # Current demo index
        show_ruleset_index = 0
        # Whether we're not showing a demo (None) or if we're showing one, whether a light is up (True) of not (False)
        show_is_uptime = None
        # Used as a flag to detect if buttons actions should process
        is_interactible = True
        # Time of the last render
        time_draw = 0

        def __init__(
                self, buttons, ruleset = None, completion_action = None, failure_action = None,
                downtime_duration = 1, uptime_duration = 1, first_simon_len = 3, simon_len_step = 1,
                **kwargs,
            ):
            super(SimonGame, self).__init__(**kwargs)
            # TODO: Add optional button to show sequence again

            self.base_buttons = buttons
            self.downtime_duration = downtime_duration
            self.uptime_duration = uptime_duration
            self.completion_action = completion_action
            self.failure_action = failure_action

            if ruleset:
                self.ruleset = ruleset
            else:
                generated_len = renpy.random.randint(0, 2*len(buttons))
                self.ruleset = []
                for i in range(generated_len):
                    self.ruleset.append(renpy.random.randint(0, len(buttons)-1))

            self.first_simon_len = min(first_simon_len, len(self.ruleset))
            self.simon_len_step = simon_len_step
            self.current_simon_len = self.first_simon_len

        def post_init(self):
            """
            Called on first usage as init does not support creating new displayables
            """
            for i in range(len(self.base_buttons)):
                button = ManageableImageButton(
                    **self.base_buttons[i],
                    action = Function(SimonGame.on_button_click, self, i)
                )
                # Adds buttons to self.children
                # The array is handled by Container's implementation and may change on rollback
                self.add(button)

        def reset(self):
            self.time_draw = 0
            self.ruleset_index = 0
            self.show_is_uptime = None

        def on_button_click(self, button_id):
            """
            Called when a button is clicked

            `button_id`
                Index of the button in self.children
            """
            if not self.is_interactible:
                return
            if self.ruleset[self.ruleset_index] == button_id:
                if self.current_simon_len > self.ruleset_index+1:
                    self.ruleset_index = self.ruleset_index+1
                else:
                    self.goto_next_ruleset()
            else:
                self.ruleset_index = 0
                renpy.run(self.failure_action)
                self.update_simon_demonstration()

        def update_simon_demonstration(self):
            """
            Update handler for the demonstration of the simon display
            """
            if self.show_is_uptime == None:
                # Start demo
                self.toggle_buttons(False)
                self.show_is_uptime = False
                self.show_ruleset_index = 0
                self.next_auto_update = self.time_draw + self.downtime_duration
                renpy.redraw(self, self.downtime_duration)
            elif self.show_is_uptime:
                # A button was lit, shut it down
                self.show_is_uptime = False
                self.toggle_image(self.ruleset[self.show_ruleset_index], is_hovered = False)
                self.show_ruleset_index = self.show_ruleset_index + 1
                self.next_auto_update = self.time_draw + self.uptime_duration

                renpy.redraw(self, self.uptime_duration)
            else:
                # No button was lit
                if self.current_simon_len <= self.show_ruleset_index:
                    # End of demo
                    self.next_auto_update = None
                    self.show_ruleset_index = 0
                    self.show_is_uptime = None
                    self.toggle_buttons(True)
                else:
                    # Light it up
                    self.toggle_image(self.ruleset[self.show_ruleset_index], is_hovered = True)
                    self.show_is_uptime = True
                    self.next_auto_update = self.time_draw + self.downtime_duration
                    renpy.redraw(self, self.downtime_duration)

        def goto_next_ruleset(self):
            """
            Update to move to next step of the simon or trigger the victory action
            """
            self.toggle_buttons(False)
            if self.current_simon_len < len(self.ruleset):
                if self.current_simon_len + self.simon_len_step > len(self.ruleset):
                    self.current_simon_len = len(self.ruleset)
                else:
                    self.current_simon_len += self.simon_len_step
                self.ruleset_index = 0
                self.update_simon_demonstration()
            else:
                if self.completion_action:
                    renpy.run(self.completion_action)
                self.current_simon_len = self.first_simon_len
                self.ruleset_index = 0

        def render(self, width, height, st, at):
            """
            Render loop used to trigger update cycles
            """
            if st == 0:
                self.update_simon_demonstration()
            self.time_draw = st
            if self.next_auto_update:
                if self.next_auto_update < st:
                    self.update_simon_demonstration()
                else:
                    renpy.redraw(self, st - self.next_auto_update)

            return super(SimonGame, self).render(width, height, st, at)

        def toggle_buttons(self, enable_buttons):
            """
            Makes buttons interactable or disables them

            `enable_buttons`
                Whether buttons should be interactable (True) or not (False)
            """
            if enable_buttons:
                self.is_interactible = True
                for b in self.children:
                    b.unfreeze_state()
            else:
                self.is_interactible = False
                for b in self.children:
                    b.freeze_state('idle')

            renpy.redraw(self, 0)

        def toggle_image(self, button_id, is_hovered):
            """
            Set button state to hovered or idle

            `button_id`
                Index of the button in self.children
            `is_hovered`
                Whether the button should be hovered (True) of idle (False)
            """
            # True: hovered, False: idle
            button = self.children[button_id]
            if is_hovered:
                button.freeze_state('hover')
            else:
                button.freeze_state('idle')

        def set_transform_event(self, event):
            """
            Set transform event override to run post_init
            """
            if not self.is_fully_initialized:
                # TODO: move to per_interact
                self.is_fully_initialized = True
                self.post_init()
            return super(SimonGame, self).set_transform_event(event)
