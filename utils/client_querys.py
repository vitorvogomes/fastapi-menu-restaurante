import sqlite3
import uuid

def create_client(client_name: str, client_email: str, client_password: str):
    client_id = str(uuid.uuid4()) # Gera UUID
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO ClientData VALUES (?,?,?,?)",
            (client_id, client_name, client_email, client_password)
        )
    db.commit()

def get_client_list():
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM ClientData")

        client_data = cursor.fetchall()
        return client_data

def get_client_by_email(client_email: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM ClientData WHERE client_email=?",
            (client_email,)
        )
        client_data = cursor.fetchall()
        return client_data
