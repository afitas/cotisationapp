export interface User {
  id: number;
  username: string;
  email: string;
  role: 'admin' | 'abonne';
  nom: string;
  prenom: string;
  telephone: string;
  address: string;
  bloc?: string;
  nombre_voitures: number;
  est_actif: boolean;
}

export interface AnneeAbonnement {
  id: number;
  annee: number;
  est_actif: boolean;
  est_cloture: boolean;
  date_creation: string;
  date_cloture?: string;
  created_by: number;
}

export interface PlanMensuel {
  id: number;
  annee: number;
  mois: number;
  montant_conciergerie: number;
  montant_par_voiture: number;
  date_limite_paiement: string;
  created_by: number;
}

export interface Cotisation {
  id: number;
  user: number;
  plan: number;
  montant_total: number;
  statut: 'en_attente' | 'paye' | 'en_retard' | 'annule';
  date_paiement?: string;
  created_by: number;
} 