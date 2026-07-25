from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base 

class Bike(Base):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="available") 
    station_id = Column(Integer, index=True, nullable=True) 