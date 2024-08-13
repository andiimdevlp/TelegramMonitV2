@echo off

REM Verifica se o ambiente virtual existe
if not exist "venv\Scripts\activate" (
    echo Criando ambiente virtual...
    python -m venv venv
)

REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Instala as dependências, caso ainda não estejam instaladas
pip install -r requirements.txt

REM Executa o script principal
python main.py

REM Desativa o ambiente virtual ao final da execução
deactivate

pause
