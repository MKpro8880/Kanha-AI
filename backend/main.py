from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Kanha AI Backend")

class Query(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Kanha AI is running"}

@app.post("/chat")
def chat(query: Query):
    return {
        "reply": "🙏 Kanha is listening. LLM integration coming soon."
    }