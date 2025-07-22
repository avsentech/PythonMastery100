# Code #66: Demonstrate Method Overriding with Shape Hierarchy
"""
    🧠 Why This Matters?
    Used in:
    - 🎨 Drawing libraries (e.g. turtle, graphics engines)
    - 🧮 Geometry calculators and CAD software
    - 🧱 Strategy and plugin design patterns
    - 🧬 Polymorphism + inheritance in one elegant bundl
"""
# Tier: Intermediate
# Goal: Override area() methid in child classes with shape-specific logic

# Python Code
import math

# Superclass
class Shape:
    def area(self):
        return "Area method not implemented!"
    
# Subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
# Sample Usage

shapes = [
    Circle(7),
    Rectangle(10, 5),
    Triangle(6, 8)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")

# Output
"""
    Circle Area: 153.94
    Rectangle Area: 50.00
    Triangle Area: 24.00
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    Shape class         Defines generic interface
    area() method       Overridden in each subclass
    Polymorphism        Same method name, different logic
    __class__.__name__  Dynamically prints current shape type
"""
# Each subclass provides its own implementation of area()--overriding the base method.

# Real-World Connection
"""
    - Dynamic drawing or rendering systems
    - Scientific calculators and engineering tools
    - Shape detection or image segmentation logic
    - CAD or UI layout engines based on geometry rules
"""