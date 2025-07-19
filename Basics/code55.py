# Code #55: Extract All Digits from a String
"""
    🧠 Why Extract Digits?
    This scroll isolates numerical data embedded within text, which is essential in:
        - Parsing log files
        - Scraped content from the web
        - Form validation and preprocessing
        - ID and reference extraction
"""
# Tier: Intermediate
# Goal: Display only the digits found inside a string

text = input("Enter a string: ")
digits = ""

for char in text:
    if char.isdigit():
        digits += char

print("Extracted digits:", digits)

# Sample Input
"""
    My number is 98764537464 and my birth year is 1984
"""

# Output
"""
    Extracted digits: 987645374641984
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    char.isdigit()      Checks if character is a numberic digit
    Loop over text      Iterates through entire input
    += accumulator      Builds digit-only result string
"""

# How the Logic Works
"""
    - Accept text from the user
    - Loop over every character
    - Add only digits to result
    - Display final output
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "My number is 9876543210"
        ↓
    Loop → M ✘ y ✘ n ✘ u ✘ m ✘ ... 9 ✔ 8 ✔ 7 ✔ ...
        ↓
    Collect → "9876543210"
        ↓
    Output → Extracted digits
    [End]
"""

# Real-World Connection
"""
    - Used in parsing strunctured/unstructured documents
    - Power chatbot sanitaization, email scrapers, and form validators
    - Vital in extract-transform-load(ETL) options and data wrangling
"""
