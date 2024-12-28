@echo off
echo 🚀 Installation des dépendances frontend...

cd frontend

REM Installation des dépendances de base
npm install @tanstack/react-query @tanstack/react-query-devtools
npm install axios
npm install @types/node @types/react @types/react-dom typescript
npm install @reduxjs/toolkit react-redux @types/react-redux
npm install @shadcn/ui tailwindcss postcss autoprefixer
npm install zod @hookform/resolvers react-hook-form
npm install jwt-decode cookies-next

REM Types pour les dépendances
npm install -D @types/axios

REM Configuration de TypeScript
npx tsc --init

echo ✅ Installation terminée ! 