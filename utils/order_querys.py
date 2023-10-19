from models.order_models import OrderItemsModel
from typing import List

import sqlite3
import uuid
import json

def create_order(order_num: int, order_items: List[OrderItemsModel], order_status: str, order_total: float):
    order_id = str(uuid.uuid4()) #Gera um UUID
    order_items_json = json.dumps([item.dict() for item in order_items]) # Serializa a lista de itens para JSON
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO OrdersData VALUES (?,?,?,?,?)",
            (order_id, order_num, order_items_json, order_status, order_total)
        )
        db.commit()

def get_orders_list():
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM OrdersData")

        orders_data = cursor.fetchall()
        return orders_data

def get_order_by_num(order_num: int):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM OrdersData WHERE order_num=?", (order_num,))
        
        orders_data = cursor.fetchall()
        return orders_data

def delete_order(order_num: int):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM OrdersData WHERE order_num=?", (order_num,))
        db.commit()

def update_order(order_num: int, order_status: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE OrdersData SET order_status=? WHERE order_num=?", (order_status, order_num))
        db.commit()

def get_order_by_id(order_id: int):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM OrdersData WHERE order_id=?", (order_id,))

        order_data = cursor.fetchall()
        return order_data