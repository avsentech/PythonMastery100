# Code #4: Decision-Making
# Tier: Basic
# Goal: Check if a number is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even numer")
else:
    print("Odd number")

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    Condition       Uses if/else to make decisions
    Modulo          Finds remainder with %
"""

# How the Logic Works
"""
    - Input a number
    - If divisible by 2 → even
    - Else → odd
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Input → num]
        ↓
    num % 2 == 0?
        ├── Yes → Print "Even"
        └── No → Print "Odd"
    [End]
"""

# Real-World Connection
"""
    - Crucial for building smart systems—validating user input, applying filters, controlling flow
    - Powers conditional behavior in games, dashboards, and AI logic
"""