kehadiran = int(input("Masukan nilai input (%) : "))
sikap = str(input("Masukan nilai sikap (A/B/C/D) : "))
projek = int(input("jumlah project selesai : "))

if kehadiran >= 85 and sikap == "A" or sikap == "B" and projek >= 5:
    print("Selamat anda lolos dan masuk ke perusahaan tier 1")
elif kehadiran >= 85 and sikap == "A" or sikap == "B" and projek == 3 or projek == 4:
    print("Selamat anda lolos dan masuk ke perusahaan tier 2")
else:
    print("Maaf anda tidak lolos")
    print("Evaluasi :")

if kehadiran < 85:
 print("-kehadiran kurang")
if sikap == "C" or sikap == "D":
   print("-Sikap kurang baik")
if projek < 3: 
   print("-Perlu tambah projek")
