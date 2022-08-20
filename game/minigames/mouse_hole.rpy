# @Author Ayowel
init python:
    import pygame

    # This class handles the creation of a hole in the render areafor an image
    # If no filter image is provided, 
    #
    # # Parameters
    #
    # base_image:
    #     Image-like displayable used as the static background image (or the dynamic background if filter_image is None)
    # filter_image:
    #     An alpha filter to apply to the base image that will be centered on the mouse cursor. It should usually be at least twice as big as the base image
    #
    # # Examples
    #
    # ```rpy
    # image mousehole = MouseHole(
    #         base_image = "images/bg/room.png",
    #         filter_image = "images/items/hole_alpha.png",
    #         xsize = 1., ysize=1., xalign=0., yalign=0.
    #         )
    #
    # screen make_a_hole():
    #     add 'mousehole'
    # ````
    class MouseHole(renpy.Displayable):
        def __init__(self, base_image, filter_image = None, **kwargs):
            super(MouseHole, self).__init__(**kwargs)
            # @see Class documentation
            self.base_image = renpy.displayable(base_image)
            self.alpha_image = filter_image and renpy.displayable(filter_image)
            # Used to get mouse center, we use pygame to preshot the actual position
            self.cursor_pos = (0, 0)
            # Final rendered image
            self.filtered_image = None
            self.redraw_filtered_image = True
            # Rendered image location
            self.blit_pos = (0,0)

        def render(self, width, height, st, at):
            render = renpy.Render(width,height)
            if self.redraw_filtered_image:
                # If an alpha image was provided, track the mouse with it before applying to background
                # If no alpha image was provided, track the mouse with the base image instead
                if self.alpha_image:
                    lamp_size = self.alpha_image.render(width, height, st, at).get_size()
                    night_alpha = Transform(self.alpha_image, xoffset = self.cursor_pos[0]-lamp_size[0]/2, yoffset = self.cursor_pos[1]-lamp_size[1]/2)
                    self.filtered_image = AlphaMask(self.base_image, night_alpha)
                else:
                    bg_size = self.base_image.render(width, height, st, at).get_size()
                    self.blit_pos = (self.cursor_pos[0]-bg_size[0]/2, self.cursor_pos[1]-bg_size[1]/2)
                    self.filtered_image = Transform(self.base_image)
                self.redraw_filtered_image = False
            render.blit(self.filtered_image.render(width, height, st, at), self.blit_pos)
            
            return render

        # Listen for mouve move events
        def event(self, ev, x, y, st):
            if self.cursor_pos[0] != x or self.cursor_pos[1] != y:
                self.cursor_pos = (x, y)
                self.redraw_filtered_image = True
                renpy.redraw(self, 0)

        # Un visiteur ! Venu d'ailleurs !
        # Ooooooooohhhhhhhh
        def visit(self):
            if self.filtered_image:
                return [self.filtered_image]
            else:
                return []
