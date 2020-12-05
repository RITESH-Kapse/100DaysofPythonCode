def turn_right():
    turn_left()
    turn_left()
    turn_left()

x = 0

while x < 6:
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    x +=1