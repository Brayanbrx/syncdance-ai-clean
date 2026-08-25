# SyncDance AI

> Plataforma inteligente para evaluación de performances de baile y canto mediante análisis de movimiento, voz, ritmo y sincronización.

**Estado:** 🚧 En desarrollo — base técnica inicial.

## Arquitectura

El proyecto es un monorepo con un monolito modular Django REST, Angular para web y Flutter para móvil. Celery y Redis aíslan las tareas pesadas. El futuro motor de IA se mantiene desacoplado en `backend/ai_engine/`.

```text
Angular ─────┐
             ├── Django REST ── PostgreSQL
Flutter ─────┘        │
                      ▼
                    Redis
                      │
                      ▼
                    Celery ── AI Engine
```

| Capa              | Tecnología                     |
| ----------------- | ------------------------------ |
| Backend           | Django + Django REST Framework |
| Web               | Angular                        |
| Mobile            | Flutter                        |
| Base de datos     | PostgreSQL                     |
| Cola              | Redis + Celery                 |
| Documentación API | OpenAPI + Swagger              |
| Infraestructura   | Docker Compose                 |

Las decisiones y límites de módulos están detallados en [docs/ARQUITECTURA.md](docs/ARQUITECTURA.md).

## Inicio rápido

Requisitos: Git, Docker y Docker Compose.

```bash
git clone <repository-url>
cd syncdance-ai
cp .env.example .env
docker compose up --build
```

En PowerShell, copie el entorno con `Copy-Item .env.example .env`.

La migración se ejecuta al iniciar el contenedor backend. Para crear un administrador:

```bash
docker compose exec backend python manage.py createsuperuser
```

Servicios disponibles:

- Web: http://localhost:4200
- API: http://localhost:8000
- Swagger: http://localhost:8000/api/docs/
- Admin: http://localhost:8000/admin/
- Health check: http://localhost:8000/api/health/

## Estructura

```text
backend/   API, módulos de negocio, Celery y límite del AI Engine
frontend/  aplicación Angular
mobile/    aplicación Flutter
docs/      decisiones de arquitectura
```

## Desarrollo local

Sin Docker se requieren Python 3.12, Node.js 22, Angular CLI, Flutter, PostgreSQL y Redis.

Backend:

```bash
cd backend
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt
.venv/Scripts/python manage.py migrate
.venv/Scripts/pytest
```

Frontend:

```bash
cd frontend
npm ci
npm start
```

Flutter:

```bash
cd mobile
cp .env.example .env
flutter pub get
flutter run
```

Para Android Emulator, `API_BASE_URL` usa `10.0.2.2`. En iOS Simulator puede usar `localhost`; un dispositivo físico debe usar la IP local del equipo que ejecuta Django.

## Flujo base de análisis

```text
Usuario sube performance → Django → QUEUED → Redis → Celery
                                               │
                                               ▼
                              resultado simulado → COMPLETED
```

El análisis actual usa valores fijos para validar la integración. No hay MediaPipe, OpenCV, FFmpeg, procesamiento de audio ni modelos de IA.

## Convenciones

En Django, `views.py` maneja HTTP, `services.py` modifica estado, `selectors.py` consulta, `tasks.py` ejecuta trabajo Celery y `ai_engine/` alojará algoritmos. Se prioriza código explícito y no se añaden capas sin una necesidad comprobada.

## Git workflow

- `main` debe mantenerse estable.
- El trabajo se realiza en `feature/*` o `fix/*` mediante pull request.
- No se hacen commits directos a `main`.
- Se usan Conventional Commits, por ejemplo `chore: initialize SyncDance AI project`.

Ramas sugeridas: `feature/authentication`, `feature/routines`, `feature/performance-upload` y `feature/analysis-engine`.

## Roadmap

- [x] Base Django, PostgreSQL, Redis y Celery
- [x] Base Angular y Flutter
- [x] Docker Compose y documentación
- [ ] Autenticación y permisos completos
- [ ] Experiencia de rutinas y carga de performances
- [ ] Pose estimation con MediaPipe
- [ ] Análisis de voz, alineamiento temporal y scoring real
