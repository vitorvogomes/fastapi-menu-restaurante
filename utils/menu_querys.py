import sqlite3
import uuid

def create_item(item_name: str, item_description: str, item_price: float, category_name: str):
    item_id = str(uuid.uuid4())  # Gera uma UUID
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO MenuData VALUES (?, ?, ?, ?, ?)", 
            (item_id, item_name, item_description, item_price, category_name)
        )
        db.commit()

def get_menu_items():
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor() 
        cursor.execute("SELECT * FROM MenuData")

        result = cursor.fetchall()
        return result

def get_item_by_id(item_id: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM MenuData WHERE item_id=?", (item_id,))

        item_data = cursor.fetchall() # Retorna a primeira linha correspondente
        return item_data

def update_item_by_id(item_id: str, data):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE MenuData SET item_name=?, item_description=?, item_price=?, category_name=? WHERE item_id=?", 
                        (data["item_name"], data["item_description"], data["item_price"], data["category_name"], item_id)
                    )
        db.commit()

        cursor.execute("SELECT * FROM MenuData WHERE item_id=?", (item_id,))
        item_data = cursor.fetchall() # Retorna a primeira linha correspondente
        return item_data

def delete_item_by_id(item_id: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM MenuData WHERE item_id=?", (item_id,))
        db.commit()

def get_item_by_name(item_name: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM MenuData WHERE item_name=?", (item_name,))

        item_data = cursor.fetchall() # Retorna a primeira linha correspondente
        return item_data

def get_menu_categories():
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor() 
        cursor.execute("SELECT DISTINCT category_name FROM MenuData")
            
        categories = [row[0] for row in cursor.fetchall()]
        return categories

def get_item_by_category(category_name: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM MenuData WHERE category_name=?", (category_name,))

        item_data = cursor.fetchall() # Retorna a primeira linha correspondente
        return item_data






