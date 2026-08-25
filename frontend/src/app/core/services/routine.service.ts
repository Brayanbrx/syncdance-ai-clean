import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';

import { environment } from '../../../environments/environment';
import { PaginatedResponse, Routine } from '../../shared/models/api.models';

@Injectable({ providedIn: 'root' })
export class RoutineService {
  private readonly http = inject(HttpClient);

  list() {
    return this.http.get<PaginatedResponse<Routine>>(`${environment.apiBaseUrl}/routines/`);
  }
}
