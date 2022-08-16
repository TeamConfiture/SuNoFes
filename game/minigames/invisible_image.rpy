
init python:
    import math
    class InvisibleImage(renpy.Displayable):
        def __init__(self, child, opaque_distance, transparent_distance, **kwargs):
            super(InvisibleImage, self).__init__(**kwargs)
            self.child = renpy.displayable(child)

            self.opaque_distance = opaque_distance
            self.transparent_distance = transparent_distance

            self.alpha = 0.0

        def render(self, width, height, st, at):
            t = Transform(child = self.child, alpha = self.alpha)
            child_render = renpy.render(t, width, height, st, at)
            self.width, self.height = child_render.get_size()

            render = renpy.Render(self.width, self.height)
            render.blit(child_render, (0,0))
            return render

        def event(self, ev, x, y, st):
            distance = math.hypot(x - (self.width / 2), y - (self.height / 2))
            distance = max(min(distance, self.transparent_distance), self.opaque_distance)
            alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

            if alpha != self.alpha:
                self.alpha = alpha
                renpy.redraw(self, 0)

            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]
