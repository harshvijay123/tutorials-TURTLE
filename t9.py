import turtle


harsh=turtle.Turtle()
shiv=turtle.Turtle()
abhi=turtle.Turtle()
ayu=turtle.Turtle()

x=30
a=90



harsh.color('blue')
shiv.color('green')

shiv.begin_fill()
#harsh.begin_fill()

abhi.color('red')
ayu.color('yellow')


'''harsh.forward(x)
harsh.left(a)
harsh.forward(x)
harsh.left(a)
harsh.forward(x)
harsh.left(a)
harsh.forward(x)'''

shiv.left(a)
for i in range(4):
    

    
    for j in range(4):
        shiv.forward(x)
        shiv.left(a)
        shiv.forward(x)
        shiv.left(a)
        shiv.forward(x)
        shiv.left(a)
        shiv.forward(x)
        
        harsh.forward(x)
        harsh.left(a)
        harsh.forward(x)
        harsh.left(a)
        harsh.forward(x)
        harsh.left(a)
        harsh.forward(x)
    harsh.forward(2*x)
    shiv.left(a)
    shiv.forward(2*x)
    
    
shiv.end_fill()
harsh.end_fill()    

turtle.done()
