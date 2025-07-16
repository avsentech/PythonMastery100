# Code #12: Factorial Function
# Tier: Intermediate
# Goal: Define and use a function that calculates the factorial of a number

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result += 1
    return result

try:
    num = int(input("Enter a number: "))
    if num < 0:
        print(" Error: Factorial is not defined for negative numbers.")
    else:
        print(" Factorial is:", factorial(num))
except ValueError:
    print(" Invalid input! Please enter a valid initeger.")

# Concept Breakdown
"""
   Concept          Description
   -----------------------------
   Function(def)    A reusable block of code that takes input and returns output
   Loop(for)        Iterates over a range from 2 to n
   Multiplication   Accumulates the factorial value
   Input / Output   Takes user number and prints result 
"""

# How the Logic Works
"""
    Let's say you input 5.
    factorial starts with result = 1
        - Loop runs:
        - i = 2 → result = 1 × 2 = 2
        - i = 3 → result = 2 × 3 = 6
        - i = 4 → result = 6 × 4 = 24
        - i = 5 → result = 24 × 5 = 120
    Final result returned: 120
"""

#  Flowchart-Like Visualization
"""
    [Input received]
    ↓
    try to convert to int
    ↓
    If ValueError → Show "Invalid input!"
    Else if num < 0 → Show "Factorial undefined"
    Else → Call factorial → Print result
    [End]
"""

# Real-World Connection
"""
    Factorials are deeply embedded in:
    - Math: permutations, combinations, probability
    - AI/ML: recursive patterns, tree depth calculations
    - Programming: great way to understand loops and function structuring

    Error handling like this is essential for:
    - Preventing user crashes
    - Improving UX in CLI tools, websites, and SaaS dashboards
    - Building trust in your application's robustness
"""

# Notes: Running the file throwing error when giving String input actually it need to take only number right?
