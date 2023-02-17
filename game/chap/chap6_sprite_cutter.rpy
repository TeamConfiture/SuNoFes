screen chap6_sprite_cutter(next_label, fail_label):
    default succeeded = 0
    timer 0.5: # Delay before screen change on success
        repeat True
        action If(succeeded > 0, true = If(succeeded > 7, Jump(next_label), false = SetScreenVariable('succeeded', succeeded + 1)))
    default game = ImageCutter(images = [
        { 'list': {
            i*15: "images/items/citruses/Agr" + str(f) + "_" + str(i*15) + ".png" for i in range(6)
        }} for f in range(1, 6)],
        min_opaque_pixels = 80,
        completion_action = SetScreenVariable('succeeded', 1),
        missed_action = Jump(fail_label),
        cutting_action = Play('sound', renpy.random.choice(sound.Cut_Fruit)),
        time_factor = image_cutter_time_factor,
        )
    add game
