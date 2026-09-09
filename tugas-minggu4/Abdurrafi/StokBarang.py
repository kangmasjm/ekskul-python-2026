inventaris = [
    {"kode": "001", "nama": "Mouse Wireless", "stok": 15, "harga": 120000},
    {"kode": "002", "nama": "Keyboard Mechanical", "stok": 8, "harga": 450000},
    {"kode": "003", "nama": "Monitor LED", "stok": 5, "harga": 800000}
]



print("=" * 55)
print("=== SISTEM MANAJEMEN STOK BARANG TOKO SMK ===")
print("=" * 55)
print("[1] Lihat Semua Stok Barang")
print("[2] Tambah Barang Baru")
print("[3] Update Stok Barang")
print("[4] Hapus Barang dari Inventaris")
print("=" * 55)

pilihan = input("Pilih menu (1-4): ")

# --- MENU 1: READ ---
if pilihan == "1":
    print("\n=== DAFTAR INVENTARIS BARANG ===")
    print(f"{'KODE':<6} | {'NAMA BARANG':<20} | {'STOK':<5} | {'HARGA':<12}")
    print("-" * 52)

    # Membaca list satu per satu 
    item1 = inventaris[0]
    item2 = inventaris[1]
    item3 = inventaris[2]

    for item in inventaris:
        print(f"{item['kode']:<6} | {item['nama']:<20} | {item['stok']:<5} | Rp {item['harga']:,}")

# --- MENU 2: CREATE ---
elif pilihan == "2":
    print("\n=== TAMBAH BARANG BARU ===")
    kode = input("Masukkan Kode Barang (Misal: 003): ").upper()
    nama = input("Masukkan Nama Barang: ")
    stok = int(input("Masukkan Jumlah Stok: "))
    harga = int(input("Masukkan Harga Satuan (Rp) : "))

    # Membuat dictionary baru
    barang_baru = {"kode": kode, "nama": nama, "stok": stok, "harga": harga}

    # Tambah ke list inventaris
    inventaris.append(barang_baru)

    print(f"\n✅ Berhasil! Barang '{nama}' dengan kode {kode} ditambahkan.")

# --- MENU 3: UPDATE ---
elif pilihan == "3":
    print("\n=== UPDATE STOK BARANG ===")
    for idx, item in enumerate(inventaris):
        print(f"{idx + 1}. {item['nama']} (Stok Saat Ini: {item['stok']})")

    idx = int(input("Pilih nomor barang yang ingin di-update (1/2/3): ")) - 1
    stok_baru = int(input(f"Masukkan jumlah stok terbaru: "))

    # Update stok
    inventaris[idx]['stok'] = stok_baru
    print(f"\n✅ Stok '{inventaris[idx]['nama']}' berhasil diperbarui menjadi {stok_baru} unit.")

# --- MENU 4: DELETE ---
elif pilihan == "4":
    print("\n=== HAPUS BARANG ===")
    for idx, item in enumerate(inventaris):
        print(f"{idx + 1}. {item['nama']}")
    print(f"2. {inventaris[1]['nama']}")
    print(f"3. {inventaris[2]['nama']}")

    idx = int(input("Pilih nomor barang yang ingin dihapus (1/2/3): ")) - 1
    barang_dihapus = inventaris.pop(idx)

    print(f"\n🗑️ Barang '{barang_dihapus['nama']}' berhasil dihapus dari sistem.")

else:
    print("\n❌ Pilihan menu tidak valid!")

print("=" * 55)
