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

def drawCircle(x,y,size,r,g,b):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(r, g, b)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def drawLine(x1,y1,x2,y2,r,g,b):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.pencolor(r,g,b)
    t.goto(x2,y2)





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
    drawSquare(x=loc_x,y=loc_y,size=random.randint(20,50),r=random.randint(0,255),g=random.randint(0,255),b=random.randint(0,255))

for i in range(100):
    loc_x = random.randint(0,500)
    loc_y = random.randint(-500,0)
    drawTriangle(x=loc_x,y=loc_y,size=random.randint(20,50),r=random.randint(0,255),g=random.randint(0,255),b=random.randint(0,255))

for i in range(50):
    loc_x = random.randint(-500, 0)
    loc_y = random.randint(0, 500)
    size = random.randint(10,50)
    red = random.randint(0,255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    drawCircle(x=loc_x,y=loc_y,size=size,r=red,g=green,b=blue)

for i in range(100):
    drawLine(x1=random.randint(-500,0),y1=random.randint(-500,0),x2=random.randint(-500,0),y2=random.randint(-500,0),r=random.randint(0,255),g=random.randint(0,255),b=random.randint(0,255))

red = 0
green = 0
blue = 255

start_x = -500
start_y = -500

end_x = -500
end_y = 500

for i in range(100):
    drawLine(start_x,start_y,end_x,end_y,red,green,blue)
    start_y +=10
    end_x += 10



# This is the end of the drawing lab
turtle.update()
turtle.done()
