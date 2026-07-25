

API RESTful desarrollada con FastAPI, PostgreSQL y SQLAlchemy para 
la gestión de la plataforma de movilidad urbana EcoRide. El proyecto 
está completamente contenerizado con Docker y gestiona el historial 
de base de datos a través de migraciones con Alembic.


1. TECNOLOGÍAS UTILIZADAS
--------------------------------------------------------------------
- Framework: FastAPI (Python 3.10)
- Base de Datos: PostgreSQL
- ORM: SQLAlchemy
- Migraciones: Alembic
- Validación de datos: Pydantic v2
- Contenerización: Docker & Docker Compose


2. REQUISITOS DEL SISTEMA
--------------------------------------------------------------------
- Docker Desktop instalado y corriendo.
- Git instalado.


3. INSTALACIÓN Y EJECUCIÓN (PASO A PASO)
--------------------------------------------------------------------

Paso 3.1: Clonar el repositorio
   git clone https://github.com/csiv-code/ecoride_api.git
   cd ecoride_api

Paso 3.2: Configurar variables de entorno (esta el .env.example)

Paso 3.3: Construir y levantar los contenedores Docker
   Ejecuta el siguiente comando para iniciar el servicio de la API 
   y la base de datos PostgreSQL:

   docker compose up --build

Paso 3.4: Aplicar migraciones de la Base de Datos
   En una segunda ventana de terminal, aplica las migraciones de 
   Alembic para estructurar las tablas ('bikes' y 'users'):

   docker compose exec api alembic upgrade head


4. DOCUMENTACIÓN INTERACTIVA DE LA API
--------------------------------------------------------------------
Una vez que el contenedor de la API esté en ejecución, puedes acceder 
a la interfaz interactiva de Swagger UI desde tu navegador en:

http://localhost:8000/docs

Endpoints disponibles:
- /api/bikes  : CRUD completo para la gestión de bicicletas.
- /api/users  : CRUD completo para la gestión de usuarios.
====================================================================
