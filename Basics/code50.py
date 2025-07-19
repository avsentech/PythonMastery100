# Code #50: Convert String to Title Case Without
"""
    🧠 What is Title Case?
    Title Case means capitalizing the first letter of every word while keeping the rest lowercase.
    Example:
    - "python mastery is legendary" → "Python Mastery Is Legendary"
    This scroll manually replicates .title() to build logic mastery, not just rely on built-in functions.
"""
# Tier: Intermediate
# Goal: Capitalize the first letter of every word without using .title()

sentence = input("Enter a sentence: ")
words = sentence.split()
title_cased = " ".join(word[0].upper() + word[1:].lower() if word else "" for word in words)
    
print("Title-cased string:", title_cased)

# Sample Input
"""
    python mastery is legendary
""" 

# Output
"""
    Title-cased string: Python Mastery Is Legendary
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    .split()            Breaks sentence into list of words
    word[0].upper()     Uppercase first letter
    word[1:].lower()    Lowercases rest of the word
    "".join(...)        Recombines title-cased words
"""

# How the Logic Works
"""
    - Accept a sentence from the user
    - Split into words
    - Apply capitalization logic to each word
    - Rejoin and print the final sentenc
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "python mastery is legendary"
        ↓
    Split → ['python', 'mastery', 'is', 'legendary']
        ↓
    Transform → ['Python', 'Mastery', 'Is', 'Legendary']
        ↓
    Join → "Python Mastery Is Legendary"
    [End]
"""

# Real-World Connection
"""
    - Used in document formatting, UI display, and automated naming conventions
    - Powers logic in text generation tools, email builders, and slug converters
"""