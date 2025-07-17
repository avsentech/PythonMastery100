# Code #15: Count Vowels in a String
# Tier: Intermediate
# Goal: Analyze a string and count how many vowels it contains

word = input("Enter a word: ").lower()
count = 0

for char in word:
    if char in "aeiou":
        count += 1

print("Vowel count:", count)

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    String Operatoin    .lower() ensures case consistency
    Loop                Iterates through each character in the string
    Membership Test     in checks if character is a vowel
    Counter Variable    count tracks number of vowel matches
"""

# How the Logic Worls
"""
    - Ask user for a word
    - Convert word to lowercase
    - Loop through each character
    - If character is a vowel → increment count
    - Display the final coun 
"""

# Flowchart-Like Visualization
"""
    [Input → word]
        ↓
    Convert to lowercase
        ↓
    Initialize count = 0
        ↓
    FOR each char in word:
        ├── If char in "aeiou" → count += 1
        └── Else → continue
        ↓
    Print count
    [End]
"""

# Real-World Connection
"""
    - Powers text analytics: checking readability, linguistic processing, and vowel-heavy words
    - Forms foundation for building spell-check tools, speech training apps, or interactive word games
    - Helps in voice interfaces (vowels = vocal sound units), and even tuning NLP models
"""