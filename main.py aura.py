import ganjilgenap

while True:
    angka_input = input("Masukkan sebuah angka (tekan 'q' untuk keluar): ")
    
    if angka_input.lower() == "q":
        break
        
    angka_int = int(angka_input)
    hasil = ganjilgenap.cek_ganjil_genap(angka_int)
    print(hasil)