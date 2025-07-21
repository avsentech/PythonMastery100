# Code #85: Implement Merge Sort
"""
    🧠 Why This Matters?
    Used in:
    - 🧮 Backend sorting of large datasets
    - 🧾 Financial systems processing high-frequency transactions
    - 📊 Report generation and inventory management
    - 🧠 Interview prep and algorithm optimizatio
"""
# Tier: Intermediate
# Goal: Recursively split the list and merge sorted halves to produce a fully sorted result

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

    # Compare and merge elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining items

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Sample Usage

unsorted = [42, 17, 8, 99, 33, 12]
sorted_result = merge_sort(unsorted)
print("Sorted List:", sorted_result)

# Sample Output
"""
    Sorted List: [8, 12, 17, 33, 42, 99]
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    merge_sort()        Recursively splits input list
    merge()             Combine two sorted halves into a sorted list
    Base Case           A list of 1 element is already sorted
    Time Complexity     O(n log n) in all cases
"""
# Merge sort is stable, predictable and efficient choice for data-intensive environments

# Rel-World Connection
"""
    - Invoice sorting and reconsilation
    - NLP token stream ording
    - Dataset preprocessing in data science
    - Packaging automation: prioritizing by weight, value, or urgency
"""