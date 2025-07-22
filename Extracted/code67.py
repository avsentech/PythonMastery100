# Code #67: Use __str__ to Customize Class Output
"""
    🧠 Why This Matters?
    Used in:
    - 🧾 Logging & debugging
    - 📋 CLI outputs and dashboards
    - 🧬 Making objects readable instead of cryptic memory location  
"""
# Tier: Intermediate
# Goal: Override the __str__() method so print(object) shows readable information

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"📘'{self.title} by {self.author} - {self.pages} pages"
    
# Sample Usage
b1 = Book("The Python Scrolls", "Sena", 325)
print(b1)

# Output
"""
    📘 'The Python Scrolls' by Sena — 325 pages
"""

# Concept Breakdown
"""
    Concept             Descriptoin
    -------------------------------
    __str__()           Special method automatically called by print()
    f-string            Enables clean formatting
    return              Supplies readable string instead of default <Book object at 0x123>
"""
# You can format dates, currencies, or even emojis depending on the class's domain

# Without __str__
"""
    <__main__.Book object at 0x7f08ec08c100>
"""
# 👎 That’s what Python prints unless __str__ is defined

# Real-World Connection
"""
    - Invoicing apps printing readable Invoice objects
    - Game engines displaying player or scorecard data
    - E-Commerce dashboards printing product details
    - Data analysis models showing results cleanly
"""