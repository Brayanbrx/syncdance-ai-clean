import { AsyncPipe } from '@angular/common';
import { Component, inject } from '@angular/core';

import { PerformanceService } from '../../core/services/performance.service';

@Component({
  selector: 'app-performances-page',
  imports: [AsyncPipe],
  template: `
    <section class="panel">
      <h1>Performances</h1>
      <p class="muted">Historial conectado a la API.</p>
      @if (performances$ | async; as page) {
        <ul>
          @for (performance of page.results; track performance.id) {
            <li>#{{ performance.id }} · {{ performance.status }}</li>
          } @empty {
            <li>Aún no existen performances.</li>
          }
        </ul>
      }
    </section>
  `,
})
export class PerformancesPage {
  private readonly performances = inject(PerformanceService);
  readonly performances$ = this.performances.list();
}
