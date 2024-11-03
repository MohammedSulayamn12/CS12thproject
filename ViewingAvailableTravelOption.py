def view_travel_options():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TravelOptions WHERE available_seats > 0")
    options = cursor.fetchall()
    conn.close()
    return options

for option in view_travel_options():
    print(option)
