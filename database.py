import sqlite3

def get_connection():
    conn = sqlite3.connect("feedback.db")
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_number TEXT,
        department TEXT,
        year TEXT,
        category TEXT,
        satisfaction INTEGER,
        suggestion TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_feedback(roll, dept, year, category, satisfaction, suggestion):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO feedback 
    (roll_number, department, year, category, satisfaction, suggestion)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (roll, dept, year, category, satisfaction, suggestion))

    conn.commit()
    conn.close()

def get_all_feedback():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()

    conn.close()
    return data
