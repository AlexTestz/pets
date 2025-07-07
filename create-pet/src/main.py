from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import pets_routes
from src.config import settings

app = FastAPI(
    title="Create Pet Microservice",
    description="Microservice to register pets in the system",
    version="1.0.0"
)

# CORS middleware (allows React or other frontends to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up routes
app.include_router(pets_routes.router)

# Root endpoint (health check)
@app.get("/")
def health_check():
    return {"message": "✅ Create Pet Service is running!"}
