@echo off
echo 🔄 Application des migrations...

REM Activation de l'environnement virtuel
call .venv\Scripts\activate

cd backend
py manage.py makemigrations
py manage.py migrate

pause 