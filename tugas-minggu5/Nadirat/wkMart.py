# belanja di wikrama mart

# array keranjang
keranjang = []

print("=* 30")
print("SISTEM KASIH WEKA MART")
print("=* 30")

# jalanin program
while True:
    print("\n--- TAMBAH BARANG BELANJAAN ---")
    nama_barang = input("Nama barang (selesai)")

    # kondisi keluar loop
    if nama_barang.lower() == "selesai":
        break
    harga_raw = input("Harga satuan (Rp): ")
    jumlah_raw = input("Jumbah barang nya: ")

    # validasi input numerik
    if harga_raw.isdigit() and jumlah_raw.isdigit():
        harga = int(harga_raw)
        jumlah = int(jumlah_raw)

        # tambah item ke keranjang
        keranjang.append({
            "nama": nama_barang,
            "harga": harga,
            "jumlah": jumlah
        })
        print (f" '{nama_barang}' ({jumlah} pcs) berhasil ditambahkan")
    else:
        print("Error: Harga sama jumlah harus berupa angka")

        # 2. proses cetak struk
    if len(keranjang) == 0:
        print("\n Tidak ada barang dibeli, Transaksi batal")
    else:
        print("\n" + "=" * 50)
        print("STRUK BELANJAAN")
        print("=" * 50)
        print(f"{'BARANG':<18} | {'QTY':<4} | {'HARGA':<9} | {'TOTAL':<10}")
        print("-" * 50)

        total_belanja = 0

        # loop untuk membaca keranjang & menghitung total
        for item in keranjang:
            subtotal = item["harga"] * item["jumlah"]
            total_belanja += subtotal

            print(f"{item['nama']:<18} | {item['jumlah']:<4} | {item['harga']:<9,} | Rp {subtotal:<10,}")

            print("-" * 50)
            print(f"TOTAL PAYABLE : Rp {total_belanja:,}")
            print("=" * 50)
            print("     Terima kasih telah belanja di wekamart      ")