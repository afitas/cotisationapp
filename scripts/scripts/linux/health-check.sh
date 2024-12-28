#!/bin/bash

echo "🏥 Vérification de l'état du système..."

# Vérification de la base de données
echo "📊 Test de connexion à la base de données..."
python manage.py dbshell <<EOF
SELECT 1;
EOF

if [ $? -eq 0 ]; then
    echo "✅ Connexion à la base de données OK"
else
    echo "❌ Problème de connexion à la base de données"
fi

# Vérification des migrations
echo "🔍 Vérification des migrations..."
python manage.py showmigrations --list

# Vérification des services externes
echo "🌐 Vérification des services externes..."
curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/health/

# Vérification de l'espace disque
echo "💾 Vérification de l'espace disque..."
df -h | grep /dev/sda1

echo "🔄 Vérification terminée!" 