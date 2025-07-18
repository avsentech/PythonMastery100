# Code #40: Check if a Number is a Fascinating Number
"""
    🧠 What is a Fascinating Number?
    A Fascinating Number is a number with at least 3 digits, where when multiplied by 2 and 3 and concatenated with the original, the result contains all digits from 1 to 9 exactly once.
    Example:
    - 192 → 192, 384, 576 → concat: 192384576 → ✅ Fascinating
    - 853 → 853, 1706, 2559 → concat: 85317062559 → ❌ Not Fascinating
"""
# Tier: Intermediate
# Goal: Determine if a number is a fascinating number

num = int(input("Enter a number: "))

if num >= 100:
    concat = str(num) + str(num * 2) + str(num * 3)
    digits = sorted(concat)

    if digits == ['1','2','3','4','5','6','7','8','9']:
        print("Fascinating number")
    else:
        print("Not a fascinating number")

else:
    print("Not a fascinating number (less than 3 digits)")

# Sample Input 1(Fascinating)
"""
    192
"""

# Output 1
"""
    Fascinating number
"""

# Sample Input 2(Not Fascinating)
"""
    853
"""

# Output2
"""
    Not a fascinating number
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    num * 2, num * 3    Multiplies original number
    str() + concat      Combines all three numbers
    sorted()            Sorts digits for comparison
    Comparison          Checks if digits match 1-9 exactly
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Multiply by 2 and 3
    - Concatenate all three numbers
    - Sort the digits
    - Compare with ['1'–'9']
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 192
        ↓
    Concat → "192384576"
        ↓
    Digits → ['1','2','3','4','5','6','7','8','9']
        ↓
    Compare → Match → Fascinating number
    [End]

    OR

    Input → 853
        ↓
    Concat → "85317062559"
        ↓
    Digits → Repeats or missing
        ↓
    Compare → Not match → Not Fascinating
    [End]
"""

# Real-World Connection
"""
    - Used in digit-based puzzles and pattern recognition
    - Powers logic-based interview questions
    - Demonstrates string manipulation and digit uniqueness
"""