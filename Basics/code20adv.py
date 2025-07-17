# Code #20: (Advanced Output): Character Frequency with Formatted Display
# Tier: Intermediate
# Goal: Display frequency of each character in aligned, readable format

text = input("Enter a string: ").lower()
freq = {}

for char in text:
    if char.isalpha(): # Optional: ignore spaces, digits, symbols

        freq[char] = freq.get(char, 0) + 1

print("\nCharacter Frequency Report")
print("----------------------------")
for key in sorted(freq.keys()):
    print(f"{key} → {freq[key]}")

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    .get()              Safely retrieves existing value or returns default 0
    sorted()            Sorts dictionary keys alphabetically before display
    isalpha()           Filters out non-letter characters
    Formatted Output    Aligns and prints results clearly
"""

# How the Logic Works
"""
    - Normalize input using .lower()
    - Loop through each character
        → Only consider alphabet letters
        → Count frequency using dictionary
    - Sort and print each character with its frequency
"""

# Flowchart-Like Visualization
"""
    [Input → text]
        ↓
    Normalize text → .lower()
        ↓
    Initialize freq = {}
        ↓
    FOR each char in text:
        ├── If char is alphabet → update freq count
        └── Else → skip
        ↓
    Sort keys in freq
        ↓
    FOR each key:
        → Print key → freq[key]
    [End]
"""

# Real-World Connection
"""
    - Mirrors character distribution tools in editors, spell checkers, and language learners
    - Used in code reviews (e.g., variable name analysis), encryption scanners, and NLP tokenizers
    - Vital for linguistic studies, style-checking, and building AI prompts with balanced tokens
"""