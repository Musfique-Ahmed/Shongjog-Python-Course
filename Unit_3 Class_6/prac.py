# import turtle

# t = turtle.Turtle()
# for _ in range(4):  # Loop 4 times
#     t.forward(100)
#     t.right(90)  # Turn 90 degrees

# turtle.done()
import turtle


turtle.speed(1)
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
for _ in range(6):
    turtle.forward(100)
    turtle.right(60)

turtle.end_fill()

turtle.done()