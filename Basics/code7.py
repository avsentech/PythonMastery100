# Code 7: Collect Multiple Inputss in a List
# Tier: Intermediate
# Goal: Store 5 user inpputs in a list

nums = []
for _ in range(5):
    num = int(input("Enter a number: "))
    nums.append(num)
print("You entered:", nums)

# Concept Breakdown
"""
    Concept     Description
    -------------------------
    List        stores multiple elements
    Loop        Executes the input-gathering 5 times
    Append      Adds items to the list dynamically
    Type Cast   Ensures input is integer
"""

# How the Logic works
"""
    - Initialize an empty list
    - Loop runs 5 times: ask user for a number
    - Convert each input to int and store using append()
    - Print the full list at the end
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Create empty list: nums = []
        ↓
    Repeat 5 times:
        → Input number
        → Convert to int
        → Append to nums
        ↓
    Display nums
    [End]
"""

# Real-World Connection
"""
    - Simulates dynamic form collection or data ingestion from users
    - Used in feedback systems, quiz apps, and survey tools
"""