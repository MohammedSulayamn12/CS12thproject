def book_travel_option(user_id, option_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT available_seats FROM TravelOptions WHERE option_id = ?", (option_id,))
    seats = cursor.fetchone()[0]
    if seats > 0:
        cursor.execute("INSERT INTO Bookings (user_id, option_id, status) VALUES (?, ?, 'active')", (user_id, option_id))
        cursor.execute("UPDATE TravelOptions SET available_seats = available_seats - 1 WHERE option_id = ?", (option_id,))
        conn.commit()
        print("Booking created successfully!")
    else:
        print("No available seats for this option.")
    conn.close()
