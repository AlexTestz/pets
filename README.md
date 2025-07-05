# Pets Domain

## Description  
This domain groups all microservices related to pet management, including creation, retrieval, updating, and deletion of pet records.

---

## Included Microservices

- **create-pet:** Registers new pets.  
- **get-pet:** Retrieves pets (by ID or all).  
- **update-pet:** Updates pet information.  
- **delete-pet:** Deletes pets.

---

## Technologies Used

- **Language:** Python 3.10  
- **Framework:** FastAPI  
- **Database:** PostgreSQL  
- **Containers:** Docker and Docker Compose

---

## Architecture Style

- **RESTful API:** All microservices expose HTTP endpoints following REST principles.

---

## Design Patterns Applied

- **KISS:** Simple and straightforward code.  
- **DRY:** Reuse of functions and logic.  
- **SOLID:** Clear separation of concerns and easy to extend.

---

## Internal Architecture

- **N-tier architecture:** Separation between routes, controllers, schemas, utilities, and data access.  
- **MVC-like model:** Follows typical MVC responsibility separation.

---

## Security and Middleware

- **CORS:** Configured to accept requests from any origin (`allow_origins=["*"]`), useful for development.  
- **JWT:** Not implemented by default but easily integrable.

---

## Domain Structure


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


---

## Environment Variables

Each microservice uses environment variables for database and external service configuration, defined in its own `.env` file.

---

## Deployment with Docker Compose

1. Make sure Docker and Docker Compose are installed.  
2. From the root of the `pets/` domain, run:

   ```sh
   docker compose up --build


   Esto levantará todos los microservicios y la base de datos PostgreSQL definidos en el archivo `docker-compose.yml`.

3. stop services:

   ```sh
   docker compose down
   ```

---

## Main endpoints

Each microservice exposes its own endpoints. Examples:

- **create-pet:** `POST /api/pets/`
- **get-pet:** `GET /api/pets/{pet_id}` and `GET /api/pets/`
- **update-pet:** `PUT /api/pets/{pet_id}`
- **delete-pet:** `DELETE /api/pets/{pet_id}`

See the Swagger documentation for each microservice for more details.

---

## Notes

- The domain is ready to scale and add new microservices related to pets.
- CORS is open to facilitate development, but it is recommended to restrict it in production.
- You can customize the ports and environment variables in the `docker-compose.yml` file according to your needs.