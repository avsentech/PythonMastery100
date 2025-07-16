# Code 13: Formatted String
# Tier: Basic

# Goal: Print a personalized message using formatted strings

name = input("Enter your name: ")
score = int(input("Enter your score: "))
print(f"Hello {name}, your score is {score}")

# Concept Breakdown
"""
    Concept             Description
    Input               Takes data from user String Formatting   Inserts values into a string dynamically using f-strings 
    Type Casting        Converts input to integer for arithmetic or display
"""

# How the Logic Works
"""
    - Ask the user for their name → store in name
    - Ask for their score → convert to integer → store in score
    - Use an f-string to display: "Hello Sena, your score is 95
"""

# Flowchart-Like Visualization
"""
    [User Input → name] 
    ↓ 
    [User Input → score → int()] 
    ↓ 
    Format string → f"Hello {name}, your score is {score}" 
    ↓ 
    Print result [End]
"""

# Real-World Connection
"""
    - Used for personalized greetings, invoices, report summaries
    - Forms the foundation of dynamic UI messaging and templating systems
    - Improves readability over older techniques like string concatenation or .format()
"""

