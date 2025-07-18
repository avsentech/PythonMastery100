# Code #38: Check if a Number is an Automorphic Number
"""
    🧠 What is an Automorphic Number?
        An Automorphic Number is a number whose square ends with the number itself.
        Example:
            - 76^2 = 5776 → ends with 76 → ✅ Automorphic
            - 25^2 = 625 → ends with 25 → ✅ Automorphic
            - 13^2 = 169 → ends with 13 → ❌ Not Automorphic

"""
# Tier: Intermediate
# Goal: Determine if a number is an automorpphic number

num = int(input("Enter a number: "))
square = num ** 2

if str(square).endswith(str(num)):
    print("Automorphic number")
else:
    print("Not an automorphic number")

# Sample Input1(Automorphic)
"""
    76
"""

# Output1
"""
    Automorphic number
"""

# Sample Input 2 (Not Automorphiic)
"""
    23
"""

# Output2
"""
    Not an automorphic numberv
"""

# Concept Breakdown
"""
    Concept                 Description
    ------------------------------------
    num**2                  Calculates square of the number
    str(square)             Converts square to string
    .endswith(str(num))     Checks if square ends with original number
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Square the number
    - Convert both to strings
    - Check if square ends with original number
    - Print result
"""

# Flowchart-like Visualization
"""
    [Start]
        ↓
    Input → 76
        ↓
    Square → 5776
        ↓
    Endswith → "76" → Match
        ↓
    Result → Automorphic number
    [End]

    OR

    Input → 13
        ↓
    Square → 169
        ↓
    Endswith → "13" → No match
        ↓
    Result → Not Automorphic
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and digit-based puzzles
    - Powers logic-based interview questions
    - Demonstrates string slicing and pattern matching
"""