# Delete Pet Microservice

## Descripción
Microservicio encargado de eliminar mascotas registradas en el sistema.

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
delete-pet/
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
   uvicorn src.main:app --reload --port 3014
   ```

---

## Docker local

1. Construye la imagen:
   ```sh
   docker build -t delete-pet .
   ```
2. Ejecuta el contenedor:
   ```sh
   docker run -p 3014:3014 --env-file .env delete-pet
   ```

---

## Endpoints principales

### Eliminar una mascota por ID

- **DELETE** `/api/pets/{pet_id}`

DELETE http://3.214.168.136:8000/api/pets/25

#### Ejemplo de respuesta exitosa

```json
{
    "message": "Pet deleted successfully ✅",
    "pet_id": 25
}
```
#### Swagger
http://34.229.27.85:3014/docs
---

## Notas

- Antes de eliminar una mascota, se valida la existencia de la mascota en la base de datos.
- El código es fácilmente extensible para agregar autenticación, validaciones adicionales o nuevas funcionalidades.
- El CORS está abierto para facilitar el desarrollo, pero se recomienda