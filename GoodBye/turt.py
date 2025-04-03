import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Function to create a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to create a modern pattern
def modern_pattern():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for _ in range(36):
        t.color(random.choice(colors))
        draw_square(100)
        t.right(10)

# Draw the pattern
modern_pattern()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()