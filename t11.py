import turtle
import time


h=turtle.Turtle()
h.shape('square')
h.turtlesize(4)
clock=time.Clock()
for i in range(4):
    h.clear()
    h.forward(4)
    clock.tick(60)

turtle.done()
