# @Author Ayowel
init python:
    import time
    import math

    # Container class for Spirited, should not be used directly
    class SpiritedSpriteInfo():
        def __init__(self, rid, sprite, speed, direction, roll, roll_offset, duration):
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
            self.birth_time = time.time()
            # how long the sprite should stay visible before starting to disappear
            self.duration = duration
            self.sprite = sprite
            self.roll_offset = roll_offset

    # This class provides rendering for mostly-linear effects
    # such as "mystic" particles, rain, or snow
    #
    # To render outside of a called scene prefer to use SpiritedInstance
    #
    # # Arguments
    #
    # sprite_list: An array of images to use as sprites
    # renewal_rate: On average, how many sprites should be generated per second while the minimum rate is not reached
    # initial_count: How many sprites should be generated at the start
    # minimum_pool: Minimum number of sprites that must exist at the same time
    # maximum_pool: Maximum number of sprites that may exist at the same time
    # speed_range: how slow/fast a sprite may move
    # direction_range: Valid direction angle for a sprite (in radians)
    # roll_range: How far from its base direction line a sprite may "wobble"
    # ttl_range: How long a sprite may live
    # bounding_box:
    #     If != None, screen-relative limits beyond which a sprite WILL be deleted before its lifespan expires in the format (left, top, right, bottom)
    #     The calculation is performed relative to the top left corner of the sprites
    # spawn_box:
    #     If != None, screen-relative limits within which a sprite will be created in the format (left, top, right, bottom)
    #     The calculation is performed relative to the top left corner of the sprites
    # repulsor_strength: how fast sprites should run away from the mouse' cursos
    # repulsor_radius: how far the mouse's position affects sprites
    # repulsor_hardness: how strong the repulsor is at the max distance compared to on the cursor (as a multiplicator)
    # repulsor_mode: 0 to have a simple repulsor, 1 to have a tornado that goes woosh, anything else and nothing happens
    # guideline:
    #     A custom lambda function that takes four parameters and returns a displacement tuple:
    #       param1: A SpiritedSpriteInfo instance
    #       param2: The time ellapsed since the last update in milliseconds
    #       param3: A tuple that contains the displacement calculated based on Spirited's parameters
    #               This displacement must be part of the tuple returned by the function to be applied to the sprite
    #       param4: A tuple that contains the displacement that would be caused by the mouse's cursor's position
    #               This displacement must be part of the tuple returned by the function to be applied to the sprite
    #
    # # Examples
    #
    # ```rpy
    # # This screen will be called
    # image spirited = Spirited(
    #         sprite_list = ["images/sprites/light1.png", "images/sprites/light2.png"],
    #         xsize = 1., ysize = 1.,
    #         )
    # screen spirited():
    #     add 'spirited'
    #```
    # ```rpy
    # # This screen will be shown
    # image spirited = Spirited(
    #         instance_name = "forest",
    #         spirited_args = {
    #             "sprite_list": ["images/sprites/small_firefly.png", "images/sprites/big_firefly.png", "images/sprites/medium_firefly.png"],
    #             "renewal_rate": 500,
    #             "direction_range": (1.2, 1.9),
    #             "repulsor_strength": 400,
    #             "repulsor_radius": 300,
    #         }, xsize = 1., ysize = 1.,
    #         )
    # screen spirited():
    #     add 'spirited'
    # ```
    class Spirited(renpy.Displayable):
        def __init__(self,
                sprite_list, renewal_rate = 30, initial_count = 100, minimum_pool = 0, maximum_pool = None,
                speed_range = (0, 300), direction_range = (0, math.pi*2), roll_range = (0, 40), ttl_range = (1, 10),
                bounding_box = (-260, -280, 60, 300), spawn_box = (-20, 50, -80, 300),
                repulsor_strength = 0, repulsor_radius = 0, repulsor_hardness = 0, repulsor_mode = 0,
                guideline = None,
                **kwargs,
                ):
            super(Spirited, self).__init__(**kwargs)

            # Save configuration variables
            self.initial_count = initial_count
            self.renewal_rate = renewal_rate
            self.minimum_pool = minimum_pool
            self.maximum_pool = maximum_pool
            self.direction_range = direction_range
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

            # Initialize internal Displayable library with alpha levels
            # All displayables are based on sprite_list images
            self.image_collection = []
            self.image_sizes = []
            # Cursor position to compute repulsor attributes
            self.cursor_pos = (0, 0)
            # Handle the graphical part with a sprite manager
            self.manager = SpriteManager()
            # Set of rendered sprites
            self.render_set = set() 
            # last render timer
            self.last_update = None
            # Flag used to know if a render already occured
            self.first_render_time = None
            # Accumulator used to spawn a new 
            self.accumulated_spawn_odds = 0

        # Add a new sprite to the internal set
        def new_sprite(self):
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
            speed = renpy.random.randint(self.speed_range[0], self.speed_range[1])
            direction = renpy.random.random() * (self.direction_range[1] - self.direction_range[0]) + self.direction_range[0]
            roll = renpy.random.randint(self.roll_range[0], self.roll_range[1])
            roll_offset = renpy.random.random() * math.pi * 2
            ttl = renpy.random.random() * (self.ttl_range[1] - self.ttl_range[0]) + self.ttl_range[0]

            # Instanciate and add the new sprite
            self.render_set.add(
                SpiritedSpriteInfo(
                    rid,
                    sprite,
                    speed,
                    direction,
                    roll,
                    roll_offset,
                    ttl,
                )
            )

        def first_render(self):
            for i in range(len(self.base_image_list)):
                displayable = renpy.displayable(self.base_image_list[i])
                self.image_collection.append([Transform(child = displayable, alpha = j/100) for j in range(0, 101, 10)])
            self.image_sizes = [renpy.render(d[0], 0, 0, 0, 0).get_size() for d in self.image_collection]

        def render(self, width, height, st, at):
            if self.first_render_time is None:
                self.first_render()
                # Create the initial sprite
                # If we create it at init we don't get the initial "pop" effect when using a SpiritedInstance
                for i in range(self.initial_count):
                    self.new_sprite()
                self.last_update = time.time()
                self.first_render_time = self.last_update
            current_time = time.time()
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
                # FIXME: at the moment the opacity changes as fast as the view is rendered/updated instead of being tied to the clock
                # In most cases it should not make a difference though
                if sprite.cycle == 0:
                    # increase opacity as the sprite appears
                    sprite.opacity = sprite.opacity + 10
                    if sprite.opacity >= 100:
                        sprite.cycle = 1
                    sprite.sprite.set_child(self.image_collection[sprite.rid][math.floor(sprite.opacity / 10)])
                elif sprite.cycle == 2:
                    # Decrease opacity as the sprite disappears
                    if sprite.opacity <= 10: # The sprite should disappear. Forever
                        scheduled_deletions.append(sprite)
                        continue
                    sprite.opacity = sprite.opacity - 10
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

            # Schedule next update and return rendered view
            renpy.redraw(self, 0.05)
            return self.manager.render(width, height, st, at)

        # Listen for mouve move events
        def event(self, ev, x, y, st):
            self.cursor_pos = (x, y)

        def visit(self):
            return [ self.manager ]
