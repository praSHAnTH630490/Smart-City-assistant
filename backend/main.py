import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import requests
import json
# Load environment variables
load_dotenv()
COLAB_MODEL_API = os.getenv("COLAB_MODEL_API")  # e.g., https://xxxx.ngrok-free.app/chat
DATABASE_URL = "sqlite:///./app.db"

# Database setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    message = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Models
class Prompt(BaseModel):
    prompt: str

class TextInput(BaseModel):
    text: str

class FeedbackModel(BaseModel):
    user_id: str
    message: str

class PolicyRequest(BaseModel):
    query: str
    policy_text: str

class AnomalyPayload(BaseModel):
    data: list[float]

# Model call helper
def call_model(prompt: str):
    try:
        response = requests.post(COLAB_MODEL_API, json={"prompt": prompt}, timeout=30)
        response.raise_for_status()
        return response.json().get("text", "No response")
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Model call failed: {e}")

# Endpoints
@app.post("/chat")
def chat_endpoint(payload: Prompt):
    return {"response": call_model(payload.prompt)}

@app.post("/text-correction")
def correct_text(payload: TextInput):
    prompt = f"Please correct the grammar and spelling in the following text:\n\n{payload.text}\n\nReturn only the corrected version."
    return {"corrected_text": call_model(prompt)}

@app.get("/eco-tips")
def eco_tips():
    prompt = "Give a unique and practical eco-friendly tip for urban life. Include an emoji and short explanation."
    return {"tip": call_model(prompt)}

@app.post("/forecast-kpi")
def forecast_kpi(payload: AnomalyPayload):
    prompt = f"Given this historical data: {payload.data}, forecast the next 3 values. Return only a JSON list like: [x, y, z]"
    return {"forecast_next_3_periods": call_model(prompt)}

@app.post("/submit-feedback")
def submit_feedback(fb: FeedbackModel, db=Depends(get_db)):
    entry = Feedback(user_id=fb.user_id, message=fb.message)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return {"message": "Feedback submitted"}

@app.get("/feedback")
def get_feedback(db=Depends(get_db)):
    items = db.query(Feedback).all()
    return [{"user_id": i.user_id, "message": i.message} for i in items]

@app.post("/policy-summary")
def policy_summary(req: PolicyRequest):
    prompt = f"Summarize the following city policy focusing on '{req.query}':\n{req.policy_text}"
    return {"summary": call_model(prompt)}

@app.get("/weather")
def weather(city: str):
    prompt = f"Give me the current weather in {city}, including temperature, condition, and suitable emoji."
    return {"weather": {"description": call_model(prompt)}}

@app.get("/updates")
def city_updates(city: str):
    prompt = (
        f"Give me the latest updates about {city}, including political developments, IT industry news, and local happenings. "
        "Respond in JSON format like: {\"description\": \"...\", \"temp\": 31}"
    )

    try:
        raw = call_model(prompt)
        try:
            parsed = json.loads(raw) if isinstance(raw, str) else raw
        except json.JSONDecodeError:
            parsed = {"description": raw, "temp": None}  # fallback

        return {"updates": parsed}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {e}")
    
@app.get("/")
def root():
    return {"message": "Smart City Assistant Backend Running"}