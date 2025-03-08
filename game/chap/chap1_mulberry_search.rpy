screen chap1_mulberry_search(success_label = None, fail_label = None):
    if fail_label:
        button: # Button that covers the whole background
            action Jump(fail_label)
    imagebutton:
        xalign 0.97
        yalign 0.2
        if success_label:
            idle "mulberry_blinking"
            hover "mulberry_button"
            focus_mask True
            action [Play('sound', renpy.random.choice(sound.Paillete)), Jump(success_label)]
        else:
            idle "mulberry"
