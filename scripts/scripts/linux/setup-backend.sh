#!/bin/bash

echo "🚀 Configuration de l'environnement backend..."

# Vérification des prérequis
command -v python3 >/dev/null 2>&1 || { echo "❌ Python 3 est requis mais n'est pas installé."; exit 1; }
command -v psql >/dev/null 2>&1 || { echo "❌ PostgreSQL est requis mais n'est pas installé."; exit 1; }

# Configuration des variables
DB_NAME="cotisation_db"
DB_USER="cotisation_user"
DB_PASSWORD="secure_password"

# Création de l'environnement virtuel Python
echo "📦 Création de l'environnement virtuel..."
python3 -m venv venv
source venv/bin/activate

# Installation des dépendances
echo "📥 Installation des dépendances Python..."
pip install --upgrade pip
pip install -r requirements.txt

# Configuration de la base de données PostgreSQL
echo "🗄️ Configuration de la base de données..."
if psql -lqt | cut -d \| -f 1 | grep -qw $DB_NAME; then
    echo "La base de données existe déjà"
else
    psql -U postgres -c "CREATE DATABASE $DB_NAME;"
    psql -U postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
    psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
fi

# Configuration du fichier .env
echo "⚙️ Configuration des variables d'environnement..."
if [ ! -f .env ]; then
    cp .env.example .env
    sed -i "s/your-secret-key/$(openssl rand -hex 32)/" .env
    sed -i "s/your-jwt-secret/$(openssl rand -hex 32)/" .env
fi

# Migrations Django
echo "🔄 Application des migrations..."
python manage.py makemigrations
python manage.py migrate

# Création du superuser
echo "👤 Création du super utilisateur..."
python manage.py createsuperuser

echo "✅ Configuration backend terminée!" 