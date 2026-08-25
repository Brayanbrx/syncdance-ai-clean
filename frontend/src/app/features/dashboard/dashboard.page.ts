import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-dashboard-page',
  imports: [RouterLink],
  template: `
    <section class="panel">
      <p class="muted">Plataforma en construcción</p>
      <h1>Base técnica de SyncDance AI</h1>
      <p>
        La navegación web, la API y el procesamiento asíncrono están preparados para los próximos
        incrementos.
      </p>
      <p><a routerLink="/routines">Explorar rutinas</a></p>
    </section>
  `,
})
export class DashboardPage {}
