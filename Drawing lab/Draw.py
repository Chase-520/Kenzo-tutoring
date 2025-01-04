import turtle
import random
# set up canvas and turtle
screen = turtle.Screen()  # create the canvas(the worl)
t = turtle.Turtle()   # Create turtle object
turtle.colormode(255)
#t.speed(1)
turtle.tracer(0)

for i in range(4):
    t.goto(0, 0)
    t.forward(100)
    t.right(90)

def drawSquare(x,y,size):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(255,0,0)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

drawSquare(x=-200,y=200,size=206)

a = random.random()
print(a)


# This is the end of the drawing lab
turtle.update()
turtle.done()
