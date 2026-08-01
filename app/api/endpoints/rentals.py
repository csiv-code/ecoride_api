from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.schemas.rental import RentalCreate, RentalResponse
from app.crud import crud_rental

router = APIRouter()

@router.post("/", response_model=RentalResponse, status_code=201)
def create_rental(rental: RentalCreate, db: Session = Depends(get_db)):
    return crud_rental.create_rental(db=db, rental_data=rental)

@router.get("/", response_model=List[RentalResponse])
def read_rentals(
    skip: int = 0,
    limit: int = 10,
    status: Optional[str] = Query(None, description="Filtrar por estado (ej: active, completed)"),
    user_id: Optional[int] = Query(None, description="Filtrar alquileres por ID de usuario"),
    db: Session = Depends(get_db)
):
    return crud_rental.get_rentals(db=db, skip=skip, limit=limit, status=status, user_id=user_id)

@router.get("/{rental_id}", response_model=RentalResponse)
def read_rental(rental_id: int, db: Session = Depends(get_db)):
    return crud_rental.get_rental(db=db, rental_id=rental_id)

@router.patch("/{rental_id}/complete", response_model=RentalResponse)
def finish_rental(rental_id: int, db: Session = Depends(get_db)):
    """Regla de negocio: Finaliza el alquiler, libera la bici y calcula el monto total."""
    return crud_rental.complete_rental(db=db, rental_id=rental_id)

@router.delete("/{rental_id}")
def delete_rental(rental_id: int, db: Session = Depends(get_db)):
    return crud_rental.delete_rental(db=db, rental_id=rental_id)