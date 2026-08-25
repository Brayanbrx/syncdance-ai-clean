import { Routes } from '@angular/router';

import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  {
    path: 'login',
    loadComponent: () => import('./features/auth/login.page').then((m) => m.LoginPage),
  },
  {
    path: 'dashboard',
    canActivate: [authGuard],
    loadComponent: () => import('./features/dashboard/dashboard.page').then((m) => m.DashboardPage),
  },
  {
    path: 'routines',
    canActivate: [authGuard],
    loadComponent: () => import('./features/routines/routines.page').then((m) => m.RoutinesPage),
  },
  {
    path: 'performances',
    canActivate: [authGuard],
    loadComponent: () =>
      import('./features/performances/performances.page').then((m) => m.PerformancesPage),
  },
  { path: '', pathMatch: 'full', redirectTo: 'dashboard' },
  { path: '**', redirectTo: 'dashboard' },
];
