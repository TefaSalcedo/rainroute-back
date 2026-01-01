# 📋 Plan de Configuración del Backend - RainRoute

Este documento detalla los pasos para inicializar y configurar el backend de RainRoute utilizando FastAPI, PostgreSQL y Docker, alineado con los requerimientos del MVP.

## 1. Inicialización del Proyecto ✅

- [x] Crear repositorio en GitHub.
- [x] Inicializar Git local y conectar remoto.
- [x] Crear estructura base de carpetas.

## 2. Estructura del Backend (Clean Architecture)

La arquitectura seguirá un enfoque modular y escalable:

```
rainRouteBack/
├── app/
│   ├── api/            # Endpoints y rutas (v1)
│   ├── core/           # Configuración global y seguridad
│   ├── db/             # Conexión a BD y modelos base
│   ├── models/         # Modelos ORM (SQLAlchemy)
│   ├── schemas/        # Schemas Pydantic (Validación)
│   ├── services/       # Lógica de negocio y servicios externos (Clima, IA)
│   └── main.py         # Punto de entrada
├── docs/               # Documentación del proyecto
├── tests/              # Pruebas automatizadas
├── .env.example        # Variables de entorno de ejemplo
└── requirements.txt    # Dependencias
```

## 3. Próximos Pasos (Roadmap de Commits)

### Commit 1: Scaffolding (Actual)

- Estructura de carpetas.
- Configuración básica de FastAPI (`main.py`).
- Configuración de entorno (`core/config.py`).
- Definición de dependencias.

### Commit 2: Dockerización

- `Dockerfile` optimizado para Python.
- `docker-compose.yml` con servicio de API y PostgreSQL.

### Commit 3: Base de Datos y Modelos

- Configuración de SQLAlchemy (`db/session.py`).
- Modelos iniciales: `User`, `Route` (puntos A/B).
- Configuración de Alembic para migraciones.

### Commit 4: Autenticación

- Schemas de usuario (`UserCreate`, `UserLogin`).
- Endpoints de Auth (Login, Register).
- Middleware de JWT.

### Commit 5: Gestión de Rutas

- Endpoints para crear y listar rutas.
- Integración básica con API de mapas (placeholder).

### Commit 6: Servicio de Clima y Alertas

- Integración con API de clima externa.
- Lógica de detección de lluvia en ruta.
