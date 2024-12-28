@echo off
echo 🚀 Installation des dépendances frontend...

cd frontend

REM Installation des dépendances
npm install @tanstack/react-query @tanstack/react-query-devtools
npm install axios @types/axios
npm install @types/node @types/react @types/react-dom typescript
npm install @reduxjs/toolkit react-redux @types/react-redux
npm install @shadcn/ui tailwindcss postcss autoprefixer
npm install zod @hookform/resolvers react-hook-form
npm install jwt-decode cookies-next

echo ✅ Installation terminée !
pause 