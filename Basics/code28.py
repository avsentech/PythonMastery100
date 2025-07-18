# Code #26: Reverse Words in a Sentence
# Tier: Intermediate
# Goal: Reverse the order of words in a given sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = " ".join(reversed(words))
print("Reversed sentence:", reversed_sentence)

# Sample input
"""
    Python is powerful
"""

# Output
"""
    Reversed sentence: powerful is Python
"""

# Concept Breakdown
"""
    Concept     Description
    -----------------------
    .split()    Splits sentence into words
    reversed()  Reverses the list of words
    "".join()   Joins the reversed list back into a sentence
"""

# How the Logice Works
"""
    - Accept a sentence from the user
    - Split it into words
    - Reverse the list of words
    - Join them back into a sentence
    - Print the result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "Python is powerful"
        ↓
    Split → ["Python", "is", "powerful"]
        ↓
    Reverse → ["powerful", "is", "Python"]
        ↓
    Join → "powerful is Python"
        ↓
    Print
    [End]
"""

# Real-World Connection
"""
    - Used in NLP preprocessing and chatbot formatting
    - Powers reverse indexing and sentence restructuring
    - Useful in text-based games and command parsing
"""