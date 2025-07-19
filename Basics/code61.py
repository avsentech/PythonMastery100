# Code #61: Count Uppercase and Lowercase Letters in a String
"""
    🧠 Why Count Cases?
    Understanding case distribution helps in:
        - Validating text format
        - Password strength checks
        - Custom parsing or preprocessing
        - Case-sensitive encoding tasks
"""
# Tier: Intermediate
# Goal:: Return the number of uppercase and lowercase letters from a string

text = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0

for char in text:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)

# Sample Input
"""
    PythonMastery Scroll#61 Rocks!
"""

# Output
"""
    Uppercase letters: 4
    Lowercase letters: 21
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    char.isupper()      Checks for uppercase letters
    char.islower()      Checks for lowercase letters
    Counter variables   Track count independently
"""

# How the Logic Works
"""
    - Loop over input string
    - Increment counters based on case
    - Display results with labels
"""

# Flowcart-Like Visualization
"""
    [Start]
        ↓
    Input → "PythonMastery Scroll#61 Rocks!"
        ↓
    Loop & Count → P ✔ → +1, y ✔ → +1, ... R ✔ → +1
        ↓
    Results → Upper: 4, Lower: 21
    [End]
"""

# Real-World Connection
"""
    - Used in form validation, style checkers, and machine learning features
    - Pwers logic in case-based rule engines and NLP format control
    - Helpful in building clear text classifiers and analyzers
"""

