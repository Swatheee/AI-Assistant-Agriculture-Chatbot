import google.generativeai as genai
import os
from dotenv import load_dotenv
from weather_utils import get_weather_by_city

load_dotenv()
GEMINI_API_KEY = os.getenv("AIzaSyCiSXr7wE95nWFE5jTds4zpdG6mI43HzGM")


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def extract_location_with_gemini(user_input):
    prompt = f"Extract the location (like city or village) from this query: {user_input}"
    response = model.generate_content(prompt)
    return response.text.strip()

def get_gemini_response(user_query):
    try:
        location = extract_location_with_gemini(user_query)
        weather_report = get_weather_by_city(location)

        full_prompt = f"""
        You are an agricultural AI assistant. Based on the following information, provide crop suggestions, fertilizer advice, and solutions to farming problems.

        ❓ Farmer's question: {user_query}

        🌦️ Weather Info for {location}:
        {weather_report}

        Respond clearly in 2-3 paragraphs with headings like "Crop Recommendation", "Fertilizer Advice", and "Problem & Solution".
        """

        response = model.generate_content(full_prompt)
        return response.text.strip()

    except Exception as e:
        return "⚠️ Unable to process your request. Please try again later."
