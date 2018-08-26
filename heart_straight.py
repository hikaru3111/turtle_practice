import turtle
from math import cos,sin,pi

PI=pi

def draw_my_heart(ttl,x,y,radius,alpha=45,theta=210,degrees=0):
    ttl.setheading(degrees)
    ttl.penup()
    ttl.goto(x,y)
    ttl.pendown()

    r = radius
    a = alpha
    t = theta

    straight = r*(-cos((a+90)*PI/180) - cos((t+a-90)*PI/180)) / cos(a*PI/180)

    ttl.left(a)
    ttl.forward(straight)
    ttl.circle(r,t)
    ttl.left(720-2*a-2*t)
    ttl.circle(r,t)
    ttl.forward(straight)

width=700
height=700
x = 0
y = -150
r = 100

scr = turtle.Screen()
scr.title('draw a heart')
scr.setup(width, height, 0, 0)

ttl = turtle.Turtle()

ttl.speed(3)
ttl.shape('turtle')
ttl.screen.screensize(width+100, height+100)

ttl.pencolor('red')
ttl.fillcolor('red')
ttl.pensize(1)

ttl.begin_fill()
draw_my_heart(ttl,x,y,r)
ttl.end_fill()
ttl.hideturtle()
scr.exitonclick()