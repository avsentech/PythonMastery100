# Code #55: Count Frequency of Elements in a List
"""
    🧠 Why Element Frequency Matters?
    Used in:
        - 📊 Data analysis
        - 🔎 Tag or category counting
        - 🧠 NLP token frequency
        - 🔁 Repetition tracking
"""
# Tier: Intermediate
# Goal: Print the number of times each element appears in a list

data = [4, 5, 6, 4, 7, 4, 6, 7, 8, 6]
frequency = {}

for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Element Frequency:", frequency)

# Sample Input
"""
   [4, 5, 6, 4, 7, 4, 6, 7, 8, 6]
"""

# Output
"""
    Element Frequency: {4: 3, 5: 1, 6: 3, 7: 2, 8: 1}
"""

# Concept Breakdown
"""
    Concept          Description
    ----------------------------
    Dictionary       Used to store element counts or Stores element-to-frequency mapping
    Loop             Iterates through each item in the list
    Conditional      Checks if item exists in dictionary
"""

# Real-World Connection
"""
    - Detect most used ingredients in recipes
    - Analyze voting patterns or behavior logs
    - Find common errors or eventss in system logs
"""

