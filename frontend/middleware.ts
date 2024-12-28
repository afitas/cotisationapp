import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token')
  const isLoginPage = request.nextUrl.pathname === '/login'

  // Si pas de token et pas sur la page login, rediriger vers login
  if (!token && !isLoginPage) {
    return NextResponse.redirect(new URL('/login', request.url))
  }

  // Si token et sur la page login, rediriger vers le dashboard approprié
  if (token && isLoginPage) {
    const user = JSON.parse(request.cookies.get('user')?.value || '{}')
    const redirectUrl = user.role === 'admin' ? '/admin' : '/abonne'
    return NextResponse.redirect(new URL(redirectUrl, request.url))
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/login', '/admin/:path*', '/abonne/:path*']
} 