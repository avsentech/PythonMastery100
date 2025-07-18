# Code 31: Check if a Number is a Perfect Number
# Tier: Intermediate
# Goal: Determine if a number is perfect

num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print("Perfect number")
else:
    print("Not a perfect number")

# Sample Input1 (Perfect)
"""
    28
"""

# Output1
"""
    Perfect number
"""

# Sample Input2 (Not Perfect)
"""
    12
"""

# Output2
"""
    Not a perfect number
"""

# Concept Breakdown
"""
    Concept             Description
    ---------------------------
    range(1,num)        Iterates through all numbers less than num
    num%i==0            Checks if i is a divisor
    sum_of_divisors     Accumulates valid divisors
    Comparison          Checks if sum equals original number
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Loop through numbers from 1 to num-1
    - If a number divides evenly → add to sum
    - Compare sum with original number
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 28
        ↓
    Divisors → 1, 2, 4, 7, 14
        ↓
    Sum → 28
        ↓
    Compare → Equal → Perfect number
    [End]

    OR

    Input → 12
        ↓
    Divisors → 1, 2, 3, 4, 6
        ↓
    Sum → 16
        ↓
    Compare → Not equal → Not perfect
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and cryptography
    - Powers logic-based interview questions
    - Demonstrates divisor analysis and mathematical reasoning
"""