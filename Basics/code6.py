# Code #6: Print Even Numbers
# Tier: Basic
# Goal: Show even numbers from 1 to 10

for i in range(1, 11):
    if i %2 == 0:
        print(i)

# Concept Breakdown
"""
    Concept     Description
    -----------------------
    Loop        Iterates through values 1 to 10
    Condition   Checks even numbers using %
"""

# Flowchart-Like Visualization
"""
    [Start]
    ↓
    Loop i = 1 to 10
    ├── If i % 2 == 0 → Print i
    └── Else → Skip
    [End]
"""

# Real-World Connection
"""
    - Used in filtering numeric data in statistics, reports, or even hardware IO operations
    - Forms early thinking behind set filters and modulus-based check
"""