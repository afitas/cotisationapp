# Application de Gestion des Cotisations

Application web pour la gestion des cotisations résidentielles.

## Technologies utilisées

### Backend
- Python 3.9+
- Django 4.2+
- Django REST Framework
- PostgreSQL

### Frontend
- Next.js 13
- TypeScript
- Tailwind CSS
- Shadcn UI

## Installation

### Backend

```bash
# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Installer les dépendances
cd backend
pip install -r requirements.txt

# Configurer la base de données
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

### Frontend

```bash
# Installer les dépendances
cd frontend
npm install

# Lancer le serveur de développement
npm run dev
```

## Structure du projet

```
cotisation-app/
├── backend/
│   ├── apps/
│   │   ├── users/
│   │   ├── subscriptions/
│   │   ├── payments/
│   │   └── projects/
│   └── core/
└── frontend/
    ├── app/
    ├── components/
    ├── lib/
    └── types/
```

## Fonctionnalités

- Authentification JWT
- Gestion des utilisateurs (admin/abonné)
- Gestion des cotisations
- Gestion des paiements
- Tableau de bord administrateur
- Espace abonné 