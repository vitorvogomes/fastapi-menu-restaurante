from pydantic import BaseModel, conint
from typing import Optional, List
from enum import Enum

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
                "order_status": "Em preparação ou Saiu para entrega ou Entregue ou Cancelado"
            }
        }