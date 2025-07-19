# Code #57: Swap Case of Each Character in a String
"""
    🧠 What Is Case Swapping?
    This scroll transforms each uppercase letter to lowercase, and each lowercase letter to uppercase.
    Example:
        - "Python Mastery" → "pYTHON mASTERY"
        It’s a simple trick that powers formatting, encryption, and quirky text styles.
"""
# Tier: Intermediate
# Goal: Reverse the case of all alphabetic charaters

text = input("Enter a string: ")
swapped = ""

for char in text:
    if char.isupper():
        swapped += char.lower()
    elif char.islower():
        swapped += char.upper()
    else:
        swapped += char

print("Swapped case string:", swapped)

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    char.isupper()      Detects uppercase letters
    char.lower()        Converts to lowercase
    char.islower()      detects lowercase letters
    char.upper()        Converts to uppercase
    Non-alpha handling  Keeps digits and symbols untouched
"""

# How the Logic Works
"""
    - Accept a string from the user
    - Loop through each character
    - Flip case based on letter Type
    - Preserve non-alphabetic characters
    - Return transformed string  
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "Python123 Mastery"
        ↓
    Loop → P ✔ → p, y ✔ → Y, t ✔ → T, ... 1 ✘ → 1
        ↓
    Result → "pYTHON123 mASTERY"
        ↓
    Output → Swapped case string
    [End]
"""

# Real-World Connection
"""
    - Used in text formatting tools, mocking text filters, and stylistic generators
    - Powers logic in encryption preprocessng, identity masking, and case-agnostic searches
    - Also useful for coding interviews and regex challenges
"""