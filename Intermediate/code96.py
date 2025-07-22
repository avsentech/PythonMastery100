# Code #96: Use os to List Files in a Directory
"""
    🧠 Why This Matters?
    Used in:
    - 🧾 File auditing scripts
    - 🗂️ Media, backup, or asset managers
    - 🔍 Preprocessing datasets for ML
    - 🛠️ CLI bots for folder-based operation
"""
# Tier: Beginner-to-Intermediate
# Goal: List all files (excludiing folders) in a specified directory

# Python Code
import os

def list_files(folder_path):
    print(f"📂 Files inside: {folder_path}\n")
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            print(f"🗎 {file}")

# Sample Usage
list_files("e:/Practice/Python/Pythonmastry100/Intermediate")

# Output
"""
    code100.py
    🗎 code53.py
    🗎 code54.py
    🗎 code55.py
    🗎 code56.py
    🗎 code57.py
    🗎 code58.py
    🗎 code59.py
    🗎 code60.py
    🗎 code61.py
    🗎 code62.py
    🗎 code63.py
    🗎 code64.py
    🗎 code65.py
    🗎 code66.py
    🗎 code67.py
    🗎 code68.py
    🗎 code69.py
    🗎 code70.py
    🗎 code71.py
    🗎 code72.py
    🗎 code73.py
    🗎 code74.py
    🗎 code75.py
    🗎 code76.py
    🗎 code77.py
    🗎 code78.py
    🗎 code79.py
    🗎 code80.py
    🗎 code81.py
    🗎 code82.py
    🗎 code83.py
    🗎 code84.py
    🗎 code85.py
    🗎 code86.py
    🗎 code87.py
    🗎 code88.py
    🗎 code89.py
    🗎 code90.py
    🗎 code91.py
    🗎 code92.py
    🗎 code93.py
    🗎 code94.py
    🗎 code95.py
    🗎 code96.py
    🗎 code97.py
    🗎 code98.py
    🗎 code99.py
    🗎 codecreate.py
    🗎 config.txt
    🗎 error.log
    🗎 example.txt
    🗎 example_backup.txt
    🗎 gitoptimizer.py
    🗎 students.csv
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    os.listdir()        List all items in the folder
    os.path.isfile()    Filters only files (excludes folders)
    os.path.join()      Creates full path for cross-platform salary
"""
# You can extend this scroll to:
"""
    - List only .py or .txt files
    - Sort by date, size, or alphebet
    - Return file paths for advanced automation
"""

# Real-World Connection
"""
    - 🧠 Batch processing filenames for analysis
    - 📦 Displaying folder contents in GUI tools
    - 🎬 Preparing media libraries or conversion tasks
    - 📁 Auto-tagging files based on extension or metadat
"""
