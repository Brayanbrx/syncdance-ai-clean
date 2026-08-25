import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';

import { environment } from '../../../environments/environment';
import { PaginatedResponse, Performance } from '../../shared/models/api.models';

@Injectable({ providedIn: 'root' })
export class PerformanceService {
  private readonly http = inject(HttpClient);

  list() {
    return this.http.get<PaginatedResponse<Performance>>(`${environment.apiBaseUrl}/performances/`);
  }
}
