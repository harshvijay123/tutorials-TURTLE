import turtle
import math
bob=turtle.Turtle()
bob.hideturtle()

bob.getscreen().bgcolor('yellow')
bob.color('blue','cyan')
bob.begin_fill()
bob.speed(10)

  
for i in range(0,80):
    #bob.left(10)
    bob.forward(300)
    bob.left(175)



bob.end_fill()
turtle.done()
