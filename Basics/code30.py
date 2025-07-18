# Code #30: Calculate the Factorial of a Number
# Tier: Intermediate
# Goal: Compute the factorial of a given  number using a loop

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of ", num, " is ", factorial)

# Sample Input
"""
    5
"""

# Output
"""
    Factorial of 5 is 120
"""

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    range(1,num+1)  Iterates from 1 to num
    factorial*=1    Multiples each number to build factorial
    Loop            Replaces recursion with iteration
"""

# How the Logic Works
"""
    - Accept a number from the user
    - Initialize factorial to 1
    - Loop from 1 to the number
    - Multiply each value into factorial
    - Print the result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Input → 5
        ↓
    Loop → 1 × 2 × 3 × 4 × 5
        ↓
    Result → 120
        ↓
    Print → Factorial of 5 is 120
    [End]
"""

# Real-World Connection
"""
    - Used in permutations, combinations, and probability
    - Powers recursive algorithms and dynamic programming
    - Forms the basis of mathematical modeling and statistical formulas 
"""

