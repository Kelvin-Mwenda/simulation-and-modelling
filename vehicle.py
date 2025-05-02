import turtle
import random
import math

# Screen setup
screen = turtle.Screen()
screen.title("Car Inventory Visualization")
screen.setup(1000, 700)
screen.bgcolor("#87CEEB")  # Sky blue background


# Create ground
def draw_ground():
    ground = turtle.Turtle()
    ground.speed(0)
    ground.penup()
    ground.hideturtle()
    ground.goto(-500, -150)
    ground.pendown()
    ground.fillcolor("#8B4513")  # Brown color for ground
    ground.begin_fill()
    for _ in range(2):
        ground.forward(1000)
        ground.right(90)
        ground.forward(250)
        ground.right(90)
    ground.end_fill()


# Function to generate random car details
def generate_car_details(vehicle_type):
    makes = {
        "car": [
            "Toyota",
            "Honda",
            "Ford",
            "Chevrolet",
            "Nissan",
            "Mazda",
            "BMW",
            "Mercedes",
        ],
        "suv": [
            "Jeep",
            "Toyota",
            "Ford",
            "Honda",
            "Subaru",
            "Range Rover",
            "BMW",
            "Audi",
        ],
        "truck": [
            "Ford",
            "Chevrolet",
            "Ram",
            "Toyota",
            "GMC",
            "Nissan",
            "Dodge",
            "Hummer",
        ],
    }

    models = {
        "car": [
            "Corolla",
            "Civic",
            "Focus",
            "Malibu",
            "Altima",
            "Mazda3",
            "3 Series",
            "C-Class",
        ],
        "suv": ["Wrangler", "RAV4", "Explorer", "CR-V", "Outback", "Sport", "X5", "Q7"],
        "truck": [
            "F-150",
            "Silverado",
            "1500",
            "Tacoma",
            "Sierra",
            "Titan",
            "Ram",
            "H2",
        ],
    }

    make = random.choice(makes[vehicle_type])
    model = random.choice(models[vehicle_type])
    year = random.randint(2015, 2024)
    mileage = random.randint(5000, 150000)
    price = random.randint(5000, 60000)

    return {
        "make": make,
        "model": model,
        "year": year,
        "mileage": mileage,
        "price": f"${price:,}",
    }


# Function to generate random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"


# Helper function to set turtle position and heading
def setup_turtle(t, x, y, heading=0):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()


# Function to draw a more realistic flower
def draw_flower(x, y, size=30):
    flower = turtle.Turtle()
    flower.speed(0)
    flower.hideturtle()

    # Draw stem
    setup_turtle(flower, x, y - size)
    flower.pensize(3)
    flower.pencolor("green")
    flower.setheading(90)  # Point upward
    flower.forward(size * 2)

    # Save position for flower head
    center_x, center_y = flower.xcor(), flower.ycor()

    # Draw leaves
    leaf_positions = [-size / 2, size / 2]
    for leaf_pos in leaf_positions:
        setup_turtle(flower, center_x, center_y - size + leaf_pos)
        flower.setheading(135 if leaf_pos < 0 else 45)
        flower.pencolor("green")
        flower.fillcolor("#90EE90")  # Light green
        flower.begin_fill()

        # Draw leaf
        flower.forward(size / 2)
        for _ in range(180):
            flower.forward(size / 60)
            flower.right(1)
        flower.forward(size / 2)
        flower.end_fill()

    # Draw petals
    setup_turtle(flower, center_x, center_y)
    petal_color = random_color()
    flower.fillcolor(petal_color)

    for _ in range(8):  # 8 petals for more detail
        flower.pendown()
        flower.begin_fill()
        # Draw elongated petal
        flower.setheading(_ * 45)  # Evenly space petals
        for i in range(45):
            flower.forward(size / 20)
            flower.right(4)
        flower.end_fill()
        flower.penup()

    # Draw center
    setup_turtle(flower, center_x, center_y)
    center_color = random_color()
    flower.fillcolor(center_color)
    flower.begin_fill()
    flower.circle(size / 5)
    flower.end_fill()


# ======== VEHICLE DRAWING FUNCTIONS ========


