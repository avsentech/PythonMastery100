# Code #100: Build a Personal Expense Tracker (CLI)
"""
    🧠 Why This Matters?
    Used in:
    - 📒 Managing daily expenses without bulky apps
    - 💻 CLI-based productivity tools
    - 📈 Tracking spending patterns for analysis
    - 🧠 Saving time with automation and simplicit
"""
# Tier: Intermediate-to-Advanced
# Goal: Add, view, and analyze persnal expenses via a terminal app

# Python Code (Minimal CLI Tracker)
import csv
from datetime import datetime

FILE = "expenses.csv"

def add_expense(amount, category, note=""):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, note])
    print("✅ Expense added!")

def view_expenses():
    print("\n📋 Expense History:")
    try:
        with open(FILE, mode="r") as f:
            reader = csv.reader(f)
            for row in reader:
                print("🗓️", row[0], "| 💰", row[1], "| 📂", row[2], "| 📝", row[3])
    except FileNotFoundError:
        print("⚠️ No expenses logged yet.")

def main():
    print("💰 Personal Expense Tracker 💰")
    while True:
        print("\nOptions:\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("🔘 Enter choice (1-3): ")

        if choice == "1":
            amount = input("💸 Amount: ")
            category = input("📂 Category: ")
            note = input("📝 Optional Note: ")
            add_expense(amount, category, note)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Exiting tracker. Stay frugal!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the tracker

main()

# Sample Interaction
"""
    1. Add Expense
    2. View Expenses
    3. Exit
    🔘 Enter choice (1-3): 2

    📋 Expense History:
    🗓️ 2025-07-22 | 💰 5000 | 📂 rent | 📝 Paid for July 2025
    🗓️ 2025-07-22 | 💰 200 | 📂 Milk | 📝 Daily milk product

    Options:
    1. Add Expense
    2. View Expenses
    3. Exit
    🔘 Enter choice (1-3): 3
    👋 Exiting tracker. Stay frugal!
"""

# Concept Breakdown
"""
    Concept         Description
    ----------------------------
    csv.writer()    Logs expenses to a persistent file
    datetime.now()  Captures timestamp for each expense
    input()         CLI interaction for user choices
    try-except      Handles file absence gracefully
"""
# You can expand this into monthly analysis, plotting graphs, or syncing with cloud.

# Real-World Extension Ideas
"""
    - 📈 Monthly totalsand category breakdown
    - 📊 Date visualizaton with matplotlib or pandas
    - 🧾 Export to Excel or Google Sheets
    - 📲 Convert to Flask app or sreamlit dashboard
    - 🔔 Budget alerts with thresholds
"""