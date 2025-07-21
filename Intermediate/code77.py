# Code #77: Backup a File Before Overwriting
"""
    🧠 Why This Matters?
    Used in:
    - 🔐 Preventing accidental data loss
    - 🧾 Safe overwrites in reporting, database dumps
    - 🧮 Versioning and rollback mechanisms
    - 📦 Daily snapshots before update
"""
# Tier: Intermediate
# Goal: Copy an original file to a backup before modifying the original

# Python Code
import shutil
import os

original = "example.txt"
backup = "example_backup.txt"

# Ensure the original file exists

if os.path.exists(original):
    shutil.copyfile(original, backup)
    print(f"Backup created: {backup}")

    # Now safely overwrite the original

    with open(original, "w") as file:
        file.write("Overwritten content safter creating backup.")
    print(f"{original} has been safely overwritten.")
else:
    print(f"File '{original}' does not exist. Cannot create backup.")

# Output
"""
    Backup created: example_backup.txt
    example.txt has been safely overwritten.
"""

# Concept Breakdown
"""
    Concept                     Explanation
    ----------------------------------------
    shutil.copyfile()           Copies content from original to backup
    os.path.exists()            Ensure file exists before action
    "w" mode                    Overwrites file with new content
    Safety logic                Prevents crashing if file is missing
"""
# Extendable to include timestamps in backup names like "exammple_2025_07_21.txt" or use directories like /backup/.

# Real-World Connection
"""
    - Git hooks creating pre-modification backups
    - ML pipelines preserving config snapshots
    - Log archival systems before nightly rotations
    - User settings backed up before edits
"""