import psycopg2
from psycopg2.extras import RealDictCursor
from src.config import settings

def get_connection():
    try:
        return psycopg2.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            cursor_factory=RealDictCursor
        )
    except Exception as e:
        print("❌ Database connection error:", e)
        raise
