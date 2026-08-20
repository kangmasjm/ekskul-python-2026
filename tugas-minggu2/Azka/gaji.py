print("=== Sistem Penghitung Gaji Karyawan SMK ===")
nama = input("masukkan Nama Karyawan: ")
golongan = input("pilih Golongan (A/B/C): ").upper()
total_jam_kerja = int(input("total Jam Kerja: "))
rating_performa = float(input("rating Performa (1 - 5): "))

A = int(50000)
B = int(35000)
C = int(25000)

if golongan == "A":
    tarif_per_jam = A * total_jam_kerja
elif golongan == "B":
    tarif_per_jam = B * total_jam_kerja
elif golongan == "C":
    tarif_per_jam = C * total_jam_kerja

if total_jam_kerja >= 40 and rating_performa >= 4:
    jam_lembur = total_jam_kerja - 40
    gaji_lembur = jam_lembur * tarif_per_jam * 1.5
    bonus_performa = tarif_per_jam * 0.1

print("\n=== slip gaji karyawan ===")
print(f"nama Karyawan: {nama}")
print(f"golongan: {golongan}")
print(f"tarif per jam: {tarif_per_jam}")
print(f"gaji pokok (40 jam kerja): {tarif_per_jam * 40}")
print(f"gaji lembur ({jam_lembur} jam): {gaji_lembur}")
print(f"bonus performa: {bonus_performa}")

print(f"Total Gaji: {tarif_per_jam * 40 + gaji_lembur + bonus_performa}")
