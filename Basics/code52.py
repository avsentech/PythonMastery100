# Code #52: Replace All Vowels in a String with a Given Character
"""
    🧠 Why Replace Vowels?
    This scroll lets you mask or modify vowels, useful in text encoding, word games, speech-to-text filters, and data obfuscation.
    Example:
    - Input: "Python is legendary" with * → Output: "Pyth*n *s l*g*nd*ry"
"""
# Tier: Intermediate
# Goal: Replace all vowels (A,E,I,O,U) with a user-specified character

text = input("Enter a string: ")
replacement  = input("Enter replacement character: ")

vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char in vowels:
        result += replacement
    else:
        result += char

print("Modified string:", result)

# Sample Input
"""
    Enter a string: Python is legendary
    Enter replacement character: *
"""

# Output
"""
    Modified sttring: Pyth*n *s l*g*nd*ry
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    vowels = ...        Defines all uppercase/lowercase vowels
    Loop through text   Checks each character
    if char in vowels   Determines vowel match
    Replacement logic   Substitutes with custom character
"""

# How the Logic Works
"""
    - Accept a senternce and a replacement character
    - Loop through each character
    - Replace if vowel, else keep original
    - Print modified string
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "Python is legendary", replacement → "*"
        ↓
    Loop → P, y, t, h, o → * → n, i → * → ...
        ↓
    Build → "Pyth*n *s l*g*nd*ry"
        ↓
    Output → Modified string
    [End]
"""

# Real-World Connection
"""
    - Used in text obfuscation, word puzzles, and language filters
    - Useful for custom speech encoding, chatbot word masking, or playful string generation
    - Powers logic in captcha decoders, SMS filters, and text stylezers
"""