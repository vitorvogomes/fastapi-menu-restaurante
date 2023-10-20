import sqlite3
import uuid

def create_booking(num_people: int, booking_status: str, booking_date: str, client_email: str):
    booking_id = str(uuid.uuid4()) #Gera um UUID
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO BookingData VALUES (?,?,?,?,?)",
            (booking_id, num_people, booking_status, booking_date, client_email)
        )  
        db.commit()

def get_booking_list():
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM BookingData")

        booking_data = cursor.fetchall()
        return booking_data

def update_booking(booking_id: str, booking_status: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "UPDATE BookingData SET booking_status=? WHERE booking_id=?",
            (booking_status, booking_id)
        ) 
        db.commit() 

def get_booking_by_id(booking_id: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM BookingData WHERE booking_id=?",
            (booking_id,)
        )

        booking_data = cursor.fetchall()
        return booking_data

def validate_client_booking(booking_date: str, client_email: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM BookingData WHERE booking_date=? AND client_email=?",
            (booking_date, client_email)
        )

        booking_data = cursor.fetchall()
        return booking_data

def booking_query_params(booking_date: str, booking_status: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM BookingData WHERE booking_date=? OR booking_status=?",
            (booking_date, booking_status)
        )

        booking_data = cursor.fetchall()
        return booking_data