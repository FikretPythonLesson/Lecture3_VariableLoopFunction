import turtle
turtle.speed(0)
turtle.bgcolor("yellow")
turtle.color("blue", "red")
turtle.pensize(1)
turtle.begin_fill()

for i in range(30):
    if i <= 10:
        k = i * 10
    else:
        k = 0
        
    turtle.left(12)
    turtle.forward(100 + k)
    turtle.left(90)
    turtle.forward(100 + k)
    turtle.left(90)
    turtle.forward(100 + k)
    turtle.left(90)
    turtle.forward(100 + k)
    turtle.left(90)

turtle.end_fill()

turtle.done()
