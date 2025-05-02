import tkinter as tk
import random
import math
from tkinter import messagebox


class VehicleVisualization:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Inventory Visualization")
        self.root.geometry("800x600")

        # Initialize vehicle data
        self.vehicle_types = ["Car", "SUV", "Truck"]
        self.current_vehicle = self.generate_random_vehicle(self.vehicle_types[0])

        # Set up the main canvas
        self.canvas = tk.Canvas(root, width=800, height=500, bg="white")
        self.canvas.pack(pady=10)

        # Information display
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(fill=tk.X, padx=20)

        self.info_label = tk.Label(
            self.info_frame, text="", font=("Arial", 12), justify=tk.LEFT
        )
        self.info_label.pack(anchor=tk.W)

        # Navigation buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.car_button = tk.Button(
            self.button_frame,
            text="View Car",
            command=lambda: self.change_vehicle("Car"),
        )
        self.car_button.pack(side=tk.LEFT, padx=10)

        self.suv_button = tk.Button(
            self.button_frame,
            text="View SUV",
            command=lambda: self.change_vehicle("SUV"),
        )
        self.suv_button.pack(side=tk.LEFT, padx=10)

        self.truck_button = tk.Button(
            self.button_frame,
            text="View Truck",
            command=lambda: self.change_vehicle("Truck"),
        )
        self.truck_button.pack(side=tk.LEFT, padx=10)

        self.random_button = tk.Button(
            self.button_frame, text="Generate New", command=self.regenerate_current
        )
        self.random_button.pack(side=tk.LEFT, padx=10)

        # Draw initial vehicle
        self.draw_vehicle()

    def generate_random_vehicle(self, vehicle_type):
        """Generate random vehicle data based on type"""
        makes = {
            "Car": ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "Mazda"],
            "SUV": ["Jeep", "Ford", "Toyota", "Honda", "Subaru", "Chevrolet"],
            "Truck": ["Ford", "Chevrolet", "Ram", "Toyota", "GMC", "Nissan"],
        }

        models = {
            "Car": [
                "Camry",
                "Civic",
                "Accord",
                "Corolla",
                "Altima",
                "Sentra",
                "Fusion",
            ],
            "SUV": ["Cherokee", "Explorer", "RAV4", "CR-V", "Forester", "Equinox"],
            "Truck": ["F-150", "Silverado", "Ram 1500", "Tacoma", "Sierra", "Tundra"],
        }

        year = random.randint(2010, 2023)
        make = random.choice(makes[vehicle_type])
        model = random.choice(models[vehicle_type])
        mileage = random.randint(1000, 150000)
        price = random.randint(5000, 50000)

        # Random color (RGB)
        color = self.generate_random_color()

        return {
            "type": vehicle_type,
            "year": year,
            "make": make,
            "model": model,
            "mileage": mileage,
            "price": price,
            "color": color,
        }

    def generate_random_color(self):
        """Generate a random color in hex format"""
        # Generate random RGB values (0-255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Convert to hex format
        return f"#{r:02x}{g:02x}{b:02x}"

    def generate_random_flower_colors(self, count=6):
        """Generate a list of random colors for flowers"""
        colors = []
        for _ in range(count):
            colors.append(self.generate_random_color())
        return colors

    def change_vehicle(self, vehicle_type):
        """Change to a different vehicle type"""
        self.current_vehicle = self.generate_random_vehicle(vehicle_type)
        self.draw_vehicle()

    def regenerate_current(self):
        """Generate a new random vehicle of the current type"""
        self.current_vehicle = self.generate_random_vehicle(
            self.current_vehicle["type"]
        )
        self.draw_vehicle()

    def draw_vehicle(self):
        """Draw the current vehicle and surrounding environment"""
        self.canvas.delete("all")  # Clear canvas

        # Draw ground/background
        self.canvas.create_rectangle(0, 350, 800, 500, fill="#8a8a8a", outline="")

        # Get vehicle dimensions based on type
        dimensions = self.get_vehicle_dimensions(self.current_vehicle["type"])

        # Draw the 3D vehicle based on type
        vehicle_color = self.current_vehicle["color"]

        if self.current_vehicle["type"] == "Car":
            self.draw_car(400, 350, dimensions, vehicle_color)
        elif self.current_vehicle["type"] == "SUV":
            self.draw_suv(400, 350, dimensions, vehicle_color)
        elif self.current_vehicle["type"] == "Truck":
            self.draw_truck(400, 350, dimensions, vehicle_color)

        # Draw flowers around vehicle
        self.draw_flowers(6)

        # Update information display
        self.update_info_display()

    def get_vehicle_dimensions(self, vehicle_type):
        """Get random dimensions for the vehicle type"""
        if vehicle_type == "Car":
            return {
                "length": random.uniform(180, 200),
                "width": random.uniform(70, 80),
                "height": random.uniform(45, 55),
            }
        elif vehicle_type == "SUV":
            return {
                "length": random.uniform(190, 210),
                "width": random.uniform(75, 85),
                "height": random.uniform(65, 75),
            }
        elif vehicle_type == "Truck":
            return {
                "length": random.uniform(210, 230),
                "width": random.uniform(75, 85),
                "height": random.uniform(60, 70),
                "bed_length": random.uniform(60, 80),
            }

    def draw_car(self, x, y, dimensions, color):
        """Draw a 3D car representation"""
        length = dimensions["length"]
        width = dimensions["width"]
        height = dimensions["height"]

        # Scale dimensions for display
        scale = 1.05
        length = length / scale
        width = width / scale
        height = height / scale

        # Base coordinates
        x1 = x - length / 2
        x2 = x + length / 2
        y1 = y - height
        y2 = y

        # Car body (main rectangle) - Raised slightly to make room for wheels
        body_bottom = y2 - height * 0.2  # Raise the bottom of the body

        self.canvas.create_polygon(
            x1,
            y1 + height * 0.4,  # Front bottom
            x1,
            y1 + height * 0.1,  # Front top
            x1 + length * 0.2,
            y1,  # Hood start
            x1 + length * 0.3,
            y1,  # Windshield bottom
            x1 + length * 0.7,
            y1,  # Rear window bottom
            x1 + length * 0.8,
            y1,  # Trunk start
            x2,
            y1 + height * 0.1,  # Rear top
            x2,
            y1 + height * 0.4,  # Rear bottom
            x2,
            body_bottom,  # Rear ground (raised)
            x1,
            body_bottom,  # Front ground (raised)
            fill=color,
            outline="black",
        )

        # Windows
        window_color = "#a8d6ff"

        # Front windshield
        self.canvas.create_polygon(
            x1 + length * 0.2,
            y1,
            x1 + length * 0.3,
            y1 - height * 0.6,  # Increased height of the window top
            x1 + length * 0.7,
            y1 - height * 0.6,  # Increased height of the window top
            x1 + length * 0.8,
            y1,
            fill=window_color,
            outline="black",
        )

        # Side windows
        self.canvas.create_polygon(
            x1 + length * 0.3,
            y1,
            x1 + length * 0.3,
            y1 - height * 0.6,  # Increased height of the window top
            x1 + length * 0.7,
            y1 - height * 0.6,  # Increased height of the window top
            x1 + length * 0.7,
            y1,
            fill=window_color,
            outline="black",
        )

        # Wheels
        wheel_radius = height * 0.2
        wheel_color = "#333333"

        # Front wheel - positioned below the body
        wheel_y_pos = y2 - wheel_radius  # Center positioned at ground level

        self.canvas.create_oval(
            x1 + length * 0.2 - wheel_radius,
            wheel_y_pos - wheel_radius,
            x1 + length * 0.2 + wheel_radius,
            wheel_y_pos + wheel_radius,
            fill=wheel_color,
            outline="black",
        )

        # Rear wheel - positioned below the body
        self.canvas.create_oval(
            x1 + length * 0.8 - wheel_radius,
            wheel_y_pos - wheel_radius,
            x1 + length * 0.8 + wheel_radius,
            wheel_y_pos + wheel_radius,
            fill=wheel_color,
            outline="black",
        )

        # Details
        # Headlights
        self.canvas.create_rectangle(
            x1,
            y1 + height * 0.2,
            x1 + 10,
            y1 + height * 0.3,
            fill="yellow",
            outline="black",
        )

        # Taillights
        self.canvas.create_rectangle(
            x2 - 10,
            y1 + height * 0.2,
            x2,
            y1 + height * 0.3,
            fill="red",
            outline="black",
        )

    def draw_truck(self, x, y, dimensions, color):
        """Draw a 3D truck representation"""
        length = dimensions["length"]
        width = dimensions["width"]
        height = dimensions["height"]
        bed_length = dimensions["bed_length"]

        # Scale dimensions for display
        scale = 1.05
        length = length / scale
        width = width / scale
        height = height / scale
        bed_length = bed_length / scale

        # Base coordinates
        x1 = x - length / 2
        x2 = x + length / 2
        y1 = y - height
        y2 = y

        cab_length = length - bed_length

        # Adjust front part to be shorter
        front_length = cab_length * 0.7
        rear_length = cab_length * 0.3

        # Raise body for wheels
        body_bottom = y2 - height * 0.3  # Trucks are higher off the ground

        # Truck cab
        self.canvas.create_polygon(
            x1,
            y1 + height * 0.4,  # Front bottom
            x1,
            y1 + height * 0.1,  # Front top
            x1 + front_length * 0.2,
            y1,  # Hood start
            x1 + front_length * 0.9,
            y1,  # Roof end
            x1 + front_length,
            y1 + height * 0.4,  # Back of cab
            x1 + front_length,
            body_bottom,  # Back ground (raised)
            x1,
            body_bottom,  # Front ground (raised)
            fill=color,
            outline="black",
        )

        # Truck bed
        self.canvas.create_polygon(
            x1 + front_length,
            y1 + height * 0.3,
            x1 + front_length,
            body_bottom,
            x2,
            body_bottom,
            x2,
            y1 + height * 0.3,
            fill=color,
            outline="black",
        )

        # Bed divider
        self.canvas.create_line(
            x1 + front_length,
            y1 + height * 0.3,
            x1 + front_length,
            body_bottom,
            fill="black",
            width=2,
        )

        # Windows
        window_color = "#a8d6ff"

        # Front windshield
        self.canvas.create_polygon(
            x1 + front_length * 0.2,
            y1,
            x1 + front_length * 0.3,
            y1 - height * 0.45,  # Increased height for the top of the truck
            x1 + front_length * 0.8,
            y1 - height * 0.45,  # Increased height for the top of the truck
            x1 + front_length * 0.9,
            y1,
            fill=window_color,
            outline="black",
        )

        # Top of the truck (above the windows)
        self.canvas.create_rectangle(
            x1 + front_length * 0.2,
            y1 - height * 0.5,  # Increased height for the top
            x1 + front_length * 0.9,
            y1 - height * 0.45,
            fill="black",
            outline="black",
        )

        # Wheels
        wheel_radius = height * 0.23
        wheel_color = "#333333"

        # Front wheel - positioned below the body
        wheel_y_pos = y2 - wheel_radius  # Center positioned at ground level

        self.canvas.create_oval(
            x1 + front_length * 0.2 - wheel_radius,
            wheel_y_pos - wheel_radius,
            x1 + front_length * 0.2 + wheel_radius,
            wheel_y_pos + wheel_radius,
            fill=wheel_color,
            outline="black",
        )

        # Rear wheel - positioned below the body
        self.canvas.create_oval(
            x1 + front_length + bed_length * 0.7 - wheel_radius,
            wheel_y_pos - wheel_radius,
            x1 + front_length + bed_length * 0.7 + wheel_radius,
            wheel_y_pos + wheel_radius,
            fill=wheel_color,
            outline="black",
        )

        # Details
        # Headlights
        self.canvas.create_rectangle(
            x1,
            y1 + height * 0.2,
            x1 + 10,
            y1 + height * 0.3,
            fill="yellow",
            outline="black",
        )

        # Taillights
        self.canvas.create_rectangle(
            x2 - 10,
            y1 + height * 0.4,
            x2,
            y1 + height * 0.5,
            fill="red",
            outline="black",
        )

    def draw_suv(self, x, y, dimensions, color):
        """Draw a realistic SUV representation raised above the ground"""
        length = dimensions["length"]
        width = dimensions["width"]
        height = dimensions["height"]

        # Scale dimensions for display
        scale = 1.2
        length = length / scale
        width = width / scale
        height = height / scale

        # Raise the entire SUV above the ground
        ground_offset = 50  # Distance from the ground to the bottom of the wheels

        # Base coordinates
        x1 = x - length / 2
        x2 = x + length / 2
        y1 = y - height - ground_offset  # Top of the SUV body
        y2 = y - ground_offset  # Bottom of the SUV body

        # SUV body (main rectangle)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

        # Windows (above the body)
        window_color = "#a8d6ff"
        self.canvas.create_polygon(
            x1 + length * 0.2,
            y1,
            x1 + length * 0.3,
            y1 - height * 0.5,  # Window top
            x1 + length * 0.7,
            y1 - height * 0.5,  # Window top
            x1 + length * 0.8,
            y1,
            fill=window_color,
            outline="black",
        )

        # Wheels (round and attached to the body)
        wheel_radius = height * 0.2
        wheel_color = "#333333"

        # Front wheel
        self.canvas.create_oval(
            x1 + length * 0.2 - wheel_radius,
            y2 - wheel_radius,  # Positioned relative to the raised body
            x1 + length * 0.2 + wheel_radius,
            y2 + wheel_radius,
            fill=wheel_color,
            outline="black",
        )

        # Rear wheel
        self.canvas.create_oval(
            x2 - length * 0.2 - wheel_radius,
            y2 - wheel_radius,  # Positioned relative to the raised body
            x2 - length * 0.2 + wheel_radius,
            y2 + wheel_radius,
            fill=wheel_color,
            outline="black",
        )

        # Headlights
        self.canvas.create_rectangle(
            x1,
            y1 + height * 0.2,
            x1 + 10,
            y1 + height * 0.3,
            fill="yellow",
            outline="black",
        )

        # Taillights
        self.canvas.create_rectangle(
            x2 - 10,
            y1 + height * 0.2,
            x2,
            y1 + height * 0.3,
            fill="red",
            outline="black",
        )

    def draw_flowers(self, count=6):
        """Draw random flowers around the vehicle"""
        flower_colors = self.generate_random_flower_colors(count)

        # Define potential positions for flowers
        positions = [
            (200, 380),
            (250, 400),
            (300, 390),
            (500, 380),
            (550, 400),
            (600, 390),
            (350, 420),
            (450, 420),
            (400, 430),
        ]

        # Randomly select positions
        selected_positions = random.sample(positions, count)

        # Draw flowers at each position
        for i, pos in enumerate(selected_positions):
            self.draw_flower(pos[0], pos[1], flower_colors[i])

    def draw_flower(self, x, y, color):
        """Draw a simple flower at the given position"""
        # Flower center
        center_radius = 5
        self.canvas.create_oval(
            x - center_radius,
            y - center_radius,
            x + center_radius,
            y + center_radius,
            fill="#ffcc00",
            outline="",
        )

        # Flower petals
        petal_size = 8
        for angle in range(0, 360, 60):  # 6 petals
            rad = math.radians(angle)
            px = x + math.cos(rad) * 10
            py = y + math.sin(rad) * 10

            self.canvas.create_oval(
                px - petal_size,
                py - petal_size,
                px + petal_size,
                py + petal_size,
                fill=color,
                outline="",
            )

        # Stem
        stem_height = random.randint(25, 35)
        self.canvas.create_line(
            x, y + center_radius, x, y + stem_height, fill="green", width=2
        )

    def update_info_display(self):
        """Update the vehicle information text display"""
        vehicle = self.current_vehicle

        # Format price with commas
        formatted_price = "${:,}".format(vehicle["price"])

        # Format mileage with commas
        formatted_mileage = "{:,}".format(vehicle["mileage"])

        info_text = f"Vehicle Details:\n"
        info_text += f"Type: {vehicle['type']}\n"
        info_text += f"Make: {vehicle['make']}\n"
        info_text += f"Model: {vehicle['model']}\n"
        info_text += f"Year: {vehicle['year']}\n"
        info_text += f"Mileage: {formatted_mileage} miles\n"
        info_text += f"Price: {formatted_price}"

        self.info_label.config(text=info_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleVisualization(root)
    root.mainloop()
