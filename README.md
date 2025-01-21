## Tecnologías Principales

```
Lenguaje: Python

Framework: FastAPI (alto rendimiento, documentación automática, soporte asincrónico).

ORM: SQLAlchemy (abstracción para consultas SQL, modelado basado en clases).

Infraestructura: Docker (portabilidad, consistencia y despliegue simplificado).

Base de Datos: PostgreSQL (transacciones ACID, seguridad avanzada, extensiones ricas).
```

## Descripción del Proyecto

Este proyecto está diseñado para obtener y almacenar feriados en una base de datos. Los feriados se obtienen a través de la API oficial de feriados de Chile: (https://apis.digital.gob.cl/fl/feriados/2024).

El sistema ejecuta una consulta periódica para recuperar y almacenar los feriados. Después de cada ejecución, el proceso espera 60 segundos antes de realizar una nueva consulta. Este intervalo se ha configurado a 60 segundos para permitir una visualización rápida de los datos durante las pruebas, pero se puede ajustar según sea necesario.

Además, el sistema valida si un feriado ya está registrado en la base de datos. Si el feriado no existe, se agrega; si ya está presente, se muestra un mensaje indicando que el feriado ya fue agregado previamente.

## Requisitos previos

Asegúrate de tener instalados los siguientes programas:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Pasos para ejecutar el proyecto

### 1. Crear archivo .env

Debes crear el archivo `.env` para que funcione el proyecto completo, recuerda revisar el archivo:`.env.template`. Copia el contenido y dejalo en `.env`

### 2. Buildear y levantar el proyecto

#### **2.1. `docker-compose build`**

Sirve para construir las imagenes creadas en el docker-compose

#### **2.2. `docker-compose up -d`**

Una vez que las imágenes estén construidas, el siguiente paso es levantar los contenedores en segundo plano

### Explicación adicional de los comandos 'dev':

#### **2.3. `docker-compose exec store_backend bash`**

##### Para ver el listado de comandos vigentes, escribir dentro de la bash 'dev'

Este apartado sirve en caso de que requieran aplicar comandos para:
agregar o quitar paquetes de requirements.txt. Aplicar migraciones o crear nuevas migraciones.

1. **`dev pipi`**: Instala las dependencias sin necesidad de hacer un `docker-compose build`, ideal cuando solo necesitas instalar nuevas dependencias o actualizar las existentes en `requirements.txt`.

2. **`dev migrate`**: Aplica las migraciones

3. **`dev new_migration`**: Genera una nueva migración

### 3. Probar el Endpoint en FastAPI Docs

Una vez que el proyecto esté en funcionamiento, puedes probar los endpoints directamente desde la documentación interactiva de FastAPI.



### Acceder a la documentación

1. Asegúrate de que el proyecto esté levantado (`docker-compose up -d`).
2. Abre tu navegador y accede a: `http://localhost:8000/docs` Desde alli podras interactuar con el endpoint `Holiday`, ingresar los parámetros requeridos y probar las respuestas directamente en la interfaz.
<img width="1392" alt="Captura de pantalla 2025-01-20 a la(s) 8 53 26 p m" src="https://github.com/user-attachments/assets/c8de4464-27f0-43b2-babc-0909c7c21181" />
<img width="1062" alt="Captura de pantalla 2025-01-20 a la(s) 8 54 06 p m" src="https://github.com/user-attachments/assets/07707e45-7f55-426c-a427-bd1f76c21f23" />
