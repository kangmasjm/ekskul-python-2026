golongan_A = 50000
golongan_B = 35000
golongan_C = 25000
jam_normal = 40

def format_rupiah(nilai) :
    return f"{nilai:,}".replace(",", ".")

print("=" * 60)
print("             SISTEM PENGHITUNG GAJI KARYAWAN SMK")
print("=" * 60)

nama = input("Masukkan Nama Karyawan  : ")
pilih_gol = input("Pilih Golongan (A/B/C)  : ")
total_jam = int(input("Total Jam Kerja/Minggu  : "))
rating = int(input("Rating Performa (1 - 5) : "))


if pilih_gol.lower() == 'a':
    tarif = golongan_A
elif pilih_gol.lower() == 'b':
    tarif = golongan_B
elif pilih_gol.lower() == 'c':
    tarif = golongan_C
else:
    tarif = 0

jam_lembur = total_jam - 40

if jam_lembur < 0 :
    jam_lembur = 0

gaji_pokok = total_jam * tarif

gaji_lembur = jam_lembur * tarif

if rating >= 4 and jam_normal >= 40 :
    bonus = 200000

gaji_total = gaji_pokok + gaji_lembur + bonus

print("=" * 60)
print("         SLIP GAJI KARYAWAN")
print("=" * 60)
print(f"Nama Karyawan   : {nama}")
print(f"Golongan        : {pilih_gol.upper()}")
print("Tarif per Jam   : Rp " + format_rupiah(tarif))
print("-" * 60)
print(f"Gaji Pokok ({total_jam} jam)  : Rp " + format_rupiah(gaji_pokok))
print(f"Gaji Lembur ({jam_lembur} jam)  : Rp " + format_rupiah(gaji_lembur))
print(f"Bonus Performa        : Rp " + format_rupiah(bonus))
print("-" * 60)
print(f"TOTAL GAJI DITERIMA   : Rp " + format_rupiah(gaji_total))
print("=" * 60)
