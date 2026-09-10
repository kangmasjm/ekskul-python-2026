def tampilkan_header():
    print("=" *50)
    print("SISTEM LAYANANJASA TECH-SERVICE SMK")
    print("=" *50)
    print(" Layanan yang tersedia: ")
    print(" 1. Servis Laptop(Rp. 100.000 / jam)")
    print(" 2. install Network(Rp. 75.000 / jam)")
    print(" 3. Desain Grafis(Rp. 50.000 / jam)")
    print("=" *50)
    
    def hitung_biaya_layanan(pilihan_layanan, durasi_jam):
        """Menghitung biaya layanan berdasarkan pilihan layanan dan durasi """
        if pilihan_layanan == 1:
            biaya = durasi_jam * 100000
        elif pilihan_layanan == 2:
            biaya = durasi_jam * 75000
        elif pilihan_layanan == 3:
            biaya = durasi_jam * 50000
        else:
            biaya = 0
        return biaya
    
    def cetak_nota(nama_pelanggan, nama_layanan, durasi_jam, total_biaya):
        """Mencetak nota transaksi resmi"""
        print("\n" + "=" *50)
        print("NOTA TRANSAKSI")
        print("=" *50)
        print(f"Nama Pelanggan  : {nama_pelanggan}")
        print(f"Nama Layanan    : {nama_layanan}")
        print(f"Durasi          : {durasi_jam}")
        print(f"Biaya           : Rp. {total_biaya:,.0f}")
        print("=" *50)
        
        
    def main():
        tampilkan_header()
        nama = input("Masukan Nama Pelanggan: ")
        pilihan = int(input("Plih Layanan (1/2/3)"))
        durasi_raw = input("Masukan Durasi Layanan (jam)") 
        
        if durasi_raw.isdigit():
            durasi = int(durasi_raw)
            
            daftar_layanan ={1: "Service Laptop", 2: "Install Network", 3: "Desain Grafis"}
            
            if pilihan in daftar_layanan:
            nama_layanan = daftar_layanan[pilihan] 
            
            total = hitung_biaya_layanan
            
            cetak_nota(nama, nama_layanan, durasi, total)
        else:
            print("\n""X  Pilihan layanan tidak valid")
    else:
        print("\n" "Durasi layanan harus berupa angka")
        
        
        main()
