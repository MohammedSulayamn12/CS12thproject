def add_travel_option(type, destination, date, price, available_seats):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO TravelOptions (type, destination, date, price, available_seats) VALUES (?, ?, ?, ?, ?)",
                   (type, destination, date, price, available_seats))
    conn.commit()
    conn.close()
    print("Travel option added successfully.")
