from pydantic import BaseModel, ConfigDict
from typing import Optional

class BikeBase(BaseModel):
    status: str = "available"
    station_id: Optional[int] = None

class BikeCreate(BikeBase):
    pass

class BikeUpdate(BikeBase):
    status: Optional[str] = None

class BikeResponse(BikeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)