# Conde #19: Reverse a String Manually
# Tier: Inermediate
# Goal: Reverse an input string using a loop - not slicing

word = input("Enter a word: ")
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print("Reversed word:", reversed_word)

# Concept Breakdown
"""
    Concept                 Description
    -------------------------------------
    Input                   Takes a word from the user
    Loop(for)               Iterates through each character
    String Concatenation    Builds reversed string one character at a time
    Output                  Prints the reversed result
"""

# How the Logic Works
"""
    - Accept input word
    - Start with reversed_word = ""
    - Loop over each char in original string
    - Prepend char to reversed_word (so order flips)
    - Print final result after loop end
"""

# Flowchart-Like Visualization
"""
    [Input → word]
        ↓
    Initialize reversed_word = ""
        ↓
    FOR each char in word:
        → reversed_word = char + reversed_word
        ↓
    Print reversed_word
    [End]
"""

# Real-World Connection
"""
    - Powers palindromes, string matching, and encryption logic
    - Used in search engines and NLP to reverse tokens or detect symmetry
    - Helpful in algorithms (e.g., pointer manipulation), and in learning recursion (when reversing strings recursively)
"""