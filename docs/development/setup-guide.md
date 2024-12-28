# Guide de Développement

## Table des Matières
1. [Configuration de l'Environnement](#configuration-de-lenvironnement)
2. [Structure du Projet](#structure-du-projet)
3. [Conventions de Code](#conventions-de-code)
4. [Workflow de Développement](#workflow-de-développement)
5. [Tests](#tests)
6. [Débogage](#débogage)

## Configuration de l'Environnement

### Windows avec Docker
```batch
# Installation
scripts\windows\setup.bat

# Développement
scripts\windows\dev.bat
```

### Linux avec Docker
```bash
# Installation
./scripts/linux/setup.sh

# Développement
./scripts/linux/dev.sh
```

## Structure du Projet
```
project-root/
├── backend/
│   ├── apps/
│   │   ├── users/         # Gestion des utilisateurs
│   │   ├── subscriptions/ # Gestion des cotisations
│   │   ├── payments/      # Gestion des paiements
│   │   └── projects/      # Gestion des projets
│   └── core/             # Configuration Django
├── frontend/
│   ├── app/              # Pages Next.js
│   ├── components/       # Composants React
│   └── services/         # Services API
└── mobile/              # Application React Native
```

## Conventions de Code

### Backend (Python)
```python
# Exemple de modèle
class Subscription(models.Model):
    """
    Modèle pour gérer les cotisations des résidents.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Frontend (TypeScript)
```typescript
// Interface type
interface Subscription {
  id: number;
  userId: number;
  amount: number;
  createdAt: Date;
}

// Composant React
const SubscriptionList: React.FC = () => {
  // ...
};
```

## Workflow de Développement

1. **Création de Branche**
```bash
git checkout -b feature/nom-de-la-feature
```

2. **Tests Locaux**
```bash
# Backend
python manage.py test

# Frontend
npm run test
```

3. **Vérification du Code**
```bash
# Backend
flake8 .
black .

# Frontend
npm run lint
```

## Tests

### Backend
```bash
# Tests unitaires
python manage.py test

# Tests avec couverture
coverage run manage.py test
coverage report
```

### Frontend
```bash
# Tests unitaires
npm run test

# Tests e2e
npm run cypress
```

## Débogage

### Backend Django
```python
# Dans le code
import pdb; pdb.set_trace()

# Dans les tests
from django.test import debug; debug()
```

### Frontend React
```typescript
// Dans le code
console.log('Debug:', data);

// Dans Chrome DevTools
debugger;
```

### Docker
```bash
# Logs en temps réel
docker-compose logs -f [service]

# Shell dans un conteneur
docker-compose exec backend bash
docker-compose exec frontend sh
``` 