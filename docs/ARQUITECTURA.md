# Arquitectura

SyncDance AI parte como monolito modular Django orientado a funcionalidades. La separación es pragmática: cada app es propietaria de sus modelos y casos de uso, mientras `common/` contiene únicamente primitivas compartidas.

```text
Angular ─────┐
             ├── Django REST ── PostgreSQL
Flutter ─────┘        │
                      ▼
                    Redis
                      │
                      ▼
                    Celery
                      │
                      ▼
                   AI Engine
```

## Convenciones del backend

- `views.py`: transporte HTTP y serialización.
- `services.py`: comandos que modifican estado.
- `selectors.py`: consultas reutilizables.
- `tasks.py`: trabajo asíncrono.
- `ai_engine/`: algoritmos independientes del framework.

La base no incluye buses de comandos, repositorios genéricos, microservicios ni algoritmos reales de IA. Si el motor necesita GPU o escalado independiente, `ai_engine/` podrá extraerse detrás de una cola o API en una fase posterior.
