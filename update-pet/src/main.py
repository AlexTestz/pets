from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.pets_routes import router  

app = FastAPI(
    title="Update Pet Microservice",
    description="Microservice to update pets",
    version="1.0.0"
)

# CORS middleware (if you use frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "✅ Update Pet Service is running!"}
