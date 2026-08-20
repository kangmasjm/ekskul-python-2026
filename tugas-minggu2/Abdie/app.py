# # Cast A

# angka_teks = "150"
# harga_teks = "99.50"

# angka_int = int(angka_teks)
# harga_float = float(harga_teks)

# print ("Konversi ke angka")
# print (f"Nilai : {angka_int}, tipe data {type(angka_int)}")
# print (f"Nilai : {harga_float}, tipe data {type(harga_float)}")

# # Cast B
# umur = 25 
# pesan = "umur saya adalah " + str(umur) + " tahun"

# print("\n konversi data")
# print(pesan)
# print(f"tipe data 'umur' setelah di cast: {type (str(umur))} ")

# # Cast C

# print("\n Konversi Boolean")
# print(f"bool(1): {bool(1)}")
# print(f"bool(0): {bool(0)}")
# print(f"bool(halo): {bool("halo")}")
# print(f"bool(): {bool('')}")


# gaji gweh

nama = input("Masukan nama anda: ")
Golongan = input("Pilih golongan (A/B/C): ").upper()
Total_jam = input("Total jam kerja: ")
Rating = input("Rating perfoma: ")
jamkerja = 40

Tarif = Golongan

lembur = jamkerja * 1.5

if (Golongan == "A"):
    print(500000)
elif(Golongan == "B"):
    print(350000)
elif(Golongan == "C"):
    print(25000)
else:
    print("Golongan tidak sesuai")
    

print(f"Nama {nama}")
print(f"Golongan {Golongan}")
print(f"Tarif {Tarif}")