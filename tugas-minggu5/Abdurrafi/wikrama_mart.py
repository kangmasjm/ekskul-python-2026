keranjang = []

print("=" * 52)
print("             SISTEM KASIR WIKRAMA MART            ")
print("=" * 52)

while True:
    print("\n--- TAMBAH BARANG BELANJAAN ---")
    nama_barang = input("Nama barang (ketik 'selesai' untuk bayar): ").strip()

    if nama_barang.lower() == "selesai":
        break

    harga_raw = input("Harga satuan (Rp) : ")
    jumlah_raw = input("Jumlah barang     : ")

    if harga_raw.isdigit() and jumlah_raw.isdigit():
        harga = int(harga_raw)
        jumlah = int(jumlah_raw)

        if harga > 0 and jumlah > 0:
            keranjang.append({
                "nama": nama_barang,
                "harga": harga,
                "jumlah": jumlah
            })
            print(f"✓ '{nama_barang}' ({jumlah} pcs) berhasil ditambahkan.")
        else:
            print("Error: Harga dan jumlah harus lebih dari 0!")
    else:
        print("Error: Harga dan jumlah harus berupa angka positif!")

print("\n" + "=" * 52)
print("                   STRUK BELANJA                  ")
print("=" * 52)

if len(keranjang) == 0:
    print("Tidak ada barang dibeli. Transaksi dibatalkan.")
else:
    print(f"{'BARANG':<18} | {'QTY':<4} | {'HARGA':<11} | {'TOTAL':<11}")
    print("-" * 52)

    total_belanja = 0

    for item in keranjang:
        subtotal = item["harga"] * item["jumlah"]
        total_belanja += subtotal

        harga_fmt = f"Rp {item['harga']:,}".replace(",", ".")
        subtotal_fmt = f"Rp {subtotal:,}".replace(",", ".")

        print(f"{item['nama']:<18} | {item['jumlah']:<4} | {harga_fmt:<11} | {subtotal_fmt:<11}")

    total_fmt = f"Rp {total_belanja:,}".replace(",", ".")

    print("-" * 52)
    print(f"TOTAL BAYAR : {total_fmt}")
    print("=" * 52)
    print("       Terima kasih telah berbelanja di WIKRAMA MART     ")