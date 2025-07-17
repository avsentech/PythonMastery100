# Code #21: Filter Even Numbers from a List
# Tier: Intermediate
# Goal: Extract only even numbers from a given list

nums = [12, 5, 8, 19, 34, 7]
evens = []

for num in nums:
    if num % 2 == 0:
        evens.append(num)

print("Even numbers:", evens)

# Concept Breakdown
"""
    Concept         Description
    ---------------------------
    List            Original collection of mixed integers
    Condition       Checks if each number is divisible by 2
    Append          Stores qualifying numbers into evens list
"""

# How the Logic Works
"""
    - Start with a predefined list nums
    - Loop through each item
        → If number is divisible by 2 → append to evens
    - Print the resulting filtered list
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    nums = [12, 5, 8, 19, 34, 7]
        ↓
    Initialize evens = []
        ↓
    FOR each num in nums:
        ├── If num % 2 == 0 → append to evens
        └── Else → skip
        ↓
    Print evens
    [End]   
"""

# Real-World Connection
"""
    - Powers data filtering in dashboards, performance systems, and finance ledgers
    - Used in sensor streams where even IDs or signals have special meaning
    - Forms the bedrock of statistical sampling, machine learning preprocessing, and event log parsing
    - Critical in rule-based engines and conditional triggers where numeric matching matters
"""

# You can later evolve this into:
"""
    evens = [n for n in nums if n % 2 ==0]

    - a Pythonic one-liner using list comprehensions
"""