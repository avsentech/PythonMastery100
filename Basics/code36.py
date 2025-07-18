# Code #36: Check if a Number is a Spy Number
"""
    🧠 What is a Spy Number?
        A Spy Number is a number where the sum of its digits equals the product of its digits.
        Example:
            - 123 → 1 + 2 + 3 = 6, 1 × 2 × 3 = 6 → ✅ Spy
            - 112 → 1 + 1 + 2 = 4, 1 × 1 × 2 = 2 → ❌ Not Spy
"""
# Tier: Intermediate
# Goal: Determine if a number is a spy number

num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]

digit_sum = sum(digits)
digit_product = 1
for d in digits:
    digit_product *= d

if digit_sum == digit_product:
    print("Spy number")
else:
    print("Not a spy number")

# Sample Input1 (Spy)
"""
    123
"""

# Output1
"""
    Spy number
"""

# sample Input2 (Not Spy)
"""
    112
"""

# Output2
"""
    Not a spy number
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    str(num)            Converts number to string for digit iteration
    sum()               Adds all digits
    Loop for product    Multiples digits one by one
    Comparison          Checks if sum equals product
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Convert to list of digits
    - Calculate sum of digits
    - Calculate product of digits
    - Compare both
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 123
        ↓
    Digits → [1, 2, 3]
        ↓
    Sum → 6
    Product → 6
        ↓
    Compare → Equal → Spy number
    [End]

    OR

    Input → 112
        ↓
    Digits → [1, 1, 2]
        ↓
    Sum → 4
    Product → 2
        ↓
    Compare → Not equal → Not Spy
    [End]
"""

# Real-World Connection
"""
    - Used in digit-based puzzles and number theory
    - Powers logic-based interview questions
    - Demonstrates arithmetic operations on digit sequences
"""