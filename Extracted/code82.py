# Code #82: Find All Subsets of a List Using Recursion
"""
    🧠 Why This Matters?
    Used in:
    - 📊 Data mining and feature selection
    - 🎯 Strategy planning and decision trees
    - 🧮 Power set generation in discrete math
    - 🧪 Testing all combinations in simulation
"""
# Tier: Intermediate
# Goal: Generate all possible subsets (the power set) of a given list using recursive branching

# Python Code
def find_subsets(lst):
    if not lst:
        return [[]]
    else:
        first = lst[0]
        rest_subsets = find_subsets(lst[1:])
        subsets_with_first = [subset + [first] for subset in rest_subsets]
        return rest_subsets + subsets_with_first
    
# Sample Usage

items = [1, 2, 3]
all_subsets = find_subsets(items)
print("All Subsets:")
for subset in all_subsets:
    print(subset)

# Sample Output
"""
    []
    [3]
    [2]
    [3, 2]
    [1]
    [3, 1]
    [2, 1]
    [3, 2, 1]
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    Base Case           If list is empty, return [[]]
    Recursive Case      Build subsets from rest, then add first
    [subset + [first]]  Combines current element with existing subset
    Power Set           Includes all combinations from 0 to n items
"""
# Output grows as 2^n for a list of n elements - so recursion depth scales quickly.

# Real-World Connection
"""
    - NLP: Feature combinations in language models
    - Genetics: Trait combinations and pattern mapping
    - Inventory systems: Product bundle variations
    - Strategic analysis: Exploring decision paths
"""