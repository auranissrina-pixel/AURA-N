import tkinter as tk
from tkinter import messagebox
import db

# Pastikan tabel database sudah siap
db.buat_tabel()

def proses_login():
    username = entry_user.get()
    password = entry_pass.get()
    
    if db.cek_login(username, password):
        messagebox.showinfo("Berhasil", f"Selamat datang, {username}!")
    else:
        messagebox.showerror("Gagal", "Username atau password salah!")

def proses_daftar():
    username = entry_user.get()
    password = entry_pass.get()
    
    if not username or not password:
        messagebox.showwarning("Peringatan", "Username dan password tidak boleh kosong!")
        return
        
    if db.daftar_user(username, password):
        messagebox.showinfo("Berhasil", "Akun berhasil dibuat! Silakan login.")
    else:
        messagebox.showerror("Gagal", "Username sudah terdaftar!")

# Inisialisasi Window Utama
root = tk.Tk()
root.title("Aplikasi Login & Register")
root.geometry("350x250")
root.resizable(False, False)

# Label Judul
label_title = tk.Label(root, text="Sistem Otentikasi", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Form Input Username
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Username:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_user = tk.Entry(frame_input, width=25)
entry_user.grid(row=0, column=1, pady=5)

# Form Input Password
tk.Label(frame_input, text="Password:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
entry_pass = tk.Entry(frame_input, show="*", width=25)
entry_pass.grid(row=1, column=1, pady=5)

# Tombol Aksi
frame_btn = tk.Frame(root)
frame_btn.pack(pady=15)

btn_login = tk.Button(frame_btn, text="Login", bg="#4CAF50", fg="white", width=10, command=proses_login)
btn_login.grid(row=0, column=0, padx=5)

btn_register = tk.Button(frame_btn, text="Daftar", bg="#2196F3", fg="white", width=10, command=proses_daftar)
btn_register.grid(row=0, column=1, padx=5)

# Menjalankan Aplikasi GUI
root.mainloop()