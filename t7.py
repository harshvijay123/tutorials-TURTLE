import turtle
from math import *
h=turtle.Turtle()
h.speed(100)
h.turtlesize(0.01)
size=20
h.color('blue','yellow')
h.begin_fill()



def f(size):
    
    if size>200:
        return
    else:
        
        for i in range(4):
            h.begin_fill()
            h.forward(size)
            h.left(90)

        h.end_fill()
        
        f(size+10)

f(size)
h.end_fill()
turtle.done()
