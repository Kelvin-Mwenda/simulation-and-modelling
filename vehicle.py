import tkinter as tk
from turtle import TurtleScreen, RawTurtle
import random

# Define vehicle data with fixed details
vehicles = [
    {"type": "car", "make": "Toyota", "model": "Corolla", "mileage": 50000, "price": 15000},
    {"type": "SUV", "make": "Ford", "model": "Explorer", "mileage": 30000, "price": 25000},
    {"type": "truck", "make": "Chevrolet", "model": "Silverado", "mileage": 40000, "price": 30000},
]

# Generate random dimensions and colors for each vehicle
for vehicle in vehicles:
    if vehicle["type"] == "car":
        vehicle["length"] = random.uniform(100, 150)
        vehicle["width"] = random.uniform(50, 70)
        vehicle["height"] = random.uniform(30, 40)
    elif vehicle["type"] == "SUV":
        vehicle["length"] = random.uniform(120, 180)
        vehicle["width"] = random.uniform(60, 80)
        vehicle["height"] = random.uniform(40, 50)
    elif vehicle["type"] == "truck":
        vehicle["length"] = random.uniform(150, 200)
        vehicle["width"] = random.uniform(70, 90)
        vehicle["height"] = random.uniform(50, 60)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    vehicle["color"] = (r / 255.0, g / 255.0, b / 255.0)

# Set up Tkinter window
root = tk.Tk()
root.title("Used Car Inventory")

# Create frame for vehicle details
details_frame = tk.Frame(root)
details_frame.pack(side=tk.TOP)

# Create labels for vehicle details
make_label = tk.Label(details_frame, text="Make: ")
make_label.grid(row=0, column=0)
model_label = tk.Label(details_frame, text="Model: ")
model_label.grid(row=0, column=1)
mileage_label = tk.Label(details_frame, text="Mileage: ")
mileage_label.grid(row=0, column=2)
price_label = tk.Label(details_frame, text="Price: ")
price_label.grid(row=0, column=3)

# Create canvas for Turtle graphics
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Initialize TurtleScreen and turtle
screen = TurtleScreen(canvas)
screen.tracer(0)  # Disable animation for faster rendering
turtle = RawTurtle(screen)
turtle.speed(0)  # Fastest drawing speed

# Create frame for navigation buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM)

# Create navigation buttons
button_car = tk.Button(button_frame, text="Car", command=lambda: switch_vehicle(0))
button_car.pack(side=tk.LEFT)
button_suv = tk.Button(button_frame, text="SUV", command=lambda: switch_vehicle(1))
button_suv.pack(side=tk.LEFT)
button_truck = tk.Button(button_frame, text="Truck", command=lambda: switch_vehicle(2))
button_truck.pack(side=tk.LEFT)

# Initialize current vehicle index
current_vehicle = 0

# Function to switch between vehicles
def switch_vehicle(index):
    global current_vehicle
    current_vehicle = index
    update_display()

# Function to update the display
def update_display():
    vehicle = vehicles[current_vehicle]
    # Update labels with vehicle details
    make_label.config(text="Make: " + vehicle["make"])
    model_label.config(text="Model: " + vehicle["model"])
    mileage_label.config(text="Mileage: " + str(vehicle["mileage"]))
    price_label.config(text="Price: $" + str(vehicle["price"]))
    # Clear previous drawings
    turtle.clear()
    # Draw the new vehicle
    draw_vehicle(vehicle)
    # Update the screen
    screen.update()

# Function to project 3D points to 2D
def project(point, f):
    x, y, z = point
    if z == 0:
        z = 0.001  # Avoid division by zero
    xp = x * f / z
    yp = y * f / z
    return (xp, yp)

# Function to draw a face of the vehicle
def draw_face(points, indices, color):
    turtle.fillcolor(color)
    first = indices[0]
    xp, yp = project(points[first], f)
    turtle.penup()
    turtle.goto(xp + offset_x, yp + offset_y)
    turtle.pendown()
    turtle.begin_fill()
    for i in indices[1:] + [first]:
        xp, yp = project(points[i], f)
        turtle.goto(xp + offset_x, yp + offset_y)
    turtle.end_fill()

# Function to draw the vehicle and flowers
def draw_vehicle(vehicle):
    length = vehicle["length"]
    width = vehicle["width"]
    height = vehicle["height"]
    color = vehicle["color"]
    z_front = 100
    f = 200
    z_back = z_front + length
    # Define 3D points for the vehicle (rectangular prism)
    points = [
        (-width / 2, 0, z_front),  # Front bottom left
        (width / 2, 0, z_front),   # Front bottom right
        (-width / 2, height, z_front),  # Front top left
        (width / 2, height, z_front),   # Front top right
        (-width / 2, 0, z_back),   # Back bottom left
        (width / 2, 0, z_back),    # Back bottom right
        (-width / 2, height, z_back),  # Back top left
        (width / 2, height, z_back),   # Back top right
    ]
    # Define faces to draw
    faces = [
        [4, 5, 7, 6],  # Back
        [0, 4, 6, 2],  # Left
        [1, 5, 7, 3],  # Right
        [2, 3, 7, 6],  # Top
        [0, 1, 3, 2],  # Front
    ]
    # Draw each face
    for face in faces:
        draw_face(points, face, color)
    # Draw six flowers around the vehicle
    for _ in range(6):
        x_f = random.uniform(-100, 100)
        z_f = random.uniform(z_front - 50, z_back + 50)
        y_f = 0
        xp, yp = project((x_f, y_f, z_f), f)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        flower_color = (r / 255.0, g / 255.0, b / 255.0)
        draw_flower(xp + offset_x, yp + offset_y, flower_color)

# Function to draw a flower
def draw_flower(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # Draw yellow center
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    # Draw five petals
    petal_color = color
    turtle.setheading(0)
    for _ in range(5):
        turtle.forward(10)
        turtle.fillcolor(petal_color)
        turtle.begin_fill()
        turtle.circle(3)
        turtle.end_fill()
        turtle.backward(10)
        turtle.left(72)

# Define projection parameters
f = 200
offset_x = 0
offset_y = -200

# Display initial vehicle
update_display()

# Start Tkinter main loop
root.mainloop()