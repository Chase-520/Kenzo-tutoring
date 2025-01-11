import turtle
import random
# set up canvas and turtle
screen = turtle.Screen()  # create the canvas(the worl)
t = turtle.Turtle()   # Create turtle object
turtle.colormode(255)
#t.speed(0)
turtle.tracer(0)

for i in range(4):
    t.goto(0, 0)
    t.forward(1000)
    t.right(90)

def drawSquare(x,y,size,r,g,b):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(r,g,b)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

#drawSquare(x=-200,y=200,size=206)

def drawTriangle(x,y,size,r,g,b):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(r, g, b)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()


#drawTriangle(100,26,100)
"""
random.random() ---> a random float between 0 and 1
random.randint(min,max)
"""
a = random.randint(0,100)
print(f"the random number is {a}")

for i in range(50):
    loc_x = random.randint(0,500)
    loc_y = random.randint(0,500)
    drawSquare(x=loc_x,y=loc_y,size=50,r=random.randint(0,255),g=random.randint(0,255),b=random.randint(0,255))

for i in range(100):
    loc_x = random.randint(0,500)
    loc_y = random.randint(-500,0)
    drawTriangle(x=loc_x,y=loc_y,size=50,r=random.randint(0,255),g=random.randint(0,255),b=random.randint(0,255))

t.penup()
t.goto(0,0)
t.pendown()
t.circle(50)

t.penup()
t.goto(-100,100)
t.pendown()
t.goto(0,0)

# This is the end of the drawing lab
turtle.update()
turtle.done()
