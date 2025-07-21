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
    api_key = "4287b86b6880ee22d9a5dad325aede48" # Replace with your OpenWeatherMap API key

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

