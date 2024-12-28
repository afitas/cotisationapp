export interface ApiResponse<T> {
  count?: number;
  next?: string | null;
  previous?: string | null;
  results: T[];
}

export interface User {
  id: number;
  username: string;
  email: string;
  role: 'admin' | 'abonne';
  first_name?: string;
  last_name?: string;
  bloc?: string;
}

export interface AuthResponse {
  access: string;
  refresh: string;
  user: User;
} 