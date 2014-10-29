import turtle

def square():
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)

def move_without_draw(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()
    

square()
move_without_draw(75)

square()
move_without_draw(75)

square()
move_without_draw(75)


turtle.done()
