# Code #58:: Group Words by Length from a List
"""
    🧠 Why This Matters?
    Grouping by word length is useful for:
    - 📚 Language processing
    - 🧾 Text categorization
    - 📊 UI rendering or layout planning
    - 🧪 Vocabulary analysis and clusterin
"""
# Tier: Intermediate
# Goal: Organize words from a list into a dictionary based on their lengths

words = ['cat', 'elephant', 'dog','giraffe', 'bat', 'hippo', 'ox']
grouped = {}

for word in words:
    length = len(word)
    if length in grouped:
        grouped[length].append(word)
    else:
        grouped[length] = [word]

print("Gropued by length:",grouped)

# Sample Input
"""
    ['cat', 'elephant', 'dog', 'giraffee', 'bat', 'hippo', 'ox']
"""

# Output
"""
    Grouped by length: {3: ['cat', 'dog', 'bat'], 8: ['elephant'], 7: ['giraffe'], 5: ['hippo'], 2: ['ox']}
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    len(word)           Calculates length of each word
    dict[length]        Key grouping based on length
    append()            Adds word to existing length group
    Conditional check   Ensure key exists before appending
"""
# You can also use defaultdict(list) from collections to simplify the logic.

# Bonus Version with (defaultdict)
"""
    from collections import defaultdict

    grouped = defaultdict(list)
    for word in words:
        grouped[len(word)].append(word)
"""

# Real-World Connection
"""
    - UI font rendering by word size
    - Grouping search queries by complexity
    - Analyzing sentence construction patterns
"""