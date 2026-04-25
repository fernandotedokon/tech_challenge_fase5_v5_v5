from pydantic import BaseModel, Field

class Transaction(BaseModel):
    amount: float = Field(..., gt=0)
    user_id: int
    device_id: str
    lat: float
    lon: float
    merchant_lat: float
    merchant_lon: float
