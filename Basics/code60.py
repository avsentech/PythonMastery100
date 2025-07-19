# Code #60: Extract All Lowercase Lettersfrom a string
"""
    🧠 Why Lowercase Extraction?
    Lowercase letters are the backbone of most text:
    - Forming majority of natural language
    - Often used in passwords, tokens, or identifiers
    - Critical for pattern detection and subtle formatting
    This scroll extracts all characters in lowercase, leaving behind symbols, digits, and uppercase flair
"""
# Tier: Intermediate
# Goal: Display only lowercase alphabet characters from a string

text = input("Enter a string: ")
lowercase = ""

for char in text:
    if char.islower():
        lowercase += char

print("Extracted lowercase letters:", lowercase)

# Sample Input
"""
    My ID is A123b456c and pythonROCKS
"""

# Output
"""
    Extracted lowercase letters: yisbbcpython
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    char.islower()      Detects lowercase letters
    Loop over text      Traverses each character
    Accumulator         Builds final lowercase string
"""

# How the Logic Works
"""
    - Take input string
    - Check each character's case
    - Collect only lowercase characters
    - Print refined output
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "My ID is A123b456c and pythonROCKS"
        ↓
    Loop → M ✘ y ✔ I ✘ D ✘ ... b ✔ c ✔ ...
        ↓
    Collect → "yisbbcpython"
        ↓
    Output → Extracted lowercase letters
    [End]
"""

# Real-world Connection
"""
    - Useful for language processing, password parsing, and format enforcement
    - Powers logic in pattern tracking, data cleaning, and text scoring
    - Frequently needed in normalization routines and case-based classification
"""