# Function to draw wheels with more detail
def draw_wheel(t, x, y, radius=15):
    setup_turtle(t, x, y)

    # Tire
    t.fillcolor("black")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Rim
    setup_turtle(t, x, y + radius / 1.5)
    t.fillcolor("silver")
    t.begin_fill()
    t.circle(radius / 1.5)
    t.end_fill()

    # Hub cap
    setup_turtle(t, x, y + radius / 1.5)
    t.pencolor("gray")
    for i in range(5):  # Draw a star for hub cap
        t.forward(radius / 2)
        t.backward(radius / 2)
        t.right(72)


# Function to draw 3D car (sedan)
def draw_car(car_color):
    car = turtle.Turtle()
    car.speed(0)
    car.hideturtle()

    # Main car body - lower part
    setup_turtle(car, -120, -100)
    car.fillcolor(car_color)
    car.begin_fill()
    car.forward(240)  # Length
    car.left(45)
    car.forward(20)  # Rear slope
    car.left(45)
    car.forward(20)  # Rear height
    car.left(90)
    car.forward(200)  # Top length
    car.left(90)
    car.forward(20)  # Front height
    car.left(45)
    car.forward(20)  # Front slope
    car.left(45)
    car.forward(260)  # Return to base + extra for 3D
    car.left(90)
    car.forward(10)  # 3D width
    car.left(90)
    car.forward(260)  # Length for 3D side
    car.right(45)
    car.forward(20)  # Front slope
    car.right(45)
    car.forward(20)  # Front height
    car.right(90)
    car.forward(200)  # Top length
    car.right(90)
    car.forward(20)  # Rear height
    car.right(45)
    car.forward(20)  # Rear slope
    car.right(45)
    car.forward(240)  # Back to start
    car.end_fill()

    # Car roof
    setup_turtle(car, -60, -40)
    car.fillcolor(car_color)
    car.begin_fill()
    car.forward(120)  # Roof length
    car.left(90)
    car.forward(60)  # Roof width
    car.left(90)
    car.forward(120)  # Roof length
    car.left(90)
    car.forward(60)  # Back to start
    car.end_fill()

    # Car windows
    setup_turtle(car, -50, -30)
    car.fillcolor("lightblue")

    # Side windows (left)
    car.begin_fill()
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.end_fill()

    # Side windows (right)
    setup_turtle(car, 10, -30)
    car.begin_fill()
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.end_fill()

    # Windshield
    setup_turtle(car, -60, -30)
    car.begin_fill()
    car.left(45)
    car.forward(40)
    car.right(45)
    car.forward(20)
    car.right(90)
    car.forward(60)
    car.right(90)
    car.forward(20)
    car.right(45)
    car.forward(40)
    car.end_fill()

    # Rear window
    setup_turtle(car, 50, -30)
    car.begin_fill()
    car.forward(20)
    car.left(45)
    car.forward(40)
    car.left(45)
    car.forward(20)
    car.left(90)
    car.forward(60)
    car.end_fill()

    # Draw wheels
    draw_wheel(car, -70, -100, 20)
    draw_wheel(car, 70, -100, 20)

    # Headlights
    setup_turtle(car, -120, -80)
    car.fillcolor("yellow")
    car.begin_fill()
    car.circle(10)
    car.end_fill()

    setup_turtle(car, -120, -60)
    car.fillcolor("yellow")
    car.begin_fill()
    car.circle(10)
    car.end_fill()

    # Taillights
    setup_turtle(car, 120, -80)
    car.fillcolor("red")
    car.begin_fill()
    car.circle(10)
    car.end_fill()

    setup_turtle(car, 120, -60)
    car.fillcolor("red")
    car.begin_fill()
    car.circle(10)
    car.end_fill()

    return car


