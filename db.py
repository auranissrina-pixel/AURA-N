import sqlite3

def buat_koneksi():
    conn = sqlite3.connect("database_saya.db")
    return conn

def buat_tabel():
    conn = buat_koneksi()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    # Menambahkan username dan password bawaan (default)
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', '12345')")
    conn.commit()
    conn.close()