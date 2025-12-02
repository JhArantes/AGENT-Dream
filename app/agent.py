import os
from dotenv import load_dotenv
from strands import Agent
from strands.models.ollama import OllamaModel
from app.tools import calcular

load_dotenv()

MODEL = os.getenv("LLM_MODEL")
URL = os.getenv("OLLAMA_URL")
AGENT_NAME = os.getenv("AGENT_NAME")

llm = OllamaModel(
    model_id=MODEL,
    host=URL,
    options={
        "system": (
            "Você é um agente que responde perguntas. "
            "Se a consulta envolver cálculos, use a ferramenta 'calcular'."
        )
    }
)

agent = Agent(
    name=AGENT_NAME,
    model=llm,
    tools=[calcular]
)

async def processar_mensagem(mensagem: str) -> str:
    try:
        # Tenta métodos comuns
        if hasattr(agent, 'arun'):
            result = await agent.arun(mensagem)
        elif hasattr(agent, 'acall'):
            result = await agent.acall(mensagem)
        elif hasattr(agent, 'ainvoke'):
            result = await agent.ainvoke(mensagem)
        elif hasattr(agent, 'invoke'):
            result = await agent.invoke(mensagem)
        else:
            # Se nenhum método async, tenta síncrono
            result = agent.run(mensagem)
        
        return result.output_text
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        return f"Erro: {str(e)}"