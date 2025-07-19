# Code #59: Extract All Uppercase Letter from a String
"""
    🧠 Why Uppercase Extraction?
    Uppercase letters often indicate:
    - Initials, abbreviations, or names
    - Emphasized text, or special codes
    - Format-specific data flags
    This scroll isolates those bold entities for analysis or styling.
"""
# Tier: Intermediate
# Goal: Extract and return all uppercase alphabetic charaters

text = input("Enter a string: ")
uppercase = ""

for char in text:
    if char.isupper():
        uppercase += char

print("Extracted uppercase letters:", uppercase)

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    char.isupper()      Checks if the charater is uppercase
    Loop through text   Inspects every charater
    Accumulator logic   Collects matching charaters
"""

# How the Logic Works
"""
    - Loop through inpput
    - Check each charater
    - Append only uppercase letters
    - Present final result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "Welcome Boss Sena! Your ID is PYTHON123"
        ↓
    Loop → W ✔ e ✘ l ✘ ... B ✔ o ✘ ... Y ✔ P ✔ ...
        ↓
    Collect → "WBSYPTHON"
        ↓
    Output → Extracted uppercase letters
    [End]
"""

# Real-World Connection
"""
    - Helpful in text parsing, format detection, NLP prep
    - Used in initial extraction, code tokenization, and UI customization
    - Essential in identity preprocessing, acronym building, and document cleaning
"""