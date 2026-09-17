def tampilkan_header():
    print("=" * 50)
    print("         SISTEM LAYANAN JASA TECH-SERVICE SMK         ")
    print("=" * 50)
    print("Layanan yang tersedia :")
    print("1. Service Laptop (Rp 100.000 / jam)")
    print("2. Install Network (Rp 75.000 / jam)")
    print("3. Desain  Grafis (Rp 50.000 / jam)")
    print("=" * 50)

def hitung_biaya_layanan(pilihan_layanan, durasi_jam):
    if pilihan_layanan == 1:
        tarif_per_jam = 100000
    elif pilihan_layanan == 2:
        tarif_per_jam = 75000
    elif pilihan_layanan == 3:
        tarif_per_jam = 50000
    else:
        tarif_per_jam = 0
    return tarif_per_jam * durasi_jam

def cetak_nota(nama_pelanggan, nama_layanan, durasi, total_biaya):
    print("\n" + "=" * 50)
    print("         NOTA TRANSSAKSI         ")
    print("=" * 50)
    print(f"Nama Pelanggan  : {nama_pelanggan}")
    print(f"Layanan         : {nama_layanan}")
    print(f"Durasi          : {durasi} jam")
    print(f"Total Biaya     : Rp {total_biaya:,.0f}")
    print("=" * 50)
    print("Terimakasih telah menggunakan layanan kami!")

def main():
    tampilkan_header()

    nama = input("Masukkan Nama Pelanggan : ")
    pilihan = int(input("Pilih layanan (1/2/3) : "))
    durasi_raw = input("Masukkan Durasi Layanan (jam) : ")

    if durasi_raw.isdigit():
        durasi = int(durasi_raw)

        daftar_layanan = {1: "Service Laptop", 2: "Install Network", 3:"Desain Grafis"}

        if pilihan in daftar_layanan:
            nama_layanan = daftar_layanan[pilihan]
            total = hitung_biaya_layanan(pilihan, durasi)
            cetak_nota(nama, nama_layanan, durasi, total)

        else:
            print("\n Pilihan layanan tidak valid!")
    else:
        print("\n Durasi layanan harus berupa angka!")

main()