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
from core.kanha_brain import kanha_think
from app.offline_cmds.commands import handle_command

@app.post("/chat")
def chat(query: Query):
    offline = handle_command(query.message)
    if offline:
        return {"reply": offline}

    reply = kanha_think(query.message)
    return {"reply": reply}