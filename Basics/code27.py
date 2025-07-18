# Code #28: Count Vowels and Consonants in a Sentence
# Tier: Intermediate
# Goal: Count how many vowels and consonants are in a given sentence

sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    .lower()        Normalizes case for comparison
    isalpha()       Filters only alphabetic characters
    in vowels       Checks if character is a vowel
    Counters        Tracks vowels and consonants separately
"""

# How the Logic Works
"""
    - Accept a sentence from the user
    - Convert to lowercase
    - Loop through each character
    - If it's a letter:
    - If it's a vowel → increment vowel_count
    - Else → increment consonant_count
    - Print both counts
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "Python is powerful"
        ↓
    Lowercase → "python is powerful"
        ↓
    Loop through each character
        ├── If alphabet:
        │     ├── If vowel → vowel_count++
        │     └── Else → consonant_count++
        ↓
    Print counts
    [End]
"""

# Real-World Connection
"""
    - Used in speech processing, phonetic analysis, and text scoring
    - Powers readability metrics and linguistic profiling
    - Forms the basis of NLP preprocessing and sentiment analysis
"""