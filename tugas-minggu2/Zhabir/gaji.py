print("="*40)
print("     SISTEM PENGHITUNG GAJI KARYAWAN SMK")
print("="*40)

nama = input("Masukkan Nama Karyawan: ")
golongan = input("Pilih Golongan (A/B/C): ")
jamk = int(input("Total jam kerja/minggu: "))
perform = int(input("Rating Performa (1 - 5): "))

print("="*40)
print("     SLIP GAJI KARYAWAN")
print("="*40)

if golongan == "A":
    tarif = 50000
elif golongan == "B":
    tarif = 35000
elif golongan == "C":
    tarif = 25000
else:
    print("Pilih Golongan (A/B/C): ")    

if jamk > 40:
    lembur = tarif*1.5

if perform >= 40:
    bonus = 200000

print(f"Nama Karyawan: {nama}")
print(f"Golongan: {golongan}")
print(f"Total Jam Kerja: {jamk}")
print(f"Rating: {perform}")
