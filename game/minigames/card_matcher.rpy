# @Author Ayowel
init python:
    import math

    class CardMatcherAnchor:
        """
        Helper class for CardMatcher. Its __init__ function's parameters
        are valid attributes for CardMatcher::__init__'s anchor_definitions parameter
        """
        def __init__(self, name, xpos, ypos, group = None, target_groups = [],
                idle_button = None, hover_button = None, disabled_button = None, linked_button = None,
                is_receiver = None, is_emitter = None,
                defaults = {},
                ):
            self.name = name
            self.pos = (xpos, ypos)
            self.size = (0, 0)
            # 0 is idle, hover is 1, disabled is 2
            self.state = 0
            # button images. They MUST all have the same size for the button to work as intended
            self.idle_button = renpy.displayable(idle_button or defaults["idle_button"])
            self.hover_button = renpy.displayable(hover_button or defaults["hover_button"] or self.idle_button)
            self.disabled_button = renpy.displayable(disabled_button or defaults["disabled_button"] or self.idle_button)
            self.linked_button = renpy.displayable(linked_button or defaults["linked_button"] or self.disabled_button)
            if is_receiver is None:
                self.is_receiver = defaults["is_receiver"]
            else:
                self.is_receiver = is_receiver
            if is_emitter is None:
                self.is_emitter = defaults["is_emitter"]
            else:
                self.is_emitter = is_emitter

        def center(self):
            """
            Returns the address of the center of the sprite
            """
            return (self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2)

        def render(self, width, height, st, at):
            if self.state == 0:
                return self.idle_button.render(width, height, st, at)
            elif self.state == 1:
                return self.hover_button.render(width, height, st, at)
            elif self.state == 2:
                return self.disabled_button.render(width, height, st, at)
            elif self.state == 3:
                return self.linked_button.render(width, height, st, at)

    class CardMatcherRope(renpy.Displayable):
        """
        Helper class for CardMatcher

        `start_pos`
            Provided by CardMatcher and contains the Rope's starting point
        `end_pos`
            Provided by CardMatcher and contains the Rope's ending point
        `rope`
            An image-like displayable used to render the rope
        `start_token`
            An image-like displayable used as an overlay at the rope's starting point
        `end_token`
            An image-like displayable used as an overlay at the rope's ending point
        """
        def __init__(self,
                start_pos = (0, 0), end_pos = (0, 0), rope = None,
                start_token = None, end_token = None, **kwargs):
            # TODO: Make it possible to have tokens rotate with the rope
            # This should probably be done by creating an intermediate render BEFORE rotation
            # but requires additionnal configuration and maths before being actually usable
            super(CardMatcherRope, self).__init__(**kwargs)

            self.start_pos = start_pos
            self.end_pos = end_pos
            self.rope_displayable = rope and renpy.displayable(rope)
            if self.rope_displayable:
                self.rope_displayable_size = self.rope_displayable.render(0, 0, 0, 0).get_size()
            else:
                self.rope_displayable_size = (0, 0)
            self.start_displayable = start_token and renpy.displayable(start_token)
            if self.start_displayable:
                self.start_displayable_size = self.start_displayable.render(0, 0, 0, 0).get_size()
            else:
                self.start_displayable_size = (0, 0)
            self.end_displayable = end_token and renpy.displayable(end_token)
            if self.end_displayable:
                self.end_displayable_size = self.end_displayable.render(0, 0, 0, 0).get_size()
            else:
                self.end_displayable_size = (0, 0)

            self.is_render_up_to_date = False
            self.rendered_rope = None
            self.rendered_rope_pos = (0, 0)

        def update_render(self):
            rope_vector = (self.end_pos[0] - self.start_pos[0], self.end_pos[1] - self.start_pos[1])
            rope_length = math.sqrt(rope_vector[0] ** 2 + rope_vector[1] ** 2) or 0.00001 # Avoid 0 at all cost

            rotation_cos = rope_vector[1] / rope_length
            rotation_sin = rope_vector[0] / rope_length
            if rope_vector[0] != 0:
                rotation = math.atan(rope_vector[1] / rope_vector[0])
            else:
                if rope_vector[1] > 0:
                    rotation = -math.pi / 2
                else:
                    rotation = math.pi / 2

            # The rotated image's side have the same length as the hypothenuse of the base image
            if self.rope_displayable:
                required_tiles = math.floor(rope_length / self.rope_displayable_size[0])+1
                effective_length = required_tiles * self.rope_displayable_size[0]
                rotated_rope_image_side = math.sqrt(rope_length ** 2 + self.rope_displayable_size[1] ** 2)
                crop_factor = rope_length/effective_length
                self.rendered_rope_pos = (
                    self.start_pos[0] - rotated_rope_image_side/2 + rotation_sin * rope_length / 2,
                    self.start_pos[1] - rotated_rope_image_side/2 + rotation_cos * rope_length / 2,
                    )
                self.rendered_rope = Transform(
                    child = self.rope_displayable,
                    crop = (0, 0, crop_factor, 1.),
                    xtile = required_tiles,
                    rotate = math.degrees(rotation),
                )
            else:
                self.rendered_rope = None

        def set_rope_end(self, pos):
            if self.end_pos[0] != pos[0] or self.end_pos[1] != pos[1]:
                self.end_pos = pos
                self.is_render_up_to_date = False
                renpy.redraw(self, 0)

        def set_rope_start(self, pos):
            if self.start_pos[0] != pos[0] or self.start_pos[1] != pos[1]:
                self.start_pos = pos
                self.is_render_up_to_date = False
                renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            if not self.is_render_up_to_date:
                self.update_render()
                self.is_render_up_to_date = True
            render = renpy.Render(width,height)
            # TODO: handle rotations on start/end positions
            if self.rendered_rope:
                render.blit(self.rendered_rope.render(width, height, st, at), self.rendered_rope_pos)
            if self.start_displayable:
                render.blit(
                    self.start_displayable.render(width, height, st, at),
                    (self.start_pos[0]-self.start_displayable_size[0]/2, self.start_pos[1]-self.start_displayable_size[1]/2),
                    )
            if self.end_displayable:
                render.blit(
                    self.end_displayable.render(width, height, st, at),
                    (self.end_pos[0]-self.end_displayable_size[0]/2, self.end_pos[1]-self.end_displayable_size[1]/2),
                    )
            return render

    class CardMatcher(renpy.Displayable):
        """
        This is an object that allows to create an association game by defining anchor images, ropes to link them, and the permitted associations

        # Arguments

        `anchor_definitions`
            Dict of anchor definitions. Valid attributes are those supported by CardMatcherAnchor's init function
        `anchor_rules`
            Array of anchor_definitions key pair listing the valid associations
        `auto_base_button`
            Defaut file name pattern to use for a button if more specific options are not set. "%s" will be replaced by "idle", "hover", "disabled", or "linked" depending on requirement
        `idle_base_button`
            Default displayable to use for buttons that are not interacted with
        `hover_base_button`
            Default displayable to use for buttons that are hovered
        `disabled_base_button`
            Default displayable to use for buttons that are not active
        `linked_base_button`
            Displayable to use for buttons that are linked to another
        `rope_collection`
            Array of ropes. They may either be standalone images or valid arguments for CardMatcherRope's init function (with the exception of start_pos and end_pos)
        `rule_groups`
            alternative group-specific defaults (groups are part of an anchor's definition)
        `rope_transforms`
            Maps a rope_collection index's item to its linked version
        `rope_pull_list`
            Lists the rope indexes to use when pulling a rope (if None, all ropes may be used)
        `binding_callback`
            unused at this point
        `completion_actions`
            Renpy actions to run upon puzzle completion

        # Examples

        Minimal example

        ```rpy
        screen match_screen():
            default matcher = CardMatcher(
                anchor_definitions = {
                    1: {"xpos": 300, "ypos": 0},
                    2: {"xpos": 1500, "ypos": 900},
                },
                anchor_rules = [(1,2)],
                auto_base_button = "images/sprites/buzzer_%s.png",
                rope_collection = ["images/sprites/line_pull.png"],
                completion_actions = [Jump("chap1")]
            )
            add matcher
        ```

        More fluff

        ```rpy
        screen match_screen():
            default matcher = CardMatcher(
                anchor_definitions = {
                    1: {"group": 1, "xpos": 300, "ypos": 0},
                    4: {"group": 1, "xpos": 800, "ypos": 400},
                    5: {"group": 1, "xpos": 500, "ypos": 400},
                    6: {"group": 1, "xpos": 600, "ypos": 0},
                    2: {"group": 2, "xpos": 1500, "ypos": 900},
                    3: {"group": 2, "xpos": 400, "ypos": 200},
                    7: {"group": 2, "xpos": 300, "ypos": 200},
                    8: {"group": 2, "xpos": 500, "ypos": 200},
                },
                anchor_rules = [(1,2), (4,3), (5, 7), (6, 8)],
                auto_base_button = "images/sprites/buzzer_%s.png",
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
                completion_actions = [Jump("chap1")]
            )
            add matcher
        ```
        """
        def __init__(self, anchor_definitions = {}, anchor_rules = [],
                auto_base_button = None, idle_base_button = None, hover_base_button = None, disabled_base_button = None, linked_base_button = None,
                rope_collection = [], rule_groups = {}, rope_transforms = {}, rope_pull_list = None,
                binding_callback = None, completion_actions = None,
                **kwargs,
                ):
            super(CardMatcher, self).__init__(**kwargs)
            self.anchor_definitions = anchor_definitions
            self.anchor_rules = anchor_rules
            self.base_group_rules = rule_groups
            self.rope_transforms = rope_transforms
            self.rope_pull_list = rope_pull_list
            self.binding_callback = binding_callback
            self.completion_actions = completion_actions
            # Set defaults
            self.base_defaults = {
                "idle_button": idle_base_button or auto_base_button.replace("%s", "idle"),
                "hover_button": hover_base_button or auto_base_button.replace("%s", "hover"),
                "disabled_button": disabled_base_button or auto_base_button.replace("%s", "disabled"),
                "linked_button": linked_base_button or auto_base_button.replace("%s", "linked"),
                "is_receiver": True,
                "is_emitter": True,
            }
            self.anchor_links = []
            self.hovered_anchor = None # only one anchor may be hovered at a time
            self.dragged_anchor = None # only one anchor may be dragged at a time
            self.first_render = True
            self.static_ropes = []
            self.mouse_rope = None
            self.mouse_rope_index = 0
            self.cursor_pos = (0, 0)
            # Initialize ropes and normalize format
            self.rope_collection = []
            for rope in rope_collection:
                if isinstance(rope, renpy.Displayable) or isinstance(rope, str):
                    self.rope_collection.append({ "rope": rope })
                else:
                    self.rope_collection.append(rope)
            # Graph of valid associations to look them up in O(1)
            self.bindings_graph = {}
            for r in anchor_rules:
                self.bindings_graph[r[0]] = self.bindings_graph.get(r[0], set()).union(set([r[1]]))
                self.bindings_graph[r[1]] = self.bindings_graph.get(r[1], set()).union(set([r[0]]))
            # Pre-load anchors & ensure 
            self.anchors = {}
            for k in anchor_definitions:
                # Ensure that each anchor has at least a key defined to make future lookups easier
                if not k in self.bindings_graph.keys():
                    self.bindings_graph[k] = {}
                self.anchors[k] = CardMatcherAnchor(name = k, defaults = self.get_group_defaults(anchor_definitions[k].get("group")), **anchor_definitions[k])

        # Returns a dict of default values to use for an anchor of a specific group
        # If group_label is None, no group-specific default is injected
        def get_group_defaults(self, group_label):
            defaults = self.base_defaults
            if self.base_group_rules.get(group_label):
                defaults = self.base_defaults.copy()
                group_defaults = self.base_group_rules[group_label]
                for k in group_defaults:
                    defaults[k] = group_defaults[k]
            return defaults

        def render(self, width, height, st, at):
            render = renpy.Render(width,height)
            # Render anchors
            for k in self.anchors:
                anchor = self.anchors[k]
                anchor_render = anchor.render(width, height, st, at)
                if self.first_render:
                    anchor.size = anchor_render.get_size()
                render.blit(anchor_render, anchor.pos)
            # Render ropes
            self.update_cursor_rope()
            for rope in self.static_ropes:
                render.blit(rope.render(width, height, st, at), (0, 0))
            if self.mouse_rope:
                render.blit(self.mouse_rope.render(width, height, st, at), (0, 0))

            self.first_render = False
            return render

        def is_cursor_on_anchor(self, anchor):
            """
            Returns whether a specific anchor is under the cursor
            """
            return (anchor.pos[0] <= self.cursor_pos[0] <= anchor.pos[0] + anchor.size[0] and
                    anchor.pos[1] <= self.cursor_pos[1] <= anchor.pos[1] + anchor.size[1])

        def is_anchor_hoverable(self, anchor):
            """
            Returns whether a specific anchor should be interractible
            """
            return (
                (
                    (self.dragged_anchor is None and anchor.is_emitter) or
                    (self.dragged_anchor is not None and self.dragged_anchor != anchor.name and anchor.is_receiver)
                ) and anchor.state != 3
            )

        def add_static_rope(self, start, end, index = 0):
            """
            Add a rope to render and keep around
            """
            self.static_ropes.append(CardMatcherRope(
                **self.rope_collection[index],
                start_pos = start,
                end_pos = end,
                ))

        def update_cursor_rope(self):
            """
            Update the informations of the rope dragged by the user
            """
            if self.dragged_anchor is not None:
                if not self.mouse_rope:
                    if self.rope_pull_list:
                        self.mouse_rope_index = self.rope_pull_list[renpy.random.randint(0, len(self.rope_pull_list) - 1)]
                    else:
                        self.mouse_rope_index = renpy.random.randint(0, len(self.rope_collection) - 1)
                    self.mouse_rope = CardMatcherRope(**self.rope_collection[self.mouse_rope_index])
                self.mouse_rope.set_rope_start(self.anchors[self.dragged_anchor].center())
                self.mouse_rope.set_rope_end(self.cursor_pos)
                renpy.redraw(self, 0)
            else:
                self.mouse_rope = None

        def on_mousedown(self):
            # Start dragging from the hovered anchor
            if self.hovered_anchor:
                if self.dragged_anchor: # For some reason we receive mousedown without receiving mouseup
                    self.anchors[self.dragged_anchor].state = 0
                self.dragged_anchor = self.hovered_anchor
                self.hovered_anchor = None
                self.anchors[self.dragged_anchor].state = 2
                renpy.redraw(self, 0)

        def on_mouseup(self):
            if self.hovered_anchor and self.dragged_anchor:
                if self.hovered_anchor in self.bindings_graph.get(self.dragged_anchor, []):
                    # Record link creation and set status
                    self.anchor_links.append((self.hovered_anchor, self.dragged_anchor))
                    self.anchors[self.hovered_anchor].state = 3
                    self.anchors[self.dragged_anchor].state = 3
                    # Add a static rope
                    self.mouse_rope_index = self.rope_transforms.get(self.mouse_rope_index, self.mouse_rope_index)
                    self.add_static_rope(
                        self.anchors[self.dragged_anchor].center(), self.anchors[self.hovered_anchor].center(),
                        self.mouse_rope_index,
                        )
                    self.dragged_anchor = None
                    renpy.redraw(self, 0)
                    # Check if all links were created, if so terminate processing
                    if len(self.anchor_links) == len(self.anchor_rules):
                        if isinstance(self.completion_actions, list):
                            for action in self.completion_actions:
                                renpy.run(action)
                        else:
                            renpy.run(action)
                    return
            if self.dragged_anchor:
                # remove dragging status if we could not create a link
                self.anchors[self.dragged_anchor].state = 0
                self.dragged_anchor = None
                renpy.redraw(self, 0)

        def on_mousemove(self):
            self.update_cursor_rope()
            renpy.redraw(self, 0)
            if self.first_render: # Don't risk detecting anchors while the scene is not even rendered
                return
            # Ensure that the already-detected anchor keeps priority
            if self.hovered_anchor:
                anchor = self.anchors[self.hovered_anchor]
                if self.is_cursor_on_anchor(anchor):
                    return
            # Collision detection on all anchors & set hover state if possible
            # TODO: handle transparency
            for k in self.anchors:
                anchor = self.anchors[k]
                if self.is_cursor_on_anchor(anchor):
                    if self.is_anchor_hoverable(anchor):
                        if self.hovered_anchor and self.anchors[self.hovered_anchor].state == 1:
                            self.anchors[self.hovered_anchor].state = 0
                        self.hovered_anchor = k
                        anchor.state = 1
                        break
                else:
                    if self.hovered_anchor == k:
                        if anchor.state == 1:
                            anchor.state = 0
                        self.hovered_anchor = None

        def event(self, ev, x, y, st):
            # Do not handle events while no render occured
            if self.first_render:
                return
            # event switch
            if ev.type == 1025:
                self.on_mousedown()
            elif ev.type == 1026:
                self.on_mouseup()
            elif ev.type == 1024:
                self.cursor_pos = (x, y)
                self.on_mousemove()

        def visit(self):
            return []
