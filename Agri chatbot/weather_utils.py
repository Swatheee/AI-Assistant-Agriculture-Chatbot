import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the OpenWeatherMap API key from .env file
api_key = os.getenv("acf7f5fd5285e2a108aff544536625f9")

def get_weather_by_city(city):
    if not api_key:
        return "⚠️ OpenWeatherMap API key missing. Please check your .env file."

    # Construct the URL for the OpenWeatherMap API request
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"acf7f5fd5285e2a108aff544536625f9"}&units=metric"

    try:
        # Send the request to the API
        response = requests.get(url)
        
        # Check if the response was successful
        if response.status_code != 200:
            return f"⚠️ Failed to retrieve data: {response.status_code}. Check the city name or try again later."
        
        # Parse the response JSON
        data = response.json()

        # Check if the city was found
        if data.get("cod") != 200:
            return "⚠️ City not found. Please check the city name and try again."
        
        # Extract weather details
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        # Return formatted weather information
        return f"🌤️ Weather: {weather}\n🌡️ Temperature: {temp}°C\n💧 Humidity: {humidity}%"

    except requests.exceptions.RequestException as e:
        # Handle errors in the request process
        return f"⚠️ Error fetching weather: {str(e)}"

    except Exception as e:
        # Handle other exceptions
        return f"⚠️ Unexpected error: {str(e)}"
