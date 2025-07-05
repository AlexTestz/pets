# Create Pet Microservice

## Description  
Microservice responsible for registering pets in the system.

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
create-pet/
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

2. Execute microservice:
   ```sh
   uvicorn src.main:app --reload --port 3011
   ```

---

## Docker local

1. build image:
   ```sh
   docker build -t create-pet .
   ```
2. Execute container :
   ```sh
   docker run -p 3011:3011 --env-file .env create-pet
   ```

---

## Endpoints 

### Register a pet

- **POST** `/api/pets/`

POST http://3.214.168.136:8000/api/pets/
HEADERS     Content-Type        application/json

#### Request example

```json
{
  "name": "Firulais",
  "species": "Dog",
  "breed": "Labrador",
  "age": 3,
  "admission_date": "2025-06-12",
  "notes": "Friendly with other pets",
  "client_id": 1
}
```

#### Example of a successful response

```json
{
    "message": "Pet registered successfully ✅",
    "pet": {
        "id": 25,
        "name": "PEQUEÑIN",
        "species": "Dog",
        "breed": "Labrador",
        "age": 3,
        "admission_date": "2025-06-12",
        "notes": "Friendly with other pets",
        "client_id": 1
    }
}
```

### Swagger
http://34.229.27.85:3011/docs 
---

## Notes

- Before registering a pet, the existence of the associated customer is validated by consulting an external microservice.
- The code is easily extensible to add authentication, additional validations, or new functionality.
- CORS is open to facilitate development, but it is recommended to restrict it in production.