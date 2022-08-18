# @Author Ayowel
init python:
    import random
    import time
    import math

    # Container class for Spirited, should not be used directly is the scene is to last more than one screen
    # 
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
    # minimum_pool: Minimum number of sprites that may exist at the same time
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
    #
    # # Examples
    #
    # ```rpy
    # # This screen will be called
    # screen spirited():
    #     add Spirited(
    #         sprite_list = ["images/sprites/light1.png", "images/sprites/light2.png"],
    #         xsize = 1., ysize = 1.,
    #         )
    #```
    # ```rpy
    # # This screen will be shown
    # screen spirited():
    #     add SpiritedInstance(
    #         instance_name = "forest",
    #         spirited_args = {
    #             "sprite_list": ["images/sprites/light1.png", "images/sprites/light2.png"],
    #             "direction_range": (1.2, 1.9),
    #         }, xsize = 1., ysize = 1.,
    #         )
    # ```
    class Spirited(renpy.Displayable):
        def __init__(self,
                sprite_list, renewal_rate = 30, initial_count = 100, minimum_pool = 0, maximum_pool = 300,
                speed_range = (0, 300), direction_range = (0, math.pi*2), roll_range = (0, 40), ttl_range = (1, 10),
                bounding_box = (-260, -280, 60, 300), spawn_box = (-20, 50, -80, 300),
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

            # Initialize internal Displayable library with alpha levels
            # All displayables are based on sprite_list images
            self.image_collection = []
            for i in range(0, len(self.base_image_list)):
                displayable = renpy.displayable(self.base_image_list[i])
                self.image_collection.append([Transform(child = displayable, alpha = j/100) for j in range(0, 101, 10)])
            # Handle the graphical part with a sprite manager
            self.manager = SpriteManager()
            # 
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
            rid = random.randint(0, len(self.image_collection)-1)
            # Pick a spawn location
            if self.spawn_box:
                pos = (
                    random.randint(self.spawn_box[0], config.screen_width + self.spawn_box[2]),
                    random.randint(self.spawn_box[1], config.screen_height + self.spawn_box[3]),
                    )
            else:
                pos = (
                    random.randint(0, config.screen_width),
                    random.randint(0, config.screen_height),
                )
            # Instanciate a new transparent sprite
            sprite = self.manager.create(self.image_collection[rid][0])
            sprite.x = pos[0]
            sprite.y = pos[1]
            # Initialize other attribute according to configuration
            speed = random.randint(self.speed_range[0], self.speed_range[1])
            direction = random.random() * (self.direction_range[1] - self.direction_range[0]) + self.direction_range[0]
            roll = random.randint(self.roll_range[0], self.roll_range[1])
            roll_offset = random.random() * math.pi * 2
            ttl = random.random() * (self.ttl_range[1] - self.ttl_range[0]) + self.ttl_range[0]

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

        def render(self, width, height, st, at):
            if self.first_render_time is None:
                # Create the initial sprite
                # If we create it at init we don't get the initial "pop" effect when using a SpiritedInstance
                for i in range(0, self.initial_count):
                    self.new_sprite()
                self.last_update = time.time()
                self.first_render_time = self.last_update
            current_time = time.time()
            time_diff = current_time - self.last_update
            self.last_update = current_time
            self.accumulated_spawn_odds = self.accumulated_spawn_odds + random.random() * self.renewal_rate * time_diff
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
                # Update sprite position
                speed = sprite.speed * (current_time - sprite.birth_time)
                roll = math.sin(current_time - sprite.birth_time + sprite.roll_offset) * sprite.roll
                sprite.sprite.y = sprite.start_pos[1] - speed * math.sin(sprite.direction) + roll * math.cos(sprite.direction)
                sprite.sprite.x = sprite.start_pos[0] + speed * math.cos(sprite.direction) + roll * math.sin(sprite.direction)

            # Delete obsolete sprites
            for sprite in scheduled_deletions:
                sprite.sprite.destroy()
                self.render_set.remove(sprite)
            
            # Ensure we have at least the minimum number of sprites
            if len(self.render_set) < self.minimum_pool:
                for _ in range(0, self.minimum_pool - len(self.render_set)):
                    self.new_sprite()

            # Schedule next update and return rendered view
            renpy.redraw(self, 0.05)
            return self.manager.render(width, height, st, at)

        def visit(self):
            return [ self.manager ]

    spirited_dict = {}

    # A proxy for the Spirited class that reuses any existing instance
    # This is only usefull if a Spirited effect should last more than a few seconds
    class SpiritedInstance(renpy.Displayable):
        def __init__(self,
                instance_name = None,
                spirited_args = {},
                **kwargs,
                ):
            super(SpiritedInstance, self).__init__(**kwargs)
            self.instance_name = instance_name
            self.instance = None
            if self.instance_name is not None and spirited_dict.has_key(self.instance_name):
                self.instance = spirited_dict[self.instance_name]
            if self.instance is None:
                self.instance = Spirited(**spirited_args, **kwargs)
            if self.instance_name is not None:
                spirited_dict[self.instance_name] = self.instance

        def render(self, width, height, st, at):
            # Redraw here is required as ren'py does not honor the child's scheduling
            renpy.redraw(self, 0.05)
            return self.instance.render(width, height, st, at)

        def visit(self):
            return [ self.instance ]