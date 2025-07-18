# Code #42: Check if a Number is a Happy Number
"""
    🧠 What is a Happy Number?
    A Happy Number is a number that eventually reaches 1 when replaced repeatedly by the sum of the squares of its digits.
    If it loops endlessly in a cycle that doesn’t include 1, it’s not happy.
    Example:
    - 19 → 1^2 + 9^2 = 82 → 8^2 + 2^2 = 68 → … → 1 → ✅ Happy
    - 4 → loops in cycle → ❌ Not Happy
"""
# Tier: Intermediate
# Goal: Determine if a number is a happy number

def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

num = int(input("Enter a number: "))
if is_happy(num):
    print("Happy number")
else:
    print("Not a happy number")

# Sample Input1(Happy)
"""
    19
"""

# Output1
"""
    Happy number
"""

# Sample Input2(Not Happy)
"""
    4
"""

# Output2
"""
    Not a happy number19 
"""

# Concept Breakdown
"""
    Concept         Description
    ---------------------------
    set()           Tracks seen numbers to detect cycles
    sum(digit^2)    Squares each digit and sums
    Loop            Repeats until 1 or cycle detected
    Function        Encapsulates logic for reuse
"""

# How the Logic Works
"""
    [Start]
        ↓
    Input → 19
        ↓
    Loop → 1^2 + 9^2 = 82 → 8^2 + 2^2 = 68 → … → 1
        ↓
    Result → Happy number
    [End]

    OR

    Input → 4
        ↓
    Loop → 4^2 = 16 → 1^2 + 6^2 = 37 → … → cycle
        ↓
    Result → Not Happy
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and recursive puzzles
    - Powers logic-based interview questions
    - Demonstrates cycle detection and digit transformation
"""
