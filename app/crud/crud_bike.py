from sqlalchemy.orm import Session
from app.models.bike import Bike
from app.schemas.bike import BikeCreate, BikeUpdate

def get_bike(db: Session, bike_id: int):
    return db.query(Bike).filter(Bike.id == bike_id).first()

def get_bikes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Bike).offset(skip).limit(limit).all()

def create_bike(db: Session, bike: BikeCreate):
    db_bike = Bike(**bike.model_dump())
    db.add(db_bike)
    db.commit()
    db.refresh(db_bike)
    return db_bike

def update_bike(db: Session, db_bike: Bike, bike_update: BikeUpdate):
    update_data = bike_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_bike, key, value)
    db.commit()
    db.refresh(db_bike)
    return db_bike

def delete_bike(db: Session, db_bike: Bike):
    db.delete(db_bike)
    db.commit()
    return db_bike