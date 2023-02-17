
init python:
    import math

# Tutorial

transform tutorial_button_blink:
    alpha 1
    pause 0.5
    ease 0.5 alpha 0.8
    ease 0.5 alpha 1
    ease 0.5 alpha 0.8
    ease 0.5 alpha 1
    pause 0.5
    ease 0.3 alpha 0.2
    ease 0.3 alpha 1
    ease 0.3 alpha 0.2
    ease 0.3 alpha 1
    repeat

# lake transform - Fish 1
transform lake_wavy_patrol(child, xrange, yrange, image_width, speed_factor = 1):
    child
    parallel: # up-down motion
        yoffset 0
        yzoom 1
        easein speed_factor yoffset -yrange
        yzoom -1
        easein speed_factor yoffset 0
        repeat
    parallel: # left-right motion with flip-aroung
        xzoom -1
        xoffset 0
        linear speed_factor * 10 xoffset xrange
        linear speed_factor * 0.3:
            xzoom 0
            xoffset xrange + image_width / 2
        linear speed_factor * 0.3:
            xzoom 1
            xoffset xrange
        linear speed_factor * 10 xoffset 0
        linear speed_factor * 0.3:
            xzoom 0
            xoffset image_width / 2
        linear speed_factor * 0.3:
            xzoom -1
            xoffset 0
        repeat
# lake transform - Fish 2
transform lake_love_patrol(child, heart_height, heart_width, speed_factor = 1, initial_delay = 0):
    child
    xzoom -1
    rotate -90
    xoffset 0
    yoffset 0
    pause initial_delay
    parallel: # x offset
        easeout speed_factor xoffset heart_width/4
        easein speed_factor xoffset heart_width/2
        easeout speed_factor * 1.5 xoffset 0
        easein speed_factor * 1.5 xoffset -heart_width/2
        easeout speed_factor xoffset -heart_width/4
        easein speed_factor xoffset 0
        repeat
    parallel: # y offset
        easein speed_factor yoffset -heart_height/3
        easeout speed_factor yoffset 0
        linear speed_factor * 1.5 yoffset heart_height*2/3
        linear speed_factor * 1.5 yoffset 0
        easein speed_factor yoffset -heart_height/3
        easeout speed_factor yoffset 0
        repeat
    parallel: # rotation
        linear speed_factor rotate 0
        linear speed_factor rotate 90
        easein speed_factor * 1.5 rotate 180-math.degrees(math.atan(heart_height/heart_width))
        rotate -180 + math.degrees(math.atan(heart_height/heart_width))
        easeout speed_factor * 1.5 rotate -90
        linear speed_factor rotate 0
        linear speed_factor rotate 90
        rotate -90
        repeat
    parallel: # swim effect
        pause renpy.random.uniform(0.2, 0.9) * speed_factor
        yzoom 1
        pause renpy.random.uniform(0.2, 0.9) * speed_factor
        yzoom -1
        repeat
# lake transform - Rainbow Fish
transform lake_rainbow_patrol(child, speed_factor = 1):
    child
    xoffset 0
    yoffset 0
    parallel:
        yzoom 1
        pause 0.5
        yzoom -1
        pause 0.5
        repeat
    parallel:
        # Bottom left to top right
        xoffset 0
        yoffset 800
        rotate -20
        linear 1:
            xoffset 180
            yoffset 560
        pause 1
        parallel:
            linear 3:
                xoffset 1200
                rotate -70
        parallel:
            easeout 3:
                yoffset -300
        pause 0.5
        # Right to left
        xoffset 1500
        yoffset 180
        rotate 180
        linear 1 xoffset 1400
        pause 1.5
        parallel:
            linear 3:
                xoffset -200
                rotate 200
        parallel:
            easeout 3 yoffset -100
        pause 0.5
        # Top left to bottom left
        xoffset 400
        yoffset -300
        rotate 70
        linear 1 yoffset -185
        pause 1
        parallel:
            linear 3:
                yoffset 1200
                rotate 130
        parallel:
            ease 3 xoffset -50
        pause 0.5
        repeat

# Cheese cupboard transform
# Used to rotate sprites by an arbitrary angle
transform cheese_cupboard_angle(child, angle):
    child
    rotate angle

# Used to show the current expected cheese and animate it
transform cheese_cupboard_entrance(child, scale = 1., xalign = 0.5, yalign = 0.5):
    child
    xalign xalign
    yalign yalign
    xzoom scale
    yzoom scale
    rotate 0
    yoffset -200
    easein 1 yoffset 0
    pause 6
    parallel: # animate every once in a while
        linear 0.2 rotate 15
        linear 0.2 rotate -15
        linear 0.2 rotate 15
        linear 0.2 rotate -15
        linear 0.2 rotate 15
        linear 0.2 rotate -15
        linear 0.2 rotate 15
        easein 0.2 rotate 0
        pause renpy.random.randint(8, 12)
        repeat

transform cheese_cupboard_basket(child, scale = 1., xalign = 0.5, yalign = 0.5):
    child
    xalign xalign
    yalign yalign
    xzoom scale
    yzoom scale
    rotate 0
    pause 1.5
    parallel: # animate every once in a while
        ease 0.4 rotate 10
        ease 0.4 rotate -10
        ease 0.4 rotate 10
        ease 0.4 rotate 0
        pause renpy.random.randint(40, 80)
        repeat

# Used to make a validated cheese disappear
transform cheese_cupboard_exit(child, scale = 1., xalign = 0.5, yalign = 0.5):
    child
    xalign xalign
    yalign yalign
    xzoom scale
    yzoom scale
    parallel:
        linear 1:
            alpha 0
            zoom 0
            rotate 1000
