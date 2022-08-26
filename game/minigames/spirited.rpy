# @Author Ayowel
init python:
    import math

    class SpiritedSpriteInfo():
        """
        Container class used by Spirited, should not be used directly
        """
        def __init__(self, rid, sprite, speed, direction, roll, roll_offset, duration, fadein, fadeout, st):
            # base image id for use by Spirited upon opacity change
            self.rid = rid
            # Whether the sprite is appearing (0), stable (1), or disappearing (2)
            self.cycle = 0
            self.speed = speed
            self.direction = direction
            self.roll = roll
            self.start_pos = (sprite.x, sprite.y)
            # 0-100, used by increments of 10 in the current implementation
            self.opacity = 0
            self.birth_time = st
            # how long the sprite should stay visible before starting to disappear
            self.duration = duration
            self.sprite = sprite
            self.roll_offset = roll_offset
            self.fadein = fadein
            self.fadeout = fadeout

    class Spirited(renpy.Displayable, NoRollback):
        """
        This class provides rendering for mostly-linear effects
        such as "mystic" particles, rain, or snow.

        It must be instanciated as an image before usage.

        # Arguments

        `sprite_list`
            An array of images to use as sprites

        `renewal_rate`
            On average, how many sprites should be generated per second while the minimum rate is not reached

        `initial_count`
            How many sprites should be generated at the start

        `minimum_pool`
            Minimum number of sprites that must exist at the same time

        `maximum_pool`
            Maximum number of sprites that may exist at the same time

        `speed_range`
            How slow/fast a sprite may move

        `direction_range`
            Valid direction angle for a sprite (in radians)

        `roll_range`
            How far from its base direction line a sprite may "wobble"

        `ttl_range`
            How long a sprite may live (in seconds)

        `fadein_range`
            The time it should take for a sprite to reach 100% opacity as it appears (in seconds)
            This time IS part of the sprite's lifetime (see `ttl_range`)

        `fadeout_range`
            The time it should take for a sprite to reach 0% opacity as it disappears (in seconds)
            This time IS NOT part of the sprite's lifetime (see `ttl_range`)

        `bounding_box`
            If != None, screen-relative limits beyond which a sprite WILL be deleted before its lifespan expires in the format (left, top, right, bottom)
            The calculation is performed relative to the top left corner of the sprites

        `spawn_box`
            If != None, screen-relative limits within which a sprite will be created in the format (left, top, right, bottom)
            The calculation is performed relative to the top left corner of the sprites

        `repulsor_strength`
            How fast sprites should run away from the mouse' cursor

        `repulsor_radius`
            How far the mouse's position affects sprites

        `repulsor_hardness`
            How strong the repulsor is at the max distance compared to on the cursor (as a multiplicator)

        `repulsor_mode`
            0 to have a simple repulsor
            1 to have a tornado around the cursor
            Other values are unsupported

        `guideline`
            A custom lambda function that takes four parameters and returns a displacement tuple:
            param1: A SpiritedSpriteInfo instance
            param2: The time ellapsed since the last update in milliseconds
            param3: A tuple that contains the displacement calculated based on Spirited's parameters
                    This displacement must be part of the tuple returned by the function to be applied to the sprite
            param4: A tuple that contains the displacement that would be caused by the mouse's cursor's position
                    This displacement must be part of the tuple returned by the function to be applied to the sprite

        # Examples

        Minimal usage example

        ```rpy
        image spirited = Spirited(
            sprite_list = ["images/sprites/light1.png", "images/sprites/light2.png"],
            )
        screen spirited():
            add 'spirited'
        ```

        Make the sprites go up and avoid the mouse cursor

        ```rpy
        image spirited = Spirited(
            sprite_list = ["images/sprites/small_firefly.png", "images/sprites/big_firefly.png", "images/sprites/medium_firefly.png"],
            renewal_rate = 500,
            direction_range = (70, 110),
            repulsor_strength = 400,
            repulsor_radius = 300,
            )
        screen spirited():
            add 'spirited'
        ```

        Make it rain from above the screen and disappear around the middle

        ```rpy
        image spirited = Spirited(
            sprite_list = ["images/sprites/small_firefly.png", "images/sprites/big_firefly.png", "images/sprites/medium_firefly.png"],
            initial_count = 500,
            renewal_rate = 500,
            speed_range = (10, 150),
            direction_range = (250, 290),
            ttl_range = (1, 3),
            spawn_box = (0, -100, 0, -config.screen_height),
            )
        screen spirited():
            add 'spirited'
        ```
        """
        # Initialize internal Displayable library with alpha levels
        # All displayables are based on sprite_list images
        image_collection = []
        image_sizes = []
        # Cursor position to compute repulsor attributes
        cursor_pos = (0, 0)
        # Set of rendered sprites
        render_set = set()
        # last render timer
        last_update = 0
        # Accumulator used to know when to spawn a new sprite
        accumulated_spawn_odds = 0

        def __init__(self,
                sprite_list, renewal_rate = 30, initial_count = 100, minimum_pool = 0, maximum_pool = None,
                speed_range = (0, 300), direction_range = (0, 360), roll_range = (0, 40), ttl_range = (1, 10),
                bounding_box = (-260, -280, 60, 300), spawn_box = (-20, 50, -80, 300),
                repulsor_strength = 0, repulsor_radius = 0, repulsor_hardness = 0, repulsor_mode = 0,
                fadein_range = (0.7, 1.5), fadeout_range = (1, 2), guideline = None,
                **kwargs,
                ):
            super(Spirited, self).__init__(**kwargs)

            # Save configuration variables
            self.initial_count = initial_count
            self.renewal_rate = renewal_rate
            self.minimum_pool = minimum_pool
            self.maximum_pool = maximum_pool
            self.direction_range = (math.radians(direction_range[0]), math.radians(direction_range[1]))
            self.speed_range = speed_range
            self.roll_range = roll_range
            self.ttl_range = ttl_range
            self.bounding_box = bounding_box
            self.spawn_box = spawn_box
            self.base_image_list = sprite_list
            self.repulsor_strength = repulsor_strength
            self.repulsor_radius = repulsor_radius
            self.repulsor_radius_squared = repulsor_radius ** 2
            self.repulsor_hardness = repulsor_hardness
            self.repulsor_mode = repulsor_mode
            self.guideline = guideline
            self.fadein_range = fadein_range
            self.fadeout_range = fadeout_range

            # Handle the graphical part with a sprite manager
            self.manager = SpriteManager(update = self.update_sprites, predict = self.manager_predict)

        def manager_predict(self):
            """
            Provided to SpriteManager to predict future displayables
            """
            return [i for i in ilist for ilist in self.image_collection]

        def new_sprite(self):
            """
            Add a new sprite to the internal sprite manager which's characteristics
            will be randomly generated based on the ranges provided at init
            """
            if self.maximum_pool is not None and self.maximum_pool <= len(self.render_set):
                return
            # Pick a reference sprite to use
            rid = renpy.random.randint(0, len(self.image_collection)-1)
            # Pick a spawn location
            if self.spawn_box:
                pos = (
                    renpy.random.randint(self.spawn_box[0], config.screen_width + self.spawn_box[2]),
                    renpy.random.randint(self.spawn_box[1], config.screen_height + self.spawn_box[3]),
                    )
            else:
                pos = (
                    renpy.random.randint(0, config.screen_width),
                    renpy.random.randint(0, config.screen_height),
                )
            # Instanciate a new transparent sprite
            sprite = self.manager.create(self.image_collection[rid][0])
            sprite.x = pos[0]
            sprite.y = pos[1]
            # Initialize other attribute according to configuration
            speed = renpy.random.randint(*self.speed_range)
            direction = renpy.random.uniform(*self.direction_range)
            roll = renpy.random.randint(*self.roll_range)
            roll_offset = renpy.random.random() * math.pi * 2
            ttl = renpy.random.uniform(*self.ttl_range)
            # Avoid 0 and negative values as it would be a pain to handle later and would not make sense
            # We do want to allow them within the random number generation range though
            fadein_time = max(0.00001, renpy.random.uniform(*self.fadein_range))
            fadeout_time = max(0.00001, renpy.random.uniform(*self.fadeout_range))

            # Instanciate and add the new sprite
            self.render_set.add(
                SpiritedSpriteInfo(
                    rid = rid,
                    sprite = sprite,
                    speed = speed,
                    direction = direction,
                    roll = roll,
                    roll_offset = roll_offset,
                    duration = ttl,
                    st = self.last_update,
                    fadein = fadein_time,
                    fadeout = fadeout_time,
                )
            )

        def update_sprites(self, st):
            """
            Provided to SpriteManager to handle sprites updates
            """
            current_time = st
            time_diff = current_time - self.last_update
            self.last_update = current_time
            self.accumulated_spawn_odds = self.accumulated_spawn_odds + renpy.random.random() * self.renewal_rate * time_diff
            while self.accumulated_spawn_odds > 1:
                self.accumulated_spawn_odds = self.accumulated_spawn_odds - 1
                self.new_sprite()

            # What does this loop cost ? everything
            scheduled_deletions = []
            for sprite in self.render_set:
                # Delete sprites out of bounding box
                if self.bounding_box:
                    if (sprite.sprite.x < self.bounding_box[0] or
                            sprite.sprite.x > config.screen_width + self.bounding_box[2] or
                            sprite.sprite.y < self.bounding_box[1] or
                            sprite.sprite.y > config.screen_height + self.bounding_box[3]
                            ):
                        scheduled_deletions.append(sprite)
                        continue
                # Start disappearance for sprites that have reached their TTL
                if sprite.duration < current_time - sprite.birth_time:
                    sprite.cycle = 2
                if sprite.cycle == 0:
                    # increase opacity as the sprite appears within [0-100] range
                    sprite.opacity = min(max(sprite.opacity + time_diff * 100 / sprite.fadein, 0), 100)
                    if sprite.opacity >= 100:
                        sprite.cycle = 1
                        sprite.opacity = 100
                    sprite.sprite.set_child(self.image_collection[sprite.rid][math.floor(sprite.opacity / 10)])
                elif sprite.cycle == 2:
                    # Decrease opacity as the sprite disappears within [0-100 range]
                    sprite.opacity = min(max(sprite.opacity - time_diff * 100 / sprite.fadeout, 0), 100)
                    if sprite.opacity <= 1: # The sprite should disappear. Forever
                        scheduled_deletions.append(sprite)
                        continue
                    sprite.sprite.set_child(self.image_collection[sprite.rid][math.floor(sprite.opacity / 10)])
                # Compute reaction to mouse cursor position
                repulsor = (0, 0)
                if self.repulsor_strength != 0 and self.repulsor_radius != 0:
                    sprite_center = (sprite.sprite.x + self.image_sizes[sprite.rid][0]/2, sprite.sprite.y + self.image_sizes[sprite.rid][1]/2)
                    dist_vec = (sprite_center[0]-self.cursor_pos[0], sprite_center[1]-self.cursor_pos[1])
                    dist_squared = dist_vec[0] ** 2 + dist_vec[1] ** 2
                    # If within repulsor range, apply force in the direction of the mouse -> sprite cursor
                    # Note that the repulsor's strength evolves proportionnally to the square of the distance as it feels better
                    if self.repulsor_radius_squared > dist_squared:
                        dist = math.sqrt(dist_squared)
                        local_repulsor = (self.repulsor_strength + (self.repulsor_hardness - self.repulsor_strength) * dist_squared / self.repulsor_radius_squared) * time_diff
                        if self.repulsor_mode == 0:
                            repulsor = (local_repulsor * dist_vec[1] / dist, local_repulsor * dist_vec[0] / dist)
                        elif self.repulsor_mode == 1:
                            repulsor = (local_repulsor * dist_vec[0] / dist, -local_repulsor * dist_vec[1] / dist)

                # Calculate sprite position change
                speed = sprite.speed * time_diff
                roll = (math.sin(current_time + sprite.roll_offset) - math.sin(current_time - time_diff + sprite.roll_offset)) * sprite.roll
                displacement = (
                    -speed * math.sin(sprite.direction) + roll * math.cos(sprite.direction),
                    speed * math.cos(sprite.direction) + roll * math.sin(sprite.direction)
                    )
                if self.guideline:
                    calculated_displacement = self.guideline(sprite, time_diff, displacement, repulsor)
                else:
                    calculated_displacement = (displacement[0] + repulsor[0], displacement[1] + repulsor[1])

                # Update sprite position
                sprite.sprite.y = sprite.sprite.y + calculated_displacement[0]
                sprite.sprite.x = sprite.sprite.x + calculated_displacement[1]

            # Delete obsolete sprites
            for sprite in scheduled_deletions:
                sprite.sprite.destroy()
                self.render_set.remove(sprite)
            
            # Ensure we have at least the minimum number of sprites
            if len(self.render_set) < self.minimum_pool:
                for _ in range(self.minimum_pool - len(self.render_set)):
                    self.new_sprite()

        def first_render(self):
            """
            Resets sprites context
            """
            if len(self.image_collection) == 0:
                # Create sprite library with different transparency levels
                for i in range(len(self.base_image_list)):
                    displayable = renpy.displayable(self.base_image_list[i])
                    self.image_collection.append([Transform(child = displayable, alpha = j/100) for j in range(0, 101, 10)])
                self.image_sizes = [renpy.render(d[0], 0, 0, 0, 0).get_size() for d in self.image_collection]
            # Remove any existing sprite (only happens on new game/save reload after display in a game)
            for s in self.render_set:
                s.sprite.destroy()
            self.render_set = set()

            # Create initial sprites
            for i in range(self.initial_count):
                self.new_sprite()

        def render(self, width, height, st, at):
            if st == 0:
                self.last_update = st
                self.first_render()
            # Schedule next update and return rendered view
            renpy.redraw(self, 0.05)
            return self.manager.render(width, height, st, at)

        def event(self, ev, x, y, st):
            """
            Listen for mouve move events
            """
            self.cursor_pos = (x, y)

        def visit(self):
            return [ self.manager ]
