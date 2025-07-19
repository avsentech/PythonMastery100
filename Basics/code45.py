# Code #45: Count Frequency of Each Character in a String
"""
    🧠 What is Character Frequency?
    Character frequency reveals how often each character appears in a string.
    Example:
    - "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
    Useful for data analysis, text compression, cryptography, and interview prep.
"""
# Tier: Inermediate
# Goal: Count and display how many times each character appears in a string

text = input("Enter a string: ")
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequencies")
for char, count in frequency.items():
    print(f"{char}: {count}")

# Sample Input
"""
    banana
"""

# Output
"""
    Character frequencies:
    b: 1
    a: 3
    n: 2
"""

# Concept Breakdown
"""
    Concept                 Description
    ------------------------------------
    dict.get()              Retrieves count or defaults to 0
    Loop over string        Iterates through each character
    frequency[char]+=1      Increments count
    dict.items()            Outputs key-value pairs
"""

# How the Logic Works
"""
    - Accept a string from the user
    - Initialize empty dictionary
    - Loop through each character
    - Count occurrences
    - Display frequency map
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "banana"
        ↓
    Loop → b, a, n, a, n, a
        ↓
    Count → {'b':1, 'a':3, 'n':2}
        ↓
    Output → Frequencies
    [End]
"""

# Real-World Connection
"""
    - Used in NLP, data analysis, plagiarism detection
    - Powers algorithms like Huffman Coding
    - Essential for pattern matching and text diagnostics
"""