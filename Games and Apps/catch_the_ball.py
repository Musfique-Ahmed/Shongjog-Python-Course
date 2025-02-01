"""
Tkinter game: Catch the Ball 🎮

Game Overview:
-> A ball moves randomly across the screen.
-> The player controls a paddle using the left and right arrow keys.
-> The goal is to catch the ball before it hits the bottom!
"""

import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Catch the Ball Game")
root.geometry("500x500")
root.resizable(False, False)

# Canvas for game
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

# Create the paddle
paddle = canvas.create_rectangle(200, 450, 300, 470, fill="white")

# Create the ball
ball = canvas.create_oval(240, 50, 260, 70, fill="red")

# Ball movement variables
ball_dx = random.choice([-3, 3])
ball_dy = 3

# Paddle movement
paddle_speed = 20

def move_paddle(event):
    """Move the paddle left and right within the canvas."""
    x1, _, x2, _ = canvas.coords(paddle)
    if event.keysym == "Left" and x1 > 0:
        canvas.move(paddle, -paddle_speed, 0)
    elif event.keysym == "Right" and x2 < 500:
        canvas.move(paddle, paddle_speed, 0)

# Bind arrow keys to paddle movement
root.bind("<Left>", move_paddle)
root.bind("<Right>", move_paddle)

def move_ball():
    """Move the ball and check for collisions."""
    global ball_dx, ball_dy

    x1, y1, x2, y2 = canvas.coords(ball)

    # Ball bouncing from walls
    if x1 <= 0 or x2 >= 500:
        ball_dx = -ball_dx
    if y1 <= 0:
        ball_dy = -ball_dy

    # Check collision with paddle
    px1, py1, px2, py2 = canvas.coords(paddle)
    if y2 >= py1 and px1 <= x1 <= px2:
        ball_dy = -ball_dy

    # Move the ball
    canvas.move(ball, ball_dx, ball_dy)

    # Game over if ball reaches bottom
    if y2 >= 500:
        canvas.create_text(250, 250, text="Game Over!", font=("Arial", 24), fill="red")
    else:
        root.after(20, move_ball)

# Start the ball movement
move_ball()

# Run the game loop
root.mainloop()
