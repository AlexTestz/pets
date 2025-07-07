# Get Pet Microservice

## Description  
Microservice responsible for retrieving information of registered pets in the system.

---

## Technologies Used

- **Language:** Python 3.10  
- **Framework:** FastAPI

---

## Architecture Style

- **RESTful API:** All operations are exposed as HTTP endpoints following REST principles.

---

## Design Patterns Applied

- **KISS (Keep It Simple, Stupid):** Code is simple and straightforward, avoiding unnecessary complexity.  
- **DRY (Don't Repeat Yourself):** Functions and logic are reused to avoid duplication.  
- **SOLID:** Principles such as separation of concerns and dependency injection are applied.

---

## Database

- **PostgreSQL:** Connection using `psycopg2` and dictionary-style cursors for easier data handling.

---

## Internal Architecture

- **N-tier architecture:** Clear separation between routes (routers), controllers, schemas, utilities (utils), and data access (database).  
- **MVC-like model:** Although no explicit ORM models are used, the structure follows typical MVC separation of concerns.

---

## Security and Middleware

- **CORS:** Configured to accept requests from any origin (`allow_origins=["*"]`), useful for development and testing with frontends like React.  
- **JWT:** Currently this microservice does not implement JWT authentication but can be easily integrated in the future.

---

## Project Structure



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


---

## Environment Variables

The microservice uses environment variables for database configuration and external services. These are defined in the `.env` file.

---

## Local Execution

1. Install dependencies:  
   ```sh
   pip install -r requirements.txt

2. Ejecuta el microservicio:
   ```sh
   uvicorn src.main:app --reload --port 3013
   ```

---

## Docker local

1. build image:
   ```sh
   docker build -t get-pet .
   ```
2. Execute container:
   ```sh
   docker run -p 3013:3013 --env-file .env get-pet
   ```

---

## Endpoints 

### Look up a pet by ID

- **GET** `/api/pets/{pet_id}`

GET http://3.214.168.136:8000/api/pets/25

#### Example of a successful response

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

### See all pets

- **GET** `/api/pets/`

GET http://3.214.168.136:8000/api/pets

#### Example of a successful response

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

## Notes

- Allows you to search for pets by ID or list all registered pets.
- The code is easily extensible to add authentication, additional filters, or new features.
- CORS is open to facilitate development, but it is recommended