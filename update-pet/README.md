# Update Pet Microservice

## Description  
Microservice responsible for updating the information of registered pets in the system.

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
update-pet/
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
   uvicorn src.main:app --reload --port 3012
   ```

---

## Docker local

1. build a image:
   ```sh
   docker build -t update-pet .
   ```
2. run container:
   ```sh
   docker run -p 3012:3012 --env-file .env update-pet
   ```

---

## Endpoints 

### Update a pet

- **PUT** `/api/pets/{pet_id}`

PUT http://3.214.168.136:8000/api/pets/25
HEADERS     Content-Type        application/json


#### Request example

```json
{
  "name": "balto",
  "species": "Dog",
  "breed": "Labrador",
  "age": 3,
  "admission_date": "2025-06-12",
  "notes": "Very friendly",
  "client_id": 1
}
```

#### Example of a successful response

```json
{
    "message": "Pet updated successfully ✅",
    "pet": {
        "id": 25,
        "name": "Firulais",
        "species": "Dog",
        "breed": "Golden Retriever",
        "age": 4,
        "admission_date": "2025-06-12",
        "notes": "Now loves swimming",
        "client_id": 1
    }
}
```
### Swagger
http://34.229.27.85:3013/docs
---

## Notes

- Before updating a pet, the existence of the associated customer is validated by consulting an external microservice.
- The code is easily extensible to add authentication, additional validations, or new functionality.
- CORS is open to facilitate development, but it is recommended to restrict it in