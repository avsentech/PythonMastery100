# Code #33: Check if a Number is a Palindrome
# Tier: Intermediate
# Goal: Determine if a number is a palindrome

num = int(input("Enter a number: "))
if str(num) == str(num)[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")

# Sample Input 1 (Palindrome)
"""
    121
"""

# Output1
"""
    Palindrome number
"""

# Sample Input 2 (Not Palindrome)
"""
    123
"""

# Output2
"""
    Not a palindrome number
"""

# Concept Breakdown
"""
    Concept          Description
    -----------------------------
    str(num)         Converts number to string for reversal
    [::-1]           Reverse the string
    Comparison       Checks if reversed string equal original
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Convert it to string
    - Reverse the string
    - Compare with original
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 121
        ↓
    Reverse → "121"
        ↓
    Compare → Equal → Palindrome number
    [End]

    OR

    Input → 123
        ↓
    Reverse → "321"
        ↓
    Compare → Not equal → Not palindrome
    [End]
"""

# Real-World Connection
"""
    - Used in number theory and pattern recognition
    - Powers logic puzzles and interview questions
    - Demonstrates string manipulation applied to numeric data
"""