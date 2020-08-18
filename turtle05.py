import turtle
s = turtle.Turtle()
n = int(input('幾邊'))
for i in range(n):
    s.forward(100)
    s.left(360/n)

