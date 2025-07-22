# Code #87: Automate Daily Weather Report Using API
"""
    🧠 Why This Matters?
    Used in:
    - 🗓️ Smart dashboards & IoT displays
    - 📧 Daily weather email digests
    - 🚗 Travel and logistics planning apps
    - 📱 Personal assistants & bot
"""
# Tier: Inermediate
# Goal: Fetch current weather data for a specific city using an API and display a human-firendly summary

# Pythoon Code
import requests

def get_weather(city):
    api_key = "<here you can place your api key>" # Replace with your OpenWeatherMap API key

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Bengaluru&appid={api_key}&units=metric"

    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["humidity"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"📍 Weather in {city}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌬️ Wind Speed: {wind_speed} m/s")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌈 Description: {weather.capitalize()}")
    else:
        print(f"Failed to retrieve weather for {city}. Status code:", response.status_code)

# Sample Usage
get_weather("Bengaluru")

# How to Get Your OpenWeatherMap API Key 
"""
    - Visit the https://home.openweathermap.org/
    - Login using your email, username and password
    - Confirm your email via the verification link they send
    - After logging in, go to https://home.openweathermap.org/api_keys
    - You'll see a default key already generated (you can rename it or create new ones)
    - Copy the key - it's your APPID for all API calls
    - Use it in your code at : api_key = "your_actual_api_key
    - Example call: https://api.openweathermap.org/data/2.5/weather?q=Bengaluru&appid=your_actual_api_key&units=metric
"""

# Concept Breakdown
"""
    Concept                     Description
    ----------------------------------------------------------------
    request.get()               Fetches data from live API
    data["main"]["temp"]        Accesses temperature info
    Units in "metric"           Uses Celsius & meters for SI format
    weather[0]["description"]   Short forecast summary
"""
# You can expand to fetch hourly/weekly reports, convert data to speech, or trigger alerts based on thresholds

# Real-World Connection
"""
    - Create  your own daily weatther notifier
    - Plan outdoor activities with wind/humidity checks
    - Use in chatbots or smart mirror displays
    - Attach to email automation for travel tips
"""