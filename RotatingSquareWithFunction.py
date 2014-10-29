import turtle

turtle.speed(0)
turtle.begin_fill()

def drawSquare(sideLength, penColor, fillColor):
    turtle.color(penColor, fillColor)
    turtle.forward(sideLength)
    turtle.left(90)
    turtle.forward(sideLength)
    turtle.left(90)
    turtle.forward(sideLength)
    turtle.left(90)
    turtle.forward(sideLength)
    turtle.left(90)

def moveForward(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()

def rotate(angle):
    turtle.left(angle)

for _ in range(12):
    drawSquare(50, "red", "yellow")
    moveForward(70)
    rotate(30)

turtle.end_fill()
turtle.done()
