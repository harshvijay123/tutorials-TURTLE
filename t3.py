import turtle
def star(harsh):
   
    harsh.getscreen().bgcolor('black')

    harsh.color('deepskyblue')
    harsh.begin_fill()
    for i in range(5):
        harsh.forward(300)

        
        for i in range(5):
            harsh.forward(200)
            harsh.left(216)  
            
            
        harsh.left(216)
        
    harsh.end_fill()
star(turtle)
turtle.done()
