import turtle
h=turtle.Turtle()


h.speed(10)
h.turtlesize(0.01)
h.color('blue','yellow')
h.begin_fill()

for j in range(0,101,10):
    for i in range(4):
        h.color((255,0,255),(255,0,0))
        
    
    
        h.forward(100+j)
        h.left(90)
h.end_fill()


turtle.done()
