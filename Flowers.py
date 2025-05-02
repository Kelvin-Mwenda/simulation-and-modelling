import turtle as t
import random


def rand_colors():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


def drawflower():

    # Define minimum and maximum size ranges for the flower
    min_size = 0.14  # Minimum size factor
    max_size = 0.15  # Maximum size factor
    # Random size factor for the flower within the specified range
    size_factor = random.random() * (max_size - min_size) + min_size

    # Set initial position
    t.penup()
    t.left(180)
    t.fd(1150 * size_factor)
    t.pendown()
    t.right(180)

    # flower base
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.circle(10 * size_factor, 180)
    t.circle(25 * size_factor, 110)
    t.left(50)
    t.circle(60 * size_factor, 45)
    t.circle(20 * size_factor, 170)
    t.right(24)
    t.fd(30 * size_factor)
    t.left(10)
    t.circle(30 * size_factor, 110)
    t.fd(20 * size_factor)
    t.left(40)
    t.circle(90 * size_factor, 70)
    t.circle(30 * size_factor, 150)
    t.right(30)
    t.fd(15 * size_factor)
    t.circle(80 * size_factor, 90)
    t.left(15)
    t.fd(45 * size_factor)
    t.right(165)
    t.fd(20 * size_factor)
    t.left(155)
    t.circle(150 * size_factor, 80)
    t.left(50)
    t.circle(150 * size_factor, 90)
    t.end_fill()

    # Petal 1
    t.left(150)
    t.circle(-90 * size_factor, 70)
    t.left(20)
    t.circle(75 * size_factor, 105)
    t.setheading(60)
    t.circle(80 * size_factor, 98)
    t.circle(-90 * size_factor, 40)

    # Petal 2
    t.left(180)
    t.circle(90 * size_factor, 40)
    t.circle(-80 * size_factor, 98)
    t.setheading(-83)

    # Leaves 1
    t.fd(30 * size_factor)
    t.left(90)
    t.fd(25 * size_factor)
    t.left(45)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(-80 * size_factor, 90)
    t.right(90)
    t.circle(-80 * size_factor, 90)
    t.end_fill()
    t.right(135)
    t.fd(60 * size_factor)
    t.left(180)
    t.fd(85 * size_factor)
    t.left(90)
    t.fd(80 * size_factor)

    # Leaves 2
    t.right(90)
    t.right(45)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(80 * size_factor, 90)
    t.left(90)
    t.circle(80 * size_factor, 90)
    t.end_fill()
    t.left(135)
    t.fd(60 * size_factor)
    t.left(180)
    t.fd(60 * size_factor)
    t.right(90)
    t.circle(200 * size_factor, 60)


def main():
    t.hideturtle()  # Hide the turtle icon while drawing
    t.speed(0)  # Speed up drawing
    t.tracer(1, 0)  # Skip animation of drawing
    t.penup()
    t.goto(750, -230)

    for i in range(6):
        drawflower()
    t.setheading(0)


# Draw the environment first before cars
main()
