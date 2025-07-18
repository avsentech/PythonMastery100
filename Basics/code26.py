# Code27: Check if a string is a Palindrome
# Tier: Intermediate
# Goal: Determine if a given string reads the same forward and backward

text = input("Enter a word: ").lower()
if text == text[::-1]:
    print("Palandrome")
else:
    print("Not a palandrome")

# Sample Input1 (Palindrome)
"""
    madam
"""

# Output1
"""
    Palindrome
"""

# sample Input 2 (Not a Palindrome)
"""
    python
"""

# Output2
"""
    Not a palindrome
"""

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    .lower()        Normalizes case for comparison
    [::-1]          Reverse the string
    ==              Compares original and reversed string
"""

# How the Logic Works
"""
    - Accept a word from the user
    - Convert to lowercase for case-insensitive comparison
    - Reverse the string using slicing
    - Compare original and reversed
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
    ↓
    Input → "madam"
    ↓
    Lowercase → "madam"
    ↓
    Reverse → "madam"
    ↓
    Compare → Equal → Palindrome
    [End]

    OR

    Input → "python"
    ↓
    Lowercase → "python"
    ↓
    Reverse → "nohtyp"
    ↓
    Compare → Not equal → Not a palindrome
    [End]
"""

# Real-World Connection
"""
    - Used in text validation, DNA sequence analysis, and linguistic studies
    - Powers logic puzzles, interview questions, and string manipulation tasks
    - Forms the basis of symmetric pattern detection in algorithms
"""

