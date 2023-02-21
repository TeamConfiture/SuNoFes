
screen tutorial_button(prompt):
    text prompt align (0.5, 0.03) size 50
    imagebutton at tutorial_button_blink:
        auto "tutorial_button_%s"
        pos (230, 580)
        action [With(dissolve), Return()]

init python:
    def tutorial_dragdrop_dragged_handler(drags, drop):
        if drop:
            # Manually ensure that images' bytes overlap
            # This is done by sampling the overlapping area and is
            # not 100% accurate but sufficient in most cases
            drag = drags[0]
            drag_render = drag.render(drag.w, drag.h, 0, drag.at)
            drop_render = drop.render(drop.w, drop.h, 0, drop.at)
            drag_pos = drag.get_placement()
            drop_pos = drop.get_placement()
            common_pos = (max(drag_pos[0], drop_pos[0]), max(drag_pos[1], drop_pos[1]))
            common_width = (
                min(drag_pos[0] + drag_render.get_size()[0], drop_pos[0] + drop_render.get_size()[0]) - common_pos[0],
                min(drag_pos[1] + drag_render.get_size()[1], drop_pos[1] + drop_render.get_size()[1]) - common_pos[1],
                )
            is_overlapping = False
            for i in range(100):
                x_f = (i%10)/10
                y_f = math.floor(i/10)/10
                drag_projection = (
                    common_pos[0] + common_width[0] * x_f - drag_pos[0],
                    common_pos[1] + common_width[1] * y_f - drag_pos[1],
                )
                drop_projection = (
                    common_pos[0] + common_width[0] * x_f - drop_pos[0],
                    common_pos[1] + common_width[1] * y_f - drop_pos[1],
                )
                if drag_render.is_pixel_opaque(*drag_projection) and drop_render.is_pixel_opaque(*drop_projection):
                    is_overlapping = True
                    break
            if is_overlapping:
                renpy.run(SetScreenVariable('boot_collected', True))

screen tutorial_dragdrop(prompt):
    default boot_collected = False
    text prompt align (0.5, 0.03) size 50
    timer 0.2 repeat True action If(boot_collected, [With(dissolve), Return()])
    draggroup:
        if not boot_collected:
            drag:
                child "tutorial_boot"
                align (0.482, 0.04)
                focus_mask True
                droppable False
                dragged tutorial_dragdrop_dragged_handler
        drag:
            child "tutorial_basket"
            align (0.24, 0.545)
            draggable False
