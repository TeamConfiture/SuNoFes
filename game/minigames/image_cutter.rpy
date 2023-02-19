init python:
    # This is bugged, good luck everyone
    import math

    renpy.register_shader("half_slice",
        variables = """
            attribute vec4 a_position;
            uniform vec2 u_line_point;
            uniform float u_line_angle;
            varying vec2 st;
        """, vertex_300 = """
            st = a_position.xy - u_line_point.xy;
        """, fragment_300 = """
            float rotated_xpos = st.x * sin(u_line_angle) + st.y * cos(u_line_angle);
            float v_alpha_factor = smoothstep(-1, 1, rotated_xpos);
            gl_FragColor *= v_alpha_factor;
        """
    )

transform image_cutter_half(point = (0, 0), angle = 0):
    shader "half_slice"
    u_line_point point
    u_line_angle angle

init python:
    def get_rope_from_line_and_square(start, end, corner1, corner2):
        """
        Returns the starting and ending point where a line crosses a square as a tuple
        of tuples (or None if there is no match).

        The first tuple is guaranteed to be the left-most point of the rope.

        # Parameters

        `start`
            A point of the line as a tuple

        `end`
            A different point of the line as a tuple

        `corner1`
            Tuple of a corner of the square

        `corner2`
            Tuple of the opposite corner of the square
        """
        topleft = (min(corner1[0], corner2[0]), max(corner1[1], corner2[1]))
        bottomright = (max(corner1[0], corner2[0]), min(corner1[1], corner2[1]))
        if start[0] == end[0]:
            # Horizontal line
            if topleft[0] < start[0] < bottomright[0]:
                return (start[0], bottomright[1]), (start[0], topleft[1])
        elif start[1] == end[1]:
            # Vertical line
            if topleft[1] < start[1] < bottomright[1]:
                return (topleft[0], start[1]), (bottomright[0], start[1])
        else:
            # no special case, we can use regular processing
            # Get factors in f(x) = ax + b (line's equation)
            a = (end[1] - start[1]) / (end[0] - start[0])
            b = start[1] - start[0] * a
            entrypoint = None
            f_left = a * topleft[0] + b
            if bottomright[1] <= f_left <= topleft[1]:
                entrypoint = (topleft[0], f_left)
            else:
                f_target = bottomright[1] if a > 0 else topleft[1]
                x_target = (f_target - b) / a
                if topleft[0] <= x_target <= bottomright[0]:
                    entrypoint = (x_target, f_target)
            if entrypoint:
                f_right = a * bottomright[0] + b
                if bottomright[1] <= f_right <= topleft[1]:
                    exitpoint = (bottomright[0], f_right)
                else:
                    # exitpoint is guaranteed to exist as there was an entrypoint
                    f_target = topleft[1] if a > 0 else bottomright[1]
                    x_target = (f_target - b) / a
                    exitpoint = (x_target, f_target)
                return entrypoint, exitpoint
        return None

    class ImageCutterPattern:
        """
        Helper class used to generate different patterns when spawning the images
        """
        patterns = ['start_bump', 'carnival', 'sides', 'varied']
        def __init__(self, kind = None, duration = 3., density = 1.):
            self.kind = kind or renpy.random.choice(patterns)
            self.duration = duration
            self.density = 1.
        def get_duration(self):
            return self.duration
        def get_schedule(self, image_reference):
            if self.kind == 'start_bump':
                i = [renpy.random.randrange(len(image_reference)) for _ in range(3)]
                return {
                    0.1 * self.duration: [ImageCutterImage(
                        image = image_reference[i[0]],
                        position = (config.screen_width / 2, config.screen_height),
                        speed = (0, -500),
                        rotation_speed = renpy.random.uniform(0, math.pi / 2),
                        rotation = renpy.random.uniform(0,2) * math.pi,
                    )],
                    0.75 * self.duration:[ImageCutterImage(
                        image = image_reference[i[0]],
                        position = (config.screen_width / 3, config.screen_height),
                        speed = (0, -500),
                        rotation_speed = renpy.random.uniform(0, math.pi / 2),
                        rotation = renpy.random.uniform(0,2) * math.pi,
                    ), ImageCutterImage(
                        image = image_reference[i[0]],
                        position = (config.screen_width * 2 / 3, config.screen_height),
                        speed = (0, -500),
                        rotation_speed = renpy.random.uniform(0, math.pi / 2),
                        rotation = renpy.random.uniform(0,2) * math.pi,
                    )],
                }
            elif self.kind == 'carnival':
                l = [(
                    renpy.random.randint(0, len(image_reference) - 1),
                    renpy.random.choice([-1, 1]),
                    ) for i in range(math.floor(self.density * 3))]
                return {
                    i * (self.duration) / (len(image_reference) + 3): [ImageCutterImage(
                        image = image_reference[j[0]],
                        position = (0 if j[1] < 0 else config.screen_width, config.screen_height),
                        speed = (500 * -j[1], renpy.random.uniform(-500, -700)),
                        rotation_speed = renpy.random.uniform(0, math.pi / 2),
                        rotation = renpy.random.uniform(0,2) * math.pi,
                    )] for i, j in enumerate(l)
                }
            elif self.kind == 'sides':
                l = [(
                    renpy.random.randint(0, len(image_reference) - 1),
                    renpy.random.choice([-1, 1]),
                    ) for i in range(math.floor(self.density * 3))]
                return {
                    i * (self.duration) / (len(image_reference) + 3): [ImageCutterImage(
                        image = image_reference[j[0]],
                        position = (0 if j[1] < 0 else config.screen_width, renpy.random.uniform(0, config.screen_height * 2 / 3)),
                        speed = (500 * -j[1], renpy.random.uniform(-100, -300)),
                        rotation_speed = renpy.random.uniform(0, math.pi / 2),
                        rotation = renpy.random.uniform(0,2) * math.pi,
                    )] for i, j in enumerate(l)
                }
            elif self.kind == 'varied':
                i = [renpy.random.randint(0, len(image_reference) - 1) for i in range(3)]
                return {
                    0.1 * self.duration: [ImageCutterImage(
                        image = image_reference[j],
                        position = (renpy.random.uniform(config.screen_width / 5, config.screen_width * 2 / 3 ), config.screen_height),
                        speed = (0, -500),
                        rotation_speed = renpy.random.uniform(0, math.pi / 2),
                        rotation = renpy.random.uniform(0, 2) * math.pi,
                    )] for j in i
                }
            elif self.kind == 'empty':
                return {}
            else:
                raise "Unsupported pattern type: " + str(self.kind)
    class ImageCutterImage:
        """
        Helper class used by ImageCutter to handle individual sprites
        """
        processed_image = None
        last_render = None
        def __init__(self,
                image, speed = (100, 50), rotation = 0, rotation_speed = 0.3, position = (-60, 500),
                acceleration = (0, 150), size = (0, 0), fresh = 0, timeout = 0,
                ):
            self.image = image
            self.speed = speed
            self.rotation_speed = rotation_speed # radians/s
            self.rotation = rotation
            self.pos = position
            self.acceleration = acceleration
            self.size = size
            self.fresh = fresh
            self.timeout = timeout
            self.fade_out_base_st = None
            self.fade_out_time = 1

        def split(self, line_start, line_end):
            cursor_angle = math.atan(
                (line_end[1] - line_start[1]) / (line_end[0] - line_start[0]) if line_end[0] != line_start[0] else 0
                )
            images = [
                image_cutter_half(line_start, cursor_angle),
                image_cutter_half(line_start, cursor_angle + math.pi),
            ]
            images[0].add(self.image)
            images[1].add(self.image)
            return [
                ImageCutterImage(images[0],
                    speed = [*self.speed],
                    rotation = self.rotation,
                    rotation_speed = self.rotation_speed + math.pi / 4,
                    position = [*self.pos],
                    acceleration = self.acceleration,
                    fresh = self.fresh + 1,
                    timeout = self.timeout,
                ), ImageCutterImage(images[1],
                    speed = [*self.speed],
                    rotation = self.rotation,
                    rotation_speed = self.rotation_speed - math.pi / 4,
                    position = [*self.pos],
                    acceleration = self.acceleration,
                    fresh = self.fresh + 1,
                    timeout = self.timeout,
                ),
            ]

        def move(self, st_diff):
            self.speed = (self.speed[0] + self.acceleration[0] * st_diff, self.speed[1] + self.acceleration[1] * st_diff)
            self.pos = (self.pos[0] + self.speed[0] * st_diff, self.pos[1] + self.speed[1] * st_diff)
            self.rotation += self.rotation_speed * st_diff
            self.processed_image = Transform(
                child = self.image,
                rotate = math.degrees(self.rotation),
            )

        def render(self, width, height, st, at):
            self.last_render = self.processed_image.render(width, height, st, at)
            self.size = self.last_render.get_size()
            return self.last_render

    class ImageCutter(renpy.Displayable):
        """
        Fruit-Ninja "clone" in Renpy.

        Don't use it, it's better this way.

        # Parameters

        `images`
            The base fruit images to use as an array of
            * Strings if there is no rotated version or additional information
            * Dicts with:
                * A 'list' subdict which's keys are counter-clockwise rotations in degrees (0 to 90) and values are images. The 0 key is mandatory
                * An optional 'actions' subdict with the following optional subkeys:
                    * on_cut: Action to run if this sprite is cut
                    * on_fall: Action tu run if this sprite "falls" below the screen

        `completion_action`
            What to do once no valid cut target is on the screen or scheduled

        `missed_action`
            What to do when a fruit falls without being cut

        `cutting_action`
            What to do when a fruit is cut

        `min_opaque_pixels`
            The number of pixels that should be cut in a fruit for the cut to be 'valid'

        `cut_frequency`
            How frequently cuts should be tested for. Too high and the cuts may fail, too low and the cuts will lack accuracy

        # Example

        ```rpy
        screen sprite_cutter():
        default game = ImageCutter(images = [
                    { 'list':
                        { i*15: "images/fish/happy_fish_scaled_" + str(i*15) + ".png" for i in range(6) },
                    }],
                    min_opaque_pixels = 80,
                    completion_action = Jump('next_chapter'),
                    missed_action = Jump('insults')
                    )
        add game
        ```
        """
        is_cutting = False
        st = 0
        cutables = []
        expired_cutables = []
        last_create = 0
        last_cut = 0
        current_pattern_index = -1
        current_pattern_schedule = None
        pattern_start = 0
        finalized = False

        def __init__(self, images, cutting_action = None, completion_action = None, missed_action = None, min_opaque_pixels = 40, cut_frequency = 0.1, patterns = None, time_factor = 1., **kwargs):
            super(ImageCutter, self).__init__(**kwargs)
            self.image_info = images
            self.cutting_actions = cutting_action
            self.completion_action = completion_action
            self.missed_cutable_actions = missed_action
            self.min_opaque_pixels = min_opaque_pixels
            self.time_factor = time_factor
            self.cut_frequency = cut_frequency
            self.cursor_pos = renpy.get_mouse_pos()
            if patterns:
                self.patterns = patterns
            else:
                self.patterns = [ImageCutterPattern(kind = 'start_bump')]
                for i in range(8):
                    random_pattern = renpy.random.choice(ImageCutterPattern.patterns)
                    self.patterns.append(ImageCutterPattern(kind = random_pattern))

        def render(self, width, height, st, at):
            st *= self.time_factor
            self.update_cycle(st)
            render = renpy.Render(width, height)
            for c in self.expired_cutables:
                if c.processed_image:
                    r = c.render(width, height, st, at)
                    render.blit(r, (c.pos))
            for c in self.cutables:
                if c.processed_image:
                    r = c.render(width, height, st, at)
                    render.blit(r, (c.pos))
            renpy.redraw(self, 0)
            return render

        def completion_scan(self):
            """
            Checks whether everything is cut and nothing is pending and triggers the completion action if it is
            """
            if (self.current_pattern_index == len(self.patterns) - 1
                    and (self.current_pattern_schedule is None or len(self.current_pattern_schedule.keys()) == 0)
                    and len(self.cutables) == 0
                    and not self.finalized
                    ):
                renpy.run(self.completion_action)
                self.finalized = True

        def update_cycle(self, st):
            if st == 0:
                # Implicitly restart on new display cycle
                self.finalized = False
                self.current_pattern_index = -1
                self.cutables = []
                self.expired_cutables = []
            st_diff = st - self.st
            self.st = st
            # Delete images that fell too low and trigger actions if they should have been cut
            deletion_list = []
            for c in self.cutables:
                c.move(st_diff)
                if c.pos[1] > config.screen_height + 100:
                    deletion_list.append(c)
            for d in deletion_list:
                renpy.run(self.missed_cutable_actions)
                self.cutables.remove(d)
            deletion_list = []
            for c in self.expired_cutables:
                c.move(st_diff)
                if c.pos[1] > config.screen_height + 100:
                    deletion_list.append(c)
            for d in deletion_list:
                self.expired_cutables.remove(d)
            # Update scheduled image spawns and render those elapsed
            if self.current_pattern_index == -1 or (
                    self.current_pattern_index < len(self.patterns) - 1 and self.pattern_start + self.patterns[self.current_pattern_index].get_duration() < st
                    ):
                self.current_pattern_index += 1
                self.current_pattern_schedule = self.patterns[self.current_pattern_index].get_schedule(self.image_info)
                self.pattern_start = st
            self.last_create = st
            deletion_list = []
            for k in self.current_pattern_schedule.keys():
                if st > self.pattern_start + k:
                    cutables = self.current_pattern_schedule[k]
                    deletion_list.append(k)
                    for c in cutables:
                        self.cutables.append(c)
            for d in deletion_list:
                self.current_pattern_schedule.pop(d)
            self.completion_scan()

        def is_colliding(self, asset, start, end):
            """
            Returns whether a sprite should be cut

            `asset`
                The sprite to test

            `start`
                The previous position of the mouse cursor

            `end`
                The next position of the mouse cursor
            """
            relevant_point = None
            range_len = 10
            for i in range(range_len):
                p = (end[0] + (start[0] - end[0]) * i / range_len, end[1] + (start[1] - end[1]) * i / range_len)
                if asset.last_render.is_pixel_opaque(p[0] - asset.pos[0], p[1] - asset.pos[1]):
                    relevant_point = p
                    break
            if not relevant_point:
                return False
            # Ensure that we cut through a significant-enough section that the split would be visible
            # we do this by ensuring there is enough opaque pixels along the section
            a = (end[1] - start[1]) / (end[0] - start[0]) if end[0] != start[0] else 999999
            accumulator = 0
            # Prepare exploration
            # The lambda is probably very expensive to run here, but w/e
            if a == 999999:
                x_or_y = relevant_point[1]
                get_pos = lambda y: (relevant_point[0], y)
            elif a == 0:
                x_or_y = relevant_point[0]
                get_pos = lambda x: (x, relevant_point[1])
            elif abs(a) > 1:
                x_or_y = relevant_point[1]
                get_pos = lambda y: ((y - relevant_point[1]) / a + relevant_point[0], y)
            else:
                x_or_y = relevant_point[0]
                get_pos = lambda x: (x, (x - relevant_point[0]) * a + relevant_point[1])
            # Count opaque pixels
            # TODO: Only check pixels "behind" the cursor movement to make it look like the cut occurs only
            # after the mouse cursor has sufficiently penetrated the sprite
            # TODO: use approximated sampling instead of raw validation, it will make the code easier to maintain and faster at a small precision cost
            tmp_x_or_y = x_or_y
            while accumulator < self.min_opaque_pixels:
                tmp_x_or_y += 1
                new_pos = get_pos(tmp_x_or_y)
                if asset.last_render.is_pixel_opaque(new_pos[0]-asset.pos[0], new_pos[1]-asset.pos[1]):
                    accumulator += 1
                else:
                    break
            tmp_x_or_y = x_or_y
            while accumulator < self.min_opaque_pixels:
                tmp_x_or_y -= 1
                new_pos = get_pos(tmp_x_or_y)
                if asset.last_render.is_pixel_opaque(new_pos[0]-asset.pos[0], new_pos[1]-asset.pos[1]):
                    accumulator += 1
                else:
                    break
            return accumulator >= self.min_opaque_pixels

        def process_collisions(self, start, end):
            """
            Cuts images that should be cut

            Note that with the current behavior, the mouse cursor must be ON the image at the moment the mousemove event is received
            """
            if (start[0] == end[0] and start[1] == end[1]):
                return
            deletion_list = []
            addition_list = []
            for c in self.cutables:
                # If cursor in image area
                if (c.timeout < self.st and c.last_render):
                    rope = get_rope_from_line_and_square(start, end, c.pos, (c.pos[0] + c.size[0], c.pos[1] + c.size[1]))
                    if rope and self.is_colliding(c, start, end):
                        # Split if enough opaque pixel on the line
                        c.timeout = self.st + 0.5
                        addition_list += c.split((start[0] - c.pos[0], start[1] - c.pos[1]), (end[0] - c.pos[0], end[1] - c.pos[1]))
                        renpy.run(self.cutting_actions)
                        deletion_list.append(c) # We're going to split this, it's ok it'll survive... somewhat
            for c in deletion_list:
                # TODO: remove by index with pop instead of by value
                self.cutables.remove(c)
            for c in addition_list:
                self.expired_cutables.append(c)

        def event(self, ev, x, y, at):
            if ev.type == 1025: # mousedown
                self.is_cutting = True
            elif ev.type == 1026: # mouseup
                self.is_cutting = False
            elif ev.type == 1024: # mousemove
                pass
            if self.st > self.last_cut + self.cut_frequency:
                self.last_cut = self.st
                if self.is_cutting:
                    self.process_collisions(self.cursor_pos, (x, y))
                self.cursor_pos = (x, y)  
            return super(ImageCutter, self).event(ev, x, y , at)
