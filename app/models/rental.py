from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float, String
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    bike_id = Column(Integer, ForeignKey("bikes.id"), nullable=False)
    
    start_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    end_time = Column(DateTime, nullable=True)
    status = Column(String, default="active", index=True)  # active, completed, cancelled
    total_cost = Column(Float, default=0.0)

    # Relaciones ORM
    user = relationship("User", back_populates="rentals")
    bike = relationship("Bike", back_populates="rentals")