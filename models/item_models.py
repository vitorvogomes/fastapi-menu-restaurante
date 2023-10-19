from pydantic import BaseModel
from typing import Optional

class ItemModel(BaseModel):
    item_id: Optional[str] = None
    item_name: str
    item_description: str
    item_price: float
    category_name: str

    class Config:
        json_schema_extra = {
            "example": {
                "item_name": "Nome do Item",
                "item_description": "Descrição do Item",
                "item_price": 9.99,
                "category_name": "Categoria do Item"
            }
        }