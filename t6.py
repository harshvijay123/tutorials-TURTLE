import turtle
h=turtle.Turtle()
h.speed(1000)
for k in range(1,5):
    for i in range(1,40):
        for j in range(1,5):
            h.forward(10)
            h.left(90)
        h.penup()
        h.forward(10)
        h.pendown()
    h.right(90)


turtle.done()
