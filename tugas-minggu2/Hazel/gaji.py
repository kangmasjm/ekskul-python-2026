print("=" * 30)
print("Sistem Penghitung Gaji Karyawan SMK")
print("=" * 30)


nama = input("Masukkan Nama Karyawan : ")
golongan = input("Pilih Golongan (A/B/C) : ")
jam_kerja = input("Total Jam Kerja/Minggu : ")
rating = input("Rating Performa (1 - 5) : ") 

if gol == "A":
    tarif = 50.000
elif gol == "B":
    tarif == 35.000
elif gol == "C":
    tarif == 20.000

total_kerja = jam_kerja * 1.5


if (total_kerja >= 40):
    print()

print("=" * 30)
print("SLIP GAJI KARYAWAN")
print("=" * 30)

print(f"Nama Karyawan        : {nama}")
print(f"Golongan             : {golongan}")
print(f"Tarif Per Jam        : {jam_kerja}")

print("-" * 30)

print(f"Gaji Pokok (40 Jam)        : {total_kerja}")
print(f"Cita - Cita                : {cita_cita}")