# Code #81: Implement Binary search on a Sorted List
"""
    🧠 Why This Matters?
    Used in:
    - 🧮 Search engines and database queries
    - 🔍 Real-time filtering in apps or dashboards
    - 🧾 Range lookups in pricing, analytics, and finance
    - 🎮 Games (collision detection, map navigation
"""
# Tier: Intermediate
# Goal: Recursively search for an element in a sorted list

# Python Code
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1 # Not found
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)
    
# Sample Usage

numbers = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10

result = binary_search(numbers, target)
if result != 1:
    print(f"Found {target} at index {result}.")
else:
    print(f"{target} not found in list.")

# Sample Output
"""
    Found 10 at index 4.
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    low/high            Defines current search boundaries
    mid                 Middle index of current segment
    Recursion           Narrows search by checking left or right
    Return index        Position of found element or -1 if absent
"""
# Optimized for sorted lists. For unsorted list, use linear search or sort befoore searching.

# Real-World connection
"""
    - Locating inventory items by SKU
    - Searching historical price ranges
    - Quick lookup in leaderboard ranks
    - Accessing indexed records in databases
"""
