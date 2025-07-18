# Code #39: Check if a Numberis a Tech Number
"""
    A Tech Number is a number with even number of digits, which when split into two equal halves and added, then squared, gives back the original number.
        Example:
        - 2025 → split: 20 + 25 = 45 → 45^2 = 2025 → ✅ Tech
        - 3025 → split: 30 + 25 = 55 → 55^2 = 3025 → ✅ Tech
        - 1234 → split: 12 + 34 = 46 → 46^2 = 2116 → ❌ Not Tech
"""
# Tier: Intermediate
# Goal: Determine if a number is a tech number

num = int(input("Enter a number: "))
num_str = str(num)

if len(num_str) % 2 == 0:
    mid = len(num_str) // 2
    first_half = int(num_str[:mid])
    second_half = int(num_str[mid:])
    total = first_half +second_half

    if total ** 2 == num:
        print("Tech number")
    else:
        print("Not a tech number")

else:
    print("not a tech number (odd number of digits)")

# Sample Input1 (Tech)
"""
    2025
"""

# Output1
"""
    Tech Number
"""

# Sample Input2 (Not Tech)
"""
    1234
"""

# Output 2
"""
    Not a tech number
"""

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    str(num)        Converts number to string
    len(num_str)    Checks digit count
    [:mid] & [mid:] Splits into halves
    total** 2       Squares the sum of halves
    Comparison      Checks if result equals original number
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Check if it has even number of digits
    - Split into two halves
    - Add the halves
    - Square the sum
    - Compare with original number
    - Print result
"""

# Fowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 2025
        ↓
    Split → 20 + 25 = 45
        ↓
    Square → 45^2 = 2025
        ↓
    Compare → Equal → Tech number
    [End]

    OR

    Input → 1234
        ↓
    Split → 12 + 34 = 46
        ↓
    Square → 46^2 = 2116
        ↓
    Compare → Not equal → Not Tech
    [End]
"""

#Real-World Connection
"""
    - Used in digit-based puzzles and number theory
    - Powers logic-based interview questions
    - Demonstrates string slicing and arithmetic validation
"""