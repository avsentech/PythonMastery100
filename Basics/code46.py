# Code #46: Check if Two strings Are Anagrams
"""
    🧠 What is an Anagram?
    An Anagram is a word or phrase formed by rearranging the letters of another word using all original characters exactly once.
    Example:
    - "listen" ↔ "silent" → ✅ Anagram
    - "hello" ↔ "world" → ❌ Not Anagram
"""
# Tier: Intermediate
# Goal: Determine if two strings are anagrams (case-insensitive, no extra characters)

def is_anagram(str1, str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    return sorted(str1) == sorted(str2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_anagram(s1, s2):
    print("Anagram")
else:
    print("Not an anagram")

# Sample Input1 (Anagram)
"""
    listen
    silent
"""

# Output1
"""
    Anagram
"""

# sample Input2 (Not Anagram)
"""
    hello
    world
"""

# Output2
"""
    Not an anagram
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    .replace(" ","")    Remove spaces
    .lower()            Ensures case-insensitivity
    sorted()            Compares character order
    ==                  checks if sorted lists match
"""

# How the Logic Works
"""
    - Accept two strings from the user
    - Clean strings: remove spaces, lowercase
    - Sort characters in each string
    - Compare sorted lists
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "listen", "silent"
        ↓
    Clean → lowercase + no spaces
        ↓
    Sort → ['e','i','l','n','s','t']
        ↓
    Compare → Equal → Anagram
    [End]

    OR

    Input → "hello", "world"
        ↓
    Sort → Different letters
        ↓
    Compare → Not equal → Not anagram
    [End]
"""

# Real-World Connection
"""
    - Used in cryptography, spell checkers, word games
    - Powers algorithms in NLP and data normalization
    - Common in interview questions on string manipulation
"""