# Code #53: Merge Two Lists Without Duplicates
"""
    🧠 Why Merge Lists Uniquely?
    Used in scenarios like:
    - Combining tags, categories, or IDs
    - Merging datasets from multiple sources
    - Avoiding duplication in user inputs
"""
# Tier: Beginner
# Goal: Combine two lists, ensuring no repeated values

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged = list(set(list1 + list2))
print("Merged List:", merged)

# Sample Input
"""
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
"""

# Output (Order may vary due to set)
"""
Merged List: [1, 2, 3, 4, 5, 6]
"""