# Function to draw 3D SUV
def draw_suv(car_color):
    suv = turtle.Turtle()
    suv.speed(0)
    suv.hideturtle()

    # Main SUV body
    setup_turtle(suv, -130, -100)
    suv.fillcolor(car_color)
    suv.begin_fill()
    suv.forward(260)  # Length
    suv.left(90)
    suv.forward(90)  # Height
    suv.left(90)
    suv.forward(260)  # Top length
    suv.left(90)
    suv.forward(90)  # Back to start
    suv.end_fill()

    # SUV 3D effect
    setup_turtle(suv, 130, -100)
    suv.fillcolor(car_color)
    suv.begin_fill()
    suv.left(30)
    suv.forward(30)  # Depth
    suv.left(60)
    suv.forward(90)  # Height
    suv.left(120)
    suv.forward(30)  # Top depth
    suv.left(60)
    suv.forward(90)  # Back to start
    suv.end_fill()

    # Top 3D effect
    setup_turtle(suv, -130, -10)
    suv.fillcolor(car_color)
    suv.begin_fill()
    suv.forward(260)  # Length
    suv.left(150)
    suv.forward(30)  # Depth
    suv.left(30)
    suv.forward(260)  # Top length
    suv.left(30)
    suv.forward(30)  # Back to start
    suv.end_fill()

    # Windows
    window_positions = [(-100, -50), (-30, -50), (40, -50)]
    for x, y in window_positions:
        setup_turtle(suv, x, y)
        suv.fillcolor("lightblue")
        suv.begin_fill()
        for _ in range(4):
            suv.forward(50)
            suv.left(90)
        suv.end_fill()

    # Draw wheels with larger size for SUV
    draw_wheel(suv, -70, -100, 25)
    draw_wheel(suv, 70, -100, 25)

    # Headlights
    setup_turtle(suv, -130, -70)
    suv.fillcolor("yellow")
    suv.begin_fill()
    suv.circle(12)
    suv.end_fill()

    # Taillights
    setup_turtle(suv, 130, -70)
    suv.fillcolor("red")
    suv.begin_fill()
    suv.circle(12)
    suv.end_fill()

    # SUV roof rack
    setup_turtle(suv, -120, -10)
    suv.pensize(3)
    suv.pencolor("black")
    suv.forward(240)

    # Roof rack supports
    for x in [-100, -20, 60, 120]:
        setup_turtle(suv, x, -10)
        suv.setheading(90)
        suv.backward(5)

    return suv


# Function to draw 3D truck
def draw_truck(car_color):
    truck = turtle.Turtle()
    truck.speed(0)
    truck.hideturtle()

    # Cabin
    setup_turtle(truck, -120, -100)
    truck.fillcolor(car_color)
    truck.begin_fill()
    truck.forward(80)  # Cabin length
    truck.left(90)
    truck.forward(80)  # Cabin height
    truck.left(90)
    truck.forward(80)  # Top length
    truck.left(90)
    truck.forward(80)  # Back to start
    truck.end_fill()

    # Cabin 3D effect
    setup_turtle(truck, -40, -100)
    truck.fillcolor(car_color)
    truck.begin_fill()
    truck.left(30)
    truck.forward(30)  # Depth
    truck.left(60)
    truck.forward(80)  # Height
    truck.left(120)
    truck.forward(30)  # Top depth
    truck.left(60)
    truck.forward(80)  # Back to start
    truck.end_fill()

    # Top 3D effect for cabin
    setup_turtle(truck, -120, -20)
    truck.fillcolor(car_color)
    truck.begin_fill()
    truck.forward(80)  # Length
    truck.left(150)
    truck.forward(30)  # Depth
    truck.left(30)
    truck.forward(80)  # Top length
    truck.left(30)
    truck.forward(30)  # Back to start
    truck.end_fill()

    # Cargo bed
    setup_turtle(truck, -40, -100)
    truck.fillcolor(car_color)
    truck.begin_fill()
    truck.forward(160)  # Cargo length
    truck.left(90)
    truck.forward(40)  # Cargo wall height
    truck.left(90)
    truck.forward(160)  # Top length
    truck.left(90)
    truck.forward(40)  # Back to start
    truck.end_fill()

    # Cargo 3D effect
    setup_turtle(truck, 120, -100)
    truck.fillcolor(car_color)
    truck.begin_fill()
    truck.left(30)
    truck.forward(30)  # Depth
    truck.left(60)
    truck.forward(40)  # Height
    truck.left(120)
    truck.forward(30)  # Top depth
    truck.left(60)
    truck.forward(40)  # Back to start
    truck.end_fill()

    # Top 3D effect for cargo
    setup_turtle(truck, -40, -60)
    truck.fillcolor(car_color)
    truck.begin_fill()
    truck.forward(160)  # Length
    truck.left(150)
    truck.forward(30)  # Depth
    truck.left(30)
    truck.forward(160)  # Top length
    truck.left(30)
    truck.forward(30)  # Back to start
    truck.end_fill()

    # Windows
    setup_turtle(truck, -100, -60)
    truck.fillcolor("lightblue")
    truck.begin_fill()
    for _ in range(4):
        truck.forward(40)
        truck.left(90)
    truck.end_fill()

    # Draw wheels
    draw_wheel(truck, -80, -100, 25)  # Front wheel
    draw_wheel(truck, 0, -100, 25)  # Middle wheel
    draw_wheel(truck, 80, -100, 25)  # Rear wheel

    # Headlights
    setup_turtle(truck, -120, -70)
    truck.fillcolor("yellow")
    truck.begin_fill()
    truck.circle(12)
    truck.end_fill()

    # Taillights
    setup_turtle(truck, 120, -70)
    truck.fillcolor("red")
    truck.begin_fill()
    truck.circle(12)
    truck.end_fill()

    return truck


