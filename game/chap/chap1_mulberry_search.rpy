screen chap1_mulberry_search(success_label = None, fail_label = None):
    if fail_label:
        button: # Button that covers the whole background
            action Jump(fail_label)
    imagebutton:
        idle "mulberry"
        xalign 0.97
        yalign 0.2
        if success_label:
            hover "mulberry_button"
            focus_mask True
            action Jump(success_label)
