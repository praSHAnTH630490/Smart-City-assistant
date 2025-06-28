
# 🌇 Sustainable Smart City Assistant AI

A **full-stack AI-powered assistant** built for the sustainable cities of the future.  
It delivers intelligent city services like weather insights, urban policies, eco tips, and smart chat — powered by **FastAPI**, **Streamlit**, and the **IBM Granite Foundation Model** hosted on **IBM Watson AI**


![Smart City Assistant](https://img.shields.io/badge/Powered%20By-FastAPI%20%7C%20IBM%20Granite-brightgreen)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-orange)
![Backend](https://img.shields.io/badge/Backend-FastAPI-blue)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Under_Development-yellow)

---

## 🚀 Project Overview

The **Sustainable Smart City Assistant** is designed to help citizens and tourists:

- 🧭 Navigate smarter  
- 🌤️ Stay informed on climate and air quality  
- 🛡️ Track crime and safety metrics  
- 🌱 Receive sustainability and eco-friendly tips  
- 💬 Talk to an intelligent assistant powered by **IBM Granite AI**

---

## 🔑 Key Capabilities

- ✅ **Live Weather Forecast & Air Quality**
- 🛡️ **City Safety & Crime Stats**
- 🏙️ **Must-See Place Recommender**
- 🧠 **Conversational AI Chatbot**
- 📝 **Grammar & Spelling Correction**
- 📘 **Policy Generator & Checker**
- 🍃 **Sustainability Tips & Awareness**
- 🌐 **Seamless Frontend + Backend Integration**

---

## 🛠️ Tech Stack

| Layer         | Tech Used                               |
|---------------|------------------------------------------|
| 💻 Frontend   | Streamlit, HTML/CSS (custom styling)     |
| 🧠 Backend    | FastAPI, Python 3, Requests               |
| 🤖 Model Host | Google Colab + Ngrok (IBM Granite Model) |
| 🌐 API Comm.  | REST (JSON over HTTP)                    |
| ☁️ Deployment | GitHub, Render                           |

---
📁 Project Structure

smart_city_assistant/
├── backend/                          
│   ├── main.py                       # FastAPI backend               
│   ├── requirements.txt              # Backend Python dependencies
│   ├── .env                          # Optional environment variables
│   ├── .gitignore                    # Ignore venv, __pycache__, etc.
│   └── README.md                     # Backend-specific documentation
│
├── frontend/                         # Streamlit frontend
│   ├── app.py                        # Main Streamlit application
│   ├── assets/                       # Images, icons, logos, animations, etc.
│   ├── styles.css                    # Optional custom CSS for better UI
│   ├── README.md                     # Frontend-specific documentation
│
├── model_colab/                      # Model hosting (IBM Granite on Colab)
│   ├── granite_model_inference.ipynb # Colab notebook with ngrok serving
│   └── model_config.json             # Any model-related prompt/config info
│
├── render.yaml                       # Deployment config for Render (backend)
├── LICENSE                           # MIT License or similar
├── README.md                         # Root README (project overview)
└── .gitignore                        # Ignore venv, .ipynb_checkpoints, etc.


📂 Description of Each Folder

Folder/File          Purpose
backend/FastAPI      server with endpoints that talk to the AI model via ngrok
frontend/Streamlit   dashboard UI that communicates with FastAPI backend
model_colab/Jupyter  notebook that hosts the IBM Granite model using ngrok
render.yaml	         Tells Render.com how to deploy the backend
README.md	         Overall project guide and documentation
requirements.txt	 Lists backend or shared Python dependencies
.gitignore	         Excludes venv folders, cache, large binaries from Git


## 💡 Features in Action

- 🔌 **Modular API**: Every feature is mapped to its own route in FastAPI.
- 🔄 **Colab Integration**: The backend connects to your AI model via `/chat`.
- 🌱 **Eco-Aware Intelligence**: Promotes responsible urban behavior.
- 💬 **Natural Language Interface**: Ask questions in plain English.

---

## 🧪 Quickstart (Local Setup)

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/praSHAnTH630490/Smart-City-assistant.git
cd Smart-City-assistant/backend

🧱 2. Create & Activate Virtual Environment

python -m venv venv

venv\Scripts\activate        # On Windows
# or
source venv/bin/activate
     # On Linux/Mac

📦 3. Install Dependencies

pip install -r requirements.txt

🚀 4. Run FastAPI Server

uvicorn main:app --reload

Access it via:

👉 http://localhost:8000/docs (Swagger UI)

📡 API Endpoints

Endpoint	            Description
/chat	                AI chat assistant via IBM Granite
/text-correction	    Fixes grammar & spelling
/climate-update	        Real-time weather and air quality
/place-recommendation	City travel & tourism suggestions
/smartcity-data	        Urban data: crime, oxygen, traffic, etc.
/policy-generator	    Draft city policies with AI

All endpoints forward prompts to your Colab-hosted IBM Granite model using a secure ngrok URL.

🌍 Deploying to Render
📁 Add render.yaml

services:
  - type:           web
    name:           smart-city-backend
    env:            python
    plan:           free
    buildCommand:   pip install -r requirements.txt
    startCommand:   uvicorn main:app --host 0.0.0.0 --port 10000
    autoDeploy:     true

🔧 Deploy in 1 Minute

Push this project to GitHub

Login to Render

Click "New Web Service"

Connect this GitHub repo

Use the render.yaml file or paste build/start commands manually

✅ Your backend is now live!

🔗 Useful Resources

📚 FastAPI Docs

🎨 Streamlit Docs

🧠 IBM Granite AI

🛰️ Ngrok

☁️ Render Hosting

👨‍💻 Author

* Prashanth

🔗 GitHub Profile

📄 License
This project is released under the MIT License.
Feel free to explore, fork, contribute, and innovate 🚀

💡 Built for a greener, smarter, AI-powered city experience 🌍✨


---

