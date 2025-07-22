# Code55: Find the Second Largest Number in a List
"""
    🧠 Why Learn This?
    In scoreboards, leaderboards, and comparative logic, picking the runner-up is as crucial as the winner.
    This scroll helps you extract that wisdom through sorting or iteration.
"""
#Tier: Beginner-to-Intermediate
# Goal: Identify and return the second largest number in a list

numbers = [45, 21, 67, 89, 34, 67]
unique = list(set(numbers)) # Remove duplicates
unique.sort(reverse=True) # Sort in descending order

if len(unique) >= 2:
    second_largest = unique[1]
    print("Second largest number:", second_largest)
else:
    print("Not enough unique numbers to determine the second largest.")

# Concept Breakdown
"""
    Concept             Description
    ----------------------------
    set()               Removes duplicates from the list
    sort()              Sorts the list in descending order
    Indexing            Accesses the second largest element
    unique[1]           Picks second largest after first
    Conditional check   Prevents error in small or uniform lists
"""

# Edge case Handling
"""
    If list has fewer than two unique elements:

    numbers = [99]

    Output:

    Not enough unique elements.

    Always validate before accessing fixed index positions.
"""

# Real-World Connection
"""
    - Second-place scores in exams or games
    - Market analytics: second-best performing asset
    - Runner-up ranking logic in competitions
"""