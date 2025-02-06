# API REST para la Gestión de Alumnos (Grupos A-J)

Este proyecto implementa una API REST utilizando FastAPI para la gestión de alumnos en diferentes grupos (A hasta J). Permite realizar operaciones básicas como la creación, lectura, actualización y eliminación de registros de alumnos.

## Descripción Detallada

La API REST proporciona endpoints para interactuar con la información de los alumnos. Está desarrollada con FastAPI, lo que garantiza un alto rendimiento y una fácil documentación interactiva (Swagger UI). Los datos de los alumnos se almacenan actualmente en listas en memoria dentro de cada enrutador, por lo que no son persistentes entre ejecuciones. En una implementación real, se recomienda utilizar una base de datos.

### Endpoints

A continuación, se describen los endpoints disponibles para cada grupo (A-J):

#### Grupo A

*   **`GET /grupo_a`**: Obtiene una lista con todos los alumnos del grupo A.
*   **`POST /grupo_a`**: Crea un nuevo alumno en el grupo A.
*   **`PUT /grupo_a`**: Actualiza la información de un alumno existente del grupo A.
*   **`DELETE /grupo_a/{id}`**: Elimina un alumno del grupo A por su ID.

#### Grupo B

*   **`GET /grupo_b`**: Obtiene una lista con todos los alumnos del grupo B.
*   **`POST /grupo_b`**: Crea un nuevo alumno en el grupo B.
*   **`PUT /grupo_b`**: Actualiza la información de un alumno existente del grupo B.
*   **`DELETE /grupo_b/{id}`**: Elimina un alumno del grupo B por su ID.

#### ... (Repetir la estructura para los grupos C hasta J)

### Modelo de Datos (`User`)

Los datos de cada alumno se representan mediante un objeto `User` con los siguientes campos:

*   `id` (entero): Identificador único del alumno.
*   `Name` (string): Nombre del alumno.
*   `LastName` (string): Apellido del alumno.
*   `Age` (entero): Edad del alumno.


## Tecnologías Utilizadas

*   FastAPI
*   Uvicorn

