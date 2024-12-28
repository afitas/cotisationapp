@echo off
echo 🚀 Création des applications Django...

REM Création des dossiers d'applications
mkdir backend\apps\users
mkdir backend\apps\subscriptions
mkdir backend\apps\payments
mkdir backend\apps\projects
mkdir backend\apps\announcements

REM Initialisation des applications
cd backend
python manage.py startapp users apps/users
python manage.py startapp subscriptions apps/subscriptions
python manage.py startapp payments apps/payments
python manage.py startapp projects apps/projects
python manage.py startapp announcements apps/announcements

echo ✅ Applications créées ! 