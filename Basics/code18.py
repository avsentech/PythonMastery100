# Code #18: Loop Through Dictionary
# Tier: Intermediate
# Goal: Iterate over alll key-value paris in a dictionary

student = {
    "name": "Sena",
    "age": 22,
    "grade": "A"
}
for key,value in student.items():
    print(key, "→", value)

# Concept Breakdown
"""
    Concept     Description
    ------------------------
    Dictionary  Stores structured data in key-value format
    .items()    Returns all key-value pairs as tuples
    Loop (for)  Unpacks keys and values one-by-one
    Output      Prints both key and value to the console
"""

# How the Logic Works
"""
- Define dictionary with keys like "name", "age", "grade"
- Use .items() to extract key-value pairs
- Loop through each pair → print key → value
"""

# Flowchart-Like Visualization
"""
    [Start]
        ↓
    student = { name: Sena, age: 22, grade: A }
        ↓
    Call .items() → returns (key, value) pairs
        ↓
    FOR each key, value:
        → Print key → value
        ↓
    Repeat for all pairs
    [End]
"""

# Real-World Connection
"""
    - Essential in reading and handling JSON data from APIs
    - Powers admin dashboards, data reports, and logs
    - Used heavily in config parsing, form generation, and dynamic UI rendering
    - Mirrors backend frontend exchanges in dictionaries like user profiles, settings, or app responses
"""