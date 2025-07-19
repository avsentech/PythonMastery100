# Code #51: Reverse Each word in a Sentence
"""
    🧠 What Does It Mean?
    This scroll flips each word individually, keeping their original positions intact.
    Example:
    - "Python Mastery is Legendary" → "nohtyP yretsaM si yradnegeL"
    Useful for text filters, puzzles, and data masking techniques
"""
# Tier: Intermediate
# Goal: Reverse the characters inside each word, not the word order

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)

print("Reverrsed word sentence:", result)

# Sample Input
"""
    Python mastery is legendary
"""

# Output
"""
    Reversed-word sentence: nohtyP yretsam si yradnegeL
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    .split()            Breaks sentence into list of words
    word[::-1]          Reverse each word using slicing
    "".join(...)        Reassembles reversed words into a sentence
"""

# How the Logic Works
"""
    - Accept a sentence from the user
    - Split sentence into words
    - Reverse each word using slicing
    - Join reversed words with spaces
    - Print the final strin
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "Python mastery is legendary"
        ↓
    Words → ['Python', 'mastery', 'is', 'legendary']
        ↓
    Reverse → ['nohtyP', 'yretsam', 'si', 'yradnegeL']
        ↓
    Join → "nohtyP yretsam si yradnegeL"
    [End]
"""

# Real-World Connection
"""
    - Used in cryptographic obfuscation, language challenges, and data transformations
    - Powers logic in reverse-reading apps, text decoders, and brain teasers
"""