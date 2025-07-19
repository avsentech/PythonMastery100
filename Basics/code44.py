# Code #44: Check if a Number is a Trimorphic Number
"""
    🧠 What is a Trimorphic Number?
    A Trimorphic Number is a number whose cube ends with the number itself.
    Example:
    - 4^3 = 64 → ends with 4 → ✅ Trimorphic
    - 5^3 = 125 → ends with 5 → ✅ Trimorphic
    - 24^3 = 13824 → ends with 24 → ✅ Trimorphic
    - 10^3 = 1000 → ends with 10 → ❌ Not Trimorphic
"""
# Tier: Intermediate
# Goal: Determine if a number is a trimorphic number

num = int(input("Enter a number: "))
cube = num ** 3

if str(cube).endswith(str(num)):
    print("Trimorphic number")
else:
    print("Not a trimorphic number")

# Sample Input1 (Trimorphic)
"""
    24
"""

# Output
"""
    Trimorphic number
"""

# Sample Input2 (Not Trimorphic)
"""
    10
"""

# Output2
"""
    Not a trimorphic number
"""

# Concept Breakdown
"""
    Concept                 Description
    ----------------------------
    num**3                  Calculates cube of the number
    str(cube).endswith()    Checks if cube ends with original number
    String Comparison       Validates end pattern march
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Cube the number
    - Convert both to strings
    - Check if cube ends with original number
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 24
        ↓
    Cube → 13824
        ↓
    Endswith → "24" → Match
        ↓
    Result → Trimorphic number
    [End]

    OR

    Input → 10
        ↓
    Cube → 1000
        ↓
    Endswith → "10" → No match
        ↓
    Result → Not Trimorphic
    [End]
"""

# Real-World Connection
"""
    - Used in digit-based puzzles and number theory
    - Powers logic-based interview questions
    - Demonstrates string slicing and cube validation
"""