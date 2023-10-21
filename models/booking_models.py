from pydantic import BaseModel, conint, validator
from typing import Optional
from enum import Enum
from datetime import datetime

class BookingStatusModel(str, Enum):
    Solicitado = "Solicitado"
    Confrimado = "Confirmado"
    Cancelado = "Cancelado"

class BookingModel(BaseModel):
    booking_id: Optional[str] = None
    num_people: conint(ge=1, le=50)
    booking_status: BookingStatusModel
    booking_date: str
    client_email: str

    @validator("booking_date")
    def validate_booking_date(cls, value):
        try:
            booking_date = datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Data inválida. Use o formato 'DD/MM/YYYY'.")
        
        current_date = datetime.now().date()

        if booking_date < current_date:
            raise ValueError("Data inválida. Data deve ser igual ou posterior à data atual.")
        
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "num_people": 5,
                "booking_status": "Solicitado",
                "booking_date": "01/01/2023",
                "client_email": "email@teste.com"
            }
        }