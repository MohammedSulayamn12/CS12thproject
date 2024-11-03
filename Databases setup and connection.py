import sqlite3

def connect_db():
    conn = sqlite3.connect('travel_booking.db')
    return conn

def setup_database():
    conn = connect_db()
    cursor = conn.cursor()
    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    ''')
    # Create TravelOptions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TravelOptions (
            option_id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            destination TEXT,
            date TEXT,
            price REAL,
            available_seats INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            option_id INTEGER,
            status TEXT,
            FOREIGN KEY (user_id) REFERENCES Users(user_id),
            FOREIGN KEY (option_id) REFERENCES TravelOptions(option_id)
        )
    ''')
    conn.commit()
    conn.close()

setup_database()
