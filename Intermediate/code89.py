# Code #89: Create a CLI Tool to Convert Currency Using API
"""
    🧠 Why This Matters?
    Used in:
    - 🧮 Travel calculators & expense tools
    - 💵 E-commerce price localization
    - 📈 Financial dashboards
    - 🛠️ CLI bots that automate cross-border report
"""
# Tier: Intermediate
# Goal: Build a command-line tool that fetches real-time exchange rates via API and converts between two currencies

# Python Code (Using exchangerate.host -Free & No API Key Needed)
import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}&access_key=e36a4ef7eae382326e59c7c1c2ec4983"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result = data["result"]
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        print("❌ Failed to fetch exchange rates. Try again later.")

# Sample CLI Usage

if __name__ == "__main__":
    print("🌍 Currency Converter")
    from_curr = input("Convert from (e.g., USD):").upper()
    to_curr = input("convert to (e.g., INR):").upper()
    amt = float(input("Amount: "))

    convert_currency(from_curr, to_curr, amt)

# Sample Output
"""
    🌍 Currency Converter  
    Convert from (e.g., USD): USD  
    Convert to (e.g., INR): INR  
    Amount: 100  
    100 USD = 8332.00 INR
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    exchangerate.host   Free currency conversion API (no signup)
    Input via input()   CLI tool prompts user to enter currencies
    JSON parsing        Extracts result from response data
    Formatting          Round result with .2f precision
"""
# You can add support for historical rates, currency symbols, or even loop-based conversions.

# Real-World Connection
"""
    - Convert expenses in budgetting apps
    - Travel bots or destination planners
    - Price converters for global storefronts
    - Tax software handling forex-based invoices
"""

