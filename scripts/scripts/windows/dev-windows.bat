@echo off
echo 🚀 Démarrage de l'environnement de développement...

REM Démarrage des conteneurs
docker-compose up -d

echo ✨ Services démarrés !
echo Pour voir les logs : docker-compose logs -f
echo Pour arrêter : docker-compose down 