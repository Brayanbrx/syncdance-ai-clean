import { AsyncPipe } from '@angular/common';
import { Component, inject } from '@angular/core';

import { RoutineService } from '../../core/services/routine.service';

@Component({
  selector: 'app-routines-page',
  imports: [AsyncPipe],
  template: `
    <section class="panel">
      <h1>Rutinas</h1>
      <p class="muted">Listado conectado a la API.</p>
      @if (routines$ | async; as page) {
        <ul>
          @for (routine of page.results; track routine.id) {
            <li>{{ routine.name }} · {{ routine.difficulty }}</li>
          } @empty {
            <li>Aún no existen rutinas.</li>
          }
        </ul>
      }
    </section>
  `,
})
export class RoutinesPage {
  private readonly routines = inject(RoutineService);
  readonly routines$ = this.routines.list();
}
