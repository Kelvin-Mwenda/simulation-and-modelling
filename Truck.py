import turtle as t
import random
import vehicles as v
import Flowers as rose


def rand_colors():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


def drawTruck():
    t.hideturtle()
    t.speed(0)

    # Define minimum and maximum size ranges for the car
    min_size = 0.5  # Minimum size factor
    max_size = 1.5  # Maximum size factor
    # Random size factor for the car within the specified range
    size_factor = random.random() * (max_size - min_size) + min_size

    # Draw rectangle representing car body
    t.penup()
    t.goto(-200 * size_factor, -50 * size_factor)
    t.pendown()
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.forward(400 * size_factor)
    t.left(90)
    t.forward(200 * size_factor)
    t.left(90)
    t.forward(400 * size_factor)
    t.left(90)
    t.forward(200 * size_factor)
    t.end_fill()
    t.penup()

    # Draw outer trapezium representing the front part
    t.goto(200 * size_factor, 100 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.forward(100 * size_factor)
    t.right(55)
    t.forward(183 * size_factor)
    t.setheading(180)
    t.forward(204 * size_factor)
    t.end_fill()

    # Draw inner trapezium for front part
    t.penup()
    t.goto(210 * size_factor, 90 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.forward(80 * size_factor)
    t.right(55)
    t.forward(83 * size_factor)
    t.setheading(180)
    t.forward(128 * size_factor)
    t.right(90)
    t.forward(69 * size_factor)
    t.end_fill()

    # Draw outer back tire
    t.penup()
    t.goto(-130 * size_factor, -90 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(0.0, 0.0, 0.0)
    t.begin_fill()
    t.circle(40 * size_factor)
    t.end_fill()

    # Draw inner back tire
    t.penup()
    t.goto(-130 * size_factor, -75 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(25 * size_factor)
    t.end_fill()

    # Draw front outer tire
    t.penup()
    t.goto(280 * size_factor, -90 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(0.0, 0.0, 0.0)
    t.begin_fill()
    t.circle(40 * size_factor)
    t.end_fill()

    # Draw front inner tire
    t.penup()
    t.goto(280 * size_factor, -75 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(25 * size_factor)
    t.end_fill()


def main():
    t.setup(width=1280, height=650, startx=0, starty=0)
    rose.main()

    drawTruck()

    # Create a Truck object for a used 2002
    # Toyota pickup with 40 000 miles, priced
    # at $12, 000, with a 4-wheel drive.
    truck = v.Truck("Toyota", 2002, 40000, 12000.0, "4WD")

    # Writing the text on screen for details about the BMW
    boldfont = ("Arial", 14, "bold")  # Font used for writing on screen
    regfont = ("Cambri", 12, "normal")  # Regular font

    t.penup()
    t.goto(-100, 290)
    t.right(90)
    t.write("USED CAR INVENTORY", font=boldfont)

    t.goto(-200, 280)
    t.write(
        "==========================================================================="
    )

    t.goto(-200, 260)
    t.write("Make", font=boldfont)
    t.goto(-200, 240)
    t.write(f"{truck.get_make()}", font=regfont)
    t.goto(-130, 260)
    t.write("Model", font=boldfont)
    t.goto(-130, 240)
    t.write(f"{truck.get_model()}", font=regfont)
    t.goto(-60, 260)
    t.write("Mileage", font=boldfont)
    t.goto(-60, 240)
    t.write(f"{truck.get_mileage()}", font=regfont)
    t.goto(20, 260)
    t.write("Price", font=boldfont)
    t.goto(20, 240)
    t.write(f"{truck.get_price()}", font=regfont)
    t.goto(90, 260)
    t.write("Drive type", font=boldfont)
    t.goto(100, 240)
    t.write(f"{truck.get_drive_type()}", font=regfont)
    t.done()
