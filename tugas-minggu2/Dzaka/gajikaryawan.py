print("="*40)
print("SISTEM PENGHITUNG GAJI KARYAWAN")
print("="*40)

nama = input("Masukkan nama karyawan: ")
gol = input("Pilih Golongan (A/B/C): ")
jam = int(input("Total jam kerja/minggu: "))
rating = int(input("Rating performa(1-5): "))



if gol == "A":
    tarif = 50000
elif gol == "B":
    tarif = 35000
elif gol == "C":
    tarif = 25000

pokok = tarif * jam

if jam > 40:
    lembur = tarif * 1.5

if rating >= 4:
    bonus = 200000

print("="*40)
print("SLIP GAJI KARYAWAN")
print("="*40)

print(f"Nama karyawan: {nama}")
print(f"Golongan: {gol}")
print(f"Tari per Jam: {tarif}")
print("-"*40)
print(f"Gaji pokok ({jam} jam): {pokok}")
print(f"Gaji lembur ()")
