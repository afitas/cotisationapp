@echo off
echo 🚀 Configuration de l'environnement Python...

REM Vérification de Python
py --version 2>NUL
if errorlevel 1 (
    echo ❌ Python n'est pas installé ou n'est pas dans le PATH
    pause
    exit /b 1
)

REM Se positionner à la racine du projet
cd ..

REM Vérification si .venv existe déjà
if exist .venv (
    echo 🗑️ Suppression de l'ancien environnement virtuel...
    rmdir /s /q .venv
)

echo 📦 Création de l'environnement virtuel...
py -m venv .venv

REM Vérification si la création a réussi
if not exist .venv\Scripts\activate.bat (
    echo ❌ Échec de la création de l'environnement virtuel
    pause
    exit /b 1
)

echo 🔄 Activation de l'environnement virtuel...
call .venv\Scripts\activate.bat

REM Vérification de l'activation
py -c "import sys; print(sys.prefix)" | findstr /i ".venv" >nul
if errorlevel 1 (
    echo ❌ Échec de l'activation de l'environnement virtuel
    pause
    exit /b 1
)

echo 📥 Mise à jour de pip...
py -m pip install --upgrade pip

echo 📥 Installation des dépendances...

REM Vérification si requirements.txt existe
if not exist backend\requirements.txt (
    echo ⚠️ requirements.txt non trouvé, création des dépendances de base...
    (
        echo Django==5.0.0
        echo djangorestframework==3.14.0
        echo djangorestframework-simplejwt==5.3.1
        echo django-cors-headers==4.3.1
        echo psycopg2-binary==2.9.9
        echo python-dotenv==1.0.0
        echo django-filter==23.5
        echo drf-yasg==1.21.7
    ) > backend\requirements.txt
)

pip install -r backend\requirements.txt

REM Création du projet Django
echo 🔄 Configuration du projet Django...

REM Sauvegarde des fichiers existants si nécessaire
if exist backend\apps (
    echo 📦 Sauvegarde des applications existantes...
    if not exist backup mkdir backup
    xcopy /E /I /Y backend\apps backup\apps
)

REM Suppression du dossier backend existant
if exist backend (
    echo 🗑️ Nettoyage du dossier backend...
    rmdir /s /q backend
)

REM Création du nouveau projet Django
echo 🔄 Création du nouveau projet Django...
py -m django-admin startproject core backend

REM Restauration des applications
if exist backup\apps (
    echo 📦 Restauration des applications...
    xcopy /E /I /Y backup\apps backend\apps
) else (
    echo 📦 Création des applications Django...
    cd backend
    mkdir apps
    cd apps
    py ..\manage.py startapp users
    py ..\manage.py startapp subscriptions
    py ..\manage.py startapp payments
    py ..\manage.py startapp projects
    py ..\manage.py startapp announcements
    cd ..
)

echo 🔄 Application des migrations...
cd backend
py manage.py makemigrations
py manage.py migrate

echo ✅ Configuration terminée !
echo.
echo 📝 Pour activer l'environnement virtuel :
echo     .venv\Scripts\activate
echo.
echo 🚀 Pour démarrer le serveur :
echo     cd backend
echo     set ENV_PATH=.env.development
echo     py manage.py runserver

pause 