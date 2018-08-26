import turtle

ttl = turtle.Turtle()
width = 400
height = 400

def draw_circle(ttl,x,y,r,color):
    #ttl.begin_fill()
    ttl.penup()
    ttl.goto(x,y-r)
    ttl.pendown()
    ttl.pencolor(color)
    ttl.circle(r,360)
    #ttl.fillcolor(color)
    #ttl.end_fill()

scr = turtle.Screen()
scr.setup(width,height)
for i in range(6,0,-1):
    radius = i*20
    draw_circle(ttl,0,0,radius,"red")
scr.exitonclick()
