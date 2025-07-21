# Code #90: Automate File Renamig in a Folder
"""
    🧠 Why This Matters?
    Used in:
    - 📁 Organizing project assets and archives
    - 🧾 Standardizing filenames for backups
    - 🧠 Preprocessing datasets in ML pipelines
    - 🎬 Renaming media, screenshots, or log
"""
# Tier: Intermediate
# Goal: Loop through a folder and rename all files using a custom naming convention

# Python Code (Using os and datetime)
import os
from datetime import datetime

def rename_files(folder_path, prefix="file", extension=".txt"):
    files = os.listdir(folder_path)

    for index, filename in enumerate(files, start=1):
        old_path = os.path.join(folder_path, filename)

        # Skip directories

        if not os.path.isfile(old_path):
            continue

        # Build new filename

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"{prefix}_{timestamp}_{index}{extension}"
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"✅ Renamed: {filename} → {new_filename}")

# Sample Usage

rename_files("e:/Practice/RenameFolder", prefix="doc", extension=".txt")

# Sample Output
"""
    ✅ Renamed: notes.txt.txt → doc_20250721_215243_1.txt
    ✅ Renamed: summary.txt.txt → doc_20250721_215243_2.txt
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    os.listdir()        Liss all items in folder
    os.path.isfile()    Filters out directories
    datetime.now()      Adds unique timestamp to filename
    os.rename()         Performs the actual file renaming
"""
