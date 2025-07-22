# Code #56: Sort a Dictionary by Value
"""
    🧠 Why Sort by Value?
    Used for:
    - Ranking players, products, or keywords
    - Sorting budgets, scores, or votes
    - Creating dashboards or report summaries
"""
# Tier: Intermediate
# Goal: Sort a dictionary based on its values in descending order

scores = {'Alice': 78,'Bob': 92, 'Charlie': 85, 'David': 67}
# Sort using lamba and dictionary items
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print("Sorted by score:", sorted_scores)

# Concept Breakdown
"""
    Concept                      Description
    -----------------------------------------
    .items()                     Retrieves key-value pairs
    lambda item:item[1]          Extracts the value for sorting, sorted based on values
    reverse=True                 Ensures descending order
    dict()                       Converts sorted list back to dictionary
"""

# For ascending order, just remove reverse=True

# Real-World Connection
"""
    - Sort top-selling products by revenue
    - Display student grades by performance
    - Rank words by frequency in NLP pipelines
"""