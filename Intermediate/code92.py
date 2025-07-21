# Code #92: Build a Simple URL Shortener
"""
🧠 Why This Matters?
Used in:
- 💼 Marketing & campaign link tracking
- 🔗 Sharing readable URLs on social media
- 🧠 Preprocessing links for datasets & bots
- 📈 Analytics platforms & dashboard
"""
# Tier: Intermediate
# Goal: Use an external API to shorten a long URL with a Python script

# Python Code (Using shrtco.de API - Free & No Signup)

import requests

def shorten_url(long_url):
    api_url = f"https://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)

    if response.status_code == 201:
        data = response.json()
        short_url = data["result"]["short_link"]
        print("🔗 Shortened URL:", short_url)
    else:
        print("❌ Failed to shorten URL.")
        print("📡 Status Code:", response.status_code)
        print("📝 Response:", response.text)

# Sample Usage

long_url_input = input("Enter URL to shorten: ")
shorten_url(long_url_input)
