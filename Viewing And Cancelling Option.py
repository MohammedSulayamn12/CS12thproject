def view_user_bookings(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Bookings WHERE user_id = ? AND status = 'active'", (user_id,))
    bookings = cursor.fetchall()
    conn.close()
    return bookings

def cancel_booking(booking_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Bookings SET status = 'cancelled' WHERE booking_id = ?", (booking_id,))
    conn.commit()
    print("Booking cancelled successfully.")
    conn.close()
