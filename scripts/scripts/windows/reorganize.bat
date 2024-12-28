@echo off
echo 🔄 Réorganisation des fichiers...

REM Déplacement des fichiers de documentation
move architecture-technique.md docs\architecture\
move class-diagram.mermaid docs\architecture\
move usecase-diagram.mermaid docs\architecture\
move workflow-diagram.mermaid docs\architecture\
move systeme-utilisateur.mermaid docs\database\

REM Déplacement des scripts Windows
move scripts\setup-windows.bat scripts\windows\setup.bat
move scripts\dev-windows.bat scripts\windows\dev.bat

REM Déplacement des scripts Linux
move scripts\setup-backend.sh scripts\linux\setup.sh
move scripts\deploy.sh scripts\linux\deploy.sh

REM Déplacement des fichiers Docker
move Dockerfile.dev scripts\docker\backend.Dockerfile
move frontend\Dockerfile.dev scripts\docker\frontend.Dockerfile
move docker-compose.yml scripts\docker\

echo ✅ Réorganisation terminée ! 