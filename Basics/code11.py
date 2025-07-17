# Code #11: Tuple Basics

colors = ("red", "green", "blue") # Creates a tuple with 3 string items
print("First color:", colors[0])  # Accesses the first item (index 0) and prints it

# What is Tuple?
"""
    What is Tuples in Python?
   
    - A tuple is a sequence of values, like a list, but immutable—you can't change its elements after it's created.
    - Tuples use parentheses: ()
    - Commonly used for:
        - Fixed data collections (e.g., RGB values, coordinates)
        - Return values from functions that shouldn't be modified
        - Dictionary keys, because they're hashable

"""

# Flowchart-like Visualization
"""
    [Start]
        ↓
    Define tuple → ("red", "green", "blue")
        ↓
    Access index [0] → "red"
        ↓
    Print → First color: red
    [End]
"""

# Guru Wisdom: Why Tuples Matter
"""
    Performance: Tuples are slightly faster than lists
    Safety: Prevents accidental changes
    Structure: Oftern used for database rows, coordinates, or grouped data like (x,y)
"""

# Sample Expansion
"""
    Want to show all colors with a loop?
 
    for color in colors:
        print("Color:", color)

    Or slice them:

    print("Last two colors:", colors[1:])
"""

# Real-World Connection
"""
    - Tuples are used to store coordinates, RGB values, database rows, or config constants
    - Enables stable data structures in apps and APIs
"""