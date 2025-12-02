import requests
import json

def ask_ollama(prompt, model="llama3.2:3b"):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': model,
            'prompt': prompt,
            'stream': False,
            'options': {
                'temperature': 0.7,
                'num_predict': 200
            }
        }
    )
    return response.json()['response']

# Teste
if __name__ == "__main__":
    answer = ask_ollama("Tell me about agentic AI")
    print(answer)


