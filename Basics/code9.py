# Code 9: Random Number Generator
# Tier: Basic
# Goal: Generate a random number between 1 and 100

import random
rand_num = random.randint(1, 100)
print("Random number:", rand_num)

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    Module          Imports Python's built-in random module
    randint         Returns integer between range values
    Output          Prints result to console
"""

# How the Logic Works
"""
    - Import the random module
    - Use randint(1, 100) to generate number
    - Print result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Import random module
        ↓
    Generate rand_num using randint
        ↓
    Print rand_num
    [End]
"""

# Real-World Connection
"""
    - Powers lottery systems, dice games, random password generation, and test sampling
    - Core technique in simulations and machine learning training
"""
