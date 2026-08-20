print("=" * 40)
print("SISTEM PENGHITUNG GAJI KARYAWAN SMK")
print("=" * 40)

nama = input("Masukkan nama karyawan : ")
gol = input("Pilih Golongan (A/B/C)").upper
jam = input("Total jam kerja/minggu")
rating = input("Rating Peforma (1 - 5)")
gaji = jam * gol

if gol == "A":
    print("50.000")
elif gol == "B":
    print("35.000")
elif gol == "C":
    print("25.000")
else:
    print("Pilih Golongan A/B/C")

if jam > 40: 
    print(gaji * 1.5)
else:
    print(gaji)

print("=" * 40)
print("SLIP GAJI KARYAWAN")
print("=" * 40)

print(f"Nama Karyawan : {nama}")
print(f"Golongan : {gol}")
 # print(f"Tarif per jam : {}")

print("-" * 40)
print(f"Gaji Pokok ({jam}) : {gaji}")
