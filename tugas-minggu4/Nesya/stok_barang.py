inventaris = [
    { "kode": "B01", "nama": "Mouse Wireless", "stok": 15, "harga": 120000 },
    { "kode": "B02", "nama": "Keyboard Mechanical", "stok": 8, "harga": 450000  }
]

print("=" * 55)
print("      SISTEM MANAJEMEN STOK BARANG TOKO SMK      ")
print("=" * 55)
print("[1] Lihat Semua Stok Barang")
print("[2] Tambah Barang Baru")
print("[3] Update Stok Barang")
print("[4] Hapus Barang Dari Inventaris")
print("=" * 55)

pilihan = input("Pilih menu (1-4): ")

#MENU 1: READ
if pilihan == "1":
    print("\n--- DAFTAR INVENTARIS BARANG ---")
    print(f"{'KODE' :<6} | {'NAMA BARANG' :<20} | {'STOK' :<5} | {'HARGA' :<12}")
    print("-" * 55)

    item1 = inventaris[0]
    item2 = inventaris[1]
    item3 = inventaris[2]

    print(f"{item1['kode']:<6} | {item1['nama']:<20} | {item1['stok']:<5} | {item1['harga']:,}")
    print(f"{item2['kode']:<6} | {item2['nama']:<20} | {item2['stok']:<5} | {item2['harga']:,}")
    print(f"{item3['kode']:<6} | {item3['nama']:<20} | {item3['stok']:<5} | {item3['harga']:,}")

elif pilihan == "2":
    print("\n--- TAMBAH BARANG BARU ---")
    kode = input("Masukkan Kode Barang (misal B03): ").upper()
    nama = input("Masukkan Nama Barang            : ")
    stok = int(input("Masukkan Jumlah Stok            : "))
    harga = int(input("Masukkan Harga Satuan (Rp)       : "))

    barang_baru = { "kode": kode, "nama": nama, "stok": stok, "harga": harga }
    inventaris.append(barang_baru)

    print(f"\n Berhasil! Barang '{nama}' dengan kode '{kode}' ditambahkan.")

elif pilihan == "3":
    print("\n--- UPDATE STOK BARANG ---")
    print(f"1. {inventaris[0]['nama']} (Stok saat ini: {inventaris[0]['stok']})")
    print(f"2. {inventaris[1]['nama']} (Stok saat ini: {inventaris[1]['stok']})")

    idx = int(input("Pilih barang yang ingin diupdate (1-2): ")) - 1
    stok_baru = int(input(f"Masukkan jumlah stok baru: "))

    inventaris[idx]['stok'] = stok_baru
    print(f"\n Stok {inventaris[idx]['nama']} berhasil diperbarui menjadi {stok_baru} unit. ")

elif pilihan == "4":
    print("\n--- HAPUS BARANG  ---")
    print(f"1. {inventaris[0]['nama']}")
    print(f"2. {inventaris[1]['nama']}")

    idx = int(input("Pilih nomor barang yang ingin dihapus (1-2): ")) - 1
    barang_dihapus = inventaris.pop(idx)
    print(f"\n Berhasil! Barang '{barang_dihapus['nama']}' berhasil dihapus dari sistem.")

else:
    print("\n Pilihan Menu Tidak Valid.")

print("=" * 55)
