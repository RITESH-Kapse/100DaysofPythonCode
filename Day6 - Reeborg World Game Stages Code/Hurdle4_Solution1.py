def turn_right():
    turn_left()
    turn_left()
    turn_left()

def do_this():
    turn_left()
    while front_is_clear() and wall_on_right():
        move()
    while right_is_clear():
        turn_right()
        move()
        
while not at_goal():
    if wall_in_front():
        do_this()
    else:
        move()
