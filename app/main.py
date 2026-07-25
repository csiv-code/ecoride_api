from fastapi import FastAPI
from app.api.endpoints import bikes, users  
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EcoRide API",
    description="Plataforma de renta de bicicletas (Movilidad Urbana)",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a EcoRide API. Visita /docs para ver la documentación interactiva."
    }

app.include_router(bikes.router, prefix="/api/bikes", tags=["Bikes"])

app.include_router(users.router, prefix="/api/users", tags=["Users"])