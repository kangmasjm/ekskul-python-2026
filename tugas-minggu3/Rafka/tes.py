print ("=" * 40)
print ("SKENARIO 1:SISTEM SELEKSI KELAYAKAN MAGANG / PKL INDUSTRI")
print ("=" * 40)

nilaiKehadiran = int (input("Nilai Kehadiran (%) :"))
nilaiSikap = input ("Nilai Sikap (A/B/C/D) :".upper())
project = int (input("Jumlah Project Selsai :"))

if nilaiKehadiran >= 85 and nilaiSikap == "A" or nilaiSikap =="B" and project >= 5:
    print ("Magang di Perusahaan Tier-1")
elif nilaiKehadiran >= 85 and nilaiSikap == "A" or nilaiSikap =="B" and project == 3 or project == 4:
    print ("Magang di Perusahaan Tier-2")
elif nilaiKehadiran <= 85 and nilaiSikap == "C" or nilaiSikap =="D" and project < 3:
    print ("Belum Layak Magang (Wajib Magang)")
else :
    print ("Tidak Lulus")

print ("=" * 40)
