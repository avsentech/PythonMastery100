# Code #71: Count Lines, Words, and Characters in a File
"""
    🧠 Why This Matters?
    Used in:
    - 📄 Document parsing
    - 📚 Essay and article analyzers
    - 🧾 Report generators
    - 🧮 CLI tools for file stat
"""
# Tier: Beginner
# Goal: Read a text file and count its lines, words, and characters

# Python Code
filename = "example.txt"

with open(filename, "r") as file:
    content = file.read()
    lines = content.splitlines()
    words = content.split()
    characters = len(content)

print(f"Lines: {len(lines)}")
print(f"Words: {len(words)}")
print(f"Characters: {characters}")

# Sample (example.txt)
"""
    Python is amazing.
    This file is here for testing.
    We are counting lines, words, and characters.
"""

# Sample Output
"""
    Lines: 3
    Words: 15
    Characters: 90
"""

# Concept Breakdown
"""
    Metric          How it Calculated
    ---------------------------------
    Lines           Split by newline using .splitlines()
    Words           Split by whitespace using .split()
    Characters      Length of full string using len()
"""
# You can extend this logic with frequency counters, top keywords, or sentence structure analysis.

# Real-World Connection
"""
    - Content length checkers for blogs or documentation
    - Preprocessing text in NLP pipelines
    - Resume analyzers and form validators
    - File stats for command-line toolsor IDEs
"""

