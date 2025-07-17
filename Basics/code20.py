# Code #20: Frequency of Characters in a string
# Tier: Intermediate
# Goal: Count how often each character appears in a given string

text = input("Enter a string:").lower()
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for key, value in freq.items():
    print(key, "→", value)

# Concept Breakdown
"""
    Concept         Description
    ---------------------------
    .lower()        Normalizes case for consistent comparison
    Dictionary      Stores each character as a key, count as value
    Loop            Traverses each character in string
    Condition       Updates count if key exists, or creates new entry
"""

# How the Logic Works
"""
    - Convert string to lowercase for uniformity
    - Initialize empty dictionary
    - Loop through each character:
    → If character already exists in freq, increment its value
    → Else, add key with initial value of 1
    - Finally, loop through freq and print each character and its count
"""

# Flowchart-Like Visualization
"""
    [Input → text]
        ↓
    Convert to lowercase
        ↓
    Initialize empty dict: freq = {}
        ↓
    FOR each char in text:
        ├── If char in freq → freq[char] += 1
        └── Else → freq[char] = 1
        ↓
    FOR each key, value in freq:
        → Print key → value
    [End]
"""

# Real-World Connection
"""
    - Foundational for building word/letter analytics, spell checkers, and predictive typing
    - Used in spam filters, language analysis, encryption tools, and digital forensics
    - Helps visualize text patterns (like heatmaps, frequency graphs) in NLP models
"""

# Want to exclude spaces or symbols? Add a condition like:
"""
if char.isalpha():
"""