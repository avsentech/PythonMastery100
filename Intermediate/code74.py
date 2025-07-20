# Code #74: Read CSV File and Convert to Dictionary
"""
    🧠 Why This Matters?
    Used in:
    - 📊 Data analysis and ETL pipelines
    - 🧾 Importing survey results or user databases
    - 📇 CRM tools, dashboards, and billing apps
    - 💬 NLP training sets and configuration loadin
"""
# Tier: Intermediate
# Goal: Convert a CSv file into a list of dictionaries using csv.DictReader

# Pythong Code
import csv
filename = "students.csv"

with open(filename,mode="r") as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

print("CsV as Dictionary List:")
for entry in data:
    print(entry)

# Sample Output
"""
    CSV as Dictionary List:
    {'name': 'Sena', 'grade': 'A+'}
    {'name': 'Raj', 'grade': 'B'}
    {'name': 'Anika', 'grade': 'A'}
"""

# Concept Breakdown
"""
    Concept                     Description
    --------------------------------------------
    csv.DictReader()            Reads rows as dictionaries using headers
    row for row in header       Builds list from each dictionary row
    Keys from header            name, grade used as dictionary keys
"""
# You can now access any record with row['name'], filter data, or convert to JSON as needed

# Real-World Connection
"""
    - Importing student data into apps
    - Reading product catalogs into e-commerce backends
    - Feeding dashboards with tabular data
    - Preprocessing training sets in ML/NLP tools
"""
