# Code #59: Flatten a Nested List
"""
    🧠 Why Flatten?
    Used for:
    - Pre-processing data for ML pipelines
    - Cleaning CSV or JSON structures
    - Simplifying deeply nested configuration
"""
# Tier: Intermediate
# Goal: Convert a nested list into a flat, one-dimensional list

# Method 1: Using Nested Loops (Basic)

nested = [[1, 2], [3, 4], [5, 6]]
flattened = []

for sublist in nested:
    for item in sublist:
        flattened.append(item)

print("Flatended List:", flattened)

# Output
"""
    Flattened List: [1, 2, 3, 4, 5, 6]
"""

# Method 2: List Comprehension

flattened_comprehension = [item for sublist in nested for item in sublist]
print("Flattened Comprehension:", flattened_comprehension)

# Method 3: With

from itertools import chain
flattened_with = list(chain(*nested))
print("Flattened with: ", flattened_with)

# Concept Breakdown
"""
    Technique           Description
    --------------------------------
    Nested loops        Explicit iteration over sublists
    List comprehension  One-liner flattening logic
    itertool.chain()    Built-in utility for flattening
"""
# For deeper levels of nesting (e.g. lists within lists within lists), recursion or external libraries are needed

# Deep Nesting Example
"""
    nested = [1, [2, [3, 4]], 5]
"""
# Tip: Use recursive logic or libraries like more_itertools, numpy, or pandas for complex structures

# Real-world Connection
"""
    - Merge multi-level form inputs
    - Flatten comment threads or logs
    - Simplify matrix or tensor preprocessing
"""
