import os

from fastapi import HTTPException
import requests
from src.database.database import get_connection
from src.schemas.pet_schema import PetUpdate


def update_pet_in_db(pet_id: int, pet_data: PetUpdate):
    try:
        conn = get_connection()
        cur = conn.cursor()

        #  Check if the pet exists
        cur.execute("SELECT * FROM pets WHERE id = %s", (pet_id,))
        existing_pet = cur.fetchone()
        if existing_pet is None:
            raise HTTPException(status_code=404, detail="Pet not found")
        

         #  Validate client_id (if provided)
        if pet_data.client_id is not None:
            client_service_url = os.getenv("GET_CLIENT_URL", "http://localhost:3002")
            try:
                response = requests.get(f"{client_service_url}/api/clients/{pet_data.client_id}")
                if response.status_code == 404:
                    raise HTTPException(status_code=404, detail="Client not found")
                elif not response.ok:
                    raise HTTPException(status_code=500, detail="Error validating client")
            except requests.exceptions.RequestException:
                raise HTTPException(status_code=500, detail="Client service not reachable")

        #  Prepare the fields to be dynamically updated
        fields = []
        values = []

        for field, value in pet_data.dict(exclude_unset=True).items():
            fields.append(f"{field} = %s")
            values.append(value)

        if not fields:
            raise HTTPException(status_code=400, detail="No fields to update")

        # 3️⃣ Run UPDATE
        query = f"""
            UPDATE pets SET {', '.join(fields)}
            WHERE id = %s
            RETURNING *;
        """
        values.append(pet_id)
        cur.execute(query, tuple(values))

        updated_pet = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return updated_pet

    except HTTPException:
        raise
    except Exception as e:
        print("❌ Error updating pet:", e)
        raise HTTPException(status_code=500, detail="Server error while updating pet")
