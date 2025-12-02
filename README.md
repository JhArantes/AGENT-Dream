# AI Chat API — FastAPI + Strands Agents + Ollama

Este projeto implementa uma API de chat integrada com um Agente de IA local,
utilizando o SDK Strands Agents e o modelo Ollama rodando localmente.

O agente possui:
- Conversação geral
- Tool personalizada para cálculos matemáticos
- Integração com FastAPI

---

## 🚀 Funcionalidades

- Endpoint `/chat` para conversação
- Uso de modelo LLM local pelo Ollama
- Tool matemática que resolve expressões
- Configuração via `.env`
- Respostas rápidas via FastAPI + Uvicorn

---

## 🧱 Requisitos

- Python 3.10+
- Ollama instalado
- Modelo local (ex.: `llama3.1`)

---

## 📦 Instalação

### 1. Instale o Ollama
Baixe em: https://ollama.com

### 2. Baixe o modelo desejado
```bash
ollama pull llama3.1
