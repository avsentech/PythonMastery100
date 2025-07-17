# Code #16: Sorting a List
# Tier: Basic
# Goal: sort a list of numbers in ascending order

nums = [42, 17, 23, 8, 99]
nums.sort()
print("Sorted list: ", nums)

# Concept Breakdown
"""
    Concept     Description
    --------------------------------
    List        A collection that canbe recodered
    .sort()     Built-in method to sort items in-place
    Output      Displays the sorted result
"""

# How the Logic Works
"""
    - Define a list with unsorted numbers
    - Apply .sort() method to arrange elements from smallest to largest
    - Print the result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Define nums = [42, 17, 23, 8, 99]
        ↓
    Apply nums.sort()
        ↓
    List now = [8, 17, 23, 42, 99]
        ↓
    Print sorted list
    [End]
"""

# Real-World Connection
"""
    - Used in dashboards (ranking, top performers), finance apps (price movement), search results, and reports
    - Essential for organizing data before filtering, analyzing, or visualizing
    - Underpins sorting algorithms (bubble, merge, quick sort)—critical in computer science foundations
"""

# Want to explore sorting in descinding order? You can use:
"""
    nums.sort(reverse=true)
"""