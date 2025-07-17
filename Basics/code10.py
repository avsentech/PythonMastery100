# Code #10: sum of Digits of a Number

num = int(input("Enter a number: ")) # Accepts a number from the user and coverts it to an integer
total = 0 # Initializes total as zero to store the running sum of digits
while num > 0: # Loop starts only if number is greater than 0
    digit = num % 10 # Extracts last digit (modulus operation gives remainder)
    total += digit # Adds that digiit to the total
    num //= 10 # Removes lastt digit by doing integer division
print("Sum of ditits", total) # Final result print after loop ends

# Core Concepts 
# Modulus (%) -> gets the last digit of a number
# Integer division (//) drops the last digit
# Loopping continues until number is fully broken down

# Flowchart-Like Execution
"""
   [Input number → num]
      ↓
   Initialize total = 0
      ↓
   WHILE num > 0:
      ↳ digit = num % 10
      ↳ total += digit
      ↳ num = num // 10
      ↓
   Print total
   [End]
"""

# Sample Run
"""
   Suppose user inputs 543
   - Step 1: digit = 543 % 10 = 3 → total = 0 + 3 → num = 543 // 10 = 54
   - Step 2: digit = 54 % 10 = 4 → total = 3 + 4 → num = 54 // 10 = 5
   - Step 3: digit = 5 % 10 = 5 → total = 7 + 5 → num = 5 // 10 = 0
   - DONE → total = 12
"""

# Real world Use
"""
   - Great for digit analytics: numerology, digital root, checksum algorithms
   - Forms the foundation of patterns in competitive coding and math puzzles35
"""


