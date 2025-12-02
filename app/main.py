from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import processar_mensagem

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(payload: ChatInput):
    resposta = await processar_mensagem(payload.message)
    return {"response": resposta}
