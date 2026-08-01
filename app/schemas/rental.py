from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class RentalBase(BaseModel):
    user_id: int
    bike_id: int

class RentalCreate(RentalBase):
    pass

class RentalUpdate(BaseModel):
    status: Optional[str] = None
    end_time: Optional[datetime] = None
    total_cost: Optional[float] = None

class RentalResponse(RentalBase):
    id: int
    start_time: datetime
    end_time: Optional[datetime] = None
    status: str
    total_cost: float

    model_config = ConfigDict(from_attributes=True)