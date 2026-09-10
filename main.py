# Mengimpor modul fungsi dan modul database
import mymodule
import db
import getpass


def tampilkan_menu_awal():
    print("\n=== SELAMAT DATANG ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")


def tampilkan_menu(username):
    print(f"\n=== MENU PROGRAM (login sebagai: {username}) ===")
    print("1. Cek Ganjil Genap")
    print("2. Cek Bilangan Prima")
    print("3. Lihat Riwayat")
    print("4. Hapus Riwayat")
    print("5. Logout")


def input_password(prompt="Password: "):
    """Menggunakan getpass agar password tidak tampil di layar (fallback ke input biasa jika gagal)."""
    try:
        return getpass.getpass(prompt)
    except Exception:
        return input(prompt)


def proses_register():
    print("\n--- REGISTER AKUN BARU ---")
    username = input("Buat username: ").strip()
    if not username:
        print("Username tidak boleh kosong.")
        return
    password = input_password("Buat password: ")
    if not password:
        print("Password tidak boleh kosong.")
        return

    berhasil = db.daftar_user(username, password)
    if berhasil:
        print("Registrasi berhasil! Silakan login.")
    else:
        print("Username sudah digunakan, silakan pilih username lain.")


def proses_login():
    print("\n--- LOGIN ---")
    username = input("Username: ").strip()
    password = input_password("Password: ")

    if db.cek_login(username, password):
        print(f"Login berhasil. Selamat datang, {username}!")
        return username
    else:
        print("Username atau password salah.")
        return None


def menu_utama(username):
    while True:
        tampilkan_menu(username)
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            try:
                angka = int(input("\nMasukkan angka: "))
                hasil = mymodule.cek_ganjil_genap(angka)
                print(f"Hasil: Angka {angka} adalah bilangan {hasil}.")
                db.simpan_riwayat(username, angka, "Ganjil/Genap", hasil)
            except ValueError:
                print("Input harus berupa angka bulat!")

        elif pilihan == "2":
            try:
                angka = int(input("\nMasukkan angka: "))
                is_prima = mymodule.cek_prima(angka)
                if is_prima:
                    hasil = "Prima"
                    print(f"Hasil: Angka {angka} ADALAH bilangan prima.")
                else:
                    hasil = "Bukan Prima"
                    print(f"Hasil: Angka {angka} BUKAN bilangan prima.")
                db.simpan_riwayat(username, angka, "Prima", hasil)
            except ValueError:
                print("Input harus berupa angka bulat!")

        elif pilihan == "3":
            data = db.tampilkan_riwayat(username)
            if not data:
                print("\nBelum ada riwayat.")
            else:
                print("\n=== RIWAYAT PENGECEKAN ===")
                print(f"{'ID':<4}{'Angka':<8}{'Jenis':<15}{'Hasil':<15}{'Waktu'}")
                for row in data:
                    id_, angka, jenis, hasil, waktu = row
                    print(f"{id_:<4}{angka:<8}{jenis:<15}{hasil:<15}{waktu}")

        elif pilihan == "4":
            konfirmasi = input("\nYakin ingin menghapus semua riwayat? (y/n): ")
            if konfirmasi.lower() == "y":
                db.hapus_riwayat(username)
                print("Riwayat berhasil dihapus.")

        elif pilihan == "5":
            print(f"\nSampai jumpa, {username}!")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih 1-5.")


def main():
    db.buat_tabel()  # pastikan tabel database sudah ada

    while True:
        tampilkan_menu_awal()
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            username = proses_login()
            if username:
                menu_utama(username)

        elif pilihan == "2":
            proses_register()

        elif pilihan == "3":
            print("\nTerima kasih! Program selesai.")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih 1, 2, atau 3.")


if __name__ == "__main__":
    main()