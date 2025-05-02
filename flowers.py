import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
turtle.tracer(0)  # Disable auto-screen updates for smooth animation

# Function to draw a petal with animation
def draw_petal(color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(40, 60)
        t.left(120)
        t.circle(40, 60)
        t.left(120)
        turtle.update()  # Update the screen to show gradual animation
        time.sleep(0.1)  # Small delay for effect
    t.end_fill()

# Function to draw a flower with animation
def draw_flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    petal_colors = ["red", "blue", "yellow", "purple", "orange"]
    
    # Animated petals
    for _ in range(6):
        draw_petal(random.choice(petal_colors))
        t.right(60)
    
    # Animated center
    t.penup()
    t.goto(x, y - 15)
    t.pendown()
    t.fillcolor(random.choice(["brown", "black", "pink"]))
    t.begin_fill()
    for _ in range(36):  # Circle grows in steps
        t.circle(15, 10)
        turtle.update()
        time.sleep(0.05)
    t.end_fill()

# Draw multiple flowers at random locations
for _ in range(5):
    x, y = random.randint(-200, 200), random.randint(-200, 200)
    draw_flower(x, y)

t.hideturtle()
turtle.done()
