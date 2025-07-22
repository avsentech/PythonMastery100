# Code #84: Implement Merge Sort
"""
    🧠 Why This Matters?
    Used in:
    - 🔁 Efficient large-scale sorting
    - 💻 Backend data processing
    - 📊 Financial systems handling massive data streams
    - 🧮 Algorithm interviews and performance-critical apps
"""
# Tier: Intermediate
# Goal: Sort a list by recursively dividing it and merging sorted halves

# Python Code
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare and merge

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Sample Usage

unsorted = [42, 12, 89, 7, 33, 18]
sorted_result = merge_sort(unsorted)
print("Sorted List:", sorted_result)

# Output
"""
    Sorted List: [7, 12, 18, 33, 42, 89]
"""

# Concept Breakdown
"""
    Component           Desccription
    --------------------------------
    merge_sort()        Splits list recursively and returns sorted halves
    merge()             Combines two sorted lists into one
    Base Case           Lists of 1 element are inherently sorted
    Efficiency          Time complexity: O(n log n)
"""
# Mergesort is stablle, predictable, and performs well even on large datasets.

# Real-World Connection
"""
    - Sorting customer orders, transactions, or messages
    - Organizing memory blocks in OS or compilers
    - Structuring chat history, logs, and notifications
    - Used in ML preprocessing pipelines for sorting features
"""