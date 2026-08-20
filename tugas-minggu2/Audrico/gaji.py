# angka_teks = "150"
# harga_teks = "67.67"

# angka_int = int(angka_teks)
# harga_float = float(harga_teks)

# print("---koversi ke angka---")
# print(f"nilai: {angka_int}, Tipe Data: {type(angka_int)}")
# print(f"nilai: {harga_float}, Tipe Data: {type(harga_float)}")


# umur = 25
# pesan = "Umur saya adalah " + str(umur) + " Tahun."

# print("---konversi ke string---")
# print(pesan)
# print(f"tipe data 'umur' setelah di cast: {type(str(umur))}")

# print("---Konversi ke boolean---")
# print(f"bool(1): {bool(1)}")
# print(f"bool(0): {bool(0)}")
# print(f"bool(halo): {bool('halo')}")
# print(f"bool('): {bool('')}")

nama = str(input("Masukan nama karyawan "))
golongan = str(input("masukan golongan A/B/C ")).upper()
jam_kerja = int(input("Masukan Jumlah Jam Kerja "))
rating = int(input("Masukan Rating Performa 1-5 "))
tarif_kerja = 0
if rating >= 4 and jam_kerja >= 40:
    Bonus = 200000
else:
    Bonus = "Tidak ada bonus"
if golongan == "A":
    tarif_kerja = 50000
elif golongan == "B":
    tarif_kerja = 35000
else:
    tarif_kerja = 25000
gaji_pokok = jam_kerja * tarif_kerja
lembur = jam_kerja - 40
if lembur > 0:
    gaji_lembur = lembur * int(tarif_kerja * 1.5)
else:
    gaji_lembur = "Tidak ada jam lembur"
print("-" * 30) 
print(f"Nama Karyawan : {nama}")
print(f"Golongan : {golongan}")
print(f"Tarif Per Jam : {tarif_kerja}")
print("-" * 30)
print(f"Gaji Pokok : {gaji_pokok}")
print(f"Gaji Lembur : {gaji_lembur}")
print(f"Bonus Performa: {Bonus}")
