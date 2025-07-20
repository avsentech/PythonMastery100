# Code #60: Remove Duplicate from a List of Dictionaries
"""
    🧠 Why This Matters?
    Duplicate records in a list of dictionaries can:
    - Skew results in data analysis
    - Inflate reports or logs
    - Break API responses or configuration file
"""
# Tier: Intermediate
# Goal:: Remove duplicate dictionaries from a list based on full value match

# Method 1: Using set with frozenset
data = [
    {'name': 'Sena', 'age': 28},
    {'name': 'Raj', 'age': 30},
    {'name': 'Sena', 'age': 28}
]

unique = []
seen = set()

for item in data:
    identifier = frozenset(item.items())
    if identifier not in seen:
        seen.add(identifier)
        unique.append(item)

print("Unique dictionaries:", unique)

# Sample Input
"""
    [
        {'name': 'Sena', 'age': 28},
        {'name': 'Raj', 'age': 30},
        {'name': 'Sena', 'age': 28}
    ]
"""

# Output
"""
    Unique dictionaries: [{'name': 'Sena', 'age':28}, {'name': 'Raj', 'age': 30}]
"""

# Concept Breakdown
"""
    Technique           Explanation
    ------------------------------
    .items()            Gets key-value pairs as tuples
    .frozenset()        Immutable and hashable representation
    set()               Tracks which dictionary has been seen
    Loop check          Ensures duplicates aren't added again 
"""
# frozenset(dict.items()) allows a dictionary to be used as set member (since normal dicts aren't hashable)

# Bonus: Based on Specific Key Only
"""
    If you want to remove duplicates based on a specific key (e.g.'name' only)

    data = [{'name': 'Sena'}, {'name': 'Raj'}, {'name': 'Sena'}]
    seen_names = set()
    unique = []

    for item in data:
        if item['name] not in seen_names:
            seen_names.add(item['name'])
            unique.append(item)
"""

# Real-World Connection
"""
    - Deduplicating user submissions or registrations
    - Filtering log entries or audit trails
    - Cleaning product recods in inventory lists
"""
