def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    return "Ganjil"

def cek_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

nomor = 17
print(f"Angka {nomor} adalah bilangan {cek_ganjil_genap(nomor)}.")





if cek_prima(nomor):
    print(f"Angka {nomor} ADALAH bilangan prima.")
else:
    print(f"Angka {nomor} BUKAN bilangan prima.")