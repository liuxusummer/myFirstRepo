# 画五环
from turtle import *
def draw(cl,x,y):
    pencolor(cl)
    penup()
    goto(x,y)
    pendown()
    circle(60)
setup(800,800)
pensize(10)

draw('blue',-150,0)
draw('black',0,0)
draw('red',150,0)
draw('yellow',-75,-50)
draw('green',75,-50)
done()
