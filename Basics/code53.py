# Code # 53: count Occurances of a Substring in a String
"""
    🧠 What Is a Substring Match?
    A substring is any slice of characters that exists within a larger string. This scroll helps count how many times a particular word or phrase appears in a text.
    Example:
    - "python python pythonic" → "python" appears 2 times
    - "abcabcabc" → "abc" appears 3 times
"""
# Tier: Intermediate
# Goal: Count the exact number of times a substring appears in a given string

text = input("Enter the main string: ")
substr = input("Enter the substring to count: ")

count = text.count(substr)

print(f"The substring '{substr} appears {count} time(s).")

# Sample Input:
"""
    Enter the main string: python python python
    Enter the substring to count: python
"""

# Output
"""
    The substring 'python' appears 2 time(s).
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    .count(substr)      Returns exact number of non-overlapping matches
    Case-sensitive      Counts only perfect matches
"""

# How the Logic Works
"""
    - Accept the main string and target substring
    - Use .count() to find how often it appears
    - Display the result with formatting
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "python python pythonic", Substring → "python"
        ↓
    Count → 2 (doesn't include 'pythonic')
        ↓
    Output → The substring 'python' appears 2 time(s)
    [End]
"""