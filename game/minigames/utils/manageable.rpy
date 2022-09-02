# @Author Ayowel
init python:
    def auto_image_choice(a, b, name, auto, required=False):
        """
        This is an adaptation of renpy's _imagebutton function's
        choice function. For internal use of this file only.
        """
        if a or b:
            return a or b
        if auto is not None:
            rv = renpy.config.imagemap_auto_function(auto, name)
            if rv is not None:
                return rv
        if required:
            if auto:
                raise Exception("Imagebutton does not have a %s image. (auto=%r)." % (name, auto))
            else:
                raise Exception("Imagebutton does not have a %s image." % (name,))
        return None

    class ManageableImageButton(ImageButton):
        """
        This Button supports freezing its display state and adding custom a custom transition animation when changing state

        `auto`
            Add support for auto parameter to the base ImageButton as it is normally part of the proxy instanciation function

        `frozen_state`
            A valid parameter for ManageableImageButton.freeze_state

        `animator`
            The animation handler upon state change
        """

        st = 0
        last_prefix = None

        def __init__(self, auto = None, frozen_state = None, animator = None, **kwargs):
            if auto:
                kwargs["idle_image"] = auto_image_choice(kwargs.get("idle"), kwargs.get("idle_image"), "idle", auto, required=True)
                kwargs["hover_image"] = auto_image_choice(kwargs.get("hover"), kwargs.get("hover_image"), "hover", auto)
                kwargs["insensitive_image"] = auto_image_choice(kwargs.get("insensitive"), kwargs.get("insensitive_image"), "insensitive", auto)
                kwargs["selected_idle_image"] = auto_image_choice(kwargs.get("selected_idle"), kwargs.get("selected_idle_image"), "selected_idle", auto)
                kwargs["selected_hover_image"] = auto_image_choice(kwargs.get("selected_hover"), kwargs.get("selected_hover_image"), "selected_hover", auto)
                kwargs["selected_insensitive_image"] = auto_image_choice(kwargs.get("selected_insensitive"), kwargs.get("selected_insensitive_image"), "selected_insensitive", auto)
            super(ManageableImageButton, self).__init__(**kwargs)

            self.animator = animator
            if frozen_state:
                self.enforced_state = frozen_state + '_'
            else:
                self.enforced_state = None

        def render(self, width, height, st, at):
            self.st = st
            renpy.redraw(self, 10.)
            if st == 0 and self.animator:
                self.animator.base_images(**self.state_children)
            return super(ManageableImageButton, self).render(width, height, st, at)

        def select_state(self, selected = True, animate = True):
            self.selected = selected
            # TODO: handle animate
            renpy.redraw(self, 0)

        def get_placement(self):
            placement = super(ManageableImageButton, self).get_placement()
            if self.animator:
                placement = self.animator.update_placement(placement)
            return placement

        def freeze_state(self, display_state = None, animate = True):
            """
            Freeze the button's display to it's current state or an arbitrary state

            `display_state`
                If provided, display_state should be 'idle', 'hover', 'insensitive', or any of those preceded by 'selected_'
            """
            # TODO: handle animate
            if display_state:
                self.enforced_state = display_state
                renpy.redraw(self, 0)
            else:
                self.enforced_state = self.style.prefix

        def unfreeze_state(self, animate = True):
            """
            Unfreeze the button's display
            """
            # TODO: handle animate
            self.enforced_state = None
            renpy.redraw(self, 0)

        def get_child(self):
            """
            Internal function of ImageButton overloaded to provide the expected capabilities of this button
            """
            child = self.style.child or self.state_children[self.style.prefix]
            if self.enforced_state:
                child = self.state_children.get(self.enforced_state + '_', child)

            if self.style.prefix != self.last_prefix and self.animator:
                self.animator.new_transition(self.last_prefix, self.style.prefix, self.st, child)
                self.last_prefix = self.style.prefix

            if self.animator:
                anim = self.animator.animate(self, self.st)
                if anim:
                    child = anim

            return child
