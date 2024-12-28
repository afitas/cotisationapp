@echo off
echo 🚀 Démarrage de l'environnement de développement...

REM Activation de l'environnement virtuel
call .venv\Scripts\activate

REM Configuration de l'environnement
set ENV_PATH=.env.development

REM Démarrage du serveur Django
cd backend
py manage.py runserver

pause 