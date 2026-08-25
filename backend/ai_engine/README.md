# AI Engine

Este modulo sera el nucleo de la inteligencia artificial y analisis tecnico

Este paquete reserva el límite del futuro motor de análisis para mantenerse independiente de Django.

- `pose/`: MediaPipe, normalización de landmarks, ángulos y comparación de poses. Estimacion de Postura.
- `voice/`: extracción de pitch, afinación y ritmo vocal.
- `alignment/`: sincronización temporal y Dynamic Time Warping. Alinear alumno e instructor
- `scoring/`: Dance, Voice, Rhythm, Sync y Overall Score.

La tarea Celery usa resultados fijos únicamente para validar el flujo de infraestructura.
