# Code 3: User Input & Logic
# Tier: Basic
# oal: Square a number entered by the user

num = int(input("Enter a number: "))
square = num ** 2
print("Square is: ", square)

# Concept Breakdown
"""
    Concept         Descriptioin
    ----------------------------
    Input           Receives number from user
    Type Casting    Converts string input to integer
    Arithmetic      Calculates square
"""

# How the Logic Works
"""
    - Take user input
    - Convert input to integer
    - Square the number
    - Print the result
"""

# Flowchart-Like Visualization
"""
    [Input → num]
    ↓
    Convert to int
    ↓
    Compute square = num ** 2
    ↓
    Print square
    [End]
"""

# Real-World Connection
"""
- Enables user interaction in command-line tools, games, and quizzes
- Builds the foundation for form handling in web apps
"""