print("=" * 40)
print("SISTEM PENGHITUNG GAJI KARYAWAN")
print("=" * 40)

nama = input("Masukkan Nama Karyawan: ")
golongan = input("Pilih Golongan (A/B/C): " .upper())
jam = int(input("Total Jam Kerja/Minggu: "))
rating = int(input("Rating Perfoma (1 - 5): "))

print("=" * 40)
print("SLIP GAJI KARYAWAN")
print("=" * 40)

if rating >= 4 and jam >=40:
    bonus = 200000
else:
    bonus = 0

if golongan == "A":
    tarif_perjam = 50000
elif golongan == "B":
    tarif_perjam = 35000
else:
    tarif_perjam = 25000
    
    gaji_pokok = tarif_perjam * jam


if jam > 40:
    gaji_lembur = (jam - 40) * tarif_perjam
else:
    gaji_lembur = 0

print(f"Nama Karyawan : {nama}")
print(f"Golongan : {golongan}")
print(f"Total Jam Kerja : {jam}")
print(f"Rating : {rating}")
print("="*50)
print(f"bonus : {bonus}")
print(f"Gaji Pokok : {gaji_pokok}")
print(f"gaji lembur : {gaji_lembur}")
print("="*50)
print(f"Total Gaji : {gaji_pokok + bonus + gaji_lembur}")


