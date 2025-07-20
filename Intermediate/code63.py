# Code #63: Implement Inheritance with Vehicle and Car Classes
"""
    🧠 Why This Matters?
    Used in:
    - 🚙 Real-world object hierarchies (Vehicle → Car)
    - 🛠️ Reusing logic from parent classes
    - ⚙️ Framework design and plugin architectur
"""
# Tier: Intermediate
# Goal: Create a base class Vehicle and child class Car that inherits its features and adds its own

# Python Code

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        return f"{self.brand} engine started."

    def get_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"
    
# Child class

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year) # Inherit from Vehicle

        self.model = model

    def get_car_info(self):
        base_info = self.get_info()
        return f"{base_info}, Model: {self.model}"
    
# Sample Usage

my_car = Car("Toyota", 2020, "Corolla")
print(my_car.start_engine())
print(my_car.get_car_info())

# Sample Output
"""
    Toyota engine started.
    Brand: Toyota, Year: 2020, Model: Corolla
"""

# Concept Breakdown
"""
    Concept                     Purpose
    ------------------------------------
    class Vehicle               Defines common structure
    class Car(Vehicle)          Inherits from Vehicle
    super()                     Initializes parent class attributes
    Method inheritance          Car gets start_engine() & get_info()
"""
# You can override inherited methods or add new ones in the child class as needed.

# Real-World Connection
"""
    - Django class-based views extending base templates
    - API clients reusing authentication and request logic
    - Game engine (Entity → Player, NPC, Enemy)
"""