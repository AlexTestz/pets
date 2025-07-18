from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import pets_routes

app = FastAPI(
    title="Get Pets Microservice",
    description="Microservice to retrieve pets data",
    version="1.0.0"
)

# Enable CORS (if React or Frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up routes
app.include_router(pets_routes.router)

@app.get("/")
def root():
    return {"message": "✅ Get Pet Service is running!"}
