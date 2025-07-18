# Code #37: Check if a Number is a Sunny Number
"""
    🧠 What is a Sunny Number?
        A Sunny Number is a number for which the next number (n+1) is a perfect square.
        Example:
            - 8 + 1 = 9 → √9 = 3 → ✅ Sunny
            - 10 + 1 = 11 → √11 ≠ integer → ❌ Not Sunny
"""
# Tier: Intermediate
# Goal: Determine if a number is a sunny number

import math

num = int(input("Enter a number: "))
next_num = num + 1
sqrt_next = math.sqrt(next_num)

if sqrt_next == int(sqrt_next):
    print("Sunny number")
else:
    print("Not a sunny number")

# Sample Input1 (Sunny)
"""
    8
"""

# Output1
"""
    Sunny number
"""

# Sample Input 2(Not Sunny)
"""
    10
"""

# Output2
"""
    Not a sunny number
"""

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    num + 1         Checks the next number
    math.sqrt()     Calculates
    int(sqrt)       Verifies if root is whole number
    Comparison      Determines if next number is perfect square
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Add 1 to the number
    - Calculate square root of the result
    - Check if it’s an integer
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 8
        ↓
    Next → 9
        ↓
    √9 → 3 → Integer
        ↓
    Result → Sunny number
    [End]

    OR

    Input → 10
        ↓
    Next → 11
        ↓
    √11 → 3.316 → Not Integer
        ↓
    Result → Not Sunny
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and mathematical puzzles
    - Powers logic-based interview questions
    - Demonstrates square root and integer validation
"""