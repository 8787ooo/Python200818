import turtle
turtle.shape('turtle')
turtle.penup()
s = 20
for i in range(30):
    turtle.stamp()
    s+=3
    turtle.forward(s)
    turtle.right(24)
turtle.done()

