export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export interface Routine {
  id: number;
  name: string;
  description: string;
  instructor: string;
  difficulty: 'BEGINNER' | 'INTERMEDIATE' | 'ADVANCED';
  is_active: boolean;
}

export interface Performance {
  id: number;
  student: string;
  routine: number;
  status: 'UPLOADED' | 'QUEUED' | 'PROCESSING' | 'COMPLETED' | 'FAILED';
  created_at: string;
}
