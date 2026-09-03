inventaris=[
    {"kode": "B01", "nama": "Laptop", "stok": 10, "harga": 150000},
    {"kode": "B02", "nama": "Mouse", "stok": 25, "harga": 50000},
]

print("=" *55)
print("DAFTAR INVENTARIS")
print("=" *55)
print("[1] Lihat semua barang")
print("[2] Tambah barang")
print("[3] Ubah barang")
print("[4] Hapus barang")
print('=' *55)

pilihan = input("Masukkan pilihan (1-4): ")

if pilihan == "1":
    print("-------Daftar Barang-------")
    print(f"{'kode':<6}{'nama':<20}{'stok':<5}{'harga':<12}")

item1 = inventaris[0]
item2 = inventaris[1]

print(f"{item1['kode']:<6}{item1['nama']:<20}{item1['stok']:<5}{item1['harga']:<12}")
print(f"{item2['kode']:<6}{item2['nama']:<20}{item2['stok']:<5}{item2['harga']:<12}")


if pilihan == "2":
    print("-------Tambah Barang-------")
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    stok = int(input("Masukkan stok barang: "))
    harga = int(input("Masukkan harga barang: "))

    brang_baru = {"kode": kode, "nama": nama, "stok": stok, "harga": harga}
    inventaris.append(brang_baru)

    print(f"Berhasil menambahkan barang '{nama}' dengan kode {kode}.")
    print(f"{item1['kode']:<6}{item1['nama']:<20}{item1['stok']:<5}{item1['harga']:<12}")
    print(f"{item2['kode']:<6}{item2['nama']:<20}{item2['stok']:<5}{item2['harga']:<12}")
    print(f"{brang_baru['kode']:<6}{brang_baru['nama']:<20}{brang_baru['stok']:<5}{brang_baru['harga']:<12}")

if pilihan == "3":
    print("-------update Barang-------")
    print(f"1.{inventaris[0]['nama']} (stok saat ini: {inventaris[0]['stok']})")
    print(f"2.{inventaris[1]['nama']} (stok saat ini: {inventaris[1]['stok']})")

idx = int(input("Pilih barang yang ingin diubah (1/2): ")) - 1
stok_baru = int(input("Masukkan stok baru: "))

inventaris[idx]['stok'] = stok_baru
print(f" stok'{inventaris[idx]['nama']}' berhasil diubah menjadi {stok_baru}.")

if pilihan == "4":
    print("-------Hapus Barang-------")
    print(f"1.{inventaris[0]['nama']}")
    print(f"2.{inventaris[1]['nama']}")

idx = int(input("Pilih barang yang ingin dihapus (1/2): ")) - 1
barang_dihapus = inventaris.pop(idx)
print(f"Barang '{barang_dihapus['nama']}' berhasil dihapus dari inventaris.")