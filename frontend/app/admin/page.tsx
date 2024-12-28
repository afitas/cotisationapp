'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'

export default function AdminPage() {
  const router = useRouter()

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem('user') || '{}')
    if (!user.role || user.role !== 'admin') {
      router.push('/')
    }
  }, [router])

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Dashboard Admin</h1>
      <div className="grid gap-4 grid-cols-1 md:grid-cols-3">
        <div className="p-4 bg-white rounded-lg shadow">
          <h2 className="font-bold mb-2">Cotisations</h2>
          <p>Gérer les cotisations</p>
        </div>
        <div className="p-4 bg-white rounded-lg shadow">
          <h2 className="font-bold mb-2">Utilisateurs</h2>
          <p>Gérer les utilisateurs</p>
        </div>
        <div className="p-4 bg-white rounded-lg shadow">
          <h2 className="font-bold mb-2">Projets</h2>
          <p>Gérer les projets</p>
        </div>
      </div>
    </div>
  )
} 