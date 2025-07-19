# Code #49: Check if a String is a Pangram
"""
    🧠 What is a Pangram?
    A Pangram is a sentence that contains every letter of the alphabet at least once.
    Example:
    - "The quick brown fox jumps over the lazy dog" → ✅ Pangram
    - "Hello world" → ❌ Not Pangram
"""
# Tier: Intermediate
# Goal: Detect wwhether a string includes all 26 alphabet letters

import string

def is_pangram(text):
    text = text.lower()
    letters = set(text)
    return set(string.ascii_lowercase).issubset(letters)

sentence  = input("Entera sentence: ")
if is_pangram(sentence):
    print("Pangram")
else:
    print("Not a pangram")

# Sample Input1(Pangram)
"""
    The quick brown fox jumps over the lazy dog
"""
# Output1
"""
    Pangram
"""

# Sample Input2(Not Pangram)
"""
    Python mastery grows with practice
"""

# Output2
"""
    Not a pangram
"""

# Concept Breakdown
"""
    Concept                     Description
    ----------------------------------------
    string.ascii_lowercase      Reference to all lowercase alphabet characters
    set(text)                   Unique letters from input
    issubset()                  Verifies full alphabet is present
"""

# How the Logic Works
"""
    - Accept a sentence from the user
    - Convert to lowercase
    - Create a set of characters
    - Check if all 26 alphabets are present
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "The quick brown fox jumps over the lazy dog"
        ↓
    Convert & Create Set
        ↓
    Check if contains A-Z
        ↓
    Result → Pangram
    [End]

    OR

    Input → "Python mastery grows with practice"
        ↓
    Missing letters
        ↓
    Result → Not Pangram
    [End]
"""

# Real-World Connection
"""
    - Used in font testing, typewriter demos, and language design
    - Powers text generation benchmarks
    - Enhances exercises in spelling, writing, and data completeness checks
"""