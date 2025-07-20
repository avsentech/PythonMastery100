# Code #57: Covert List of Tuples to Dictionary
"""
    🧠 Why This Matters?
    This scroll shines when handling:
    - CSV rows or database records
    - API responses with paired data
    - User inputs mapped to preferences, scores, or identifier
"""
# Tier: Beginner
# Goal: Convert a list of tuples into a dictionary

pairs = [('apple', 3), ('banana', 5), ('orange', 2)]

converted_dict = dict(pairs)
print("Converted Dictionary:", converted_dict)

# Sample Input
"""
    [('apple', 3), ('banana', 5), ('orange', 2)]
"""

# Output
"""
    Converted Dictionary: {'apple':3, 'banana': 5, 'orange':2}
"""

# Concept Breakdown
"""
    Concept         Purpose
    -----------------------
    typle           Each pair acts as (key,value)
    dict()          Converts iterable of tuples into a dictionary
    []              Square brackets define the list container
"""

# Each first element becomes a key; second becomes its value

# Duplicate Key Behavior
"""
    Python dictionaries overwrite earlier entries with the latest if keys are repeated:

    pairs = [('a',1),('b',1),('a',1)]
    print(dict(pairs)) # Output: {'a':5, 'b':2}
"""
# Tip: Use grouping logic if you want to preserve all duplicate keys.

# Real-World Connection
"""
    - Converting product-price pairs from spreadsheet rows
    - API mapping of userID and preferences
    - Scoreboard construction from (player,score) pairs
"""