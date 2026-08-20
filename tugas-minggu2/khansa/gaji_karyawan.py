print("=" * 40)
print("SISTEM PENGHITUNG GAJI KARYAWAN SMK")
print("=" * 40)

nama = input("Masukkan Nama Karyawan: ")
gol = input("Masukkan Golongan (A/B/C): ").upper()
jam = int(input("Total Jam Kerja/Minggu: "))
rate = int(input("Rating Performa (1-5): "))

if gol == "A":
    gaji_pokok = 50000
elif gol == "B":
    gaji_pokok = 35000
elif gol == "C":
    gaji_pokok = 25000
else:
    print("Golongan tidak valid!")
    exit()

if rate < 1 or rate > 5:
    print("Rating harus antara 1 sampai 5!")
    exit()

# Menghitung lembur
if jam > 40:
    jam_lembur = jam - 40
else:
    jam_lembur = 0

if jam_lembur > 0 and rate >= 4:
    gaji_lembur = 1.5 * gaji_pokok * jam_lembur
else:
    gaji_lembur = 0


total_gaji = gaji_pokok * 40 + gaji_lembur

print("=" * 40)
print(f"Nama Karyawan          : {nama}")
print(f"Golongan               : {gol}")
print(f"Total Jam Kerja/Minggu : {jam}")
print(f"Rating Performa        : {rate}")
print(f"Gaji Per Jam           : Rp {gaji_pokok: }")
print(f"Jam Lembur             : {jam_lembur} jam")
print(f"Gaji Lembur            : Rp {gaji_lembur: }")
print(f"Total Gaji             : Rp {total_gaji: }")
print("=" * 40)