# Function to draw flowers around a vehicle
def draw_flowers_around(num_flowers=6):
    flower_positions = []
    # Generate random positions for flowers
    for _ in range(num_flowers):
        x = random.randint(-350, 350)
        # Make sure flowers are on the ground
        y = random.randint(-140, -120)
        # Avoid placing flowers too close to each other
        valid_position = True
        for fx, fy in flower_positions:
            if math.sqrt((x - fx) ** 2 + (y - fy) ** 2) < 80:
                valid_position = False
                break
        if valid_position:
            flower_positions.append((x, y))
            draw_flower(x, y, random.randint(20, 35))


# Function to display car details
def display_details(details, title="Vehicle Details"):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(-450, 250)

    # Display title
    text.write(title, align="left", font=("Arial", 24, "bold"))

    # Display car details
    text.goto(-450, 200)
    info_text = f"Make: {details['make']}\n"
    info_text += f"Model: {details['model']}\n"
    info_text += f"Year: {details['year']}\n"
    info_text += f"Mileage: {details['mileage']} miles\n"
    info_text += f"Price: {details['price']}"

    text.write(info_text, align="left", font=("Arial", 18, "normal"))


# Function to create button
def create_button(x, y, width, height, text, callback):
    button = turtle.Turtle()
    button.hideturtle()
    button.penup()
    button.goto(x, y)

    # Draw button
    button.pendown()
    button.fillcolor("#4682B4")  # Steel Blue
    button.begin_fill()
    for _ in range(2):
        button.forward(width)
        button.left(90)
        button.forward(height)
        button.left(90)
    button.end_fill()

    # Draw button border
    button.pencolor("black")
    button.pensize(2)
    for _ in range(2):
        button.forward(width)
        button.left(90)
        button.forward(height)
        button.left(90)

    # Write text
    button.penup()
    button.goto(x + width / 2, y + height / 3)
    button.color("white")
    button.write(text, align="center", font=("Arial", 14, "bold"))

    # Register click event
    def check_click(x_click, y_click):
        if x <= x_click <= x + width and y <= y_click <= y + height:
            callback()

    screen.onclick(check_click)


# Main visualization functions
def show_car():
    screen.clear()
    screen.bgcolor("#87CEEB")  # Sky blue background

    # Draw ground
    draw_ground()

    # Generate car details
    car_details = generate_car_details("car")

    # Display details
    display_details(car_details, "Car Details")

    # Draw car with random color
    car_color = random_color()
    draw_car(car_color)

    # Draw flowers around the car
    draw_flowers_around()

    # Create buttons for navigation
    create_button(300, -250, 150, 50, "View SUV", show_suv)
    create_button(100, -250, 150, 50, "View Truck", show_truck)


