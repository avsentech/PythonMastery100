# Coe #47: Remove Duplicate Characters from a string
"""
    🧠 Why Remove Duplicates?
    Removing duplicate characters helps create distinct sets, optimize data storage, and eliminate redundant noise—especially useful in tokenization, compression, and clean-up routines.
    Example:
    - "banana" → "ban"
    - "apple" → "aple"
"""
# Tier: Inermediate
# Goal: Remove repeated characters while preserving the first occurence order

text = input("Enter a string: ")
seen = set()
result = ""

for char in text:
    if char not in seen:
        seen.add(char)
        result += char

print("String after removing duplicates:", result)

# Sample Input
"""
    banana
"""

# Output
"""
    string after removing duplicates: ban
"""

# Concept Breakdown
"""
    Concept                 Description
    -------------------------------------
    set()                   Tracks characters we've already seen
    result += char          Builds new string only with unique characters
    Looop over string       Preserves original character order
"""

# How the Logic Works
"""
    - Accept a string from the user
    - Use a set to store seen characters
    - Loop through each character
    - Add only if unseen
    - Print cleaned string
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "banana"
        ↓
    Loop → b ✔ a ✔ n ✔ a ✘ n ✘ a ✘
        ↓
    Result → "ban"
    [End]    
"""

# Real-World Connection
"""
    - Used in data deduplication and normalization
    - Useful in web scraping, text cleaning, and preprocessing
    - Powers logic in compression algorithms and search filter
"""
