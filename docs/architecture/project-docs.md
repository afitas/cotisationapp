# Documentation du Projet - Système de Gestion des Cotisations

## 1. Fichier README.md principal
```markdown
# Système de Gestion des Cotisations Résidentielles

## Description
Système de gestion des cotisations mensuelles pour une cité résidentielle.

## Technologies
- Backend: Django REST Framework
- Frontend: Next.js 14
- Mobile: React Native
- Base de données: PostgreSQL
- Authentication: JWT

## Structure du Projet
[Structure détaillée des dossiers et fichiers]

## Installation
[Instructions détaillées d'installation]

## Configuration
[Variables d'environnement et configurations nécessaires]
```

## 2. Spécifications Techniques (technical-specs.yaml)
```yaml
project:
  name: residence-management
  version: 1.0.0
  architecture: microservices

database:
  models:
    CustomUser:
      fields:
        - name: username
          type: string
          unique: true
        - name: role
          type: string
          choices: [admin, abonne]
        - name: bloc
          type: string
          nullable: true
        - name: nombre_voitures
          type: integer
          default: 0
      
    Plan:
      fields:
        - name: mois
          type: integer
        - name: annee
          type: integer
        - name: montant_conciergerie
          type: decimal
        - name: montant_par_voiture
          type: decimal

    Cotisation:
      fields:
        - name: user_id
          type: foreign_key
          references: CustomUser
        - name: plan_id
          type: foreign_key
          references: Plan
        - name: total_montant
          type: decimal

api_endpoints:
  - path: /api/auth
    methods: [POST]
    description: Authentication endpoint
  - path: /api/users
    methods: [GET, POST, PUT, DELETE]
    description: User management
  - path: /api/cotisations
    methods: [GET, POST]
    description: Cotisation management
```

## 3. API Schema (openapi.yaml)
```yaml
openapi: 3.0.0
info:
  title: API de Gestion des Cotisations
  version: 1.0.0
paths:
  /api/auth/login:
    post:
      summary: Authentification utilisateur
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                password:
                  type: string
      responses:
        200:
          description: Login successful
          content:
            application/json:
              schema:
                type: object
                properties:
                  token:
                    type: string

  /api/cotisations:
    get:
      summary: Liste des cotisations
      parameters:
        - in: query
          name: month
          schema:
            type: integer
        - in: query
          name: year
          schema:
            type: integer
```

## 4. Types TypeScript (types.ts)
```typescript
interface User {
  id: number;
  username: string;
  role: 'admin' | 'abonne';
  bloc?: string;
  nombreVoitures: number;
  fraisConciergerie: number;
}

interface Plan {
  id: number;
  mois: number;
  annee: number;
  montantConciergerie: number;
  montantParVoiture: number;
}

interface Cotisation {
  id: number;
  userId: number;
  planId: number;
  totalMontant: number;
  createdAt: Date;
  payments: Payment[];
}
```

## 5. Configuration CI/CD (.github/workflows/main.yml)
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: |
          npm install
          npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        if: github.ref == 'refs/heads/main'
        run: |
          # deployment steps
```
