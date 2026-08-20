print("=" * 40)
print("FORM PENDAFTARAN BIODATA SISWA")
print("=" * 40)
nama = input("Nama Lengkap: ")
golongan = input("Pilih Golongan (A/B/C) : ").parse
jam = input("Total Jam Kerja/Minggu : ")
rating =  input("Rating Performa (1-5) :")

gaji_pokok = 0
if golongan == "A" :
    gaji_pokok = 50000
elif golongan == "B":
    gaji_pokok = 35000
elif golongan == "C":
    gaji_pokok = 25000

jam_lembur = 0
if jam > 40:
    jam_lembur = gaji_pokok * 1.5

bonus = 0
if rating >=4 and jam >=40:
    bonus = 200000

total = (gaji_pokok * jam) + jam_lembur + bonus


print("=" * 40)
print("\n SLIP GAJI KARYAWAN")
print("\n =" * 40)
print(f"Nama Karyawan : {nama}")
print(f"Golongan : {golongan}")
print(f"Tarif Per Jam : Rp {gaji_pokok}")
print(f"Gaji Pokok : Rp {gaji_pokok}")
print(f"Gaji Lembur : Rp {bonus}")
print(f"Bonus Performa : Rp {bonus}")
print(f"Total Gaji yang Diterima : Rp {total}")
