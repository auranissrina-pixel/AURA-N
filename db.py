import sqlite3

def buat_koneksi():
    conn = sqlite3.connect("database_saya.db")
    return conn

def buat_tabel():
    conn = buat_koneksi()
    cursor = conn.cursor()
    
    # Tabel Users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    
    # Tabel Riwayat
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS riwayat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            aksi TEXT,
            tanggal TEXT
        )
    """)
    
    # Menambahkan user default admin
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', '12345')")
    conn.commit()
    conn.close()

def daftar_user(username, password):
    conn = buat_koneksi()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        berhasil = True
    except sqlite3.IntegrityError:
        berhasil = False
    conn.close()
    return berhasil

def cek_login(username, password):
    conn = buat_koneksi()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    hasil = cursor.fetchone()
    conn.close()
    return hasil is not None

def simpan_riwayat(username, *args):
    conn = buat_koneksi()
    cursor = conn.cursor()
    # Menggabungkan data argumen menjadi teks aksi
    detail_aksi = " ".join(map(str, args))
    cursor.execute(
        "INSERT INTO riwayat (username, aksi, tanggal) VALUES (?, ?, datetime('now', 'localtime'))",
        (username, detail_aksi)
    )
    conn.commit()
    conn.close()