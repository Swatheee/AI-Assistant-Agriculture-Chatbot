🌾 AI AgriChatbot – Intelligent Farming Assistant
An AI-powered multilingual chatbot built to support farmers by providing real-time, personalized agricultural guidance using voice/text interaction and smart AI suggestions.

🧠 Project Overview
**AI AgriChatbot** is a smart virtual assistant that helps farmers receive instant support related to crop selection, weather-based suggestions, fertilizer use, pest control, and general farming practices. It supports multiple languages and enables both voice and text input/output, making it accessible to all users including those with low literacy levels. The chatbot uses Google’s Gemini API for intelligent replies and integrates weather data for context-aware suggestions.

 🚀 Features
- 🤖 **AI-Powered Responses** via Gemini API  
- 🌦️ **Real-Time Weather Suggestions** (OpenWeatherMap API)  
- 🎙️ **Voice Input and Output Support**  
- 🌐 **Multilingual Translation & Speech Output**  
- 📊 **Optional Crop Stats and Charts**  
- 🖼️ **Image Upload for Future Crop Detection Use**  
- 🧑‍🌾 **Farmer-Friendly UI** using Streamlit  
- 🌗 **Dark/Light Theme Toggle**

 🏗️ Project Structure
AGRI_CHATBOT/
│
├── .env # API keys and config
├── ai_response.py # Handles AI replies using Gemini
├── chart_utils.py # Crop/price chart utilities
├── gemini_utils.py # Gemini API helper
├── main.py # Streamlit App Entry Point
├── translator.py # Language detection and translation
├── voice_input.py # Handles voice input and output
├── weather_utils.py # Real-time weather logic
├── requirements.txt # Python dependencies
└── assets/ # Backgrounds, icons, etc.

 ⚙️ Installation & Setup
1. Clone the Repository
```bash
git clone https://github.com/your-username/AI-AgriChatbot.git
cd AI-AgriChatbot

2. Create Virtual Environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install Requirements
pip install -r requirements.txt

4. Setup Environment Variables
Create a .env file in the root directory with:
GEMINI_API_KEY=your_google_generativeai_key
WEATHER_API_KEY=your_openweathermap_key

▶️ Run the Application
streamlit run main.py

🤝 Contribution
Contributions are welcome! Open issues or pull requests for improvements or new features.

👩‍💻 Developed By
Swathi Duggineni
Student | AI Enthusiast | Builder of Smart Farming Solutions 🌱


Let me know if you'd like me to customize this for a team project or generate badges (like build status, license, etc.) too.


