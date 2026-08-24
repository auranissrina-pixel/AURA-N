while True:
    angka = input("Masukkan sebuah angka tekan \"q\" untuk keluar: ")
    
    if angka == "q":
        break

    angka = int(angka)

    if angka % 2 == 0:
        print(f"Angka {angka} adalah bilangan GENAP.")
    else:
        print(f"Angka {angka} adalah bilangan GANJIL.")

