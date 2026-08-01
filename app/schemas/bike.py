from pydantic import BaseModel
from typing import Optional

class BikeBase(BaseModel):
    brand: str
    model: str
    is_available: Optional[bool] = True
    price_per_hour: Optional[float] = 5.0

class BikeCreate(BikeBase):
    pass

class BikeUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    is_available: Optional[bool] = None
    price_per_hour: Optional[float] = None

class BikeResponse(BikeBase):
    id: int

    class Config:
        from_attributes = True