# Code #75: Log Erros to a File Using Try-Except
"""
    🧠 Why This Matters?
    Used in:
    - 🔍 Debugging production scripts
    - 📋 Creating persistent audit trails
    - 📦 Automated exception tracking
    - 🧾 Cron jobs, scrapers, and diagnostic
"""
# Tier: Intermediate
# Goal: Catch exceptions, write them to a .log file, and notify the user

# Python Code

log_file = "error.log"

try:
    result = 10 /0 # Example error: division by zero

except Exception as e:
    with open(log_file, "a") as log:
        log.write(f"Error: {str(e)}\n")
    print("An error occured. Logged to file.")

# Sample Output
"""
    An error occurred. Logged to file.
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    try-except          Catches unexpected runtime failures
    Exception           Generic error type (can be narrowed later)
    str(e)              Extracts error message from exception object
    log.write()         Appends message to a persistent file
"""
# You can log timestamps, traceback info, error type, or user context for deeper insight.

# Real-World Connection
"""
    - Web apps logging API failures
    - Background scripts writing to error reports
    - Debug info for finance tools and form validators
    - IoT or embedded systems capturing rare faults
"""