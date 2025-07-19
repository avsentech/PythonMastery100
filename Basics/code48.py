# Code #48: Find the Longest Word in a Sentence
"""
    🧠 What Does It Mean?
    This scroll identifies the longest and shortest word in a sentence—measured by character length.
    Example:
    - "The quick brown fox jumps over the lazy dog" → longest: "jumps"
    - "PythonMastery100 is legendary" → longest: "PythonMastery100"
"""
# Tier: Intermediate
# Goal: Extract and display the longest word from a given sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
smallest = min(words, key=len)

print("Longest word:", longest)
print("Shortest word:", smallest)
print("Length:", len(longest))

# Sample Input
"""
    Practice makes mastery unstoppable
"""

# Output
"""
    Longest word: unstoppable
    Length: 11
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    .split()            Breaks sentence into words
    max(...,key=len)    Finds word with max character length
    len()               Measures word length
"""

# How the Logic Works
"""
    - Accept a sentence from the user
    - Split into list of words
    - Use max() to find the longest word
    - Display word and its length
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "Practice makes mastery unstoppable"
        ↓
    Split → ["Practice", "makes", "mastery", "unstoppable"]
        ↓
    Max → "unstoppable" (11)
        ↓
    Output → Longest word
    [End]
"""

# Real-World Connection
"""
    - Used in text summarization and linguistic analysis
    - Powers word games, spell-checkers, and content scoring
    - Valuable in UI design to dynamically adjust layout based on text
"""