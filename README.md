# 🌇 Sustainable Smart City Assistant AI

![Smart City Assistant](https://img.shields.io/badge/AI-Smart%20City%20Assistant-brightgreen)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-orange)
![Backend](https://img.shields.io/badge/Backend-FastAPI-blue)
![AI](https://img.shields.io/badge/AI-IBM%20watsonx.ai%20%7C%20Granite-purple)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Under%20Development-yellow)

A **full-stack AI-powered Smart City Assistant** designed to provide intelligent and practical city-related services through a simple conversational interface.

The project combines **Streamlit**, **FastAPI**, **IBM watsonx.ai**, **IBM Granite**, and **SQLite** to create an interactive platform for citizens and urban users.

---

## 🚀 Project Overview

The **Sustainable Smart City Assistant** provides an AI-powered interface where users can interact with different smart-city services.

The system is designed around a simple architecture:

```text
User
 │
 ▼
Streamlit Frontend
 │
 │ REST API / JSON
 ▼
FastAPI Backend
 │
 ├──────────────► IBM watsonx.ai
 │                    │
 │                    ▼
 │               IBM Granite
 │
 └──────────────► SQLite Database
                       │
                       ▼
                    Feedback
```

The application can be extended in the future with real-time APIs, external city datasets, maps, transportation data, air-quality services, and other smart-city services.

---

## 🔑 Key Capabilities

### 🤖 AI Chat Assistant

Users can ask questions using natural language and receive responses generated through IBM watsonx.ai.

### 📝 Text Correction

Corrects grammar and spelling in user-provided text.

### 🍃 Eco Tips

Provides practical sustainability and environmentally friendly tips for urban life.

### 📊 KPI Forecasting

Accepts historical numerical data and uses the AI model to generate a forecast for the next three values.

### 📘 Policy Summary

Allows users to provide a city policy and ask the AI to summarize a specific aspect of it.

### 🌤️ Weather Information

Provides concise weather-related information for a requested city through the AI service.

### 🏙️ City Updates

Generates city-related updates including local happenings, IT-industry news, and general city developments.

### 💬 Feedback System

Users can submit feedback, which is stored in a SQLite database and can later be retrieved through the backend.

---

## 🛠️ Tech Stack

| Layer                   | Technology      |
| ----------------------- | --------------- |
| 💻 Frontend             | Streamlit       |
| ⚙️ Backend              | FastAPI         |
| 🐍 Programming Language | Python          |
| 🤖 AI Platform          | IBM watsonx.ai  |
| 🧠 AI Model             | IBM Granite     |
| 🌐 API Communication    | REST / JSON     |
| 🗄️ Database            | SQLite          |
| 🔗 ORM                  | SQLAlchemy      |
| 🚀 API Server           | Uvicorn         |
| 🔐 Configuration        | Python dotenv   |
| ☁️ Deployment           | Render / GitHub |

---

# 📁 Project Structure

```text
Smart-City-Assistant/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
│
├── docs/
│   ├── architecture.md
│   └── screenshots/
│
├── .github/
│   └── workflows/
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📂 Folder & File Description

| Folder/File                 | Purpose                                    |
| --------------------------- | ------------------------------------------ |
| `backend/`                  | FastAPI backend application                |
| `backend/main.py`           | API routes, AI integration, database logic |
| `backend/requirements.txt`  | Backend dependencies                       |
| `backend/.env.example`      | Example backend environment variables      |
| `frontend/`                 | Streamlit frontend application             |
| `frontend/app.py`           | Main user interface                        |
| `frontend/requirements.txt` | Frontend dependencies                      |
| `frontend/.env.example`     | Example frontend configuration             |
| `docs/`                     | Project documentation                      |
| `docs/architecture.md`      | System architecture documentation          |
| `docs/screenshots/`         | Project screenshots                        |
| `.github/`                  | GitHub configuration and workflows         |
| `.gitignore`                | Files that should not be committed         |
| `LICENSE`                   | Project license                            |
| `README.md`                 | Main project documentation                 |

---

# 💡 How the Application Works

## 1️⃣ User Interaction

The user interacts with the Streamlit frontend.

```text
User → Streamlit UI
```

The frontend provides interfaces for chat, text correction, eco tips, forecasting, policy summaries, weather information, city updates, and feedback.

---

## 2️⃣ API Request

When a user performs an action, the Streamlit application sends a REST request to the FastAPI backend.

```text
Streamlit
    ↓
HTTP Request
    ↓
FastAPI
```

Data is exchanged using JSON where appropriate.

---

## 3️⃣ AI Processing

For AI-powered features, FastAPI sends a carefully constructed prompt to IBM watsonx.ai.

```text
FastAPI
   ↓
IBM watsonx.ai
   ↓
IBM Granite
   ↓
Generated Response
```

The generated result is returned to the frontend.

---

## 4️⃣ Database

The project currently uses SQLite for storing user feedback.

```text
User Feedback
     ↓
FastAPI
     ↓
SQLAlchemy
     ↓
SQLite
```

This keeps the current project lightweight and easy to run locally.

---

# 📡 API Endpoints

| Method | Endpoint           | Description                          |
| ------ | ------------------ | ------------------------------------ |
| `GET`  | `/`                | Check backend status                 |
| `POST` | `/chat`            | AI-powered chat assistant            |
| `POST` | `/text-correction` | Correct grammar and spelling         |
| `GET`  | `/eco-tips`        | Generate an eco-friendly tip         |
| `POST` | `/forecast-kpi`    | Forecast the next 3 numerical values |
| `POST` | `/submit-feedback` | Store user feedback                  |
| `GET`  | `/feedback`        | Retrieve submitted feedback          |
| `POST` | `/policy-summary`  | Summarize a city policy              |
| `GET`  | `/weather`         | Generate weather information         |
| `GET`  | `/updates`         | Generate city-related updates        |

---

# 🧪 Local Setup

## 📋 Prerequisites

Install the following before running the project:

* Python 3.x
* Git
* Internet connection
* IBM watsonx.ai account/project
* IBM watsonx.ai API key

---

# 🔁 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-City-Assistant.git
cd Smart-City-Assistant
```

---

# ⚙️ 2. Backend Setup

Open a terminal in the project root.

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 3. Configure IBM watsonx.ai

Create a file named:

```text
backend/.env
```

Add:

```env
WATSONX_API_KEY=your_watsonx_api_key
WATSONX_PROJECT_ID=your_watsonx_project_id
WATSONX_URL=https://eu-de.ml.cloud.ibm.com
```

### ⚠️ Security

Never upload the real `.env` file to GitHub.

The repository contains `.env.example` only.

Never expose:

```text
WATSONX_API_KEY
WATSONX_PROJECT_ID
```

in source code, screenshots, README files, or public repositories.

---

# 🚀 4. Start the Backend

From the `backend` directory:

```bash
uvicorn main:app --reload
```

The backend will normally run at:

```text
http://127.0.0.1:8000
```

You can check the backend:

```text
http://127.0.0.1:8000/
```

Expected response:

```json
{
  "message": "Smart City Assistant Backend Running",
  "status": "online"
}
```

---

# 📖 5. Open API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to test the available API endpoints.

---

# 💻 6. Frontend Setup

Open a **new terminal**.

From the project root:

```bash
cd frontend
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔗 7. Configure Frontend API URL

Create:

```text
frontend/.env
```

Add:

```env
API_BASE_URL=http://127.0.0.1:8000
```

This tells the Streamlit frontend where the FastAPI backend is running.

---

# 🎨 8. Start Streamlit

From the `frontend` directory:

```bash
streamlit run app.py
```

Streamlit will provide a local address similar to:

```text
http://localhost:8501
```

Open that address in your browser.

---

# 🔄 Complete Local Run

You need **two terminals**.

### Terminal 1 — Backend

```bash
cd Smart-City-Assistant/backend
venv\Scripts\activate
uvicorn main:app --reload
```

### Terminal 2 — Frontend

```bash
cd Smart-City-Assistant/frontend
venv\Scripts\activate
streamlit run app.py
```

Then open the Streamlit URL in your browser.

---

# 🧪 Testing Checklist

Before pushing the project to GitHub, verify:

* [ ] Backend starts successfully
* [ ] `/` endpoint works
* [ ] Swagger documentation opens
* [ ] AI chat works
* [ ] Text correction works
* [ ] Eco tips work
* [ ] KPI forecasting works
* [ ] Feedback submission works
* [ ] Feedback retrieval works
* [ ] Policy summary works
* [ ] Weather feature works
* [ ] City updates work
* [ ] Streamlit frontend starts
* [ ] Frontend communicates with FastAPI
* [ ] `.env` is not tracked by Git
* [ ] API keys are not present in source code
* [ ] `venv/` is not tracked
* [ ] `__pycache__/` is not tracked

---

# 🗄️ Database

The application currently uses **SQLite**.

The database is automatically created by SQLAlchemy when the backend starts.

Current feedback table:

```text
feedback
│
├── id
├── user_id
└── message
```

The SQLite database is intentionally excluded from Git using `.gitignore`.

This allows every developer to create their own local database environment.

---

# 🔒 Security

The project follows basic security practices for a development project.

### Environment Variables

Sensitive IBM watsonx.ai credentials are stored in `.env`.

### Git Protection

The following should not be committed:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
*.db
*.sqlite
```

### Example Configuration

The repository contains:

```text
.env.example
```

instead of real credentials.

---

# ☁️ Deployment

The backend can be deployed to a platform such as Render.

A production deployment should provide environment variables through the hosting platform rather than committing secrets to GitHub.

Example backend start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Required environment variables:

```text
WATSONX_API_KEY
WATSONX_PROJECT_ID
WATSONX_URL
```

For the frontend, configure:

```text
API_BASE_URL=<your-deployed-backend-url>
```

---

# 🐳 Future Deployment Options

The project can later be extended with:

* Docker
* GitHub Actions
* Render
* Railway
* AWS
* Azure
* Google Cloud

---

# 🛣️ Future Improvements

The current version provides the foundation for a larger Smart City platform.

Possible future improvements include:

* 🌤️ Real-time weather API integration
* 🌫️ Real-time air-quality data
* 🚦 Traffic monitoring
* 🚌 Public transportation information
* 🗺️ Interactive city maps
* 🏙️ Place recommendations
* 🛡️ Real-time safety information
* 📊 City analytics dashboards
* 👤 User authentication
* 🗄️ PostgreSQL/MySQL production database
* 🔐 JWT authentication
* 📱 Mobile application
* 🌐 Production deployment
* 🤖 Improved AI agent capabilities
* 📈 Advanced forecasting models

---

# 📸 Screenshots

Project screenshots can be stored inside:

```text
docs/screenshots/
```

Example:

```text
docs/
└── screenshots/
    ├── dashboard.png
    ├── ai-chat.png
    ├── eco-tips.png
    ├── forecast.png
    └── feedback.png
```

Screenshots can then be displayed in this README using:

```markdown
![Smart City Dashboard](docs/screenshots/dashboard.png)
```

---

# 📚 Learning & Documentation Resources

* **FastAPI** — Web API framework for Python
* **Streamlit** — Python framework for building interactive applications
* **SQLAlchemy** — Python SQL toolkit and ORM
* **IBM watsonx.ai** — Enterprise AI platform
* **IBM Granite** — IBM's family of foundation models
* **Uvicorn** — ASGI server for Python applications
* **GitHub** — Source control and collaboration

---

# 🤝 Contributing

Contributions and suggestions are welcome.

A typical contribution workflow is:

```text
Fork
  ↓
Create Branch
  ↓
Make Changes
  ↓
Test
  ↓
Commit
  ↓
Push
  ↓
Pull Request
```

Before submitting changes, make sure the application still runs correctly.

---

# 👨‍💻 Author

**Prashanth**

GitHub:

`https://github.com/YOUR_USERNAME/Smart-City-Assistant`

---

# 📄 License

This project is released under the **MIT License**.

You are free to use, modify, and distribute the project according to the terms of the license.

---

# 🌍 Vision

The goal of this project is to explore how **Artificial Intelligence can make interactions with city services simpler, more accessible, and more sustainable**.

> 🌱 **Smarter technology. Better cities. A more sustainable future.**

---

⭐ If you find this project useful, consider giving the repository a star!
