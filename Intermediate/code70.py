# Code #70: Read and Write Text Files
"""
    🧠 Why This Matters?
    Used in:
    - 🧾 Saving notes, logs, or configuration details
    - 📥 Loading stored data for analysis or dashboards
    - 📝 Building CLI tools, editors, or audit system
"""
# Tier: Beginner
# Goal: Write content to a text file, then read it back and display the result

# Python Code
filename = "example.txt"

# write content to file

with open(filename, "w") as file:
    file.write("Hello, Sena!\nWelcome to the File Handling module.")

# Read content from file

with open(filename, "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Sample Output
"""
    File Content:
     Hello, Sena!
    Welcome to the File Handling module.
"""

# Concept Breakdown
"""
    Operation           Description
    -------------------------------
    "w" mode            Writes new content, overwrites if file exits
    "r" mode            Reads entire file content
    .write()            Writes string data to file
    .read()             Fetches full content at a string
    with block          Auto-closes file after operation
"""
# You can also use "a" for append mode or "x" to exclusively create files.

# Real-World Connection
"""
    - Saving output logs and chat transcripts
    - Readingscraped text fromlocal storage
    - Preloading model configurations from .txt files
    - Writing user feedback or settings to disk
"""