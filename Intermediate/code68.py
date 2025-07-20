# Code #68: Override __eq__() to Compare Class Instances
"""
    🧠 Why This Matters?
    Used in:
    - 🔍 Equality checks for data models
    - 🧪 Testing and assertions
    - 📦 Object comparison in databases, APIs, and collection
"""
# Tier: Intermediate
# Goal: Define logic to compare two objects by their internal data, not their location in memory

# Python Code
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False
    
# Sample Usage

p1 = Product("Laptop", 999.99)
p2 = Product("Laptop", 999.99)
p3 = Product("Monitor", 299.99)

print(p1 == p2)  # True: same data

print(p1 == p3)  # False: different product

# Sample Output
"""
    True
    False
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    __eq__()            Define custom equality logic
    isinstance()        Ensures comparison is with a Product type
    == operator         Redirected to __eq__() when used on objects
"""
# without overriding __eq__(), Python compares by memory locatoin (id()), not contents.

# Real-World Connection
"""
    - Comparing invoice records or purchase items
    - Testing if two users have same credentials
    - Comparing config or log entries across systems
"""