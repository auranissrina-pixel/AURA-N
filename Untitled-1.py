def jalankan_modul_matematika():
    # List untuk menyimpan riwayat perhitungan
    riwayat = []
    
    while True:
        print("\n" + "="*30)
        print(" KALKULATOR MATEMATIKA DASAR")
        print("="*30)
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Cek Ganjil atau Genap")
        print("5. Cek Bilangan Prima")
        print("X. Keluar")
        print("="*30)
        
        pilihan = input("Masukkan pilihan Anda (1-5 atau X): ").strip().upper()
        
        if pilihan == 'X':
            # Menampilkan riwayat sebelum keluar
            print("\n" + "="*30)
            print("      RIWAYAT PERHITUNGAN")
            print("="*30)
            if not riwayat:
                print("Tidak ada perhitungan yang dilakukan.")
            else:
                for i, catatan in enumerate(riwayat, 1):
                    print(f"{i}. {catatan}")
            print("="*30)
            print("Keluar dari program. Sampai jumpa!\n")
            break
            
        # Perhitungan yang membutuhkan dua angka
        if pilihan in ['1', '2', '3']:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == '1':
                    hasil_teks = f"{angka1} + {angka2} = {angka1 + angka2}"
                elif pilihan == '2':
                    hasil_teks = f"{angka1} - {angka2} = {angka1 - angka2}"
                elif pilihan == '3':
                    hasil_teks = f"{angka1} * {angka2} = {angka1 * angka2}"
                
                print(f"\nHasil: {hasil_teks}")
                riwayat.append(hasil_teks) # Menyimpan ke riwayat
                
            except ValueError:
                print("\nKesalahan: Harap masukkan nilai angka yang valid.")
                
        # Perhitungan yang membutuhkan satu angka bulat (integer)
        elif pilihan in ['4', '5']:
            try:
                angka = int(input("Masukkan bilangan bulat: "))
                
                if pilihan == '4':
                    status = "Genap" if angka % 2 == 0 else "Ganjil"
                    hasil_teks = f"{angka} adalah bilangan {status}."
                    
                elif pilihan == '5':
                    if angka <= 1:
                        hasil_teks = f"{angka} BUKAN bilangan prima."
                    else:
                        is_prime = True
                        for i in range(2, int(angka ** 0.5) + 1):
                            if angka % i == 0:
                                is_prime = False
                                break
                        
                        if is_prime:
                            hasil_teks = f"{angka} ADALAH bilangan prima."
                        else:
                            hasil_teks = f"{angka} BUKAN bilangan prima."
                            
                print(f"\nHasil: {hasil_teks}")
                riwayat.append(hasil_teks) # Menyimpan ke riwayat
                
            except ValueError:
                print("\nKesalahan: Harap masukkan bilangan bulat untuk operasi ini.")
                
        else:
            print("\nPilihan tidak valid. Harap masukkan angka antara 1 dan 5, atau X untuk keluar.")

if __name__ == "__main__":
    jalankan_modul_matematika()