# Code #24: Convert Two Lists into a Dictionary
# Tier: Intermediate
# Goal: Combine two lists-one of keys, one of values-into a dictionary

keys = ["name", "age", "grade"]
values = ["Sena", 22, "A"]

student = dict(zip(keys, values))
print("Student dictionary:", student)

# Output
"""
 Student dictionary: {'name': 'Sena', 'age': 22, 'grade': 'A'}
"""

# Concept Breakdown
"""
    Concept     Description
    ------------------------
    zip()       Pairs elements from two lists
    dict()      Converts paired tuples into a dictionary
    Lists       Separate collections of keys and values
    Output      Displays the resulting dictionary
"""

# How the Logic Works
"""
- Define two lists: one for keys, one for values
- Use zip() to pair corresponding elements
- Convert zipped result into a dictionary using dict()
- Print the final dictionar
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    keys = ["name", "age", "grade"]
    values = ["Sena", 22, "A"]
        ↓
    zip(keys, values) → [("name", "Sena"), ("age", 22), ("grade", "A")]
        ↓
    dict(zip(...)) → student dictionary
        ↓
    Print student
    [End]
"""

# Real-World Connection
"""
    - Used in form processing (field names + user inputs)
    - Powers JSON construction, API payloads, and config builders
    - Essential in data science for column-value mapping
    - Common in Excel-to-Python conversions and CSV parsing
"""