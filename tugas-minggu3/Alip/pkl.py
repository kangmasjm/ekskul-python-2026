print("=" * 60)
print("SKENARIO 1: SISTEM SELEKSI KELAYAKAN MAGANG PKL")
print("=" * 60)

hadir = int(input("Masukan Nilai Kehadiran(%) : "))
sikap = input("Masukan Nilai Sikap(A/B/C/D) : ".upper())
projek = int(input("Masukan Jumlah Projek : "))

if hadir >= 85 and sikap == "A" or sikap == "B" and projek >= 5:
    print("Magang di Perusahaan Tier-1 (BUMN/Unicorn)")
elif hadir >= 85 and sikap == "A" or sikap == "B" and projek == 3 or projek == 4:
    print("Magang Di Perusaahaan Tier-2 (StartUp/Lokal Industri)")
elif hadir < 85 and sikap == "C" or sikap == "D" and projek < 3:
    print("Belum Mahir Magang (Wajib Magang)")
else:
    print("Tidak Lulus")

print("=" * 60)
