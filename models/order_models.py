from pydantic import BaseModel, conint, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

class OrderStatusModel(str, Enum):
    AguardandoPagamento = "Pendente"
    Confirmado = "Confirmado"
    EmPreparacao = "Preparo"
    SaiuParaEntrega = "Retirada"
    Entregue = "Entregue"
    Cancelado = "Cancelado"

class OrderItemsModel(BaseModel):
    item_name: str
    item_qtd: int

    class Config:
        json_schema_extra = {
            "example": {
                "order_items": [
                    {
                        "item_name": "Nome do Item 01",
                        "item_qtd": 2
                    },
                    {
                        "item_name": "Nome do Item 02",
                        "item_qtd": 2
                    }
                ]
            }
        }

class OrderModel(BaseModel):
    order_id: Optional[str] = None
    order_num: conint(ge=10000, le=99999)
    order_items: List[OrderItemsModel]
    order_status: OrderStatusModel
    order_total: Optional[float] = None
    order_date: str
    client_email: str

    @validator("order_date")
    def validate_order_date(cls, value):
        try:
            # Tente analisar a data no formato "DD/MM/YYYY"
            order_date = datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Data inválida. Use o formato 'DD/MM/YYYY'.")

        # Obtenha a data atual
        current_date = datetime.now().date()

        if order_date < current_date:
            raise ValueError("Data inválida. Data deve ser igual ou posterior à data atual.")

        return value

    class Config:
        json_schema_extra = {
            "example": {
                "order_num": 12345,
                "order_items": [
                    {
                        "item_name": "Nome do Item 01",
                        "item_qtd": 2
                    },
                    {
                        "item_name": "Nome do Item 02",
                        "item_qtd": 2
                    }
                ],
                "order_status": "Em preparação ou Saiu para entrega ou Entregue ou Cancelado",
                "order_date": "01/01/2023",
                "client_email": "email@teste.com"
            }
        }