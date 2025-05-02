import turtle as t
import random
import Flowers as rose
import Truck as truck
import Suv as sv
import vehicles as v
import tkinter as tk


def rand_colors():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


def drawCar():
    t.hideturtle()
    t.speed(0)

    # Define minimum and maximum size ranges for the car
    a = 0.5  # Minimum size factor
    b = 1.5  # Maximum size factor
    u = random.random()
    # Random size factor for the car within the specified range
    size_factor = a + (u * (b - a))

    # Draw rectangle representing car body
    t.penup()
    t.goto(-200 * size_factor, -50 * size_factor)
    t.pendown()
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.forward(400 * size_factor)
    t.left(90)
    t.forward(50 * size_factor)
    t.left(90)
    t.forward(400 * size_factor)
    t.left(90)
    t.forward(50 * size_factor)
    t.end_fill()
    t.penup()

    # Draw outer trapezium
    t.goto(-150 * size_factor, 0)
    t.setheading(0)
    t.fillcolor(rand_colors())
    t.begin_fill()
    t.pendown()
    t.left(40)
    t.forward(80 * size_factor)
    t.setheading(0)
    t.forward(150 * size_factor)
    t.right(40)
    t.forward(80 * size_factor)
    t.end_fill()

    # Draw left inner trapezium
    t.fillcolor("grey")
    t.begin_fill()
    t.penup()
    t.goto(-130 * size_factor, 5 * size_factor)
    t.setheading(0)
    t.pendown()
    t.left(40)
    t.forward(60 * size_factor)
    t.setheading(0)
    t.forward(70 * size_factor)
    t.right(90)
    t.forward(40 * size_factor)
    t.right(90)
    t.forward(117 * size_factor)
    t.end_fill()

    t.penup()
    t.backward(117 * size_factor)
    t.left(90)
    t.backward(40 * size_factor)
    t.setheading(0)
    t.forward(10 * size_factor)
    t.pendown()

    # Draw right inner trapezium
    t.fillcolor("grey")
    t.begin_fill()
    t.forward(60 * size_factor)
    t.right(40)
    t.forward(61 * size_factor)
    t.setheading(180)
    t.forward(108 * size_factor)
    t.right(90)
    t.forward(41 * size_factor)
    t.end_fill()

    # Draw outer back tire
    t.penup()
    t.goto(-120 * size_factor, -75 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(0.0, 0.0, 0.0)
    t.begin_fill()
    t.circle(25 * size_factor)
    t.end_fill()

    # Draw inner back tire
    t.penup()
    t.goto(-120 * size_factor, -65 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(15 * size_factor)
    t.end_fill()

    # Draw front outer tire
    t.penup()
    t.goto(120 * size_factor, -75 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(0.0, 0.0, 0.0)
    t.begin_fill()
    t.circle(25 * size_factor)
    t.end_fill()

    # Draw front inner tire
    t.penup()
    t.goto(120 * size_factor, -65 * size_factor)
    t.setheading(0)
    t.pendown()
    t.fillcolor("grey")
    t.begin_fill()
    t.circle(15 * size_factor)
    t.end_fill()


def open_suv():

    t.title("Simulation and Modeling")
    t.clearscreen()
    sv.main()


def open_truck():

    t.title("Simulation and Modeling")
    t.clearscreen()
    truck.main()


def open_car():

    t.title("Simulation and Modeling")
    t.clearscreen()
    rose.main()
    main()


def main():
    t.setup(width=1280, height=650, startx=0, starty=0)
    screen = t.Screen()

    drawCar()
    canvas = screen.getcanvas()

    Car_button = tk.Button(
        canvas.master, text="CAR", command=open_car, bg="lightblue", fg="black"
    )
    Suv_button = tk.Button(
        canvas.master, text="SUV", command=open_suv, bg="lightgreen", fg="black"
    )
    Truck_button = tk.Button(
        canvas.master, text="TRUCK", command=open_truck, bg="lightcoral", fg="black"
    )

    Car_button.pack()
    Car_button.place(x=10, y=10)

    Suv_button.pack()
    Suv_button.place(x=50, y=10)

    Truck_button.pack()
    Truck_button.place(x=90, y=10)

    car = v.Car("BMW", 2001, 70000, 15000.0, 4)
    boldfont = ("Arial", 14, "bold")  # Font used for writing on screen
    regfont = ("Cambri", 12, "normal")  # Regular font

    t.penup()
    t.goto(-100, 290)
    t.right(90)
    t.color("blue")  # Set text color to blue
    t.write("USED CAR INVENTORY", font=boldfont)

    t.goto(-200, 280)
    t.color("black")  # Set text color to black
    t.write(
        "==========================================================================="
    )

    t.goto(-200, 260)
    t.color("red")  # Set text color to red
    t.write("Make", font=boldfont)
    t.goto(-200, 240)
    t.color("green")  # Set text color to green
    t.write(f"{car.get_make()}", font=regfont)
    t.goto(-130, 260)
    t.color("red")
    t.write("Model", font=boldfont)
    t.goto(-130, 240)
    t.color("green")
    t.write(f"{car.get_model()}", font=regfont)
    t.goto(-60, 260)
    t.color("red")
    t.write("Mileage", font=boldfont)
    t.goto(-60, 240)
    t.color("green")
    t.write(f"{car.get_mileage()}", font=regfont)
    t.goto(20, 260)
    t.color("red")
    t.write("Price", font=boldfont)
    t.goto(20, 240)
    t.color("green")
    t.write(f"{car.get_price()}", font=regfont)
    t.goto(90, 260)
    t.color("red")
    t.write("Number of doors:", font=boldfont)
    t.goto(150, 240)
    t.color("green")
    t.write(f"{car.get_doors()}", font=regfont)
    t.done()


main()
