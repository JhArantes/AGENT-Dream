@echo off
REM Ativar venv e rodar uvicorn
call venv\Scripts\activate
uvicorn app.main:app --reload