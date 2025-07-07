# Delete Pet Microservice

## Description  
Microservice responsible for deleting registered pets in the system.

---

## Technologies Used

- **Language:** Python 3.10  
- **Framework:** FastAPI

---

## Architecture Style

- **RESTful API:** All operations are exposed as HTTP endpoints following REST principles.

---

## Design Patterns Applied

- **KISS (Keep It Simple, Stupid):** Code is straightforward and simple, avoiding unnecessary complexity.  
- **DRY (Don't Repeat Yourself):** Functions and logic are reused to avoid duplication.  
- **SOLID:** Principles such as separation of concerns and dependency injection are applied.

---

## Database

- **PostgreSQL:** Connection through `psycopg2` using dictionary-style cursors for easier data handling.

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


---

## Environment Variables

The microservice uses environment variables for database configuration and external services. These are defined in the `.env` file.

---

## Local Execution

1. Install dependencies:  
   ```sh
   pip install -r requirements.txt

---

## Docker local

1. build  imagen:
   ```sh
   docker build -t delete-pet .
   ```
2. execute container:
   ```sh
   docker run -p 3014:3014 --env-file .env delete-pet
   ```

---

## Endpoints 

### Delete pet by id

- **DELETE** `/api/pets/{pet_id}`

DELETE http://3.214.168.136:8000/api/pets/25

#### Example of a successful response

```json
{
    "message": "Pet deleted successfully ✅",
    "pet_id": 25
}
```
#### Swagger
http://34.229.27.85:3014/docs
---

## Notes

- Before deleting a pet, the existence of the pet in the database is validated.
- The code is easily extensible to add authentication, additional validations, or new functionality.
- CORS is open to facilitate development, but it is recommended