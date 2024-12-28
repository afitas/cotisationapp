'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'

export default function AbonnePage() {
  const router = useRouter()

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem('user') || '{}')
    if (!user.role || user.role !== 'abonne') {
      router.push('/')
    }
  }, [router])

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Espace Abonné</h1>
      <div className="grid gap-4 grid-cols-1 md:grid-cols-2">
        <div className="p-4 bg-white rounded-lg shadow">
          <h2 className="font-bold mb-2">Mes Cotisations</h2>
          <p>Voir mes cotisations</p>
        </div>
        <div className="p-4 bg-white rounded-lg shadow">
          <h2 className="font-bold mb-2">Mon Profil</h2>
          <p>Gérer mon profil</p>
        </div>
      </div>
    </div>
  )
} 