# 🌆 Streamlit Frontend — Sustainable Smart City Assistant AI

This is the **frontend interface** for the Sustainable Smart City Assistant AI — built using **Streamlit** to provide users with an interactive dashboard that communicates with the FastAPI backend and IBM Granite model hosted via Colab.

---

## 🎯 Purpose

This frontend allows users to:
- Chat with an AI assistant
- View smart city data (climate, air quality, safety, etc.)
- Get real-time weather reports and eco tips
- Perform grammar and spelling correction
- Use custom policy or forecast generators

All functionality is powered by backend APIs served over a live URL.

---

## 🚀 How to Run Locally

### 🔧 1. Clone the Project & Navigate to `frontend/`


git clone https://github.com/praSHAnTH630490/Smart-City-assistant.git
cd Smart-City-assistant/frontend

🧪 2. Create and Activate a Virtual Environment (optional but recommended)

python -m venv venv
venv\Scripts\activate  # On Windows

📦 3. Install Requirements

pip install -r requirements.txt
▶️ 4. Run the App

streamlit run streamlit_app.py
Access it at: http://localhost:8501

🌐 Backend API Requirement

This app expects a publicly accessible FastAPI backend, deployed via Render or ngrok.

In your streamlit_app.py, set:


API_URL = "https://your-backend-url.onrender.com"
Or use st.secrets for safer API key management:


import streamlit as st
import requests

API_URL = st.secrets["api_url"]
Then set your secrets.toml in .streamlit/:

api_url = "https://smart-city-backend.onrender.com"
📁 File Structure

frontend/

├── streamlit_app.py         # Main dashboard code
├── styles.css               # Optional custom styling
├── requirements.txt         # Required packages
├── .streamlit/
│   └── secrets.toml         # For securely storing backend URL or API keys
└── README.md                # This file

📸 Preview (Optional GIF / Screenshot)

Add a screenshot or GIF preview of your UI here

🤝 Author

Prashanth

🔗 GitHub

📄 License
This project is licensed under the MIT License.

💡 Designed for smarter, safer, and more sustainable urban futures 🌍
