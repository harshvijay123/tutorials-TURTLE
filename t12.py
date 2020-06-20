import turtle
import random
h=turtle.Turtle()
turtle.bgcolor('yellow')
h.speed(0)
h.turtlesize(0.01)
t='orange','red','pink','cyan','forestgreen','blue','gray','skyblue','black','white','brown','lightgreen','orchid'
for i in range(200):
    h.pu()
    h.goto(random.randint(-650,650),random.randint(-350,350))
    h.pd()
    h.dot(random.randint(10,100),random.choice(t))
    h.write(i)
turtle.done()
