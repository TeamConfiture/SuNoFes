init python:
    import math
    class KonamiCode(renpy.Displayable):
        def __init__(self, konami_action, **kwargs):
            super(KonamiCode, self).__init__(**kwargs)
            self.konami_action = konami_action
            self.konami_scancodes = [82, 82, 81, 81, 80, 79, 80, 79]
            self.konami_index = 0

        def render(self, width, height, st, at):
            render = renpy.Render(0, 0)
            return render

        def event(self, ev, x, y, st):
            if ev._type == 769: # This is a keyup event
                if ev.scancode == self.konami_scancodes[self.konami_index]:
                    if self.konami_index == len(self.konami_scancodes)-1:
                        self.konami_action()
                        self.konami_index = 0
                    else:
                        self.konami_index = self.konami_index + 1
                else:
                    self.konami_index = 0
            return None
