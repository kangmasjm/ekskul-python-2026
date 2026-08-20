print("=" * 40)
print("FORM PENDAFTARAN BIODATA SISWA")
print("=" * 40)
nama = input("Nama Lengkap: ")
golongan = input("Pilih Golongan (A/B/C) : ").upper()
jam = int(input("Total Jam Kerja/Minggu : "))
rating =  int(input("Rating Performa (1-5) :"))


if golongan == "A" :
    gaji = 50000
elif golongan == "B":
    gaji = 35000
elif golongan == "C":
    gaji = 25000

if rating < 1 or rating > 5:
    print("Rating harus antara 1 sampai 5!")
    exit()


bonus = 0
if rating >=4 and jam >=40:
    bonus = 200000


if jam > 40 and rating >= 4:
    gaji_lembur = 1.5 * gaji * (jam - 40)
else:
    gaji_lembur = 0

gaji_pokok = gaji * jam
total = gaji_pokok + gaji_lembur + bonus


print("=" * 40)
print(" SLIP GAJI KARYAWAN")
print("\n =" * 40)
print(f"Nama Karyawan : {nama}")
print(f"Golongan : {golongan}")
print(f"Tarif Per Jam : Rp {gaji}")
print(f"Gaji Pokok : Rp {gaji_pokok}")
print(f"Bonus Performa : Rp {bonus}")
print(f"Total Gaji yang Diterima : Rp {total}")
