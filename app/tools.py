from strands import tool
import math

@tool
def calcular(expressao: str) -> float:
    """
    Executa cálculos matemáticos com segurança.
    Suporta operações e funções do módulo math.
    """
    try:
        # Ambiente seguro com funções do math
        permitido = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        
        # Remove acesso a builtins
        permitido["__builtins__"] = {}

        # Executa expressões matemáticas safely
        resultado = eval(expressao, permitido, {})
        
        return resultado

    except Exception as e:
        return f"Erro ao calcular: {str(e)}"
