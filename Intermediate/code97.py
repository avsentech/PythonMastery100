# Code #97: Zip and Unzip Files Using zipfile
# Tier: Intermediate
# Goal: Create and extract ZIP archives with Python

#Python Code
import zipfile
import os

def zip_files(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                zipf.write(file_path, arcname=file)
    print(f"🗜️ Created ZIP: {zip_name}")

def unzip_file(zip_name, extract_to):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"📂 Extracted to: {extract_to}")

# Sample Usage

zip_files("e:/Practice/Python/Pythonmastry100/Intermediate", "intermediate_code.zip")
unzip_file("intermediate_code.zip", "e:/Practice/Python/Pythonmastry100/Extracted")