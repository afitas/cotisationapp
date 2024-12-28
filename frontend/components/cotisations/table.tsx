'use client'

import React from 'react'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

interface Cotisation {
  id: number;
  user_details: {
    username: string;
  };
  plan_details: {
    mois: number;
    annee: number;
  };
  montant_total: number;
  statut: string;
}

export function CotisationsTable() {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Utilisateur</TableHead>
          <TableHead>Plan</TableHead>
          <TableHead>Montant</TableHead>
          <TableHead>Statut</TableHead>
          <TableHead>Actions</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {/* Les données seront ajoutées plus tard */}
      </TableBody>
    </Table>
  )
} 