import sys
import requests

api_key = "YOUR_API_KEY_HERE"  # Get your API key from openweathermap.org

# Get city name from command-line argument
try:
    city = sys.argv[1]
except IndexError:
    sys.exit("Missing command-line argument")

# Call the weather API
try:
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    )

    response.raise_for_status()

    data = response.json()

    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(
        f"City: {city}\n"
        f"Temperature: {temp}°C\n"
        f"Condition: {condition}\n"
        f"Humidity: {humidity}%\n"
        f"Wind speed: {wind_speed} m/s"
    )

except requests.RequestException:
    sys.exit("Request failed")