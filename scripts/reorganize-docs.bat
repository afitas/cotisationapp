@echo off
echo 🔄 Réorganisation de la documentation...

REM Création de la nouvelle structure
mkdir docs\Old
mkdir docs\New

REM Déplacement des anciens fichiers vers Old
move docs\architecture\* docs\Old\architecture\
move docs\database\* docs\Old\database\
move docs\deployment\* docs\Old\deployment\
move docs\development\* docs\Old\development\

REM Création des nouveaux dossiers pour la nouvelle documentation
mkdir docs\New\architecture
mkdir docs\New\database
mkdir docs\New\api
mkdir docs\New\frontend
mkdir docs\New\mobile
mkdir docs\New\deployment

echo ✅ Réorganisation terminée ! 