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

# Concept Breakdown
"""
    Concept          Description
    ----------------------------
    + operator        Combines both lists
    set()             Removes duplicates by converting to a set
    list()           Converts the set back to a list for display/use
"""

# Note: If maintaining order is critical, use a manual loop or dict.fromkeys() instead of set.

# Edge Case Handling
"""
    - Empty lists: Merging two empty lists should yield an empty list.
    - All duplicates: If both lists are identical, the result should be a single instance of the values.
    - Mixed types: If lists contain different data types, ensure compatibility before merging.
"""

# Real-World Connection
"""
    - Merging user preferences or search history
    - Filtering duplicate transactions or logs
    - Consolidating item lists from multiple files or APIs 
"""