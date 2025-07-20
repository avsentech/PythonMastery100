# Code #64: Use @property Decorator to Control Attribute Access
"""
    🧠 Why This Matters?
    Used in:
    - 🔒 Encapsulation with clean syntax
    - 🛡️ Preventing direct access to sensitive data
    - 📦 Designing clean APIs and classes (like Django models
"""
# Tier: Intermediate
# Goal: Create a class that uses @property for controlled access to a private attribute

# Python Code
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # private variable

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, amount):
        if amount < 0:
            print("Salary cannot be negative.")
        else:
            self.__salary = amount

# Sample Usage

emp = Employee("Sena", 50000)
print(emp.salary)       # Calls the getter

emp.salary = 55000      # Calls the setter

print(emp.salary)

emp.salary = -1000      # Invalid attempt

# Sample Output
"""
    50000
    55000
    Salary cannot be negative.
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    @property           Exposes a method like an attribute
    Getter method       Allows safe read access to private variable
    Setter method       Adds validation before modifying
    __salary            Kept hidden with controlled public interface
"""
# The same approach works for derived values, formatting logic, or flag toggles.

# Real-World Connection
"""
    - Django ORM models expose fields using @property
    - Finance apps controlling access to balances/sensitive values
    - Configuration engines exposing derived values with logic
"""
