init python:
    import pygame
    class PoorMansAnimatedImageButton(renpy.Container):
        """
        This class only exists because the collision mask of ImageButtons
        does not move along its internal image if it is animated.

        Also, ImageButtons return a copy of the internal image at each state change,
        which resets the animation.

        DO NOT USE xanchor or yanchor on the images, thank you
        """
        last_render = None
        def __init__(self, idle_image, action = None, **kwargs):
            super(PoorMansAnimatedImageButton, self).__init__(renpy.easy.displayable(idle_image), **kwargs)
            self.action = action
        def render(self, width, height, st, at):
            self.last_render = super(PoorMansAnimatedImageButton, self).render(width, height, st, at)
            return self.last_render
        def event(self, ev, x, y, st):
            if self.last_render and self.action and ev.type == pygame.MOUSEBUTTONUP:
                if self.last_render.is_pixel_opaque(x, y):
                    renpy.run(self.action)
            return super(PoorMansAnimatedImageButton, self).event(ev, x, y, st)
