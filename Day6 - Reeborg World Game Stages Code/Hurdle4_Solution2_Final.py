def turn_right():
    turn_left()
    turn_left()
    turn_left()

def do_this():
    turn_left()
	
    while wall_on_right():
        move()
	
	turn_right()
	move()
	turn_right()
	
	while front_is_clear():
	move()
	
	turn_left()

while not at_goal():
    if wall_in_front():
        do_this()
    else:
        move()