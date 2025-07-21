# Code #80: Check if a String is a Palindrome Using Recusion
"""
    🧠 Why This Matters?
    Used in:
    - 🔍 Natural language processing
    - 📚 Text pattern validation
    - 🧪 Algorithm practice and interview questions
    - 🧮 Symbolic computation and DNA sequence analysi
"""
# Tier: Intermediate
# Goal: Recursively check whether a given string is a palindrome

# Python Code
def is_palindrome(s):
    s = s.strip().lower().replace(" ", "")    # Normalize input

    return _check_recursive(s)

def _check_recursive(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return _check_recursive(s[1:-1])
    
# Sample Usage

word = "Radar"
print(f"Is '{word}' a palindrome?", is_palindrome(word))

# Sample Output
"""
    Is 'Radar' a palindrome? True
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    s.strip().lower()   Cleans input for comparison
    Base Case           String length ≤ 1 means it's a palindrome
    Recursive Case      Check first and last characters, trim & repeat
    Helper Function     _check_recursive isolates recursion logic
"""
# Extendable to ignore punctuation, compare phrases, or process numeric palidromes

# Real-World Connection
"""
    - Validating mirror strings in bioinformatics
    - Chat moderation or spam detection
    - Puzzle games with word reversal challenges
    - Text-based CAPTCHA or code symmetry checks
"""
