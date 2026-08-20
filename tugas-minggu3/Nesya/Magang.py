print("=== SISTEM SELEKSI KELAYAKAN MAGANG ===")

kehadiran = int(input("Masukkan nilai kehadiran: "))
sikap = input("Masukkan nilai sikap (A/B/C/D): ").upper()
project = int(input("Masukkan jumlah project selesai: "))

if kehadiran >= 85 and (sikap == "A" or sikap == "B") and project >= 3:
    status = "LOLOS"

    if project >= 5:
        kategori = "Magang Tier 1 (BUMN/Unicorn)"
    else:
        kategori = "Magang Tier 2 (Startup/Industri Lokal)"

    evaluasi = "Semua persyaratan magang sudah terpenuhi."

else:
    status = "BELUM LAYAK MAGANG"
    kategori = "Wajib remedial"

    if kehadiran < 85:
        evaluasi = "Perbaiki nilai kehadiran."
    elif sikap == "C" or sikap == "D":
        evaluasi = "Perbaiki nilai sikap."
    elif project < 3:
        evaluasi = "Tambah jumlah project."

print("\n=== HASIL SELEKSI ===")
print("Status   :", status)
print("Kategori :", kategori)
print("Evaluasi :", evaluasi)
