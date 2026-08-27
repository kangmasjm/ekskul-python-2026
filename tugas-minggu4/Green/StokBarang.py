# SISTEM MANAJEMEN BARANG PAKAI CLI 

# 1. Inisiasi data awal (list of disctionaries)
inventaris = [
    {"kode" : "B01", "nama": "Mouse Wireless", "stok" : 15, "harga" : 120000},
    {"kode" : "B02", "nama": "Keyboard Mechanical", "stok" : 8, "harga" : 450000}
]


print("=" * 55)
print("         SISTEM MANAJEMEN STOK BARANG TOKO SMK       ")
print("=" * 55)
print("[1] Lihat Semua Stok Barang")
print("[2] Tambah Stok Barang Baru")
print("[3] Update Stok Barang")
print("[4] Hapus Barang dari Inventaris")
print("=" * 55)

pilihan = input("Pilih menu (1-4): ")

# MENU 1 READ
if pilihan == "1":
    print("\n--- DAFTAR INVENTARIS BARANG ---")
    print(f"{'KODE':<6} | {'NAMA BARANG':<20} | {'STOK':<5} | {'HARGA':<12}")
    print("-" * 52)

    # Membaca List satu persatu
    item1 = inventaris[0]
    item2 = inventaris[1]

    print(f"{item1['kode']:<6} | {item1['nama']:<20} | {item1['stok']:<5} | Rp {item1['harga']:,}")
    print(f"{item2['kode']:<6} | {item2['nama']:<20} | {item2['stok']:<5} | Rp {item2['harga']:,}")

# READ
elif pilihan == "2":
    print("TAMBAH BARANG BARU")
    kode = input("Masukan Kode Barang: ").upper()
    nama = input("Masukan Nama Barang: ")
    stok = int(input("Masukan Jumlah Stok: "))
    harga = int(input("Masukan Harga Satuan(Rp): "))

    # Mambuat dictionary baru
    barang_baru = {"kode": kode, "nama": nama, "stok": stok, "harga": harga}

    #tambah list ke inventaris
    inventaris.append(barang_baru)

    item1 = inventaris[0]
    item2 = inventaris[1]
    item3 = inventaris[2]

    print(f"{item1['kode']:<6} | {item1['nama']:<20} | {item1['stok']:<5} | Rp {item1['harga']:,}")
    print(f"{item2['kode']:<6} | {item2['nama']:<20} | {item2['stok']:<5} | Rp {item2['harga']:,}")
    print(f"{item3['kode']:<6} | {item3['nama']:<20} | {item3['stok']:<5} | Rp {item3['harga']:,}")
    print("\n Berhasil!")

# UPDATE
elif pilihan == "3":
    print("\n --- UPDATE STOK BARANG ---")
    print(f"1. {inventaris[0]['nama']} (Stok Saat ini: {inventaris[0]['stok']})")
    print(f"2. {inventaris[1]['nama']} (Stok Saat ini: {inventaris[1]['stok']})")

    idx = int(input("Pilih nomor barang yang ingin di update(1/2): "))
    stok_baru = int(input("Masukan jumlah stok terbaru: "))

    # Update Stock
    inventaris[idx]["stok"] = stok_baru
    print(f"\n Stok '{inventaris[idx]['nama']}' BERHASIL DIPERBARUI menjadi {stok_baru}")

# DELETE
elif pilihan == "4":
    print('\n --- HAPUS BARANG ---')
    print(f"1. {inventaris[0]['nama']}")
    print(f"2. {inventaris[1]['nama']}")

    idx = int(input("Pilih nomor barang yang ingin dihapus: "))
    barang_dihapus = inventaris.pop(idx)

    print("\n Barang '{barang_dihapus['nama']}' berhasil dihapus dari sistem.")

else:
    print("\n Pilihan menu tidak valid")

print("=" * 55)
