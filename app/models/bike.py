from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Bike(Base):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    is_available = Column(Boolean, default=True)  
    price_per_hour = Column(Float, default=5.0)
    rentals = relationship("Rental", back_populates="bike", cascade="all, delete-orphan")