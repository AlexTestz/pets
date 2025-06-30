import os
import requests
from fastapi import HTTPException
from src.schemas.pet_schema import PetCreate
from src.database.database import get_connection


def create_pet_in_db(pet: PetCreate):
    try:

         # 🌐 Leer dirección y puerto del microservicio de clientes desde variables de entorno
        CLIENT_SERVICE_HOST = os.getenv("CLIENT_SERVICE_HOST", "localhost")
        CLIENT_SERVICE_PORT = os.getenv("CLIENT_SERVICE_PORT", "3002")
        CLIENT_SERVICE_URL = f"http://{CLIENT_SERVICE_HOST}:{CLIENT_SERVICE_PORT}/api/clients/{pet.client_id}"

        # 🔍 Validar si el cliente existe haciendo una solicitud al microservicio de clientes
        try:
            response = requests.get(CLIENT_SERVICE_URL)
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="Client not found")
            elif not response.ok:
                raise HTTPException(status_code=500, detail="Error validating client")
        except requests.exceptions.RequestException as req_err:
            print("❌ Error contacting client service:", req_err)
            raise HTTPException(status_code=500, detail="Client service not reachable")

        # ✅ Insertar mascota en la base de datos local
        conn = get_connection()
        cur = conn.cursor()

        query = """
            INSERT INTO pets (name, species, breed, age, admission_date, notes, client_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING *;
        """

        cur.execute(query, (
            pet.name,
            pet.species,
            pet.breed,
            pet.age,
            pet.admission_date,
            pet.notes,
            pet.client_id
        ))

        new_pet = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return new_pet

    except HTTPException as e:
        raise e
    except Exception as e:
        print("❌ Error saving pet:", e)
        raise HTTPException(status_code=500, detail="Server error while saving pet")