def show_suv():
    screen.clear()
    screen.bgcolor("#87CEEB")  # Sky blue background

    # Draw ground
    draw_ground()

    # Generate SUV details
    suv_details = generate_car_details("suv")

    # Display details
    display_details(suv_details, "SUV Details")

    # Draw SUV with random color
    suv_color = random_color()
    draw_suv(suv_color)

    # Draw flowers around the SUV
    draw_flowers_around()

    # Create buttons for navigation
    create_button(300, -250, 150, 50, "View Car", show_car)
    create_button(100, -250, 150, 50, "View Truck", show_truck)


def show_truck():
    screen.clear()
    screen.bgcolor("#87CEEB")  # Sky blue background

    # Draw ground
    draw_ground()

    # Generate truck details
    truck_details = generate_car_details("truck")

    # Display details
    display_details(truck_details, "Truck Details")

    # Draw truck with random color
    truck_color = random_color()
    draw_truck(truck_color)

    # Draw flowers around the truck
    draw_flowers_around()

    # Create buttons for navigation
    create_button(300, -250, 150, 50, "View Car", show_car)
    create_button(100, -250, 150, 50, "View SUV", show_suv)


# Initialize turtle settings
turtle.tracer(0, 0)  # Turn off animation for faster drawing

# Start with the car view
show_car()

# Update the screen
turtle.update()

# Run the main loop
turtle.mainloop()


# import turtle
# import random
# import math

# # Screen setup
# screen = turtle.Screen()
# screen.title("Car Inventory Visualization")
# screen.setup(800, 600)
# screen.bgcolor("lightgray")


# # Function to generate random car details
# def generate_car_details(vehicle_type):
#     makes = {
#         "car": ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"],
#         "suv": ["Jeep", "Toyota", "Ford", "Honda", "Subaru"],
#         "truck": ["Ford", "Chevrolet", "Ram", "Toyota", "GMC"],
#     }

#     models = {
#         "car": ["Corolla", "Civic", "Focus", "Malibu", "Altima"],
#         "suv": ["Wrangler", "RAV4", "Explorer", "CR-V", "Outback"],
#         "truck": ["F-150", "Silverado", "1500", "Tacoma", "Sierra"],
#     }

#     make = random.choice(makes[vehicle_type])
#     model = random.choice(models[vehicle_type])
#     year = random.randint(2015, 2024)
#     mileage = random.randint(5000, 150000)
#     price = random.randint(5000, 40000)

#     return {
#         "make": make,
#         "model": model,
#         "year": year,
#         "mileage": mileage,
#         "price": f"${price:,}",
#     }


# # Function to generate random color
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     # Convert RGB to hex color string
#     return f"#{r:02x}{g:02x}{b:02x}"


# # Function to draw a flower
# def draw_flower(x, y, size=20):
#     flower = turtle.Turtle()
#     flower.speed(0)
#     flower.hideturtle()
#     flower.penup()
#     flower.goto(x, y)

#     # Draw petals with random color
#     petal_color = random_color()
#     flower.fillcolor(petal_color)

#     for _ in range(6):  # 6 petals
#         flower.pendown()
#         flower.begin_fill()
#         flower.circle(size / 2)
#         flower.end_fill()
#         flower.penup()
#         flower.forward(size / 2)
#         flower.right(60)

#     # Draw center with contrasting color
#     flower.goto(x, y)
#     center_color = random_color()
#     flower.fillcolor(center_color)
#     flower.begin_fill()
#     flower.circle(size / 4)
#     flower.end_fill()


# # Function to draw a basic car
# def draw_car(t, car_color):
#     # Set the fill color for the car
#     t.fillcolor(car_color)

#     # Draw main body
#     t.pendown()
#     t.begin_fill()
#     t.forward(100)
#     t.left(90)
#     t.forward(20)
#     t.left(45)
#     t.forward(30)
#     t.left(45)
#     t.forward(50)
#     t.left(45)
#     t.forward(30)
#     t.left(45)
#     t.forward(20)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#     t.forward(40)
#     t.end_fill()

#     # Draw windows
#     t.penup()
#     t.goto(t.xcor() - 30, t.ycor())
#     t.pendown()
#     t.left(90)
#     t.forward(30)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(30)

