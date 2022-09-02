screen chap6_sprite_cutter(next_label, fail_label):
    default game = ImageCutter(images = [
                { 'list': {
                    i*15: "images/items/citruses/Agr" + str(f) + "_" + str(i*15) + ".png" for i in range(6)
                }} for f in range(1, 6)],
                min_opaque_pixels = 80,
                completion_action = Jump(next_label),
                missed_action = Jump(fail_label),
                # TODO: add cutting_sound parameter
                )
    add game
