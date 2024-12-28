# Guide de Déploiement

## Table des Matières
1. [Prérequis](#prérequis)
2. [Environnement de Production](#environnement-de-production)
3. [Déploiement avec Docker](#déploiement-avec-docker)
4. [Déploiement Manuel](#déploiement-manuel)
5. [Configuration](#configuration)
6. [Sécurité](#sécurité)

## Prérequis
- Docker et Docker Compose
- Serveur Linux (Ubuntu 20.04 LTS recommandé)
- Domain name configuré
- Certificat SSL

## Environnement de Production

### Variables d'Environnement
```env
# Backend
DJANGO_SETTINGS_MODULE=core.settings.production
DJANGO_SECRET_KEY=votre-clé-secrète
ALLOWED_HOSTS=votredomaine.com
DATABASE_URL=postgresql://user:password@db:5432/cotisation_db

# Frontend
NEXT_PUBLIC_API_URL=https://api.votredomaine.com
```

### Configuration SSL
```nginx
server {
    listen 443 ssl;
    server_name votredomaine.com;
    
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    
    # ... autres configurations SSL
}
```

## Déploiement avec Docker

1. **Préparation**
```bash
# Cloner le repository
git clone https://github.com/votre-repo/cotisation-app.git
cd cotisation-app

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos valeurs
```

2. **Construction et Démarrage**
```bash
# Construire les images
docker-compose -f docker-compose.prod.yml build

# Démarrer les services
docker-compose -f docker-compose.prod.yml up -d
```

3. **Migrations et Données Initiales**
```bash
# Appliquer les migrations
docker-compose exec backend python manage.py migrate

# Créer un super utilisateur
docker-compose exec backend python manage.py createsuperuser
```

## Sécurité

### Liste de Contrôle
- [ ] Variables d'environnement sécurisées
- [ ] Certificats SSL à jour
- [ ] Pare-feu configuré
- [ ] Sauvegardes automatisées
- [ ] Monitoring mis en place

### Sauvegardes
```bash
# Backup de la base de données
docker-compose exec db pg_dump -U postgres cotisation_db > backup.sql

# Restauration
docker-compose exec db psql -U postgres cotisation_db < backup.sql
```

## Monitoring

### Services à Surveiller
- Backend Django
- Frontend Next.js
- Base de données PostgreSQL
- Nginx
- Certificats SSL

### Commandes Utiles
```bash
# Vérifier les logs
docker-compose logs -f

# Vérifier l'état des services
docker-compose ps

# Redémarrer un service
docker-compose restart [service]
``` 