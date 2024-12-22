import turtle

# set up canvas and turtle
screen = turtle.Screen()  # create the canvas(the worl)
t = turtle.Turtle()   # Create turtle object


for i in range(4):
    t.goto(0, 0)
    t.forward(100)
    t.right(90)

def drawSquare(x,y,size):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)

drawSquare(x=-200,y=200,size=206)


# This is the end of the drawing lab
turtle.done()
