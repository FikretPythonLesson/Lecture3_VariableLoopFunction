import turtle

def square():
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)

square()
turtle.penup()
turtle.forward(75)
turtle.pendown()

square()
turtle.penup()
turtle.forward(75)
turtle.pendown()

square()
turtle.penup()
turtle.forward(75)
turtle.pendown()


turtle.done()
