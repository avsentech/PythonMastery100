# Code #3: Check if a Number is a Neon Number
"""
    A Neon Number is a number where the sum of the digits of its square equals the number itself.
    Example:
        - 9^2 = 81 → 8 + 1 = 9 → ✅ Neon
        - 12^2 = 144 → 1 + 4 + 4 = 9 → ❌ Not Neon
"""

# Tier: Intermediate
# Goal: Determine if a number is a neon number

num = int(input("Enter a number: "))
square = num ** 2
digit_sum = sum(int(digit) for digit in str(square))

if digit_sum == num:
    print("Neon number")
else:
    print("Not a neon number")

# Sample Input1 (Neon)
"""
    9
"""

# Output1
"""
    Neon number
"""

# Sample Input 2 (Not Neon)
"""
    12
"""

# Output 2
"""
    Not a neon number
"""

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    num**2          Calculates square of the number
    str(square)     Converts square to string for digit iteratioin
    sum()           Adds all digits of the square
    Comparison      Checks if digit sum equals original number
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Square the number
    - Convert square to string
    - Sum its digits
    - Compare with original number
    - Print result
"""

# Flowchart-Like Visualizationo
"""
    [Start]
        ↓
    Input → 9
        ↓
    Square → 81
        ↓
    Digit Sum → 8 + 1 = 9
        ↓
    Compare → Equal → Neon number
    [End]

    OR

    Input → 12
        ↓
    Square → 144
        ↓
    Digit Sum → 1 + 4 + 4 = 9
        ↓
    Compare → Not equal → Not neon
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and digit-based puzzles
    - Powers logic-based interview questions
    - Demonstrates digit manipulation and mathematical reasoning
"""