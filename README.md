## Requisitos previos

Asegúrate de tener instalados los siguientes programas:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Pasos para ejecutar el proyecto

### 1. Buildear y levantar el proyecto

#### **1.1. `docker-compose build`**

Sirve para construir las imagenes creadas en el docker-compose

#### **1.2. `docker-compose up -d`**

Una vez que las imágenes estén construidas, el siguiente paso es levantar los contenedores en segundo plano

### Explicación adicional de los comandos 'dev':

#### **1.3. `docker-compose exec store_backend bash`**

##### Para ver el listado de comandos vigentes, escribir dentro de la bash 'dev'

Este apartado sirve en caso de que requieran aplicar comandos para:
agregar o quitar paquetes de requirements.txt. Aplicar migraciones o crear nuevas migraciones.

1. **`dev pipi`**: Instala las dependencias sin necesidad de hacer un `docker-compose build`, ideal cuando solo necesitas instalar nuevas dependencias o actualizar las existentes en `requirements.txt`.

2. **`dev migrate`**: Aplica las migraciones

3. **`dev new_migration`**: Genera una nueva migración
