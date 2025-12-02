import shutil
import os

VENV_PATH = "venv"  # altere se sua venv tiver outro nome

if os.path.exists(VENV_PATH):
    print(f"Removendo o ambiente virtual '{VENV_PATH}'...")
    shutil.rmtree(VENV_PATH)
    print("Ambiente removido com sucesso!")
else:
    print("Nenhum ambiente virtual encontrado.")

print("Criando nova venv...")
os.system(f"python -m venv {VENV_PATH}")

print("Nova venv criada!")
