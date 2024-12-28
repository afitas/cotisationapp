#!/bin/bash

echo "🚀 Configuration de l'environnement frontend..."

# Vérification de Node.js
command -v node >/dev/null 2>&1 || { echo "❌ Node.js est requis mais n'est pas installé."; exit 1; }

# Installation des dépendances Node.js
echo "📦 Installation des dépendances..."
cd frontend
npm install

# Configuration des variables d'environnement
echo "⚙️ Configuration des variables d'environnement..."
if [ ! -f .env.local ]; then
    cp .env.example .env.local
    
    # Génération d'une clé API aléatoire si nécessaire
    echo "NEXT_PUBLIC_API_KEY=$(openssl rand -hex 32)" >> .env.local
fi

# Installation et configuration de Tailwind CSS
echo "🎨 Configuration de Tailwind CSS..."
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Installation des dépendances UI
echo "🎯 Installation des composants UI..."
npm install @shadcn/ui @tanstack/react-query @tanstack/react-query-devtools

# Construction initiale
echo "🏗️ Construction initiale..."
npm run build

echo "✅ Configuration frontend terminée!" 