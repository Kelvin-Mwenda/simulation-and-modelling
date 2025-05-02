import turtle as t
import random
import Flowers as rose
import vehicles as v


def rand_colors():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


def drawSUV():
    # Define minimum and maximum size ranges for the car
    min_size = 0.5  # Minimum size factor
    max_size = 1.5  # Maximum size factor
    # Random size factor for the car within the specified range
    size_factor = random.random() * (max_size - min_size) + min_size

    # Draw rectangle representing suv body
    t.penup()
    t.goto(-200 * size_factor, -50 * size_factor)
    t.pendown()
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.forward(400 * size_factor)
    t.left(90)
    t.forward(60 * size_factor)
    t.left(90)
    t.forward(400 * size_factor)
    t.left(90)
    t.forward(60 * size_factor)
    t.end_fill()
    t.penup()

    # Draw boot tire
    t.goto(-200 * size_factor, 0)
    t.pendown()
    t.setheading(180)
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.circle(20 * size_factor, 180)
    t.end_fill()
    t.penup()

    # Draw outer trapezium
    t.goto(-200 * size_factor, 10 * size_factor)
    t.setheading(0)
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.pendown()
    t.left(40)
    t.forward(80 * size_factor)
    t.setheading(0)
    t.forward(200 * size_factor)
    t.right(40)
    t.forward(80 * size_factor)
    t.end_fill()

    # Draw left inner trapeziuum
    t.fillcolor("grey")
    t.begin_fill()
    t.penup()
    t.goto(-180 * size_factor, 15 * size_factor)
    t.setheading(0)
    t.pendown()
    t.left(40)
    t.forward(60 * size_factor)
    t.setheading(0)
    t.forward(100 * size_factor)
    t.right(90)
    t.forward(40 * size_factor)
    t.right(90)
    t.forward(147 * size_factor)
    t.end_fill()

    t.penup()
    t.backward(147 * size_factor)
    t.left(90)
    t.backward(40 * size_factor)
    t.setheading(0)
    t.forward(10 * size_factor)
    t.pendown()

    # Draw right inner trapezium
    t.fillcolor("grey")
    t.begin_fill()
    t.forward(80 * size_factor)
    t.right(40)
    t.forward(60 * size_factor)
    t.setheading(180)
    t.forward(127 * size_factor)
    t.right(90)
    t.forward(40 * size_factor)
    t.end_fill()

    # Draw outer back tire
    t.penup()
    t.goto(-140 * size_factor, -85 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(0.0, 0.0, 0.0)
    t.begin_fill()
    t.circle(25 * size_factor)
    t.end_fill()

    # Draw inner back tire
    t.penup()
    t.goto(-140 * size_factor, -75 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(15 * size_factor)
    t.end_fill()

    # Draw front outer tire
    t.penup()
    t.goto(140 * size_factor, -85 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(0.0, 0.0, 0.0)
    t.begin_fill()
    t.circle(25 * size_factor)
    t.end_fill()

    # Draw front inner tire
    t.penup()
    t.goto(140 * size_factor, -75 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(15 * size_factor)
    t.end_fill()


def main():
    t.setup(width=1280, height=650, startx=0, starty=0)

    rose.main()
    drawSUV()

    # Create an SUV object for a used 2000
    # Volvo with 30, 000 miles, priced
    # at $18,500, with 5 passenger capacity.
    suv = v.SUV("Volvo", 2000, 30000, 18500.0, 5)

    # Writing the text on screen for details about the BMW
    boldfont = ("Arial", 14, "bold")  # Font used for writing on screen
    regfont = ("Cambri", 12, "normal")  # Regular font

    t.penup()
    t.goto(-100, 290)
    t.right(90)
    t.color("blue")  # Set text color to blue
    t.write("USED CAR INVENTORY", font=boldfont)

    t.goto(-200, 280)
    t.write(
        "==========================================================================="
    )

    t.goto(-200, 260)
    t.write("Make", font=boldfont)
    t.goto(-200, 240)
    t.write(f"{suv.get_make()}", font=regfont)
    t.goto(-130, 260)
    t.write("Model", font=boldfont)
    t.goto(-130, 240)
    t.write(f"{suv.get_model()}", font=regfont)
    t.goto(-60, 260)
    t.write("Mileage", font=boldfont)
    t.goto(-60, 240)
    t.write(f"{suv.get_mileage()}", font=regfont)
    t.goto(20, 260)
    t.write("Price", font=boldfont)
    t.goto(20, 240)
    t.write(f"{suv.get_price()}", font=regfont)
    t.goto(90, 260)
    t.write("Passenger Capacity", font=boldfont)
    t.goto(170, 240)
    t.write(f"{suv.get_pass_cap()}", font=regfont)
    t.done()
