# Code #22: Find Top N Scores Using Slicing
# Tier: Intermediate
# Goal: Sort a list and extract the top 3 values

scores = [84, 91, 76, 65, 99, 87, 92]
scores.sort(reverse=True)
top_3 = scores[:3]
print("Top 3 scores:", top_3)

# Concept Breakdown
"""
    Concept                 Description
    ------------------------------------
    .sort(reverse=True)     Sorts list in descending order
    slicing([:3])           Extracts first 3 items from sorted list
    List                    stores original scores
    Output                  Prints highest values clearly
"""

# How the Logic Works
"""
    - Define a list of scores
    - Sort the list from highest to lowest
    - Slice first 3 elements → store in top_3
    - Print top scorers
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    scores = [84, 91, 76, 65, 99, 87, 92]
        ↓
    Sort scores in descending order
        ↓
    Slice top_3 = scores[:3]
        ↓
        Print top_3
    [End]
"""

# Real-Wrold Connection
"""
    - Common in leaderboards, game scores, exam results, and top sellers
    - Powers ranking systems in ecommerce, finance (top trades), and content platforms
    - Forms the basis of recommendation engines, contest grading, and KPI filterin
"""