init python:
    import math

    # This shader draws a line and makes everything at its left invisible
    renpy.register_shader("image_cutter_half_slice",
        variables = """
            uniform vec2 u_model_size;
            attribute vec4 a_position;
            uniform vec2 u_line_point;
            uniform float u_line_angle;
            varying vec2 st;
        """, vertex_300 = """
            // translate to use u_line_point as center
            st = a_position.xy - u_line_point.xy * u_model_size;
        """, fragment_300 = """
            float rotated_xpos = st.x * cos(u_line_angle) - st.y * sin(u_line_angle);
            float v_alpha_factor = smoothstep(-1, 1, rotated_xpos);
            gl_FragColor *= v_alpha_factor;
        """
    )

transform image_cutter_half(point = (0, 0), angle = 0):
    shader "image_cutter_half_slice"
    u_line_point point
    u_line_angle angle

init python:
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
            self.processed_image = None

        def split(self, line_start, line_end):
            base_size = self.image.render(0, 0, 0, 0).get_size()
            displayed_size = self.size
            # Translate coordinates to displayed image center
            line_start = (line_start[0] - displayed_size[0]/2, line_start[1] - displayed_size[1]/2)
            line_end = (line_end[0] - displayed_size[0]/2, line_end[1] - displayed_size[1]/2)
            # Rotate coordinates around displayed image
            rot_sin = math.sin(-self.rotation)
            rot_cos = math.cos(-self.rotation)
            line_start = (
                line_start[0]*rot_cos - line_start[1]*rot_sin,
                line_start[0]*rot_sin + line_start[1]*rot_cos,
                )
            line_end = (
                line_end[0]*rot_cos - line_end[1]*rot_sin,
                line_end[0]*rot_sin + line_end[1]*rot_cos,
                )
            # Translate coordinates to base image top-left
            line_start = (line_start[0] + base_size[0]/2, line_start[1] + base_size[1]/2)
            line_end = (line_end[0] + base_size[0]/2, line_end[1] + base_size[1]/2)

            # Calculate cut angle
            line_vec = (line_end[0] - line_start[0], line_end[1] - line_start[1])
            cursor_angle = math.atan(
                line_vec[0] / line_vec[1] if line_vec[1] != 0 else math.inf
                )
            # Express coordinates as a fraction of the image's size
            # This is required because Ren'Py provides a weird model_size in
            #   shaders that makes it impossible to rely on a pixel offset
            reference_point = (line_start[0] / base_size[0], line_start[1] / base_size[1])
            images = [
                image_cutter_half(reference_point, cursor_angle),
                image_cutter_half(reference_point, cursor_angle + math.pi),
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
            render = self.processed_image.render(width, height, st, at)
            self.size = render.get_size()
            return render

    class ImageCutter(renpy.Displayable):
        """
        Fruit-Ninja "clone" in Renpy.

        Don't use it, it's better this way.

        # Parameters

        `images`
            The base fruit images to use as an array of
            * Strings or Displayable if there is no rotated version or additional information

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
        last_create = 0
        last_cut = 0
        current_pattern_index = -1
        current_pattern_schedule = None
        pattern_start = 0
        finalized = False

        def __init__(self, images, cutting_action = None, completion_action = None, missed_action = None, min_opaque_pixels = 40, cut_frequency = 0.1, patterns = None, time_factor = 1., **kwargs):
            super(ImageCutter, self).__init__(**kwargs)
            self.is_cutting = False
            self.cutables = []
            self.expired_cutables = []
            self.st = 0

            self.image_info = [renpy.easy.displayable(i) if isinstance(i, str) else i for i in images]
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
            first_relevant_point = None
            range_len = 30
            asset_render = asset.processed_image.render(0, 0, 0, 0)
            cursor_vec = (end[0] - start[0], end[1] - start[1]) # vector end -> start

            for i in range(range_len):
                p = (end[0] - cursor_vec[0] * i / range_len, end[1] - cursor_vec[1] * i / range_len)
                if asset_render.is_pixel_opaque(p[0] - asset.pos[0], p[1] - asset.pos[1]):
                    relevant_point = p
                    if first_relevant_point is None:
                        first_relevant_point = relevant_point
            if relevant_point and relevant_point != first_relevant_point:
                relevant_segment = (
                    relevant_point[0] - first_relevant_point[0],
                    relevant_point[1] - first_relevant_point[1],
                    )
                squared_relevant_segment_len = math.pow(relevant_segment[0], 2) + math.pow(relevant_segment[1], 2)
                squared_opaque_dist = self.min_opaque_pixels * self.min_opaque_pixels
                if squared_relevant_segment_len >= squared_opaque_dist:
                    return True
            return False

        def process_collisions(self, start, end):
            """
            Cuts images that should be cut

            Note that with the current behavior, the mouse cursor must be ON the image at the moment the mousemove event is received
            """
            if (start[0] == end[0] and start[1] == end[1]):
                return
            deletion_list = []
            for i in range(len(self.cutables)):
                c = self.cutables[i]
                # If cursor in image area
                if (c.timeout < self.st and c.size[0]):
                    if self.is_colliding(c, start, end):
                        # Split if enough opaque pixel on the line
                        c.timeout = self.st + 0.5
                        self.expired_cutables += c.split(
                            (start[0] - c.pos[0], start[1] - c.pos[1]),
                            (end[0] - c.pos[0], end[1] - c.pos[1])
                            )
                        renpy.run(self.cutting_actions)
                        deletion_list.append(i)
            for c in reversed(deletion_list):
                self.cutables.pop(c)

        def event(self, ev, x, y, at):
            if ev.type == 1025: # mousedown
                self.is_cutting = True
                self.cursor_pos = (x, y)
                self.last_cut = self.st
            if self.st > self.last_cut + self.cut_frequency or ev.type == 1026:
                self.last_cut = self.st
                if self.is_cutting:
                    self.process_collisions(self.cursor_pos, (x, y))
                self.cursor_pos = (x, y)
            if ev.type == 1026: # mouseup
                self.is_cutting = False
            return super(ImageCutter, self).event(ev, x, y , at)
