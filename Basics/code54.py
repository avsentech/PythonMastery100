# Code #54: Remove All Occurrences of a Substring from a String
"""
    🧠 Why Do This?
    This scroll lets you clean or sanitize a string by removing a target substring entirely.
    Example:
    - "hello world hello universe" → remove "hello" → " world  universe"
    Useful in data cleaning, noise reduction, or custom parsers.
"""
# Tier: Intermediate
# Goal: Remove every occurence of a substring from the main string

text = input("Enter the main string: ")
substr  = input("Enter the substring to remove:")

result = text.replace(substr, "")

print("String after removal:",result)

# Sample Input
"""
    Enter the main string: hello world hello universe
    Enter the substring to remove:: hello
"""

# Output
"""
    String after removal: world univers
"""

# Concept Breakdown
"""
    Concept                 Description
    ------------------------------------
    .replace(a,b)           Replaces every a with b in string
    substr→""               Effectively deletes the substring
"""

# How the Logic Works
"""
    - Accept the main string and substring
    - Replace every match with an empty string
    - Print the cleaned output
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → "hello world hello universe", Sub → "hello"
        ↓
    Replace → "" (deleted)
        ↓
    Result → " world  universe"
    [End]
"""

# Real-World Connection
"""
    - Used in preprocessing scraped data, cleaning chat logs, and stripping markup tags
    - Powers logic in search filters, ad blockers, and message sanitizer
"""