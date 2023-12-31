import sqlite3

def create_database():
    with sqlite3.connect("./db_main/restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MenuData 
            (item_id TEXT PRIMARY KEY, item_name TEXT, item_description TEXT, item_price REAL, category_name TEXT)
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS OrdersData 
            (order_id TEXT PRIMARY KEY, order_num INTEGER, order_items TEXT, order_status TEXT, order_total REAL, order_date TEXT, client_email TEXT)
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS BookingData 
            (booking_id TEXT PRIMARY KEY, num_people INTEGER, booking_status TEXT, booking_date TEXT, client_email TEXT)
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ReviewsData
            (review_id TEXT PRIMARY KEY, review_description TEXT, review_score INTEGER, review_date TEXT, client_email TEXT)
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ClientData
            (user_id TEXT PRIMARY KEY, client_name TEXT, client_email TEXT UNIQUE KEY, client_password TEXT)
        """)
        db.commit()