# @Author Ayowel
init python:
    class ManageableImageButton(ImageButton):
        """
        This class implements a way to freeze the display state of an image button
        to an arbitrary state as neither .locked nor .sensitive attributes seem
        to be enough to do it and re-enable the button after
        """
        def image_choice_at_init(a, b, name, auto, required=False):
            """
            This is an adaptation of renpy's _imagebutton function's
            choice function. For internal use of this class only.
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

        enforced_imagebutton_child = None
        enforced_imagebutton_raw_child = None

        def __init__(self, auto = None, frozen_state = None, **kwargs):
            """
            `auto`
                Add support for auto parameter to the base ImageButton as it is normally part of the proxy instanciation function
            `frozen_state`
                A valid parameter for ManageableImageButton.freeze_state
            """
            if auto:
                kwargs["idle_image"] = ManageableImageButton.image_choice_at_init(kwargs.get("idle"), kwargs.get("idle_image"), "idle", auto, required=True)
                kwargs["hover_image"] = ManageableImageButton.image_choice_at_init(kwargs.get("hover"), kwargs.get("hover_image"), "hover", auto)
                kwargs["insensitive_image"] = ManageableImageButton.image_choice_at_init(kwargs.get("insensitive"), kwargs.get("insensitive_image"), "insensitive", auto)
                kwargs["selected_idle_image"] = ManageableImageButton.image_choice_at_init(kwargs.get("selected_idle"), kwargs.get("selected_idle_image"), "selected_idle", auto)
                kwargs["selected_hover_image"] = ManageableImageButton.image_choice_at_init(kwargs.get("selected_hover"), kwargs.get("selected_hover_image"), "selected_hover", auto)
                kwargs["selected_insensitive_image"] = ManageableImageButton.image_choice_at_init(kwargs.get("selected_insensitive"), kwargs.get("selected_insensitive_image"), "selected_insensitive", auto)
            super(ManageableImageButton, self).__init__(**kwargs)
            if frozen_state:
                self.enforced_state = frozen_state + '_'
            else:
                self.enforced_state = None

        def freeze_state(self, display_state = None):
            """
            Freeze the button's display to it's current state or an arbitrary state

            `display_state`
                If provided, display_state should be 'idle', 'hover', 'insensitive', or any of those preceded by 'selected_'
            """
            if display_state:
                self.enforced_state = display_state
                renpy.redraw(self, 0)
            else:
                self.enforced_state = self.style.prefix

        def unfreeze_state(self):
            """
            Unfreeze the button's display
            """
            self.enforced_state = None
            renpy.redraw(self, 0)

        def get_child(self):
            """
            Internal function of ImageButton overloaded to provide the expected capabilities of this button
            """
            if self.enforced_state:
                raw_child = self.state_children[self.enforced_state + '_']

                if raw_child is not self.enforced_imagebutton_raw_child:
                    self.enforced_imagebutton_raw_child = raw_child

                    if raw_child._duplicatable:
                        self.enforced_imagebutton_child = raw_child._duplicate(None)
                        self.enforced_imagebutton_child._unique()
                    else:
                        self.enforced_imagebutton_child = raw_child

                    self.enforced_imagebutton_child.per_interact()
                return self.enforced_imagebutton_child
            else:
                return super(ManageableImageButton, self).get_child()
