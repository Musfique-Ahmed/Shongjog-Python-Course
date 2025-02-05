import turtle

t = turtle.Turtle()

t.speed(0)

for i in range(1000):
    t.forward(i*2)
    t.right(91)

turtle.done()