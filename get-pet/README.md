# Get Pet Microservice

## Descripción
Microservicio encargado de consultar la información de mascotas registradas en el sistema.

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3.10
- **Framework:** FastAPI

---

## Estilo de arquitectura

- **API RESTful:** Todas las operaciones se exponen como endpoints HTTP siguiendo el estilo REST.

---

## Patrones de diseño aplicados

- **KISS (Keep It Simple, Stupid):** El código es sencillo y directo, evitando complejidad innecesaria.
- **DRY (Don't Repeat Yourself):** Se reutilizan funciones y lógica para evitar duplicidad.
- **SOLID:** Se aplican principios como la separación de responsabilidades y la inyección de dependencias.

---

## Base de datos

- **PostgreSQL:** Conexión mediante `psycopg2` y uso de cursores tipo diccionario para facilitar el manejo de datos.

---

## Arquitectura interna

- **N-capas:** Separación clara entre rutas (routers), controladores (controllers), esquemas (schemas), utilidades (utils) y acceso a datos (database).
- **Modelo similar a MVC:** Aunque no hay modelos ORM explícitos, la estructura sigue la separación de responsabilidades típica de MVC.

---

## Seguridad y Middleware

- **CORS:** Configurado para aceptar peticiones desde cualquier origen (`allow_origins=["*"]`), útil para desarrollo y pruebas con frontends como React.
- **JWT:** Actualmente este microservicio no implementa autenticación JWT, pero puede integrarse fácilmente en el futuro.

---

## Estructura del proyecto

```
get-pet/
│
├── src/
│   ├── main.py
│   ├── routers/
│   ├── controllers/
│   ├── schemas/
│   ├── utils/
│   └── database/
│
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## Variables de entorno

El microservicio utiliza variables de entorno para la configuración de la base de datos y servicios externos. Estas se definen en el archivo `.env`.

---

## Ejecución local

1. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
2. Ejecuta el microservicio:
   ```sh
   uvicorn src.main:app --reload --port 3013
   ```

---

## Docker local

1. Construye la imagen:
   ```sh
   docker build -t get-pet .
   ```
2. Ejecuta el contenedor:
   ```sh
   docker run -p 3013:3013 --env-file .env get-pet
   ```

---

## Endpoints principales

### Consultar una mascota por ID

- **GET** `/api/pets/{pet_id}`

GET http://3.214.168.136:8000/api/pets/25

#### Ejemplo de respuesta exitosa

```json
{
    "id": 25,
    "name": "Firulais",
    "species": "Dog",
    "breed": "Labrador",
    "age": 3,
    "admission_date": "2025-06-12",
    "notes": "Friendly with other pets",
    "client_id": 1
}
```

### Consultar todas las mascotas

- **GET** `/api/pets/`

GET http://3.214.168.136:8000/api/pets

#### Ejemplo de respuesta exitosa

```json
[
  {
    "id": 25,
    "name": "Firulais",
    "species": "Dog",
    "breed": "Labrador",
    "age": 3,
    "admission_date": "2025-06-12",
    "notes": "Friendly with other pets",
    "client_id": 1
  },

```
#### Swagger
http://34.229.27.85:3012/docs

---

## Notas

- Permite consultar mascotas por ID o listar todas las mascotas registradas.
- El código es fácilmente extensible para agregar autenticación, filtros adicionales o nuevas funcionalidades.
- El CORS está abierto para facilitar el desarrollo, pero se recomienda