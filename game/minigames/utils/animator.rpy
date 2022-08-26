# @author Ayowel
init python:

    class SelectedCardAnimator():
        """
        This is an animator to use with Manageable objects in manageable.rpy

        This animator performs a "rotation" of the sprites when the transition
        label changes from containing or not containing the string 'selected_"
        """
        state_children = {}
        animation_base_st = 0
        st = 0
        animating = False
        previous_image = None
        future_image = None
        images_width = 0
        def __init__(self, animation_time = 0.3):
            self.animation_time = animation_time
        def base_images(self, **children):
            """
            Load a base set of state keys to use during animations

            `children`
                A dict that contains image-list displayables to use when new states are received
            """
            self.state_children = children

        def new_transition(self, previous, next, st, future = None):
            """
            Inform that a new transition should occur

            `previous`
                Previous state
            `next`
                State to animate toward
            `st`
                The current animation timestamp at the time the transition occurs
            `future`
                An image-like displayable to use instead of the value corresponding to `next` in the internal dict
            """
            self.previous_image = self.future_image
            if previous is None or next is None:
                # Do not animate if we don't know where we are or where we're going
                self.animating = False
            elif ('selected_' in previous) == ('selected_' in next):
                # handle hover/idle sprite changes
                if self.is_animating():
                    self.future_image = future or self.state_children.get(next) or self.future_image
            else:
                self.future_image = future or self.state_children.get(next)
                if not self.previous_image:
                    self.previous_image = self.state_children.get(previous)
                self.animating = self.future_image and self.previous_image
                # Perform additionnal setup should an animation run
                if self.animating:
                    base_st_offset = st - self.animation_base_st
                    # Handle selection change while an animation is running
                    if base_st_offset < self.animation_time:
                        self.animation_base_st = st - base_st_offset
                    else:
                        self.animation_base_st = st
                    self.images_width = self.future_image.render(0, 0, 0, 0).get_size()[0]

        def is_animating(self):
            """
            Internal function used to know whether an animation is ongoing
            """
            return self.animating and self.st - self.animation_base_st < self.animation_time

        def update_placement(self, placement):
            """
            Get an updated location of the base displayable

            `placement`
                The default object placement
            """
            if self.is_animating():
                current_time = self.st - self.animation_base_st
                cutoff_st = self.animation_time/2
                if current_time > cutoff_st:
                    scale_factor = (current_time - cutoff_st) / cutoff_st
                else:
                    scale_factor = (cutoff_st - current_time) / cutoff_st
                scale_factor = 1 - max(2/self.images_width, scale_factor)
                moved = (
                    math.floor((placement[0] or 0) + scale_factor * self.images_width/2),  placement[1],
                    placement[2], placement[3], placement[4], placement[5], placement[6],
                    )
                return moved
            else:
                return placement

        def animate(self, caller, st):
            """
            Compute the current animation to render and return it

            `caller`
                The parent's context, must support renpy.redraw
            `st`
                The current render timestamp
            """
            self.st = st
            if self.is_animating():
                current_time = self.st - self.animation_base_st
                cutoff_st = self.animation_time/2
                if current_time > cutoff_st:
                    scale_factor = (current_time - cutoff_st) / cutoff_st
                    image = self.future_image
                else:
                    scale_factor = (cutoff_st - current_time) / cutoff_st
                    image = self.previous_image
                scale_factor = max(2/self.images_width, scale_factor)
                renpy.redraw(caller, 0.02)
                return im.FactorScale(image, scale_factor, 1.)
            else:
                self.animating = False
                return None
