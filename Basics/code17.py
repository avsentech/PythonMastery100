# Code #17: Dictionary Basics
# Tier: Intermediate
# Goal: Store and retrieve key-value paris using a dictionary

student = {
    "name": "Sena",
    "age": 22,
    "grade": "A"
}
print("Name:", student["name"])

# Concept Breakdown
"""
    Concept     Description
    ------------------------
    Dictionary  Stores data in key-value format
    Key Access  Retrieve values by their key (e.g, "name")
    Output      Displays data from dictionary
"""

# How the Logic Works
"""
    - Define a dictionary named student with 3 key-value pairs
    - Use the key "name" to access the associated value
    - Print the result
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    Define student = { "name": ..., "age": ..., "grade": ... }
        ↓
    Access value using student["name"]
        ↓
    Print "Name: Sena"
    [End]
"""

# Real-World Connection
"""
    - Core data structure in Python APIs, JSON files, and configuration settings
    - Used in web apps (user profiles), finance (ledger entries), and machine learning (parameter maps)
    - Powers everything from database records to RESTful request payloads
"""

