print("=== PROGRAM CEK GANJIL / GENAP ===")

try:
    angka = int(input("Masukkan sebuah angka: "))

    if angka % 2 == 0:
        print(f"Angka {angka} adalah bilangan GENAP.")
    else:
        print(f"Angka {angka} adalah bilangan GANJIL.")

except ValueError:
    print("[Kesalahan] Harap masukkan angka bulat yang valid!")