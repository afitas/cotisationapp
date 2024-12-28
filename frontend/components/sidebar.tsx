import React from 'react'
import Link from 'next/link'

export function Sidebar() {
  return (
    <div className="w-64 border-r bg-gray-50/50">
      <nav className="space-y-2 p-4">
        <Link href="/dashboard" className="block p-2 hover:bg-gray-100 rounded">
          Tableau de bord
        </Link>
        <Link href="/cotisations" className="block p-2 hover:bg-gray-100 rounded">
          Cotisations
        </Link>
      </nav>
    </div>
  )
} 