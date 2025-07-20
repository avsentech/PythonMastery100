# Code #73: Handle File Not Found Exception Gracefully
"""
    🧠 Why This Matters?
    Used in:
    - 🧾 Reading logs or config files that may not exist
    - 📦 Error-proof file operations in real-world systems
    - 📄 CLI tools or API readers working with user-uploaded file
"""
# Tier: Beginner
# Goal: Attempt to read a file that might not exist, and respond with a user-friendly message

# Python Code
filename = "missing.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File Content:\n", content)
except FileNotFoundError:
    print(f"Error: '{filename}' doesnot exists.")

# Output (if file is missing)
"""
    Error: 'missing.txt' does not exist.
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    Try block           Runs risky file-access logic
    FileNotFoundError   Specific exception for missing files
    except block        handles error and prints friendly message
    with open(...)      Attempts to read the file
"""
# You can also offer to create the file if it's missing, or switch to fallback file.

# Real-World Connection
"""
    - Validating uploaded documents
    - Importing resource files in game engines
    - Loading configuration settings in boot scripts
    - Reading user history or save files in apps
"""