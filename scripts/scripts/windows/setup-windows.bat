@echo off
echo 🚀 Configuration de l'environnement de développement Windows...

REM Vérification de Docker
where docker >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Docker n'est pas installé ou n'est pas dans le PATH
    exit /b 1
)

REM Création du fichier .env s'il n'existe pas
if not exist .env (
    echo Création du fichier .env...
    copy .env.example .env
)

REM Construction et démarrage des conteneurs
echo 🏗️ Construction des conteneurs Docker...
docker-compose build

echo 🚀 Démarrage des services...
docker-compose up -d

REM Attente que la base de données soit prête
echo ⏳ Attente de la base de données...
timeout /t 10 /nobreak

REM Migrations Django
echo 🔄 Application des migrations...
docker-compose exec backend python manage.py migrate

echo ✅ Configuration terminée !
echo 🌐 Application accessible sur :
echo Frontend : http://localhost:3000
echo Backend API : http://localhost:8000 