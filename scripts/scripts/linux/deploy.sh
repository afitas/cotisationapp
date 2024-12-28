#!/bin/bash

# Variables d'environnement
export $(cat .env | xargs)

# Build et déploiement
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d

# Migrations
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate

# Collecte des fichiers statiques
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --no-input

# Vérification des services
docker-compose -f docker-compose.prod.yml ps 