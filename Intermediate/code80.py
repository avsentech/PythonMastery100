# Code #80: Generate Fibonacci Sequence Using Recursion
"""
    🧠 Why This Matters?
    Used in:
    - 📈 Financial predictions and simulations
    - 🧬 Genetic growth algorithms
    - 🎮 Game mechanics and scoring systems
    - 🧮 Teaching recursion and optimizatio
"""
# Tier: Beginner
# Goal: Recursively generate the first N numbers in the Fibonacci sequence
# F(n) = F(n-1) + F(n-2), with base cases F(0)=0, F(1)=1

# Python Code
def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Print first N Fibonacci numbers

N = 10
sequence = [fibonacci(i) for i in range(N)]
print("Fibonacci Sequence:", sequence)

# Sample Output
"""
    Fibonacci Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    Base Case           Direct return for n=0 and n=1
    Recursive Case      Adds fibonacci(n-1) + fibonacci(n-2)
    List Comprehension  Builds full sequence from recursive calls
"""
# Recursion mirrors mathematical truth-but inefficient for large n. Use memoization or iteration to optimize

# Real-World Connection
"""
    - Modeling natural spirals and growth
    - Neural architecture in AI simulations
    - Stock trend predictors and sequence models
    - Population growth and fractal visualizers
"""