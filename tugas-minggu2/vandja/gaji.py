print("=" * 40)
print("SISTEM PENGHITUNG GAJI KARYAWAN SMK")
print("=" * 40)

nama = input("Masukkan nama karyawan : ")
golDarah = input("Pilih Golongan (A/B/C)").upper
jamKerja = input("Total jam kerja/minggu")
rate = input("Rating Peforma (1 - 5)")
gaji = jamKerja * golDarah

if golDarah == "A":
    print("50.000")
elif golDarah == "B":
    print("35.000")
elif golDarah == "C":
    print("25.000")
else:
    print("Pilih Golongan A/B/C")

if jamKerja > 40: 
    print(gaji * 1.5)
else:
    print(gaji)

print("=" * 40)
print("SLIP GAJI KARYAWAN")
print("=" * 40)

print(f"Nama Karyawan : {nama}")
print(f"Golongan : {golDarah}")

print("-" * 40)
print(f"Gaji Pokok ({jamKerja}) : {gaji}")
