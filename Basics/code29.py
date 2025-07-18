# Code #29: Check if a Number is an Armstrong Number
# Tier: Intermediate
# Goal: Determine if a number is an Armstrong number

num = int(input("Enter a number: "))
sum_of_powers = 0
digits = len(str(num))

for digit in str(num):
    sum_of_powers += int(digit) ** digits

if sum_of_powers == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Sample Input1 (Armstrong)
"""
    153
"""

# Output1
"""
    Armstrong number
"""

# Sample Input 2 (Not Armstrong)
"""
    123
"""

# Output2
"""
    Not an Armstrong number
"""

# Concept Breakdown
"""
    Concept             Description
    ----------------------------
    str(num)            Converts number to string for digit iteration
    len(str(num))       Gets number of digits
    int(digit) ** n     Raises each digit to the power of total digits
    Comparison          Checks if sum equals original number
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Count its digits
    - Raise each digit to the power of total digits
    - Sum the results
    - Compare with original number
    - Print result
"""
# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 153
        ↓
    Digits → 3
        ↓
    Sum → 1³ + 5³ + 3³ = 153
        ↓
    Compare → Equal → Armstrong
    [End]

    OR

    Input → 123
        ↓
    Digits → 3
        ↓
    Sum → 1³ + 2³ + 3³ = 36
        ↓
    Compare → Not equal → Not Armstrong
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and algorithm puzzles
    - Powers logic-based interview questions
    - Demonstrates digit manipulation and mathematical reasoning
"""