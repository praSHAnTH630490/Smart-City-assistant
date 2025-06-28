import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from ibm_watsonx_ai import Credentials
import json

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("WATSONX_API_KEY")
project_id = os.getenv("WATSONX_PROJECT_ID")
url = os.getenv("WATSONX_URL")

# ✅ Granite model setup
creds = Credentials(api_key=api_key, url=url)
model = ModelInference(
    model_id="ibm/granite-3-2b-instruct",
    credentials=creds,
    params={"decoding_method": DecodingMethods.GREEDY, "max_new_tokens": 50},
    project_id=project_id
)

def call_model(prompt: str):
    try:
        response = model.generate(prompt=prompt)
        return response.get("results", [{}])[0].get("generated_text", "No response")
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Granite model call failed: {e}")

# ✅ Database setup
DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    message = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

# ✅ FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Models
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

# ✅ Endpoints
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
            parsed = {"description": raw, "temp": None}
        return {"updates": parsed}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {e}")

@app.get("/")
def root():
    return {"message": "Smart City Assistant Backend Running with Granite Model"}
