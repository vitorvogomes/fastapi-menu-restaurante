from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from models.order_models import OrderModel, OrderStatusModel 
from utils.order_querys import *
from utils.menu_querys import get_item_by_name

import json

order_router = APIRouter()

@order_router.get("/orders", status_code=status.HTTP_200_OK)
async def order_list(date: str | None = None, status: str | None = None):
    try:
        if date or status:
            orders_data = order_query_params(date, status)
        else:
            orders_data = get_orders_list()
        return {"orders": formatted_list(orders_data)}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"{error}"
        )

@order_router.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_new_order(order_data: OrderModel):
    try:
        order = get_order_by_num(order_data.order_num)
        if not order:
            items_verification = verify_order_items(order_data)
            if items_verification is False:
                create_order(
                    order_data.order_num,
                    order_data.order_items,
                    order_data.order_status,
                    calculate_order_total(order_data),
                    order_data.order_date,
                    order_data.client_email
                )
                return {"success": f"O pedido com o número: '{order_data.order_num}' foi criado!"}
            else:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"detail": f"Os itens: {items_verification} não foram encontrados no menu."},
                )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Já existe um pedido com o numero: '{order_data.order_num}'."
        )

@order_router.get("/orders/{order_num}", status_code=status.HTTP_200_OK)
async def order_by_num(order_num: int):
    try:
        order = get_order_by_num(order_num)
        if order:
            return {"order": formatted_list(order) }
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O pedido com o número: '{order_num}' não foi encontrado."
        )

@order_router.delete("/orders/{order_num}", status_code=status.HTTP_200_OK)
async def delete_order_by_num(order_num: int):
    try:
        order = get_order_by_num(order_num)
        if order:
            delete_order(order_num)
            return {"success": f"O pedido com o número: '{order_num}' foi deletado." }
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O pedido com o número: '{order_num}' não foi encontrado."
        )

@order_router.patch("/orders/{order_num}/status/{order_status}", status_code=status.HTTP_200_OK)
async def update_order_status(order_num: int, order_status: str):
    try:
        order = get_order_by_num(order_num)
        if order:
            matches = [member for member in OrderStatusModel if member.value == order_status]
            if matches:
                update_order(order_num, order_status)
                return {"success": f"O status do pedido: '{order_num}' foi atualizado para: '{order_status}'." }
            else:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"detail": "Valores permitidos para o status do pedido: [Pendente, Confirmado, Preparo, Retirada, Entregue, Cancelado]"}
                )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O pedido com o número: '{order_num}' não foi encontrado."
        )

def formatted_list(data): # Formatação do retorno das pesquisas no banco de dados
    order_data = []
    for item in data:
        item_data = {
            "order_id": item[0],
            "order_num": item[1],
            "order_items": json.loads(item[2]), 
            "order_status": item[3],
            "order_total": item[4],
            "order_date": item[5],
            "client_email": item[6]
        }
        order_data.append(item_data)
    return order_data

def calculate_order_total(order_data: OrderModel):
    order_items_data = [(item.item_name, item.item_qtd) for item in order_data.order_items]
    soma = 0
    for data in order_items_data:
        existent_item = get_item_by_name(data[0])
        soma += (existent_item[0][3] * data[1])
    total = f"{soma:.2f}"
    return total

def verify_order_items(order_data: OrderModel):
    try:
        order_items_names = [item.item_name for item in order_data.order_items]
        no_existent_names = []
        for names in order_items_names:
            existent_item = get_item_by_name(names)
            if not existent_item:
                no_existent_names.append(names)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )
    else:
        if no_existent_names:
            return no_existent_names
        else:
            return False