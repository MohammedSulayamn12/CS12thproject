def register_user(name, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Email already exists.")
    finally:
        conn.close()

def login_user(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login successful!")
        return user[0]  
    else:
        print("Invalid credentials.")
        return None
