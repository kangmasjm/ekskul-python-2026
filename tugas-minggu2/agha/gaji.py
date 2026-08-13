print("="*50)
print("SISTEM PENGHITUNG GAJI KARYAWAN")
print("="*50)

nama = input(f"Masukkan Nama Anda : ")
golongan = input(f"Masukkan Golongan Anda A/B/C: ".upper())
total_jam_kerja = int(input(f"Masukkan Total Jam Kerja Anda : "))
rating = int(input(f"Masukkan Rating Anda (1-5): "))

print("="*50)
print("SlIP GAJI KARYAWAN")
print("="*50)

if rating >= 4 and total_jam_kerja >=40:
    bonus = 200000
else:
    bonus = 0


if golongan == "A":
    tarif_perjam = 50000
elif golongan == "B":
    tarif_perjam = 35000
else:
    tarif_perjam = 25000



gaji_pokok = tarif_perjam * total_jam_kerja


if total_jam_kerja > 40:
    gaji_lembur = (total_jam_kerja - 40) * tarif_perjam
else:
    gaji_lembur = 0

print(f"Nama Karyawan : {nama}")
print(f"Golongan : {golongan}")
print(f"Total Jam Kerja : {total_jam_kerja}")
print(f"Rating : {rating}")
print("="*50)
print(f"bonus : {bonus}")
print(f"Gaji Pokok : {gaji_pokok}")
print(f"gaji lembur : {gaji_lembur}")
print("="*50)
print(f"Total Gaji : {gaji_pokok + bonus + gaji_lembur}")


    