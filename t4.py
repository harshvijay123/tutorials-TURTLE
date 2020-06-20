import turtle
def star(t,size):
    t.getscreen().bgcolor('black')
    t.color('cyan')
    t.begin_fill()
    t.speed(1000)

        
    if size<=10:
        return
    else:
        
        for i in range(5):
            t.forward(size)
            star(t,size/3)
            t.left(216)
    t.end_fill()


        
star(turtle,300)
