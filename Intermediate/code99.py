# Code #99: Use collections.Counter for Word Frequency
# Tier: Intermediate
# Goal: Count how often each word appears in a text

# Python Code
from collections import Counter
import re

def get_word_frequency(text):
    # Clean and tokenize the text

    text = text.lower()
    words = re.findall(r'\b\w+\b', text)    # matches words (alphanumeric)

    # Count frequency
    word_counts = Counter(words)

    # Disply results

    print("🔤 Word Frequencies:")
    for word, count in word_counts.most_common():
        print(f"{word}: {count}")

# Sample Usage

sample_text = """
Python is amazing. Python automates tasks. Python handles files, APIs, and more.
Tasks with Python are powerful and reusable. Automation is power!
"""

get_word_frequency(sample_text)

# Output
"""
    Word Frequencies:
    python: 4
    is: 2
    tasks: 2
    and: 2
    amazing: 1
    automates: 1
    handles: 1
    files: 1
    apis: 1
    more: 1
    with: 1
    are: 1
    powerful: 1
    reusable: 1
    automation: 1
    power: 1
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    re.findall()        Extracts clean word tokens from text
    Counter(words)      Counts each word's occurrence
    .most_common()      Returns sorted list by frequency
"""
# Can be extended to ignore stopwords, apply stemming, or count bigrams.

# Real-World Connection
"""
    - 🧠 NLP text mining and keyword extraction
    - 📈 Analyzing customer feedback or reviews
    - 📰 Generating tags from article headlines
    - 💬 Spam keyword detection or tweet analytic
"""