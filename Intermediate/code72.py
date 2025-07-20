# Code #72: Append Data to an Existing File
"""
    🧠 Why This Matters?
    Used in:
    - 📊 Updating reports or logs without overwriting
    - 📋 Continuous note-taking or diagnostics
    - 🧾 Adding form submissions, chat history, audit entrie
"""
# Tier: Beginner
# Goal: Open an existing file and safely add new content at the end

# Python Code
filename = "example.txt"
new_line = "This is an appended entry"

with open(filename, "a") as file:
    file.write(f"\n{new_line}")

print("New data appended successfully.")

# Output
"""
    New data appended successfully
"""

# Concept Breakdown
"""
    Concept                 Description
    ------------------------------------
    "a" mode                Opens file for appending (no overwriting)
    .write()                Adds data to the end of file
    \n newline              Ensures entry starts on a fresh line
    with block              Automatically handles file closing
"""
# You can append multiple entries in a loop or log timestamps alongside the text.

# Real-world Connection
"""
    - Adding daily journal entries
    - Appending experiment logs
    - Chat message archiving
    - Tracking diagnostic and server events
"""