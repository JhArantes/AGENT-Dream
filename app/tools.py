from strands import tool
import math

@tool
def calcular(expressao: str) -> float:
    """
    Avalia uma expressão matemática.
    Exemplo: "2 + 2 * 5" ou "math.sqrt(144)"
    """
    try:
        # escopo seguro
        allowed_names = {
            "math": math
        }

        return eval(expressao, {"__builtins__": {}}, allowed_names)

    except Exception as e:
        return f"Erro ao calcular: {e}"
