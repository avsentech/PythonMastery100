# Code #25: Count Words in a Sentence
# Tier: Intermediate
# Goal: Count how many words are in a given sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count: ", len(words))

# Sample Input
"""
    Python is powerful and elegant
"""

# Output
"""    word count: 5
"""

# Concept Breakdown
"""
    Concept         Description
    ---------------------------
    input()         Accepts user sentence
    .split()        Splits sentence into words using spaces
    len()           Counts number of words
    List            Stores individual words
"""

# How the Logic works
"""
    - Accept a sentence from the user
    - Use .split() to break it into words (default delimiter: space)
    - Count the number of words using len()
    - Print the result
"""

# Flowchar-Like Visualization
"""
    [Start]
        ↓
    Input → "Python is powerful and elegant"
        ↓
    Split → ["Python", "is", "powerful", "and", "elegant"]
        ↓
    Count → len(words) = 5
        ↓
    Print → Word count: 5
    [End]
"""
