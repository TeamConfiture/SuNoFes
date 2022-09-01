init python:
    import math

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

    class ImageCutterImage:
        """
        Helper class used by ImageCutter to handle individual sprites
        """
        processed_image = None
        last_render = None
        def __init__(self,
                image, base_images = None, speed = (100, 50), rotation = 0, rotation_speed = 0.3, position = (-60, 500),
                acceleration = (0, 60), size = (0, 0), fresh = 0, timeout = 0,
                ):
            self.image = image
            self.base_images = base_images
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
            size = renpy.easy.displayable(self.image).render(0, 0, 0, 0).get_size()
            displayed_size = self.last_render.get_size()
            rot_circle = (math.cos(self.rotation), math.sin(self.rotation))
            # Displace line in a referential that uses the image's center as (0,0) coordinate
            line_start_corrected = (line_start[0] - self.size[0] / 2, line_start[1] - self.size[1] / 2)
            line_end_corrected = (line_end[0] - self.size[0] / 2, line_end[1] - self.size[1] / 2)
            # Project line in pre-rotation target image referential
            start = (
                line_start_corrected[0] * rot_circle[0] + line_start_corrected[1] * rot_circle[1] + self.size[0] / 2,
                line_start_corrected[1] * rot_circle[0] + line_start_corrected[0] * rot_circle[1] + self.size[1] / 2)
            end = (
                line_end_corrected[0] * rot_circle[0] + line_end_corrected[1] * rot_circle[1] + self.size[0] / 2,
                line_end_corrected[1] * rot_circle[0] + line_end_corrected[0] * rot_circle[1] + self.size[1] / 2)
            if start[0] == end[0] or abs((end[1] - start[1]) / (end[0] - start[0])) > 1:
                # Vertical cut
                is_cutting_x = True
                x_factor = (start[0] + end[0]) / (2 * self.size[0])
                pleft_size = (size[0] * x_factor, size[1])
                pright_size = (size[0] * (1 - x_factor), size[1])
                crop_left = (0, 0, size[0]*x_factor, size[1])
                crop_right = (size[0] * x_factor, 0, size[0] * (1 - x_factor), size[1])
            else:
                # Horizontal cut
                is_cutting_x = False
                y_factor = (start[1] + end[1]) / (2 * self.size[1])
                pleft_size = (size[0], size[1] * y_factor)
                pright_size = (size[0], size[1] * (1 - y_factor))
                crop_left = (0, 0, size[0], size[1] * y_factor)
                crop_right = (0, size[0] * y_factor, size[0], size[1] * (1 - y_factor))

            # Compute new image's post-rotation size
            pleft_hyp = math.sqrt(pleft_size[0] ** 2 + pleft_size[1] ** 2)
            pright_hyp = math.sqrt(pright_size[0] ** 2 + pright_size[1] ** 2)

            # Get new image's center displacement
            if is_cutting_x:
                pleft_displacement = (
                    size[0] * (0.5 - x_factor / 2) * math.cos(self.rotation + math.pi),
                    size[0] * (0.5 - x_factor / 2) * math.sin(self.rotation + math.pi),
                    )
                pright_displacement = (
                    size[0] * (x_factor / 2) * math.cos(self.rotation),
                    size[0] * (x_factor / 2) * math.sin(self.rotation),
                    )
            else:
                pleft_displacement = (
                    size[0] * (0.5 - y_factor / 2) * math.sin(-self.rotation + math.pi),
                    size[0] * (0.5 - y_factor / 2) * math.cos(-self.rotation + math.pi),
                    )
                pright_displacement = (
                    size[0] * (y_factor / 2) * math.sin(-self.rotation),
                    size[0] * (y_factor / 2) * math.cos(-self.rotation),
                    )
            return [
                ImageCutterImage(im.Crop(self.image, *crop_left),
                    speed = (self.speed[0], self.speed[1]+30),
                    rotation = self.rotation,
                    rotation_speed = self.rotation_speed,
                    position = (
                        self.pos[0] + pleft_displacement[0] + (displayed_size[0] - pleft_hyp) / 2,
                        self.pos[1] + pleft_displacement[1] + (displayed_size[1] - pleft_hyp) / 2,
                        ),
                    acceleration = self.acceleration,
                    fresh = self.fresh + 1,
                    timeout = self.timeout,
                ), ImageCutterImage(im.Crop(self.image, *crop_right),
                    speed = (self.speed[0], self.speed[1]-30),
                    rotation = self.rotation,
                    rotation_speed = self.rotation_speed,
                    position = (
                        self.pos[0] + pright_displacement[0] + (displayed_size[0] - pright_hyp) / 2,
                        self.pos[1] + pright_displacement[1] + (displayed_size[1] - pright_hyp) / 2,
                        ),
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
            The base fruit images to use

        `cutting_actions`
            What to do when a fruit is cut

        `min_opaque_pixels`
            The number of pixels that should be cut in a fruit for the cut to be 'valid'
        """
        cursor_pos = (0, 0)
        is_cutting = False
        st = 0
        cutables = []
        expired_cutables = []
        last_create = 0

        def __init__(self, images, cutting_actions = None, min_opaque_pixels = 200, **kwargs):
            super(ImageCutter, self).__init__(**kwargs)
            self.images = images
            self.cutting_actions = cutting_actions
            self.min_opaque_pixels = min_opaque_pixels

        def render(self, width, height, st, at):
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
            renpy.redraw(self, 0.02)
            return render
        
        def update_cycle(self, st):
            st_diff = st - self.st
            self.st = st
            deletion_list = []
            for c in self.cutables:
                c.move(st_diff)
                if c.pos[1] > config.screen_height + 100:
                    deletion_list.append(c)
            for d in deletion_list:
                self.cutables.remove(d)
            deletion_list = []
            for c in self.expired_cutables:
                c.move(st_diff)
                if c.pos[1] > config.screen_height + 100:
                    deletion_list.append(c)
            for d in deletion_list:
                self.expired_cutables.remove(d)
            if self.last_create + 2 <= st:
                self.last_create = st
                self.cutables.append(ImageCutterImage(
                    image = self.images[renpy.random.randint(0, len(self.images)-1)],
                    position = (renpy.random.randint(300, 800), renpy.random.randint(100, 200)),
                    speed = (0, renpy.random.uniform(-100, 0)),
                    rotation_speed = renpy.random.uniform(0, 0),
                    rotation = renpy.random.uniform(0,2) * math.pi,
                ))

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
            # Ensure that we cut through a significant-enough section that the split would be visible
            # we do this by ensuring there is enough opaque pixels along the section
            a = (end[1] - start[1]) / (end[0] - start[0]) if end[0] != start[0] else 999999
            accumulator = 0
            # Prepare exploration
            # The lambda is probably very expensive to run here, but w/e
            if a == 999999:
                x_or_y = end[1]
                get_pos = lambda y: (end[0], y)
            elif a == 0:
                x_or_y = end[0]
                get_pos = lambda x: (x, end[1])
            elif abs(a) > 1:
                x_or_y = end[1]
                get_pos = lambda y: ((y - end[1]) / a + end[0], y)
            else:
                x_or_y = end[0]
                get_pos = lambda x: (x, (x - end[0]) * a + end[1])
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
                if (c.timeout < self.st and c.last_render and c.last_render.is_pixel_opaque(end[0]-c.pos[0], end[1]-c.pos[1])):
                    # Split if enough opaque pixel on the line
                    if self.is_colliding(c, start, end):
                        c.timeout = self.st + 0.5
                        addition_list += c.split((start[0] - c.pos[0], start[1] - c.pos[1]), (end[0] - c.pos[0], end[1] - c.pos[1]))
                        deletion_list.append(c) # We're going to split this, it's ok it'll survive... somewhat

                    #rope = self.line_square_rope(start, end, c.pos, (c.pos[0] + c.size[0], c.pos[1] + c.size[1]))
                    ## If image has a chance to have enough opaque pixels
                    #if (rope and (rope[1][0] - rope[0][0]) ** 2 + (rope[1][1] - rope[0][1]) ** 2 > self.min_opaque_pixels ** 2):

                    #    print(c.last_render.is_pixel_opaque(end[0] - c.pos[0], end[1] - c.pos[1]))
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
                #print("POS " + str(x) + " - " + str(y))
            if self.is_cutting:
                self.process_collisions(self.cursor_pos, (x, y))
            self.cursor_pos = (x, y)
            return super(ImageCutter, self).event(ev, x, y , at)
