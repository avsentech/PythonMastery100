# Code #41: Check if a Number is a Disarium Number
"""
    🧠 What is a Disarium Number?
    A Disarium Number is a number where the sum of its digits powered by their respective positions equals the number itself.
    Example:
    - 135 → 1^1 + 3^2 + 5^3 = 135 → ✅ Disarium
    - 89 → 8^1 + 9^2 = 89 → ✅ Disarium
    - 123 → 1^1 + 2^2 + 3^3 = 36 → ❌ Not Disarium
"""
# Tier: Intermediate
# Goal: Determine if a number is a disarium number

num = int(input("Enter a number: "))
sum_of_powers =  0

for idx, digit in enumerate(str(num), start=1):
    sum_of_powers += int(digit) ** idx

if sum_of_powers == num:
    print("Disarium number")
else:
    print("Not a disarium number")

# Sample Input1(Disarium)
"""
    135
"""

# Outut 1
"""
    Disarium number
"""

# Sample Input 2(Not Disaruim)
"""
    123
"""

# Output2
"""
    Not a disarium number
"""

# Concept Breakdown
"""
    Concept         Description
    ---------------------------
    enumerate()     Tracks digit position starting from 1
    int(digit)**idx Raises digit to its position
    sum_of_powers   Accumulates powered digits
    Comparison      Checks if sum equals original number
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Loop through digits with their positions
    - Raise each digit to its position
    - Sum the results
    - Compare with original number
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 135
        ↓
    Digits → 1, 3, 5
    Positions → 1, 2, 3
    Sum → 1^1 + 3^2 + 5^3 = 135
        ↓
    Compare → Equal → Disarium number
    [End]

    OR

    Input → 123
        ↓
    Sum → 1^1 + 2^2 + 3^3 = 36
        ↓
    Compare → Not equal → Not Disarium
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and digit-based puzzles
    - Powers logic-based interview questions
    - Demonstrates positional indexing and exponentiation
"""