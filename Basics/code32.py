# Code #32: Check if a Number is a Strong Number
# Tier: Intermediate
# Goal: Determine if a number is a strong number

import math

num = int(input("Enter a number: "))
sum_of_factorials = 0

for digit in str(num):
    sum_of_factorials += math.factorial(int(digit))

if sum_of_factorials == num:
    print("Strong number")
else:
    print("Not a strong number")

# Concept Breakdown
"""
    Concept             Description
    ----------------------------------
    str(num)            Converts number to string for digit iteration
    math.factorial()    Calculates factorial of each digit
    sum_of_factorials   Accumulates factorials of digits
    Comparison          Checks if sum equals original number
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Convert to string to iterate digits
    - For each digit, calculate its factorial
    - Sum all factorials
    - Compare with original number
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 145
        ↓
    Digits → 1, 4, 5
        ↓
    Factorials → 1! + 4! + 5! = 145
        ↓
    Compare → Equal → Strong number
    [End]

    OR

    Input → 123
        ↓
    Digits → 1, 2, 3
        ↓
    Factorials → 1! + 2! + 3! = 9
        ↓
    Compare → Not equal → Not strong
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and algorithm puzzles
    - Powers logic-based interview questions
    - Demonstrates factorial computation and digit analysis
"""