#     # Draw wheels
#     wheel_positions = [(20, -40), (80, -40)]

#     for wx, wy in wheel_positions:
#         t.penup()
#         t.goto(t.xcor() - 100 + wx, t.ycor() - 20 + wy)
#         t.pendown()
#         t.fillcolor("black")
#         t.begin_fill()
#         t.circle(10)
#         t.end_fill()

#         # Wheel center
#         t.penup()
#         t.goto(t.xcor(), t.ycor() + 5)
#         t.pendown()
#         t.fillcolor("white")
#         t.begin_fill()
#         t.circle(3)
#         t.end_fill()


# # Function to draw SUV
# def draw_suv(t, car_color):
#     # Set the fill color for the SUV
#     t.fillcolor(car_color)

#     # Draw main body
#     t.pendown()
#     t.begin_fill()
#     t.forward(120)
#     t.left(90)
#     t.forward(50)
#     t.left(90)
#     t.forward(120)
#     t.left(90)
#     t.forward(50)
#     t.end_fill()

#     # Draw windows
#     t.penup()
#     t.goto(t.xcor() + 10, t.ycor() - 10)
#     t.pendown()

#     # Windows outline
#     t.fillcolor("lightblue")
#     t.begin_fill()
#     for i in range(3):
#         t.forward(25)
#         t.left(90)
#         t.forward(20)
#         t.left(90)
#         t.forward(25)
#         t.right(90)
#         if i == 2:
#             break
#         t.forward(10)
#         t.right(90)
#     t.end_fill()

#     # Draw wheels
#     wheel_positions = [(30, -50), (90, -50)]

#     for wx, wy in wheel_positions:
#         t.penup()
#         t.goto(t.xcor() - 60 + wx, t.ycor() + wy)
#         t.pendown()
#         t.fillcolor("black")
#         t.begin_fill()
#         t.circle(15)
#         t.end_fill()

#         # Wheel center
#         t.penup()
#         t.goto(t.xcor(), t.ycor() + 7)
#         t.pendown()
#         t.fillcolor("white")
#         t.begin_fill()
#         t.circle(5)
#         t.end_fill()


# # Function to draw truck
# def draw_truck(t, car_color):
#     # Draw cabin
#     t.pendown()
#     t.fillcolor(car_color)
#     t.begin_fill()
#     t.forward(50)  # Cabin width
#     t.left(90)
#     t.forward(50)  # Cabin height
#     t.left(90)
#     t.forward(50)  # Back to start
#     t.left(90)
#     t.forward(50)
#     t.end_fill()

#     # Draw cargo area
#     t.penup()
#     t.right(90)
#     t.forward(50)
#     t.right(90)
#     t.forward(10)  # Lower height for cargo area
#     t.pendown()

#     t.fillcolor(car_color)
#     t.begin_fill()
#     t.left(90)
#     t.forward(100)  # Cargo width
#     t.left(90)
#     t.forward(40)  # Cargo height
#     t.left(90)
#     t.forward(100)  # Back to start
#     t.left(90)
#     t.forward(40)
#     t.end_fill()

#     # Draw window
#     t.penup()
#     t.goto(t.xcor() - 40, t.ycor() + 5)
#     t.pendown()

#     t.fillcolor("lightblue")
#     t.begin_fill()
#     for _ in range(4):
#         t.forward(30)
#         t.left(90)
#     t.end_fill()

#     # Draw wheels
#     wheel_positions = [(25, -50), (125, -50)]

#     for wx, wy in wheel_positions:
#         t.penup()
#         t.goto(wx, wy)
#         t.pendown()
#         t.fillcolor("black")
#         t.begin_fill()
#         t.circle(15)
#         t.end_fill()

#         # Wheel center
#         t.penup()
#         t.goto(t.xcor(), t.ycor() + 7)
#         t.pendown()
#         t.fillcolor("white")
#         t.begin_fill()
#         t.circle(5)
#         t.end_fill()


