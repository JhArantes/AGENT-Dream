from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
from app.agent import processar_mensagem

app = FastAPI()

class UserInput(BaseModel):
    message: Annotated[str, "The user's input message"]

@app.post("/chat/AgentMath")
async def chat(payload: UserInput):
    resposta = await processar_mensagem(payload.message)
    return {"response": resposta}
