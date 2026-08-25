import { Component, inject, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthService } from '../../core/auth/auth.service';

@Component({
  selector: 'app-login-page',
  imports: [ReactiveFormsModule],
  template: `
    <section class="panel stack">
      <div>
        <h1>Acceder</h1>
        <p class="muted">Base de autenticación JWT para el equipo.</p>
      </div>
      <form class="stack" [formGroup]="form" (ngSubmit)="submit()">
        <input formControlName="username" placeholder="Usuario" autocomplete="username" />
        <input
          formControlName="password"
          placeholder="Contraseña"
          type="password"
          autocomplete="current-password"
        />
        <button type="submit" [disabled]="form.invalid || loading()">Ingresar</button>
        @if (error()) {
          <p role="alert">{{ error() }}</p>
        }
      </form>
    </section>
  `,
})
export class LoginPage {
  private readonly auth = inject(AuthService);
  private readonly router = inject(Router);
  private readonly formBuilder = inject(FormBuilder);
  readonly loading = signal(false);
  readonly error = signal('');
  readonly form = this.formBuilder.nonNullable.group({
    username: ['', Validators.required],
    password: ['', Validators.required],
  });

  submit(): void {
    this.loading.set(true);
    this.error.set('');
    this.auth.login(this.form.getRawValue()).subscribe({
      next: () => this.router.navigateByUrl('/dashboard'),
      error: () => {
        this.loading.set(false);
        this.error.set('No se pudo iniciar sesión.');
      },
    });
  }
}
