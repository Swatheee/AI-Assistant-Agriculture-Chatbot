import streamlit as st
from googletrans import Translator
import requests
import os
import speech_recognition as sr
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import base64
# ------------------- Load API Keys ---------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

# ------------------- Set Gemini API ---------------------
genai.configure(api_key="AIzaSyCiSXr7wE95nWFE5jTds4zpdG6mI43HzGM") 

# ------------------- Set Background ---------------------

# ------------------- Translate ---------------------
def translate_text(text, target_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

# ------------------- Weather ---------------------
def get_weather_by_city(city):
    if not OPENWEATHERMAP_API_KEY:
        return "⚠️ OpenWeatherMap API key missing."
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return "⚠️ City not found."
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return f"🌤️ Weather: {weather}\n🌡️ Temp: {temp}°C\n💧 Humidity: {humidity}%"
    except Exception as e:
        return f"❌ Weather error: {str(e)}"

# ------------------- Voice Input ---------------------
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        try:
            audio = r.listen(source, timeout=5)
            st.success("✅ Captured voice")
            return r.recognize_google(audio)
        except:
            st.error("❌ Voice recognition failed.")
            return ""

# ------------------- Gemini AI Response ---------------------
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("models/gemini-pro")  # Fixed model name
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"

# ------------------- UI Setup ---------------------
theme = st.selectbox("Choose Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""<style>body, .stApp { background-color: #1e1e1e; color: white; }</style>""", unsafe_allow_html=True)
else:
    st.markdown("""<style>body, .stApp { background-color: #ffffff; color: black; }</style>""", unsafe_allow_html=True)



st.markdown("<h1 style='text-align: center; color: green;'>🌾 AgriChatbot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #008000;'>Multilingual | Voice Assistant | Gemini AI Powered</h4>", unsafe_allow_html=True)

languages = ["English", "Hindi", "Telugu", "Kannada", "Marathi", "Tamil", "Malayalam"]
selected_language = st.selectbox("Choose your language:", languages)

# Choose Input Mode
input_mode = st.radio("Choose Input Mode:", ["📝 Text", "🎤 Voice"])
user_input = ""

if input_mode == "📝 Text":
    user_input = st.text_input("Type your query:")
else:
    if st.button("Speak Now"):
        user_input = recognize_speech()
        if user_input:
            st.write(f"🗣️ You said: `{user_input}`")

if user_input:
    translated_input = translate_text(user_input, target_lang='en')
    st.write(f"**Translated Query (English):** {translated_input}")

    if "weather" in translated_input.lower():
        location = st.text_input("Enter your city name:")
        if location:
            weather_result = get_weather_by_city(location)
            st.success(weather_result)
    else:
        ai_response = get_gemini_response(translated_input)
        translated_response = translate_text(ai_response, target_lang=selected_language.lower())
        st.markdown(f"🌱 **AI Response in {selected_language}:** {translated_response}")
