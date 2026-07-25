from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud import crud_bike
from app.schemas.bike import BikeCreate, BikeResponse, BikeUpdate
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=BikeResponse)
def create_bike(bike: BikeCreate, db: Session = Depends(get_db)):
    """Agrega un nuevo registro de bicicleta (Equivalente a tu addnew.php)"""
    return crud_bike.create_bike(db=db, bike=bike)

@router.get("/", response_model=List[BikeResponse])
def read_bikes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene todas las bicicletas (Equivalente a leer tu tabla en index.php)"""
    return crud_bike.get_bikes(db, skip=skip, limit=limit)

@router.get("/{bike_id}", response_model=BikeResponse)
def read_bike(bike_id: int, db: Session = Depends(get_db)):
    db_bike = crud_bike.get_bike(db, bike_id=bike_id)
    if db_bike is None:
        raise HTTPException(status_code=404, detail="Bicicleta no encontrada")
    return db_bike

@router.put("/{bike_id}", response_model=BikeResponse)
def update_bike(bike_id: int, bike_update: BikeUpdate, db: Session = Depends(get_db)):
    """Actualiza una bicicleta (Equivalente a tu edit.php)"""
    db_bike = crud_bike.get_bike(db, bike_id=bike_id)
    if db_bike is None:
        raise HTTPException(status_code=404, detail="Bicicleta no encontrada")
    return crud_bike.update_bike(db=db, db_bike=db_bike, bike_update=bike_update)

@router.delete("/{bike_id}")
def delete_bike(bike_id: int, db: Session = Depends(get_db)):
    """Elimina un registro (Equivalente a tu delete.php)"""
    db_bike = crud_bike.get_bike(db, bike_id=bike_id)
    if db_bike is None:
        raise HTTPException(status_code=404, detail="Bicicleta no encontrada")
    crud_bike.delete_bike(db=db, db_bike=db_bike)
    return {"message": "Bicicleta eliminada exitosamente"}