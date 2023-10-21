from pydantic import BaseModel, conint, constr, validator
from typing import Optional

class ReviewModel(BaseModel):
    review_id: Optional[str] = None
    review_description: Optional[constr(max_length=500)] = None
    review_score: conint(ge=0, le=10)
    review_date: Optional[str] = None
    client_email: str

    class Config:
        json_schema_extra = {
            "example": {
                "review_description": "Adorei o restaurante!",
                "review_score": 10,
                "client_email": "email@teste.com"
            }
        }