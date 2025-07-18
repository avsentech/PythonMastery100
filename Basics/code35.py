# Code #35: Check if a Number is a Harshad Number
"""
    What is a Harshad Number?
    A Harshad Number (also called a Niven number) is a number that is divisible by the sum of its digits.
    Example:
        - 18 → 1 + 8 = 9 → 18 \div 9 = 2 → ✅ Harshad
        - 19 → 1 + 9 = 10 → 19 \div 10 = 1.9 → ❌ Not Harshad
"""
# Tier: Intermediate
# Goal: Determine if a number is a Harshad number

num = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(num))

if num % digit_sum == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")

# Sample Input2 (Harshed)
"""
    18
"""

# Output1
"""
    Harshad number
"""

# Sample Input2 (Not Harshed)
"""
    19
"""

# Output2
"""
    Not a Harshad number
"""

# Concept Breakdown
"""
    Concept         Description
    ---------------------------
    str(num)        Converts number to string for digit iteration
    sum()           Adds all digits of the number
    %               Checks divisibility
    Comparison      Deterines if number is divisible by digit suum
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Convert to string and sum its digits
    - Check if number is divisible by digit sum
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 18
        ↓
    Digit Sum → 1 + 8 = 9
        ↓
    Check → 18 % 9 == 0 → Harshad number
    [End]

    OR

    Input → 19
        ↓
    Digit Sum → 1 + 9 = 10
        ↓
    Check → 19 % 10 != 0 → Not Harshad
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and divisibility tests
    - Powers logic-based interview questions
    - Demonstrates digit manipulation and modular arithmetic
"""