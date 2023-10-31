from pydantic import BaseModel
from typing import Optional

class ClientModel(BaseModel):
    client_id: Optional[str] = None
    client_name: str
    client_email: str
    client_password: str

    class Config:
        json_schema_extra = {
            "exemple": {
                "client_name": "Nome do cliente",
                "client_email": "cliente@email.com",
                "client_password": "senha do cliente"
            }
        }