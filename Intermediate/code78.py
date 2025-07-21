# Code #78: Find Factorial Using Recursion
"""
    🧠 Why This Matters?
    Used in:
    - 🧪 Combinatorics and probability calculations
    - 🧮 Mathematical libraries and symbolic computation
    - 🎲 Game logic or scoring systems
    - 💡 Teaching recursion fundamental
"""
# Tier: Beginner
# Goal: Use a recursive function to calculate n!=nx(n-1)!

# Python Code
def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# sample Usage

print("Factorial of 5 is:", factorial(5))

# Output
"""
    Factorial of 5 is: 120
"""

# Concept Breakdown
"""
    Component           Description
    --------------------------------
    Base Case           n == 0 or 1 returns 1
    Recursive Case      n * factorial(n-1)
    Error Handling      Raises exception for negative inputs
"""
# The function calls itself until it reaches the base case, stacking calls like a countdown timer.

# Real-World Connection
"""
    - Calculating permutations  or combinations (nCr, nPr)
    - Computing power series (Taylor, Maclaurin expansions)
    - Evaluating mathematical expressions in scientific tools
    - Explaining recursion in coding interviews or classrooms
"""