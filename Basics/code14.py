# Code #14: Find Maximum i n a List
# Tier: Intermediate
# Goal: Traverse a list to find the largest number manually

nums = [12, 67, 34, 89, 23]
max_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num

print("Max number is:", max_num)

# Concept Breakdown
"""
Concept           Description
List              Collection of values (here, integers) 
Loop(for)         Iterates through each element in the list 
Comparison(>)     Checks if current value exceeds known max Variable 
Update            Replaces max when a bigger number is found
"""

# How the Logic Works
"""
- Start with the first item as max_num
- Loop through each num in the list: → If num > max_num, update max_num
- End loop → Print final max valu
"""

# Flowchart-Like Visualization
"""
    [Start]
    ↓
    Initialize list: nums = [12, 67, 34, 89, 23]
    ↓
    Set max_num = nums[0]
    ↓
    FOR each num IN nums:
    ├── Is num > max_num?
    │     ├── Yes → Update max_num
    │     └── No → Keep existing max_num
    ↓
    Print max_num
    [End]
"""

# Real-World Connection
"""
    - Core logic in ranking algorithms, leaderboard systems, and performance evaluations
    - Essential in finding peaks in datasets—finance, weather, sports, etc
"""