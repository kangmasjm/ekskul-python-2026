inventaris = [
    {"kode": "BRG01", "nama": "Buku Tulis", "stok": 50, "harga": 5000},
    {"kode": "BRG02", "nama": "Pensil 2B", "stok": 100, "harga": 2000}
]

print("=" * 55) 
print(" Sistem Manajemen Stok Barang Toko ") 
print("=" * 55) 
print("[1] Lihat Semua Stok Barang") 
print("[2] Tambah Barang Baru") 
print("[3] Update Stok Barang") 
print("[4] Hapus Barang dari Inventaris") 
print("=" * 55) 

pilihan = input("Pilih Menu (1-4): ") 

if pilihan == "1": 
    print("\n--DAFTAR INVENTARIS BARANG--") 
    print(f"{'KODE':<6} | {'NAMA BARANG':<20} | {'STOK':<6} | {'HARGA':<12}") 
    print("-" * 55) 
    
    item1 = inventaris[0] 
    item2 = inventaris[1] 
    print(f"{item1['kode']:<6} | {item1['nama']:<20} | {item1['stok']:<6} | {item1['harga']:<12}") 
    print(f"{item2['kode']:<6} | {item2['nama']:<20} | {item2['stok']:<6} | {item2['harga']:<12}") 

elif pilihan == "2": 
    print("\n--TAMBAH BARANG BARU--") 
    kode = input("Masukkan Kode Barang : ").upper() 
    nama = input("Masukkan Nama Barang : ") 
    stok = int(input("Masukkan Stok Barang : ")) 
    harga = int(input("Masukkan Harga Barang : ")) 
    
    barang_baru = {"kode": kode, "nama": nama, "stok": stok, "harga": harga} 
    inventaris.append(barang_baru)
    
    print(f"\nBerhasil menambahkan barang baru: {nama} dengan kode {kode}.") 
            
            item1 = inventaris[0] 
            item2 = inventaris[1] 
            item3 = inventaris[2]
            print(f"{item1['kode']:<6} | {item1['nama']:<20} | {item1['stok']:<6} | {item1['harga']:<12}") 
            print(f"{item2['kode']:<6} | {item2['nama']:<20} | {item2['stok']:<6} | {item2['harga']:<12}") 
            print(f"{item3['kode']:<6} | {item3['nama']:<20} | {item3['stok']:<6} | {item3['harga']:<12}")
            

elif pilihan == "3": 
    print("\n--UPDATE STOK BARANG--") 
    print(f"1. {inventaris[0]['nama']} (Kode: {inventaris[0]['kode']})") 
    print(f"2. {inventaris[1]['nama']} (Kode: {inventaris[1]['kode']})") 
    
    idx = int(input("Pilih barang yang ingin diupdate (1-2): ")) - 1 
    stok_baru = int(input(f"Masukkan stok baru untuk {inventaris[idx]['nama']}: ")) 
    
    inventaris[idx]['stok'] = stok_baru 
    print(f"\nBerhasil mengupdate stok barang {inventaris[idx]['nama']} menjadi {stok_baru} unit.") 

elif pilihan == "4": 
    print("\n--HAPUS BARANG DARI INVENTARIS--") 
    print(f"1. {inventaris[0]['nama']}") 
    print(f"2. {inventaris[1]['nama']}") 
    
    idx = int(input("Pilih barang yang ingin dihapus (1-2): ")) - 1 
    barang_dihapus = inventaris.pop(idx) 
    print(f"\nBerhasil menghapus barang {barang_dihapus['nama']} dari inventaris.") 

else: 
    print("\nPilihan menu tidak valid!") 

print("=" * 55)
stok
