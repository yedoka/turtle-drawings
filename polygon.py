import turtle;
t = turtle.Pen()
t.speed(0)

#Write the code that draws an equilateral polygon with 8 sides. 

t.speed(0)

n = 8;
for i in range(n):
   t.forward(100);
   t.right(360 / n);
t.reset()

#Let's make an equilateral polygon, where the number of sides is defined by a user.
t.speed(0)

n = eval(input("Enter the number of sides: "));
for i in range(n):
    t.forward(100);
    t.right(360 / n);
t.reset()

#How can one imitate a circle 
t.speed(0)

n = 100
t.pu()
t.setpos(0, -150)
t.pd()
t.color('blue', 'yellow')
t.begin_fill()
for _ in range(n):
    t.forward(10)
    t.left(360/n) 
t.end_fill()
t.reset()

#Draw the following figure with 18 angles
t.speed(0)

turtle.bgcolor('white')
t.color('blue', 'yellow')
t.begin_fill()
for i in range(18):
    t.forward(150)
    t.left(100)
t.end_fill()
t.reset()

#Draw a square with green contour and yellow filling. Change the default side width. 
t.speed(0)

t.fillcolor('yellow')
t.pencolor('green')
t.pensize(5)
sideLength = 100
t.begin_fill()
for i in range(4):
    t.forward(sideLength)
    t.left(90)
t.end_fill()
t.reset()

#Draw the following target circles
t.speed(0)

turtle.bgcolor('white')
clr = ['red', 'green']
t.pensize(5)
for i in range(10):
    t.color(clr[i%2])
    t.penup()
    t.right(90)
    t.forward(100-i*10)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.circle(100-i*10)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(100-i*10)
    t.right(90)
    t.pendown()
t.reset()

#Four arrow with changing colors from black to white
t.speed(0)

turtle.colormode(1)
t.pu()
t.fd(-200)
t.pd()
for i in range(4):
    for n in range(10):
        c = n*28/255
        t.pencolor(c,c,c)
        t.fd(10)
t.reset()

#Two squares using functions
t.speed(0)

def square(sideLength):
  for i in range(4):
    t.forward(sideLength)
    t.left(90)

lng = 50
t.penup()
t.setpos(0, -lng)
t.pendown()
square(lng)
t.penup()
t.setpos(-lng, 0)
t.pendown()
square(lng)
t.reset()
    
#Draw chess board
t.speed(0)

def square(sideLength):
  for i in range(4):
    t.forward(sideLength)
    t.right(90)
    
t.pensize(2)
t.penup()
t.setpos(-150, 150)
t.pendown()
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            t.begin_fill()
        square(50)
        t.end_fill()
        t.forward(50)
    t.penup()
    t.setpos(-150, 150-50*(i+1))
    t.pendown()
turtle.done()

