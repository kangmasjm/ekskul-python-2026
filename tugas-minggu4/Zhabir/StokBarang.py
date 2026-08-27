# 1. Inisialisasi Data Awal (List of Dictionaries)
inventaris = [
    {"kode": "B01", "nama": "Mouse Wireless", "stok": 15, "harga": 120000},
    {"kode": "B02", "nama": "Keyboard Mechanical", "stok": 8, "harga": 450000},
]

print("=" * 55)
print("     SISTEM MANAJEMEN STOK BARANG TOKO SMK       ")
print("=" * 55)
print("[1] Lihat Semua Stok Barang")
print("[2] Tambah Barang Baru")
print("[3] Update Stok Barang")
print("[4] Hapus Barang di Inventaris")
print("=" * 55)

pilihan = input("Pilihan menu(1-4): ")

# - - - MENU 1: READ - - -
if pilihan == "1":
    print("\n--- DAFTAR INVENTARUS BARANG ---")
    print(f"{'KODE':<6} | {'NAMA BARANG':<20} | {'STOK':<5} | {'HARGA':<12}")
    print("=" * 52)

    # Membaca list satu per satu
    item1 = inventaris[0]
    item2 = inventaris[1]

    print(f"{item1['kode']:<6} | {item1['nama']:<20} | {item1['stok']:<5} | Rp {item1['harga']:,}")
    print(f"{item2['kode']:<6} | {item2['nama']:<20} | {item2['stok']:<5} | Rp {item2['harga']:,}")

# - - - MENU 2: CREATE - - -
elif pilihan == "2":
    print("\n--- TAMBAH BARANG BARU ---")
    kode = input("Masukkan Kode Barang (misal B03):").upper()
    nama = input("Masukkan Nama Barang      : ")
    stok = int(input("Masukkan Jumlah Stok      : "))
    harga = int(input("Masukkan Harga Satuan(Rp)        : "))

    # Membuat dictonary baru
    barang_baru = {"kode": kode, "nama": nama, "stok": stok, "harga": harga}

    # Tambah ke list inventaris
    inventaris.append(barang_baru)

    print(f"\n✅Berhasil! Barang '{nama}' dengan kode '{kode}' ditambahkan.")

    item1 = inventaris[0]
    item2 = inventaris[1]
    item3 = inventaris[2]
    
    print(f"{item1['kode']:<6} | {item1['nama']:<20} | {item1['stok']:<5} | Rp {item1['harga']:,}")
    print(f"{item2['kode']:<6} | {item2['nama']:<20} | {item2['stok']:<5} | Rp {item2['harga']:,}")
    print(f"{item3['kode']:<6} | {item3['nama']:<20} | {item3['stok']:<5} | Rp {item3['harga']:,}")
    

# - - - MENU 3: UPDATE - - - 
elif pilihan == "3":
    print("\n--- UPDATE STOK BARANG ---")
    print(f"1. {inventaris[0]['nama']} (Stok Saat Ini: {inventaris[0]['stok']})")
    print(f"2. {inventaris[1]['nama']} (Stok Saat Ini: {inventaris[1]['stok']})")

    idx = int(input("Pilih nomor barang yang ingin di-update (1/2): ")) -1
    barang_dihapus = inventaris.pop(idx)
    print(f"\n Barang '{barang_dihapus['nama']}' berhasil dihapus dari sistem.")


else:
    print("\n Pilihan menu tidak valid!")
print("=" * 55)
