import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import api from '@/lib/axios'
import type { User } from '@/types/api'

interface AuthState {
  token: string | null;
  user: User | null;
  isAuthenticated: boolean;
  login: (credentials: { username: string; password: string }) => Promise<void>;
  logout: () => void;
}

export const useAuth = create<AuthState>()(
  persist(
    (set) => ({
      token: null,
      user: null,
      isAuthenticated: false,
      login: async (credentials) => {
        const response = await api.post('/auth/token/', credentials)
        const { access, user } = response.data
        
        set({ token: access, user, isAuthenticated: true })
        api.defaults.headers.Authorization = `Bearer ${access}`
      },
      logout: () => {
        set({ token: null, user: null, isAuthenticated: false })
        delete api.defaults.headers.Authorization
      },
    }),
    {
      name: 'auth-storage',
    }
  )
) 