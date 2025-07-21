# Code #76: Create a Simple Config Reader from a .txt File
"""
    🧠 Why This Matters?
    Used in:
    - 🧾 Reading app settings or secrets
    - 🔧 Adjusting tool behavior without editing code
    - ⚙️ Loading user preferences or runtime variable
"""
# Tier: Intermediatte
# Goal: Parse a .txt file with key=value lines and convert it into a dictionary

# Python Code
def read_config(filename):
    config = {}
    with open(filename, "r") as file:
        for line in file:
            if "=" in line and not line.strip().startswith("#"): # Skip comments

                key, value = line.strip().split("=", 1)
                config[key.strip()] = value.strip()

    return config

# Sample Usage

settings = read_config("config.txt")
print("Config Settings:", settings)

# Sample Output
"""
    Config Settings: {'username': 'Sena', 'max_retries': '5', 'timeout': '30', 'enable_logs': 'True'}
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    open(filename)      Reads file line by line
    .split("=")         Separates key and value
    .strip()            Cleans whitespace
    Dictionary          Stores config as key-value pairs
    startswith("#")     Optional: skip commment lines
"""
# You can extend with type conversion, default values, or JSON/YAML support for advanced configs.

# Real-World connection
"""
    - CLI tools loading command presets
    - Game engines loading graphic/audio settings
    - Saas dashboards customizing themes and limits
    - Automation scripts importing task instructions
"""
