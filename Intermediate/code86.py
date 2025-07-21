# Code #86:Parse JSON Response from an API
"""
    🧠 Why This Matters?
    Used in:
    - 🌍 Fetching real-time data from websites
    - 📱 Mobile and web integrations
    - 🔍 Automating reports and dashboards
    - 🧠 Learning data formats used across API
"""
# Tier: Intermediate
# Goal: Send a GET request to an API and extract meaning full data for its JSON response

# Python Code
import requests

# Sample public API (can be swapped ith any other JSON-based API)

url = "https://api.agify.io?name=Sena"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Parsed JSON Response:")
    print(f"Name: {data['name']}")
    print(f"Estimasted Age: {data['age']}")
else:
    print(f"API request failed with status code {response.status_code}")

# Sample Output
"""
    Parsed JSON Response:
    Name: Sena
    Estimated Age: 33
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    request.get()       Sends HTTP GET request to the API
    response.json()     Converts JSON response to Python dictionary
    status_code==200    Confirms successful request
    Dicionary Access    Extracts values using keys like 'name','age'
"""
# You can acess nested values too like data['location']['city'], depending on the API structure

# Real-World Connection
"""
    - Fetching currency rates, weather, crypto, movie info
    - Syncing product data or customer profiles
    - Interfacing with AI tools, automation systems
    - Chatbots using APIs for jokes, facts, or summaries
"""