@echo off
echo 👤 Création d'un super utilisateur...

REM Activation de l'environnement virtuel
call .venv\Scripts\activate

cd backend
py manage.py createsuperuser

pause 