from strands import Agent
from strands.models.ollama import OllamaModel
from app.tools import calcular

model = OllamaModel(
    model_id="llama3.1",
    host="http://localhost:11434"
)

agent = Agent(
    model=model,
    tools=[calcular],
    system_prompt="""
    You are a math assistant agent.
    When a calculation is required, use the tool 'calcular'.
    """
)

async def processar_mensagem(mensagem: str) -> str:
    """
    Função chamada pela API
    """
    resposta = agent(mensagem)
    return resposta
