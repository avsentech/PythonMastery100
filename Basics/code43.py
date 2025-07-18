# Code #43: Check if a Number is a Mgic Number
"""
    🧠 What is a Magic Number?
    A Magic Number is a number where the recursive sum of its digits eventually becomes 1.
    Example:
    - 199 → 1 + 9 + 9 = 19 → 1 + 9 = 10 → 1 + 0 = 1 → ✅ Magic
    - 123 → 1 + 2 + 3 = 6 → ❌ Not Magic
"""
# Tier: Intermediate
# Goal: Determine if a number is a magic number

def digit_sum(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

num = int(input("Enter a number: "))
if digit_sum(num) == 1:
    print("Magic number")
else:
    print("Not a magic number")

# Sample Input1 (Magic)
"""
    199
"""

# Output1
"""
    Magic number
"""

# Sample Input 2(Not Magic)
"""
    123
"""

# Output 2
"""
    Not a magic number
"""

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    sum()           Adds digits of the numberr
    while n > 9     Continues until single-digit
    Recursion-like  Repeated digit reduction
    Comparison      Checks if final digit is 1
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Sum its digits repeatedly
    - Stop when result is single-digit
    - If result is 1 → Magic
    - Else → Not Magic
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 199
        ↓
    Sum → 1 + 9 + 9 = 19 → 1 + 9 = 10 → 1 + 0 = 1
        ↓
    Compare → Equal → Magic number
    [End]

    OR

    Input → 123
        ↓
    Sum → 1 + 2 + 3 = 6
        ↓
    Compare → Not equal → Not Magic
    [End]
"""

# Real-World Connection
"""
    - Used in numerology and digit-based puzzles
    - Powers logic-based interview questions
    - Demonstrates recursive digit reduction
"""