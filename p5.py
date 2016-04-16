import turtle, math, random

def poly(t,n,d):
    for i in range(n):
        t.forward(d)
        t.left(360/n)

def newf(t,m):
    for j in range(m):
        n = random.randint(3,7)
        d = random.randint(10,50)
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        t.up()
        t.goto(x,y)
        t.down()
        poly(t,n,d)
    
#-----------------------
t = turtle.Turtle()
t.color("red")

newf(t,10)

