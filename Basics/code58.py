# Code #58: Extract All Special Charaters from a string
"""
    🧠 What Are Special Characters?
    Special characters are anything that’s not a letter or digit—symbols, punctuation, etc.
    Examples: @, #, !, %, &, *, ^, (, )
    This scroll is essential for data cleaning, security scanning, and symbol-based filtering
"""
# Tier: Intermediate
# Goals: Extract and display all special symbols from a given string

text = input("Enter a string: ")
special_chars = ""

for char in text:
    if not char.isalnum() and not char.isspace():
        special_chars += char

print("Extracted special characters:", special_chars)

# Sample Input
"""
    Welcome @Sena! Your ID is A#123B*456
"""

# Output
"""
    Extracted special characters: @!#*.
"""

# Concept Breakdown
"""
    Concept                     Description
    ----------------------------------------
    char.isalnum()              Checks if character is alphanumeric (a-z, 0-9)
    char.isspace()              Filters out spaces
    Special symbols remains     Only characters that are neither alphanumeric nor whitespace
"""

# How the Logic Works
"""
    - Loop through every character
    - Ignore letters, digits, and spaces
    - Collect only punctuation/symbol characters
    - Return final string of special characters
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "Your ID: A#123B*456!"
        ↓
    Loop → Y ✘ o ✘ u ✘ r ✘ (space ✘) I ✘ D ✘ : ✔
        ↓
    Collect → ['#', '*', '!']
        ↓
    Output → "@!#*. "
    [End]
"""

# Real-World Connection
"""
    - Used in firewall monitoring, form validation, web scriping cleanup
    - Essential in building password-strength checkers, symbol filters, and text sanitizers
    - Powers token-based analysis, emoticon tracking, and syntax filtering
"""