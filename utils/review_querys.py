import sqlite3
import uuid
from datetime import datetime

def create_review(review_description: str, review_score: int, client_email: str):
    review_id = str(uuid.uuid4()) #Gera um UUID
    review_date = datetime.now().strftime("%d/%m/%Y")
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO ReviewsData VALUES (?,?,?,?,?)",
            (review_id, review_description, review_score, review_date, client_email)
        )
        db.commit()

def get_review_list():
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM ReviewsData")

        review_data = cursor.fetchall()
        return review_data

def review_query_params(review_score: int, review_date: str):
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM ReviewsData WHERE review_score=? OR review_date=?",
            (review_score, review_date)
        )

        review_data = cursor.fetchall()
        return review_data