# # Function to draw flowers around a vehicle
# def draw_flowers_around(center_x, center_y, num_flowers=6):
#     for _ in range(num_flowers):
#         # Generate random position around the car
#         angle = random.uniform(0, 2 * math.pi)
#         distance = random.uniform(100, 200)
#         x = center_x + distance * math.cos(angle)
#         y = center_y + distance * math.sin(angle)

#         # Draw a flower at this position
#         draw_flower(x, y, random.randint(15, 25))


# # Function to display car details
# def display_details(details, y_position=200):
#     text = turtle.Turtle()
#     text.hideturtle()
#     text.penup()
#     text.goto(-300, y_position)

#     # Display car details
#     info_text = f"Make: {details['make']}\n"
#     info_text += f"Model: {details['model']}\n"
#     info_text += f"Year: {details['year']}\n"
#     info_text += f"Mileage: {details['mileage']} miles\n"
#     info_text += f"Price: {details['price']}"

#     text.write(info_text, font=("Arial", 14, "normal"))


# # Function to create button
# def create_button(x, y, width, height, text, callback):
#     button = turtle.Turtle()
#     button.hideturtle()
#     button.penup()
#     button.goto(x, y)

#     # Draw button
#     button.pendown()
#     button.fillcolor("lightblue")
#     button.begin_fill()
#     for _ in range(2):
#         button.forward(width)
#         button.left(90)
#         button.forward(height)
#         button.left(90)
#     button.end_fill()

#     # Write text
#     button.penup()
#     button.goto(x + width / 2, y + height / 4)
#     button.write(text, align="center", font=("Arial", 12, "normal"))

#     # Register click event
#     screen.onclick(
#         lambda x_click, y_click: (
#             callback()
#             if (x <= x_click <= x + width and y <= y_click <= y + height)
#             else None
#         )
#     )


# # Main visualization functions
# def show_car():
#     screen.clear()
#     screen.bgcolor("lightgray")

#     # Generate car details
#     car_details = generate_car_details("car")

#     # Display details
#     display_details(car_details)

#     # Draw car
#     car_turtle = turtle.Turtle()
#     car_turtle.speed(0)
#     car_turtle.penup()
#     car_turtle.goto(-50, 0)
#     car_turtle.pendown()

#     # Generate a random color for the car
#     car_color = random_color()
#     draw_car(car_turtle, car_color)

#     # Draw flowers around the car
#     draw_flowers_around(0, 0)

#     # Create buttons for navigation
#     create_button(200, -250, 100, 40, "View SUV", show_suv)
#     create_button(50, -250, 100, 40, "View Truck", show_truck)


# def show_suv():
#     screen.clear()
#     screen.bgcolor("lightgray")

#     # Generate SUV details
#     suv_details = generate_car_details("suv")

#     # Display details
#     display_details(suv_details)

#     # Draw SUV
#     suv_turtle = turtle.Turtle()
#     suv_turtle.speed(0)
#     suv_turtle.penup()
#     suv_turtle.goto(-50, 0)

#     # Generate a random color for the SUV
#     suv_color = random_color()
#     draw_suv(suv_turtle, suv_color)

#     # Draw flowers around the SUV
#     draw_flowers_around(0, 0)

#     # Create buttons for navigation
#     create_button(200, -250, 100, 40, "View Car", show_car)
#     create_button(50, -250, 100, 40, "View Truck", show_truck)


# def show_truck():
#     screen.clear()
#     screen.bgcolor("lightgray")

#     # Generate truck details
#     truck_details = generate_car_details("truck")

#     # Display details
#     display_details(truck_details)

#     # Draw truck
#     truck_turtle = turtle.Turtle()
#     truck_turtle.speed(0)
#     truck_turtle.penup()
#     truck_turtle.goto(-50, 0)

#     # Generate a random color for the truck
#     truck_color = random_color()
#     draw_truck(truck_turtle, truck_color)

#     # Draw flowers around the truck
#     draw_flowers_around(0, 0)

#     # Create buttons for navigation
#     create_button(200, -250, 100, 40, "View Car", show_car)
#     create_button(50, -250, 100, 40, "View SUV", show_suv)


# # Start with the car view
# show_car()

# # Run the main loop
# turtle.mainloop()
