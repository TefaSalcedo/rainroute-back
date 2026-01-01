# 🌧️ RainRoute Backend API

Backend oficial para la aplicación **RainRoute**, diseñado para proporcionar servicios de autenticación, gestión de rutas y alertas climáticas en tiempo real.

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una arquitectura en capas (Layered Architecture) enfocada en la escalabilidad y mantenibilidad, separando claramente responsabilidades.

```
rainRouteBack/
├── app/
│   ├── api/            # Capa de Presentación (Rutas y Endpoints)
│   │   └── v1/         # Versionado de API
│   ├── core/           # Configuración del Núcleo (Settings, Security)
│   ├── db/             # Capa de Persistencia (Conexión BD, Session)
│   ├── models/         # Definición de Tablas (SQLAlchemy)
│   ├── schemas/        # Objetos de Transferencia de Datos (Pydantic)
│   ├── services/       # Lógica de Negocio y Servicios Externos (Clima, IA)
│   └── main.py         # Punto de Entrada de la Aplicación
├── docs/               # Documentación Técnica y Planes
├── tests/              # Pruebas Unitarias e Integración
└── requirements.txt    # Dependencias del Proyecto
```

## 🚀 Roadmap y Trazabilidad

Este repositorio se desarrollará siguiendo un plan incremental basado en los requerimientos funcionales definidos.

| Commit / Fase | Descripción                                                    | Estado        |
| ------------- | -------------------------------------------------------------- | ------------- |
| **Init**      | Estructura base, configuración de FastAPI y Git                | ✅ Completado |
| **Docker**    | Contenerización de la API y Base de Datos PostgreSQL           | ⏳ Pendiente  |
| **Database**  | Modelado de datos (Usuarios, Rutas) y migraciones Alembic      | ⏳ Pendiente  |
| **Auth**      | Implementación de Registro, Login y JWT (RF-01, RF-02)         | ⏳ Pendiente  |
| **Routes**    | CRUD de Rutas y Puntos A/B (RF-06, RF-08)                      | ⏳ Pendiente  |
| **Weather**   | Integración con API de Clima y Motor de Alertas (RF-09, RF-10) | ⏳ Pendiente  |

## 🛠️ Tecnologías

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Deployment**: Docker

## 📦 Instalación Local

1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar servidor: `uvicorn app.main:app --reload`
