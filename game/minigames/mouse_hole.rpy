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
    # screen make_a_hole():
    #     add MouseHole(
    #         base_image = "images/bg/room.png",
    #         filter_image = "images/items/hole_alpha.png",
    #         xsize = 1., ysize=1., xalign=0., yalign=0.
    #         )
    # ````
    class MouseHole(renpy.Displayable):
        def __init__(self, base_image, filter_image = None, **kwargs):
            super(MouseHole, self).__init__(**kwargs)
            # @see Class documentation
            self.base_image = renpy.displayable(base_image)
            self.alpha_image = filter_image and renpy.displayable(filter_image)
            # Used to get mouse center, we use pygame to preshot the actual position
            self.cursor_pos = pygame.mouse.get_pos()
            # Final rendered image
            self.filtered_image = None
            self.redraw_filtered_image = True
            # Rendered image location
            self.blit_pos = (0,0)

        def render(self, width, height, st, at):
            render = renpy.Render(width,height)
            if self.redraw_filtered_image:
                # Normalize position, for some reason the pos we receive uses the physical location
                # instead of the projected location on the virtual render area
                physical_render_size = renpy.get_physical_size()
                light_pos = (
                    self.cursor_pos[0] / physical_render_size[0] * config.screen_width,
                    self.cursor_pos[1] / physical_render_size[1] * config.screen_height,
                )
                # If an alpha image was provided, track the mouse with it before applying to background
                # If no alpha image was provided, track the mouse with the base image instead
                if self.alpha_image:
                    lamp_size = self.alpha_image.render(width, height, st, at).get_size()
                    night_alpha = Transform(self.alpha_image, xoffset = light_pos[0]-lamp_size[0]/2, yoffset = light_pos[1]-lamp_size[1]/2)
                    self.filtered_image = AlphaMask(self.base_image, night_alpha)
                else:
                    print ("Alternative")
                    bg_size = self.base_image.render(width, height, st, at).get_size()
                    self.blit_pos = (light_pos[0]-bg_size[0]/2, light_pos[1]-bg_size[1]/2)
                    self.filtered_image = Transform(self.base_image)
                self.redraw_filtered_image = False
            render.blit(self.filtered_image.render(width, height, st, at), self.blit_pos)
            
            return render

        # Listen for mouve move events
        def event(self, ev, x, y, st):
            if ev.type == 1024: # cursor move event
                if ev.pos != self.cursor_pos:
                    self.cursor_pos = ev.pos
                    self.redraw_filtered_image = True
                    renpy.redraw(self, 0)

        # Un visiteur ! Venu d'ailleurs !
        # Ooooooooohhhhhhhh
        def visit(self):
            if self.filtered_image:
                return [self.filtered_image]
            else:
                return []
