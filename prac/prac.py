import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pendown()
for i in range(36):
    t.forward(100)
    t.backward(100)
    t.left(10)
turtle.done()
