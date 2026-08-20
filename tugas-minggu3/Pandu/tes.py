print("--- SISTEM SELEKSI KELAYAKAN PKL SISWA SMK ---")
nilai_hadir = int(input("Nilai Kehadiran : "))
nilai_sikap = input("Nilai Sikap : ")
projek = int(input("Jumlah Project Selesai : "))

if nilai_hadir < 85 :
    evaluasi = "Perlu diberi bimbingan konseling"
elif nilai_sikap != 'B' or nilai_sikap != 'A' :
    evaluasi = "Perlu perbaikan Sikap"
elif projek < 3 :
    evaluasi = "Perlu penambahan projek"
else :
    evaluasi = ""



if nilai_hadir >= 85 and (nilai_sikap == 'B' or nilai_sikap == 'A') and projek >= 5 :
    print("✅ LOLOS UNTUK PKL DI BUMN/UNICORN")
elif nilai_hadir >= 85 and (nilai_sikap == 'B' or nilai_sikap == 'A') and (projek == 3 or projek == 4) :
    print("✅ LOLOS UNTUK PKL DI STARTUP/LOKAL")
else :
    print(f"❌ TIDAK LOLOS UNTUK PKL \nEvaluasi : {evaluasi}")