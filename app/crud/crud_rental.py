from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timezone
from app.models.rental import Rental
from app.models.user import User
from app.models.bike import Bike
from app.schemas.rental import RentalCreate, RentalUpdate

def create_rental(db: Session, rental_data: RentalCreate):
    user = db.query(User).filter(User.id == rental_data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Regla de negocio: Usuario inactivo no puede alquilar")

    bike = db.query(Bike).filter(Bike.id == rental_data.bike_id).first()
    if not bike:
        raise HTTPException(status_code=404, detail="Bicicleta no encontrada")
    if not bike.is_available:
        raise HTTPException(status_code=400, detail="Regla de negocio: La bicicleta no está disponible actualmente")

    bike.is_available = False

    db_rental = Rental(
        user_id=rental_data.user_id,
        bike_id=rental_data.bike_id,
        status="active"
    )
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

def get_rental(db: Session, rental_id: int):
    rental = db.query(Rental).filter(Rental.id == rental_id).first()
    if not rental:
        raise HTTPException(status_code=404, detail="Alquiler no encontrado")
    return rental

def get_rentals(db: Session, skip: int = 0, limit: int = 10, status: str = None, user_id: int = None):
    query = db.query(Rental)
    if status:
        query = query.filter(Rental.status == status)
    if user_id:
        query = query.filter(Rental.user_id == user_id)
    return query.offset(skip).limit(limit).all()

def complete_rental(db: Session, rental_id: int):
    rental = get_rental(db, rental_id)
    if rental.status != "active":
        raise HTTPException(status_code=400, detail="Regla de negocio: El alquiler ya fue finalizado o cancelado")

    end_time = datetime.now(timezone.utc)
    
    start_time = rental.start_time
    if start_time.tzinfo is None:
        start_time = start_time.replace(tzinfo=timezone.utc)

    rental.end_time = end_time
    rental.status = "completed"

    bike = db.query(Bike).filter(Bike.id == rental.bike_id).first()
    if bike:
        bike.is_available = True
        duration_hours = max((end_time - start_time).total_seconds() / 3600.0, 0.5)
        rental.total_cost = round(duration_hours * getattr(bike, 'price_per_hour', 5.0), 2)

    db.commit()
    db.refresh(rental)
    return rental

def delete_rental(db: Session, rental_id: int):
    rental = get_rental(db, rental_id)

    if rental.status == "active":
        bike = db.query(Bike).filter(Bike.id == rental.bike_id).first()
        if bike:
            bike.is_available = True
            
    db.delete(rental)
    db.commit()
    return {"detail": "Alquiler eliminado exitosamente"}