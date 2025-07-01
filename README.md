# Pets Domain

## Descripción
Este dominio agrupa los microservicios relacionados con la gestión de mascotas, incluyendo la creación, consulta, actualización y eliminación de registros de mascotas.

---

## Microservicios incluidos

- **create-pet:** Registro de nuevas mascotas.
- **get-pet:** Consulta de mascotas (por ID o todas).
- **update-pet:** Actualización de información de mascotas.
- **delete-pet:** Eliminación de mascotas.

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3.10
- **Framework:** FastAPI
- **Base de datos:** PostgreSQL
- **Contenedores:** Docker y Docker Compose

---

## Estilo de arquitectura

- **API RESTful:** Todos los microservicios exponen endpoints HTTP siguiendo el estilo REST.

---

## Patrones de diseño aplicados

- **KISS:** Código sencillo y directo.
- **DRY:** Reutilización de funciones y lógica.
- **SOLID:** Separación de responsabilidades y facilidad de extensión.

---

## Arquitectura interna

- **N-capas:** Separación entre rutas, controladores, esquemas, utilidades y acceso a datos.
- **Modelo similar a MVC:** Separación de responsabilidades típica de MVC.

---

## Seguridad y Middleware

- **CORS:** Configurado para aceptar peticiones desde cualquier origen (`allow_origins=["*"]`), útil para desarrollo.
- **JWT:** No implementado por defecto, pero fácilmente integrable.

---

## Estructura del dominio

```
pets/
│
├── create-pet/
├── get-pet/
├── update-pet/
├── delete-pet/
├── docker-compose.yml
└── README.md
```

---

## Variables de entorno

Cada microservicio utiliza variables de entorno para la configuración de la base de datos y servicios externos, definidas en su respectivo archivo `.env`.

---

## Despliegue con Docker Compose

1. Asegúrate de tener Docker y Docker Compose instalados.
2. Desde la raíz del dominio `pets/`, ejecuta:

   ```sh
   docker compose up --build
   ```

   Esto levantará todos los microservicios y la base de datos PostgreSQL definidos en el archivo `docker-compose.yml`.

3. Para detener los servicios:

   ```sh
   docker compose down
   ```

---

## Endpoints principales

Cada microservicio expone sus propios endpoints. Ejemplos:

- **create-pet:** `POST /api/pets/`
- **get-pet:** `GET /api/pets/{pet_id}` y `GET /api/pets/`
- **update-pet:** `PUT /api/pets/{pet_id}`
- **delete-pet:** `DELETE /api/pets/{pet_id}`

Consulta la documentación Swagger de cada microservicio para más detalles.

---

## Notas

- El dominio está preparado para escalar y agregar nuevos microservicios relacionados con mascotas.
- El CORS está abierto para facilitar el desarrollo, pero se recomienda restringirlo en producción.
- Puedes personalizar los puertos y variables de entorno en el archivo `docker-compose.yml` según tus necesidades.