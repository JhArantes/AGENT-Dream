


# ⚙️💬 AI Chat API — FastAPI + Strands Agents + Ollama

<div align="center">

![AI Chat API](IMGs/AI_Chat_IMG.png)

**API de Chat Inteligente com Agentes Locais e Ferramentas Personalizadas**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange.svg)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## ✨ **Recursos Principais**

| Recurso | Descrição |
|---------|-----------|
| 🤖 **Agente Inteligente** | Processamento de linguagem natural com raciocínio contextual |
| 🧮 **Ferramenta Matemática** | Resolução de expressões matemáticas complexas |
| ⚡ **Baixa Latência** | Respostas rápidas via FastAPI + Uvicorn |
| 🔧 **Extensível** | Arquitetura modular para adição de novas ferramentas |
| 🔐 **Local & Privado** | Execução completa local sem dependência de APIs externas |
| 🌐 **API FastAPI** | Interface padrão para integração com outros sistemas |

---

## 📋 **Índice**

- [🚀 Começando](#-começando)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
- [⚙️ Configuração](#️-configuração)
- [🔧 Estrutura do Projeto](#-estrutura-do-projeto)
- [📡 Uso da API](#-uso-da-api)
  - [Endpoints Disponíveis](#endpoints-disponíveis)
  - [Exemplos de Uso](#exemplos-de-uso)
- [🛠️ Desenvolvimento](#️-desenvolvimento)
  - [Adicionando Novas Ferramentas](#adicionando-novas-ferramentas)
  - [Testes](#testes)
- [🤝 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)

---

## 🚀 **Começando**

### **Pré-requisitos**

Antes de começar, certifique-se de ter instalado:

- **Python 3.10 ou superior**
- **Ollama** (para execução local de modelos LLM)
- **Git** (para clonar o repositório)

### **Instalação**

#### 1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/ai-chat-api.git
cd ai-chat-api
```


#### 2. **Instale o Ollama**
  - Linux/macOS:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```
  - Windows: Baixe o instalador em [ollama.com](https://ollama.com)


#### 3. **Baixe um modelo LLM**
```bash
# Recomendado para iniciar:
ollama pull llama3.1:8b

# Alternativas populares:
# ollama pull mistral:7b
# ollama pull qwen2.5:7b
```

#### 4. **Configure o ambiente python**
```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```
#### 5. **Configure as variáveis de ambiente**
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o .env com suas configurações
nano .env  # ou use seu editor preferido
```




## 📡 Uso do Endpoint /AgenteMath

### Requisição

```bash
POST /AgenteMath
{
  "message": "Quanto é 20 * (3 + 2)?"
}
```
### Resposta (exemplo)
```bash
{
  "response": "20 * (3 + 2) = 100"
}
```

## 🛠️ Estrutura do Projeto

```bash
📁 app
 ├── agent.py        # Configuração do Agente de IA
 ├── main.py         # API FastAPI
 └── tools.py        # Tools customizadas (ex.: calculadora)
 
.env
requirements.txt
README.md
.gitignore
run_local.bat
```