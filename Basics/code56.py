# Code #56: Extract All Alphabet Characters from a String
"""
    🧠 Why Extract Alphabets?
    This scroll isolates letters only, removing digits, symbols, and whitespace—perfect for:
    - Filtering scraped data
    - Validating inputs
    - Creating clean text datasets
    - Preprocessing strings for NLP
"""
# Tier: Intermediate
# Goal: Return a string containing only alphabetic characters

text = input("Enter a string: ")
alphabets = ""

for char in text:
    if char.isalpha():
        alphabets += char

print("Extracted alphabets:", alphabets)

# Sample Input
"""
    My ID is A123B4561
"""

# Output
"""
    Extracted alphabets: MyIDisAB
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    char.isalphs()      Checks if character is a letter
    Loop through text   Iterates through entire input
    Accumulator logic   Builds new string of valid characters
"""

# How the Logic Works
"""
    - Accept user input
    - Loop through each character
    - Keep only letters (both lowercase and uppercase)
    - Print result
"""

# Flowchart-Like Visulaization
"""
    [Start]
        ↓
    Input → "My ID is A123B456!"
        ↓
    Loop → M ✔ y ✔ (space ✘) I ✔ D ✔ ...
        ↓
    Collect → "MyIDisAB"
        ↓
    Output → Extracted alphabets
    [End]
"""

# Real-World Cnnection
"""
    - Used in data cleaning, document sanitization, language model prep
    - Helpful in stripping noisy characters from scraped pages or user input
    - Forms logic in Identity masking, cipher decoding, and preprocessing pipelines
"""