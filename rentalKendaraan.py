kendaraan = []
run = True

while run:
    print("\n=== SISTEM RENTAL KENDARAAN ===")
    print("1. Tampilkan daftar kendaraan")
    print("2. Tambah kendaraan")
    print("3. Sewa kendaraan")
    print("4. Kembalikan kendaraan")
    print("5. Laporan pendapatan")
    print("6. Hapus kendaraan")
    print("7. Keluar")
    pilihan = input("Pilih menu (1-7): ").strip()

    if pilihan == "1":
        if len(kendaraan) == 0:
            print("Belum ada kendaraan.")
        else: 
            print("\nDaftar Kendaraan: ")
            for i in range(len(kendaraan)):
                data = kendaraan[i] 
                tarif = f"{data[1]:,}".replace(",",".")
                if data[2]:
                    print(f"{i + 1}. {data[0]} | Rp{tarif}/hari | Disewa | Penyewa: {data[3]} | Lama: {data[4]} hari")
                else:
                    print(f"{i + 1}. {data[0]} | Rp{tarif}/hari | Tersedia | Penyewa: - | Lama: -")
    
    elif pilihan == "2":
        nama = input("Nama kendaraan: ").strip()
        if nama == "":
            print("Nama kendaraan tidka boleh kosong.")
        else:
            tarif = input("Tarif per hari (Rp): ").strip()
            if not tarif.isdigit():
                print("Tarif harus berupa angka.")
            elif int(tarif) < 100000:
                print("Tarif minimal Rp100.000.")
            else:
                kendaraan.append([nama, int(tarif), False, "", 0])
                print("Kendaraan berhasil ditambahkan.")
    
    elif pilihan == "3":
        tersedia = []
        for i in range(len(kendaraan)):
            if not kendaraan[i][2]:
                tersedia.append(i)
        
        if len(tersedia) == 0:
            print("Tidak ada kendaraan yang tersedia.")
        else:
            print("\nKendaraan Tersedia.")
            for n in range(len(tersedia)):
                data = kendaraan[tersedia[n]]
                tarif = f"{data[1]:,}".replace(",", ".")
                print(f"{n + 1}. {data[0]} | Rp{tarif}/hari")
        
            pilih = input("Pilihan nomor kendaraan: ").strip()
            if not pilihan.isdigit() or int(pilih) < 1 or int(pilih) > len (tersedia):
                print("Pilihan tidak valid.")
            else:
                idx = tersedia[int(pilih) - 1]
                penyewa = input("Nama penyewa: ").strip()
                lama = input("Lama sewa (hari): ").strip()

                if penyewa == "":
                    print("Nama penyewa tidak boleh kosong.")
                elif not lama.isdigit() or int(lama) < 1:
                    print("Lama sewa harus angka minimal 1 hari.")
                else: 
                    lama = int(lama)
                    total = kendaraan[idx][1] * lama
                    if lama >= 7:
                        total = total * 0.10
                        print("Selamat, Anda mendapat diskon 10%.")
                    kendaraan[idx][2] = True
                    kendaraan[idx][3] = penyewa
                    kendaraan[idx][4] = lama
                    total_teks = f"{total:,.0f}".replace(",", ".")
                    print(f"Sewa berhasil. Total biaya: Rp{total_teks}")
    
    elif pilihan == "4":
        rent = []
        for i in range(len(kendaraan)):
            if kendaraan[i][2]:
                rent.append(i)
        
        if len(rent) == 0:
            print("Tidak ada kendaraan yang sedang disewa.")
        else:
            print("\nKendaraan Sedang Disewa.")
            for n in range(len(rent)):
                data = kendaraan[rent[n]]
                print(f"{n + 1}. {data[0]} | Penyewa: {data[3]} | Lama: {data[4]} hari")

            pilih = input("Pilih nomor kendaraan yang dikembalikan: ").strip()
            if not pilih.isdigit() or int(pilih) < 1 or int(pilih) > len(rent):
                print("Pilihan tidak valid.")
            else:
                idx = rent[int(pilih) - 1]
                kendaraan[idx][2] = False
                kendaraan[idx][3] = ""
                kendaraan[idx][4] = 0
                print("Kendaraan berhasil dikembalikan.")
    
    elif pilihan == "5": 
        total_pendapatan = 0
        jumlah_disewa = 0
        jumlah_tersedia = 0

        for data in kendaraan:
            if data[2]:
                biaya = data[1] * data[4]
                if data[4] >= 7:
                    biaya = biaya * 0.10
                total_pendapatan = total_pendapatan + biaya
                jumlah_disewa = jumlah_disewa + 1
            else:
                jumlah_tersedia = jumlah_tersedia + 1
        
        if jumlah_disewa > 0:
            avg = total_pendapatan / jumlah_disewa
        else:
            avg = 0
        
        total_teks = f"{total_pendapatan:,.0f}".replace(",", ".")
        rata_teks = f"{avg:,.0f}".replace(",", ".")
        print("\n=== LAPORAN PENDAPATAN ===")
        print(f"Total pendapatan (kendaraan disewa): Rp{total_teks}")
        print(f"Rata-rata pendapatan per kendaraan disewa: Rp{rata_teks}")
        print(f"Jumlah kendaraan disewa: {jumlah_disewa}")
        print(f"Jumlah kendaraan tersedia: {jumlah_tersedia}")

    elif pilihan == "6":
        if len(kendaraan) == 0:
            print("Belum ada kendaraan.")
        else:
            print("\nDaftar Kendaraan:")
            for i in range(len(kendaraan)):
                if kendaraan[i][2]:
                    status = "Disewa"
                else:
                    status = "Tersedia"
                print(f"{i + 1}. {kendaraan[i][0]} | {status}")

            pilihan = input("Pilih nomor kendaraan yang dihapus: ").strip()
            if not pilih.isdigit or int(pilih) < 1 or int(pilih) > len(kendaraan):
                print("Pilihan tidak valid.")
            else:
                idx = int(pilih) - 1
                if kendaraan[idx][2]:
                    print("Kendaraan yang sedang disewa tidak boleh dihapus.")
                else:
                    konfirmasi = input(f"Yakin hapus {kendaraan[idx][0]}? (y/n): ").strip().lower()
                    if konfirmasi == "y":
                        kendaraan.pop(idx)
                        print("Kendaraan berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")

    elif pilihan == "7":
        print("Terima kasih.")
        run = False

    else:
        print("Menu tidak valid. Pilih 1-7.")